package network;

import cache.CacheEntry;
import cache.SignalCache;
import org.pcap4j.core.*;
import org.pcap4j.packet.*;
import org.pcap4j.packet.namednumber.DataLinkType;

import java.util.concurrent.ConcurrentHashMap;

/**
 * NetworkCollector captura pacotes Wi-Fi com Pcap4j e extrai
 * informações de rede de cada frame.
 *
 * Roda em loop infinito em uma thread separada.
 *
 * Como funciona:
 * 1. Abre a interface em modo monitor
 * 2. Registra um PacketListener (callback chamado a cada pacote)
 * 3. O listener extrai MAC, SSID, segurança etc.
 * 4. Atualiza o SignalCache com as informações
 *
 * NOTA: Para capturar RSSI real, a interface precisa estar em modo monitor
 * e o driver precisa expor o RadioTap header.
 */
public class NetworkCollector implements Runnable {

    private final String interfaceName;   // Ex: "wlan0mon"
    private volatile boolean running;

    // Mapa local de NetworkInfo por MAC — complementa o cache central
    private final ConcurrentHashMap<String, NetworkInfo> networkMap;

    // Referência ao cache central (Singleton)
    private final SignalCache cache;

    public NetworkCollector(String interfaceName) {
        this.interfaceName = interfaceName;
        this.running       = true;
        this.networkMap    = new ConcurrentHashMap<>();
        this.cache         = SignalCache.getInstance();
    }

    @Override
    public void run() {
        System.out.println("[Network] 📡 Iniciando captura em " + interfaceName);

        while (running) {
            try {
                // Obtém o handle da interface de rede
                PcapNetworkInterface nif = Pcaps.getDevByName(interfaceName);
                if (nif == null) {
                    System.err.println("[Network] ❌ Interface não encontrada: " + interfaceName);
                    Thread.sleep(3000);
                    continue;
                }

                // Abre a interface para captura
                // PROMISCUOUS = captura todos os pacotes, não só os destinados a nós
                // 65536 = tamanho máximo do pacote
                // 10ms = timeout de leitura
                PcapHandle handle = nif.openLive(
                    65536,
                    PcapNetworkInterface.PromiscuousMode.PROMISCUOUS,
                    10
                );

                System.out.println("[Network] ✅ Captura iniciada em " + interfaceName);

                // PacketListener é uma interface funcional — podemos usar lambda
                // É chamado automaticamente para cada pacote capturado
                handle.loop(-1, (PacketListener) packet -> {
                    if (!running) return;
                    processPacket(packet);
                });

                handle.close();

            } catch (Exception e) {
                System.err.println("[Network] ⚠️ Erro na captura: " + e.getMessage());
                try { Thread.sleep(2000); } catch (InterruptedException ie) {
                    Thread.currentThread().interrupt();
                }
            }
        }
    }

    /**
     * Processa um pacote capturado.
     *
     * A estrutura de um frame Wi-Fi em modo monitor é:
     * [RadioTap Header] → [802.11 MAC Header] → [Payload]
     *
     * RadioTap contém metadados do rádio: RSSI, canal, taxa etc.
     * 802.11 contém MAC de origem/destino, tipo de frame etc.
     */
    private void processPacket(Packet packet) {
        try {
            int rssi = extractRssi(packet);
            String srcMac = extractSourceMac(packet);

            if (srcMac == null || srcMac.isEmpty()) return;

            // Filtra MACs de broadcast/multicast
            if (srcMac.startsWith("ff:ff") || srcMac.startsWith("01:")) return;

            // Obtém ou cria NetworkInfo para este MAC
            NetworkInfo info = networkMap.computeIfAbsent(
                srcMac, NetworkInfo::new
            );
            info.updateLastSeen();

            // Extrai informações específicas do tipo de frame
            extractNetworkDetails(packet, info);

            // Atualiza o cache central
            CacheEntry entry = cache.updateEntry(srcMac, info.getSsid());
            entry.setRawRssi(rssi);
            entry.setSecurity(info.getSecurity());
            entry.setProtocol(info.getProtocol());
            entry.setChannel(info.getChannel());
            entry.setFrequency(info.getFrequencyGhz());
            entry.addRssiHistory(rssi);

            // Aplica EMA (Exponential Moving Average) para suavizar o RSSI
            // alpha = 0.3 significa que 30% é o novo valor e 70% é o histórico
            double alpha   = 0.3;
            double current = entry.getSmoothedRssi() == 0 ? rssi : entry.getSmoothedRssi();
            entry.setSmoothedRssi(alpha * rssi + (1 - alpha) * current);

            // Calcula distância estimada (modelo log-distance)
            double distance = calculateDistance(entry.getSmoothedRssi(), -50, 3.0);
            entry.setEstimatedDistanceMeters(distance);

        } catch (Exception e) {
            // Silencia erros de pacotes malformados — é normal em captura raw
        }
    }

