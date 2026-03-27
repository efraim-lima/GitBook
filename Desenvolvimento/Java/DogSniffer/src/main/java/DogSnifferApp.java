import etc.Capture;
import etc.Configuration;
import etc.NetworkInterfaceSelector;
import etc.NetworkSelectionException;
import network.PacketProcessor;
import sensor.WitMotionReader;
import display.RadarDisplay;


/* Para iniciar a aplicação:
sudo airmon-ng check kill
sudo airmon-ng start wlan0   # substitua wlan0 pelo nome da sua interface

*/
public class DogSnifferApp {

    public static void main(String[] args) {
        try {
            // 1. Seleciona interface de rede interativamente
            Configuration config = NetworkInterfaceSelector.selectConfiguration();
            NetworkInterfaceSelector.displayResult(config);

            // 2. Sensor — modo simulado até o WT901C chegar fisicamente
            //    Para sensor real: new WitMotionReader("/dev/ttyUSB0", 9600)
            WitMotionReader sensor = new WitMotionReader();
            Thread sensorThread = new Thread(sensor, "sensor-thread");
            sensorThread.setDaemon(true);
            sensorThread.start();

            // 3. Processador de pacotes — recebe cada pacote capturado
            PacketProcessor processor = new PacketProcessor(() -> sensor.getLastData());

            // 4. Captura — abre a interface e alimenta o processor
            Capture capture = new Capture(config.getDevice(), processor);
            Thread captureThread = new Thread(capture, "capture-thread");
            captureThread.setDaemon(true);
            captureThread.start();

            // 5. Display — renderiza o radar no terminal a cada 500ms
            RadarDisplay display = new RadarDisplay(() -> sensor.getLastData());
            Thread displayThread = new Thread(display, "display-thread");
            displayThread.setDaemon(true);
            displayThread.start();

            // 6. Shutdown hook — encerra tudo com segurança no Ctrl+C
            Runtime.getRuntime().addShutdownHook(new Thread(() -> {
                System.out.println("\n[Main] 🛑 Encerrando...");
                sensor.stop();
                capture.stop();
                display.stop();
            }));

            // Mantém a thread main viva enquanto a captura roda
            captureThread.join();

        } catch (NetworkSelectionException e) {
            System.err.println("[Main] ❌ Erro de configuração: " + e.getMessage());
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}