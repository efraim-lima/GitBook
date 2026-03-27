package cache;

import java.util.ArrayDeque;
import java.util.Deque;

public class CacheEntry {

    private final String macAddress;
    private String ssid;
    private String security;
    private String protocol;
    private int    channel;
    private double frequency;

    private int    rawRssi;
    private double smoothedRssi;
    private double estimatedDistanceMeters; // ← campo que estava faltando

    private double angleX;
    private double angleY;
    private double angleZ;

    private final Deque<Integer> rssiHistory;
    private static final int MAX_HISTORY = 60;

    private long timestamp;

    public CacheEntry(String macAddress, String ssid) {
        this.macAddress  = macAddress;
        this.ssid        = ssid != null ? ssid : "<​desconhecido>";
        this.timestamp   = System.currentTimeMillis();
        this.rssiHistory = new ArrayDeque<>();
        this.angleX      = 0.0;
        this.angleY      = 0.0;
        this.angleZ      = 0.0;
    }

    /** Janela deslizante de histórico */
    public void addRssiHistory(int rssi) {
        if (rssiHistory.size() >= MAX_HISTORY) rssiHistory.pollFirst();
        rssiHistory.addLast(rssi);
    }

    /** Renova o timestamp — chamado a cada nova leitura deste MAC */
    public void touch() { // ← método que estava faltando
        this.timestamp = System.currentTimeMillis();
    }

    public long getAgeMillis() {
        return System.currentTimeMillis() - timestamp;
    }

    // --- Getters e Setters ---
    public String getMacAddress()                    { return macAddress; }
    public String getSsid()                          { return ssid; }
    public void   setSsid(String s)                  { this.ssid = s; }
    public String getSecurity()                      { return security; }
    public void   setSecurity(String s)              { this.security = s; }
    public String getProtocol()                      { return protocol; }
    public void   setProtocol(String p)              { this.protocol = p; }
    public int    getChannel()                       { return channel; }
    public void   setChannel(int c)                  { this.channel = c; }
    public double getFrequency()                     { return frequency; }
    public void   setFrequency(double f)             { this.frequency = f; }
    public int    getRawRssi()                       { return rawRssi; }
    public void   setRawRssi(int r)                  { this.rawRssi = r; }
    public double getSmoothedRssi()                  { return smoothedRssi; }
    public void   setSmoothedRssi(double s)          { this.smoothedRssi = s; }
    public double getEstimatedDistanceMeters()       { return estimatedDistanceMeters; }
    public void   setEstimatedDistanceMeters(double d){ this.estimatedDistanceMeters = d; }
    public double getAngleX()                        { return angleX; }
    public void   setAngleX(double a)                { this.angleX = a; }
    public double getAngleY()                        { return angleY; }
    public void   setAngleY(double a)                { this.angleY = a; }
    public double getAngleZ()                        { return angleZ; }
    public void   setAngleZ(double a)                { this.angleZ = a; }
    public long   getTimestamp()                     { return timestamp; }
    public Deque<Integer> getRssiHistory()           { return rssiHistory; }
}