    /**
     * Extrai o RSSI do RadioTap header.
     *
     * RadioTap é um pseudo-header adicionado pelo driver antes do frame 802.11.
     * Contém informações do rádio como RSSI, canal, taxa de dados etc.
     *
     * Se não conseguir extrair, retorna -100 (sinal muito fraco/inválido).
     */
    private int extractRssi(Packet packet) {
        // Tenta extrair do RadioTap header
        // O Pcap4j representa isso como RadiotapPacket
        try {
            // Percorre a cadeia de pacotes procurando o RadioTap
            Packet current = packet;
            while (current != null) {
                // getHeader().getRawData() contém os bytes brutos
                // O RSSI no RadioTap fica no byte de offset variável
                // dependendo dos campos presentes
                // Aqui fazemos uma extração simplificada
                byte[] raw = current.getRawData();
                if (raw != null && raw.length > 22) {
                    // Byte 22 do RadioTap geralmente contém o RSSI (signed byte)
                    // ATENÇÃO: isso varia por driver — pode precisar de ajuste
                    int rssi = (int)(byte) raw[22];
                    if (rssi < 0 && rssi > -120) return rssi; // range válido
                }
                current = current.getPayload();
            }
        } catch (Exception ignored) {}
        return -100; // valor padrão se não conseguir extrair
    }

    /**
     * Extrai o MAC de origem do frame 802.11.
     *
     * Em frames 802.11, o MAC de origem (transmitter) fica nos bytes 10-15
     * do header MAC, após o frame control (2 bytes) e duration (2 bytes)
     * e o MAC de destino (6 bytes).
     */
    private String extractSourceMac(Packet packet) {
        try {
            byte[] raw = packet.getRawData();
            if (raw == null || raw.length < 24) return null;

            // Pula o RadioTap header (tamanho nos bytes 2-3)
            int radiotapLen = ((raw[3] & 0xFF) << 8) | (raw[2] & 0xFF);
            if (radiotapLen + 16 > raw.length) return null;

            // MAC de origem: bytes 10-15 do header 802.11 (após o RadioTap)
            int offset = radiotapLen + 10;
            return String.format("%02x:%02x:%02x:%02x:%02x:%02x",
                raw[offset]   & 0xFF, raw[offset+1] & 0xFF,
                raw[offset+2] & 0xFF, raw[offset+3] & 0xFF,
                raw[offset+4] & 0xFF, raw[offset+5] & 0xFF);

        } catch (Exception e) {
            return null;
        }
    }

    /**
     * Extrai detalhes da rede do payload do frame.
     * Beacon frames (tipo 0x80) contêm SSID e capacidades.
     */
    private void extractNetworkDetails(Packet packet, NetworkInfo info) {
        try {
            byte[] raw = packet.getRawData();
            if (raw == null || raw.length < 36) return;

            int radiotapLen = ((raw[3] & 0xFF) << 8) | (raw[2] & 0xFF);
            int frameType   = raw[radiotapLen] & 0xFF;

            // 0x80 = Beacon frame, 0x50 = Probe Response
            if (frameType == 0x80 || frameType == 0x50) {
                parseBeaconFrame(raw, radiotapLen, info);
            }

        } catch (Exception ignored) {}
    }

    /**
     * Faz o parse de um Beacon frame para extrair SSID e capacidades.
     *
     * Estrutura do Beacon após o header 802.11 (24 bytes):
     * - 8 bytes: Timestamp
     * - 2 bytes: Beacon Interval
     * - 2 bytes: Capability Info
     * - N bytes: Tagged Parameters (TLV: Tag, Length, Value)
     *
     * TLV = Tag-Length-Value: cada campo tem um tag (1 byte),
     * um tamanho (1 byte) e o valor (N bytes).
     */
    private void parseBeaconFrame(byte[] raw, int radiotapLen, NetworkInfo info) {
        // Offset inicial: RadioTap + header 802.11 (24 bytes) + fixed fields (12 bytes)
        int offset = radiotapLen + 24 + 12;

        // Extrai beacon interval (bytes 8-9 após o header 802.11)
        if (radiotapLen + 32 < raw.length) {
            int beaconInterval = ((raw[radiotapLen + 25] & 0xFF) << 8)
                               | (raw[radiotapLen + 24] & 0xFF);
            info.setBeaconInterval(beaconInterval);
        }

        // Percorre os Tagged Parameters (TLV)
        while (offset + 2 < raw.length) {
            int tag    = raw[offset] & 0xFF;
            int length = raw[offset + 1] & 0xFF;

            if (offset + 2 + length > raw.length) break;

            switch (tag) {
                case 0: // SSID
                    if (length > 0) {
                        String ssid = new String(raw, offset + 2, length);
                        info.setSsid(ssid.isEmpty() ? "<​oculto>" : ssid);
                        info.setHidden(ssid.isEmpty());
                    }
                    break;

                case 1: // Supported Rates — indica o protocolo
                    info.setProtocol(inferProtocol(raw, offset + 2, length));
                    break;

                case 3: // DS Parameter Set — canal
                    if (length >= 1) {
                        int channel = raw[offset + 2] & 0xFF;
                        info.setChannel(channel);
                        info.setFrequencyGhz(channelToFrequency(channel));
                    }
                    break;

                case 48: // RSN (Robust Security Network) — WPA2/WPA3
                    parseRsnElement(raw, offset + 2, length, info);
                    break;

                case 221: // Vendor Specific — pode conter WPA1
                    parseVendorSpecific(raw, offset + 2, length, info);
                    break;
            }

            offset += 2 + length;
        }

        // Se não encontrou RSN nem WPA, é Open ou WEP
        if (info.getSecurity().equals("Desconhecida")) {
            info.setSecurity("Open/WEP");
        }
    }

