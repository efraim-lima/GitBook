package network;

import cache.CacheEntry;
import cache.SignalCache;
import org.pcap4j.packet.Packet;
import sensor.SensorData;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.function.Supplier;

public class PacketProcessor {

    private static final Map<String, String> BLUETOOTH_OUI = Map.of(
        "00:1a:7d", "Bluegiga",
        "00:1b:dc", "Apple",
        "00:1e:c2", "Nordic Semiconductor",
        "00:0a:95", "ESPRESSIF",
        "00:21:13", "Texas Instruments"
    );

    private final SignalCache                            cache;
    private final Supplier<SensorData>                   sensorSupplier;
    private final ConcurrentHashMap<String, NetworkInfo> networkMap;

    private double rssiRef  = -50.0;
    private double pathN    = 3.0;
    private double emaAlpha = 0.3;

    public PacketProcessor(Supplier<SensorData> sensorSupplier) {
        this.cache          = SignalCache.getInstance();
        this.sensorSupplier = sensorSupplier;
        this.networkMap     = new ConcurrentHashMap<>();
    }

    public void process(Packet packet) {
        try {
            byte[] raw = packet.getRawData();
            if (raw == null || raw.length < 24) return;

            int    rssi = extractRssi(raw);
            String mac  = extractSourceMac(raw);
            if (mac == null || mac.isEmpty()) return;
            if (mac.startsWith("ff:ff") || mac.startsWith("01:")) return;

            NetworkInfo info = networkMap.computeIfAbsent(mac, NetworkInfo::new);
            info.updateLastSeen();

            if (isBluetoothDevice(mac)) {
                info.setProtocol("Bluetooth");
                String vendor = bluetoothVendor(mac);
                info.setSsid("BT-" + (vendor != null ? vendor : "Dispositivo"));
                info.setSecurity("N/A");
            } else {
                extractBeaconDetails(raw, info);
            }

            CacheEntry entry = cache.updateEntry(mac, info.getSsid());

            entry.setRawRssi(rssi);
            entry.addRssiHistory(rssi);
            double prev = entry.getSmoothedRssi() == 0 ? rssi : entry.getSmoothedRssi();
            entry.setSmoothedRssi(emaAlpha * rssi + (1 - emaAlpha) * prev);
            entry.setEstimatedDistanceMeters(calculateDistance(entry.getSmoothedRssi()));

            entry.setSecurity(info.getSecurity());
            entry.setProtocol(info.getProtocol());
            entry.setChannel(info.getChannel());
            entry.setFrequency(info.getFrequencyGhz());

            SensorData sensor = sensorSupplier.get();
            entry.setAngleX(sensor.getAngleX());
            entry.setAngleY(sensor.getAngleY());
            entry.setAngleZ(sensor.getAngleZ());

        } catch (Exception ignored) {
        }
    }

    private static boolean isBluetoothDevice(String mac) {
        if (mac == null || mac.length() < 8) return false;
        String oui = mac.substring(0, 8).toLowerCase();
        return BLUETOOTH_OUI.containsKey(oui);
    }

    private static String bluetoothVendor(String mac) {
        if (mac == null || mac.length() < 8) return null;
        return BLUETOOTH_OUI.get(mac.substring(0, 8).toLowerCase());
    }

    private int extractRssi(byte[] raw) {
        try {
            if (raw.length < 8) return -100;

            int radiotapLen = ((raw[3] & 0xFF) << 8) | (raw[2] & 0xFF);
            if (radiotapLen < 8 || radiotapLen > raw.length) return -100;

            // Parse Radiotap present bitmap (little endian) and handle extension bits
            int presentOffset = 4;
            long present = 0;
            int group = 0;
            while (true) {
                if (presentOffset + 4 > raw.length) break;
                long word = ((raw[presentOffset] & 0xFFL)) |
                            ((raw[presentOffset + 1] & 0xFFL) << 8) |
                            ((raw[presentOffset + 2] & 0xFFL) << 16) |
                            ((raw[presentOffset + 3] & 0xFFL) << 24);
                present |= (word << (group * 32));
                presentOffset += 4;
                group++;
                if ((word & 0x80000000L) == 0) break;
            }

            int offset = presentOffset;
            for (int bit = 0; bit < 64; bit++) {
                if ((present & (1L << bit)) == 0) continue;

                int alignment = radiotapAlignment(bit);
                if (alignment > 0 && (offset % alignment) != 0) {
                    offset += alignment - (offset % alignment);
                }

                if (bit == 5 && offset < raw.length) { // dBm Antenna signal
                    int val = (byte) raw[offset];
                    if (val <= 0 && val > -120) return val;
                }

                offset += radiotapFieldLength(bit);
                if (offset > raw.length) break;
            }

            // Fallback: older radiotap formats where signal is at fixed offset 22
            if (raw.length > 22) {
                int rssi = (byte) raw[22];
                if (rssi < 0 && rssi > -120) return rssi;
            }

        } catch (Exception ignored) {
        }
        return -100;
    }

    private int radiotapAlignment(int fieldBit) {
        switch (fieldBit) {
            case 0: return 8; // TSFT
            case 3: return 2; // Channel
            case 8: return 1; // antenna
            default: return 1;
        }
    }

