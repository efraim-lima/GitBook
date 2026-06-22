package sensor;

public class SensorData {

    private final double angleX;
    private final double angleY;
    private final double angleZ;
    private final long   timestamp;
    private final boolean valid;

    public SensorData(double angleX, double angleY, double angleZ) {
        this.angleX    = angleX;
        this.angleY    = angleY;
        this.angleZ    = angleZ;
        this.timestamp = System.currentTimeMillis();
        this.valid     = true;
    }

    /**
     * Factory method para sensor offline.
     * Retorna ângulos zerados e valid=false.
     *
     * CONCEITO — classe anônima:
     * "new SensorData(...) { @Override ... }" cria uma subclasse
     * sem nome, só para sobrescrever isValid(). É um atalho
     * para não precisar criar uma classe separada SensorDataUnavailable.
     */
    public static SensorData unavailable() {
        return new SensorData(0, 0, 0) {
            @Override
            public boolean isValid() { return false; }
        };
    }

    public double  getAngleX()  { return angleX; }
    public double  getAngleY()  { return angleY; }
    public double  getAngleZ()  { return angleZ; }
    public long    getTimestamp(){ return timestamp; }
    public boolean isValid()    { return valid; }

    @Override
    public String toString() {
        if (!isValid()) return "SensorData[OFFLINE]";
        return String.format("SensorData[Roll=%.1f° Pitch=%.1f° Yaw=%.1f°]",
            angleX, angleY, angleZ);
    }
}