    /**
     * Faz o parse do elemento RSN para extrair WPA2/WPA3 e cifras.
     */
    private void parseRsnElement(byte[] raw, int offset, int length, NetworkInfo info) {
        if (length < 4) return;
        // Pula version (2 bytes) e group cipher (4 bytes)
        int pos = offset + 6;
        if (pos + 2 > raw.length) return;

        // Pairwise cipher count
        int pairwiseCount = ((raw[pos + 1] & 0xFF) << 8) | (raw[pos] & 0xFF);
        pos += 2;

        // Pairwise ciphers
        StringBuilder ciphers = new StringBuilder();
        for (int i = 0; i < pairwiseCount && pos + 4 <= raw.length; i++) {
            int suite = raw[pos + 3] & 0xFF;
            if (suite == 4) ciphers.append("CCMP ");
            if (suite == 2) ciphers.append("TKIP ");
            pos += 4;
        }
        info.setCipherSuite(ciphers.toString().trim());

        // AKM (Authentication Key Management)
        if (pos + 2 <= raw.length) {
            int akmCount = ((raw[pos + 1] & 0xFF) << 8) | (raw[pos] & 0xFF);
            pos += 2;
            if (akmCount > 0 && pos + 4 <= raw.length) {
                int akm = raw[pos + 3] & 0xFF;
                if (akm == 8 || akm == 9) {
                    info.setSecurity("WPA3");
                    info.setAuthKeyMgmt("SAE");
                } else if (akm == 2) {
                    info.setSecurity("WPA2-Enterprise");
                    info.setAuthKeyMgmt("EAP");
                } else {
                    info.setSecurity("WPA2");
                    info.setAuthKeyMgmt("PSK");
                }
            }
        }
    }

    /**
     * Verifica se o Vendor Specific element é WPA1 (OUI da Microsoft).
     */
    private void parseVendorSpecific(byte[] raw, int offset, int length, NetworkInfo info) {
        if (length < 4) return;
        // OUI da Microsoft para WPA: 00:50:F2:01
        if ((raw[offset] & 0xFF) == 0x00 &&
            (raw[offset+1] & 0xFF) == 0x50 &&
            (raw[offset+2] & 0xFF) == 0xF2 &&
            (raw[offset+3] & 0xFF) == 0x01) {
            if (info.getSecurity().equals("Desconhecida") ||
                info.getSecurity().equals("Open/WEP")) {
                info.setSecurity("WPA");
                info.setAuthKeyMgmt("PSK");
            }
        }
    }

    /**
     * Infere o protocolo 802.11 pelas taxas suportadas.
     */
    private String inferProtocol(byte[] raw, int offset, int length) {
        boolean hasHighRate = false;
        for (int i = 0; i < length && offset + i < raw.length; i++) {
            int rate = (raw[offset + i] & 0x7F) / 2; // Mbps
            if (rate >= 54) hasHighRate = true;
        }
        return hasHighRate ? "802.11a/g/n/ac" : "802.11b";
    }

    /**
     * Converte número de canal Wi-Fi para frequência em GHz.
     * Canais 1-14 são 2.4GHz, canais 36+ são 5GHz.
     */
    private double channelToFrequency(int channel) {
        if (channel >= 1 && channel <= 14) {
            return 2.407 + channel * 0.005;
        } else if (channel >= 36) {
            return 5.0 + (channel - 36) * 0.005;
        }
        return 0.0;
    }

    /**
     * Calcula distância estimada pelo modelo Log-Distance Path Loss.
     * d = 10 ^ ((rssiRef - rssi) / (10 * n))
     */
    private double calculateDistance(double rssi, double rssiRef, double n) {
        return Math.pow(10.0, (rssiRef - rssi) / (10.0 * n));
    }

    public void stop() { this.running = false; }

    public ConcurrentHashMap<String, NetworkInfo> getNetworkMap() {
        return networkMap;
    }
}