    private int radiotapFieldLength(int fieldBit) {
        switch (fieldBit) {
            case 0: return 8;  // TSFT
            case 1: return 1;  // Flags
            case 2: return 1;  // Rate
            case 3: return 4;  // Channel
            case 4: return 2;  // FHSS
            case 5: return 1;  // dBm Antenna signal
            case 6: return 1;  // dBm Antenna noise
            case 7: return 2;  // Lock quality
            case 8: return 1;  // TSF timestamp
            case 9: return 1;  // antenna
            case 10: return 2; // dB Antenna signal
            case 11: return 2; // dB Antenna noise
            default: return 0;
        }
    }

    private String extractSourceMac(byte[] raw) {
        try {
            int radiotapLen = ((raw[3] & 0xFF) << 8) | (raw[2] & 0xFF);
            int offset = radiotapLen + 10;
            if (offset + 6 > raw.length) return null;
            return String.format("%02x:%02x:%02x:%02x:%02x:%02x",
                raw[offset]   & 0xFF, raw[offset+1] & 0xFF,
                raw[offset+2] & 0xFF, raw[offset+3] & 0xFF,
                raw[offset+4] & 0xFF, raw[offset+5] & 0xFF);
        } catch (Exception ignored) {
            return null;
        }
    }

    private void extractBeaconDetails(byte[] raw, NetworkInfo info) {
        try {
            int radiotapLen = ((raw[3] & 0xFF) << 8) | (raw[2] & 0xFF);
            if (radiotapLen >= raw.length) return;

            int frameControl = raw[radiotapLen] & 0xFF;
            int subtype = frameControl & 0xF0;

            if (subtype == 0x80 || subtype == 0x50) { // Beacon or Probe Response
                parse80211TaggedParameters(raw, radiotapLen + 24 + 12, info);
            } else if (subtype == 0x40) { // Probe Request
                parse80211TaggedParameters(raw, radiotapLen + 24, info);
                if (info.getSsid().equals("<desconhecido>") || info.getSsid().isEmpty()) {
                    info.setSsid("<sondagem>");
                }
            }

            if (info.getSecurity().equals("Desconhecida")) {
                info.setSecurity("Open/WEP");
            }
            if (info.getProtocol().equals("Desconhecido")) {
                info.setProtocol("802.11");
            }

        } catch (Exception ignored) {
        }
    }

    private void parse80211TaggedParameters(byte[] raw, int offset, NetworkInfo info) {
        while (offset + 2 < raw.length) {
            int tag    = raw[offset] & 0xFF;
            int length = raw[offset + 1] & 0xFF;
            if (offset + 2 + length > raw.length) break;

            switch (tag) {
                case 0: // SSID
                    String ssid = length > 0 ? new String(raw, offset + 2, length).trim() : "<oculto>";
                    info.setSsid(ssid.isEmpty() ? "<oculto>" : ssid);
                    info.setHidden(length == 0);
                    break;
                case 3: // DS Parameter Set
                    if (length >= 1) {
                        int channel = raw[offset + 2] & 0xFF;
                        info.setChannel(channel);
                        info.setFrequencyGhz(channelToFrequency(channel));
                    }
                    break;
                case 48: // RSN
                    parseRsn(raw, offset + 2, length, info);
                    break;
                case 221: // Vendor Specific
                    parseVendorSpecific(raw, offset + 2, length, info);
                    break;
                default:
                    break;
            }

            offset += 2 + length;
        }
    }

    private void parseRsn(byte[] raw, int offset, int length, NetworkInfo info) {
        if (length < 6) return;
        int pos = offset + 6;
        if (pos + 2 > raw.length) return;
        int pairwiseCount = ((raw[pos + 1] & 0xFF) << 8) | (raw[pos] & 0xFF);
        pos += 2;
        for (int i = 0; i < pairwiseCount && pos + 4 <= raw.length; i++) pos += 4;
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

    private void parseVendorSpecific(byte[] raw, int offset, int length, NetworkInfo info) {
        if (length < 4) return;
        if ((raw[offset] & 0xFF) == 0x00 && (raw[offset + 1] & 0xFF) == 0x50 &&
            (raw[offset + 2] & 0xFF) == 0xF2 && (raw[offset + 3] & 0xFF) == 0x01) {
            if (info.getSecurity().equals("Desconhecida") || info.getSecurity().equals("Open/WEP")) {
                info.setSecurity("WPA");
                info.setAuthKeyMgmt("PSK");
            }
        }
    }

    private double calculateDistance(double rssi) {
        return Math.pow(10.0, (rssiRef - rssi) / (10.0 * pathN));
    }

    private double channelToFrequency(int channel) {
        if (channel >= 1 && channel <= 14) {
            return 2.407 + channel * 0.005;
        } else if (channel >= 36) {
            return 5.0 + (channel - 36) * 0.005;
        }
        return 0.0;
    }

    public void setRssiRef(double v)  { this.rssiRef  = v; }
    public void setPathN(double v)    { this.pathN    = v; }
    public void setEmaAlpha(double v) { this.emaAlpha = v; }
}
