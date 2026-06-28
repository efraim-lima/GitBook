package etc;

import org.pcap4j.core.PcapNetworkInterface;

public class Configuration {
    private final PcapNetworkInterface device;
    private final String ipAddress;

    public Configuration(PcapNetworkInterface device, String ipAddress) {
        this.device    = device;
        this.ipAddress = ipAddress;
    }

    public PcapNetworkInterface getDevice() { return device; }
    public String getIpAddress()            { return ipAddress; }

    @Override
    public String toString() {
        return "Configuration{device=" + device.getName() + ", ip=" + ipAddress + "}";
    }
}