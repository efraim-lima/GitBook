package etc;

import network.PacketProcessor;
import org.pcap4j.core.*;
import org.pcap4j.packet.Packet;

public class Capture implements Runnable {

    private final PcapNetworkInterface device;
    private final PacketProcessor      processor;
    private volatile boolean           running;
    private PcapHandle                 handle;

    private static final int SNAPLEN  = 65536;
    private static final int TIMEOUT  = 10;

    public Capture(PcapNetworkInterface device, PacketProcessor processor) {
        this.device    = device;
        this.processor = processor;
        this.running   = true;
    }

    @Override
    public void run() {
        try {
            handle = device.openLive(
                SNAPLEN,
                PcapNetworkInterface.PromiscuousMode.PROMISCUOUS,
                TIMEOUT
            );
            System.out.println("[Capture] ✅ Captura iniciada em: " + device.getName());

            handle.loop(-1, (PacketListener) (Packet packet) -> {
                if (running) processor.process(packet);
            });

        } catch (PcapNativeException | InterruptedException | NotOpenException e) {
            System.err.println("[Capture] ❌ Erro: " + e.getMessage());
        } finally {
            if (handle != null && handle.isOpen()) handle.close();
        }
    }

    public void stop() {
        this.running = false;
        if (handle != null && handle.isOpen()) {
            try { handle.breakLoop(); }
            catch (NotOpenException ignored) {}
        }
    }
}