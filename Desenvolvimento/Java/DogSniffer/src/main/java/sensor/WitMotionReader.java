package sensor;

import com.fazecast.jSerialComm.SerialPort; // ← import da biblioteca serial

public class WitMotionReader implements Runnable {

    private final String  portName;
    private final int     baudRate;
    private volatile SensorData lastData;
    private volatile boolean    running;
    private final boolean simulationMode;

    private static final byte HEADER     = 0x55;
    private static final byte ANGLE_TYPE = 0x53;

    /** Construtor para sensor real */
    public WitMotionReader(String portName, int baudRate) {
        this.portName       = portName;
        this.baudRate       = baudRate;
        this.simulationMode = false;
        this.lastData       = SensorData.unavailable();
        this.running        = true;
    }

    /** Construtor para modo simulado (sem sensor físico) */
    public WitMotionReader() {
        this.portName       = "SIMULADO";
        this.baudRate       = 0;
        this.simulationMode = true;
        this.lastData       = SensorData.unavailable();
        this.running        = true;
    }

    @Override
    public void run() {
        if (simulationMode) runSimulation();
        else                runSerial();
    }

    private void runSimulation() {
        System.out.println("[Sensor] 🎮 Modo simulado ativo.");
        double yaw = 0;
        while (running) {
            try {
                yaw = (yaw + 5) % 360;
                double pitch = Math.sin(Math.toRadians(yaw)) * 15;
                lastData = new SensorData(0, pitch, yaw); // ← 3 argumentos
                Thread.sleep(200);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
    }

    private void runSerial() {
        System.out.println("[Sensor] 🔌 Conectando em " + portName + " @ " + baudRate + " baud");

        while (running) {
            SerialPort port = SerialPort.getCommPort(portName);
            try {
                port.setBaudRate(baudRate);
                port.setNumDataBits(8);
                port.setNumStopBits(1);
                port.setParity(SerialPort.NO_PARITY);
                port.setComPortTimeouts(SerialPort.TIMEOUT_READ_BLOCKING, 1000, 0);

                if (!port.openPort()) {
                    System.err.println("[Sensor] ❌ Não foi possível abrir " + portName);
                    lastData = SensorData.unavailable();
                    Thread.sleep(2000);
                    continue;
                }

                System.out.println("[Sensor] ✅ Porta " + portName + " aberta.");
                byte[] oneByte = new byte[1];

                while (running) {
                    if (port.readBytes(oneByte, 1) < 1) continue;
                    if (oneByte[0] != HEADER) continue;

                    if (port.readBytes(oneByte, 1) < 1) continue;
                    byte type = oneByte[0];

                    byte[] data = new byte[9];
                    if (port.readBytes(data, 9) < 9) continue;

                    if (type == ANGLE_TYPE) {
                        lastData = decodeAnglePacket(data);
                    }
                }

            } catch (Exception e) {
                System.err.println("[Sensor] ⚠️ Erro: " + e.getMessage());
                lastData = SensorData.unavailable();
                try { Thread.sleep(2000); }
                catch (InterruptedException ie) {
                    Thread.currentThread().interrupt();
                    break;
                }
            } finally {
                if (port.isOpen()) port.closePort();
            }
        }
    }

    private SensorData decodeAnglePacket(byte[] data) {
        int rawX = ((data[1] & 0xFF) << 8) | (data[0] & 0xFF);
        int rawY = ((data[3] & 0xFF) << 8) | (data[2] & 0xFF);
        int rawZ = ((data[5] & 0xFF) << 8) | (data[4] & 0xFF);

        double angleX = (short) rawX / 32768.0 * 180.0;
        double angleY = (short) rawY / 32768.0 * 180.0;
        double angleZ = (short) rawZ / 32768.0 * 180.0;

        if (angleZ < 0) angleZ += 360.0;

        return new SensorData(angleX, angleY, angleZ); // ← 3 argumentos
    }

    public SensorData getLastData() { return lastData; }
    public void stop()              { this.running = false; }
}