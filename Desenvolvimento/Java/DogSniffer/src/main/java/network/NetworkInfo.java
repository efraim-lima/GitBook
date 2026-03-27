package network;

/**
 * NetworkInfo armazena todas as informações coletadas de uma rede Wi-Fi.
 *
 * Esses dados vêm dos frames capturados pelo Pcap4j:
 * - Beacon frames: enviados pelo AP periodicamente com SSID, capacidades etc.
 * - Probe Response: resposta a probe requests
 * - Data frames: frames de dados
 */
public class NetworkInfo {

    private String macAddress;      // BSSID do AP
    private String ssid;            // Nome da rede
    private String security;        // WPA2, WPA3, WEP, Open
    private String protocol;        // 802.11a/b/g/n/ac/ax
    private int channel;
    private double frequencyGhz;
    private boolean is5GHz;
    private boolean isHidden;       // SSID oculto
    private String cipherSuite;     // CCMP, TKIP etc.
    private String authKeyMgmt;     // PSK, SAE, EAP etc.
    private int beaconInterval;     // Intervalo de beacon em ms
    private long firstSeen;
    private long lastSeen;

    public NetworkInfo(String macAddress) {
        this.macAddress = macAddress;
        this.ssid       = "<​desconhecido>";
        this.security   = "Desconhecida";
        this.protocol   = "Desconhecido";
        this.firstSeen  = System.currentTimeMillis();
        this.lastSeen   = System.currentTimeMillis();
    }

    public void updateLastSeen() {
        this.lastSeen = System.currentTimeMillis();
    }

    // Getters e Setters
    public String getMacAddress()               { return macAddress; }
    public String getSsid()                     { return ssid; }
    public void setSsid(String ssid)            { this.ssid = ssid; }
    public String getSecurity()                 { return security; }
    public void setSecurity(String security)    { this.security = security; }
    public String getProtocol()                 { return protocol; }
    public void setProtocol(String protocol)    { this.protocol = protocol; }
    public int getChannel()                     { return channel; }
    public void setChannel(int channel)         { this.channel = channel; }
    public double getFrequencyGhz()             { return frequencyGhz; }
    public void setFrequencyGhz(double f)       { this.frequencyGhz = f; this.is5GHz = f >= 5.0; }
    public boolean is5GHz()                     { return is5GHz; }
    public boolean isHidden()                   { return isHidden; }
    public void setHidden(boolean hidden)       { this.isHidden = hidden; }
    public String getCipherSuite()              { return cipherSuite; }
    public void setCipherSuite(String c)        { this.cipherSuite = c; }
    public String getAuthKeyMgmt()              { return authKeyMgmt; }
    public void setAuthKeyMgmt(String a)        { this.authKeyMgmt = a; }
    public int getBeaconInterval()              { return beaconInterval; }
    public void setBeaconInterval(int b)        { this.beaconInterval = b; }
    public long getFirstSeen()                  { return firstSeen; }
    public long getLastSeen()                   { return lastSeen; }
}