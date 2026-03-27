import java.util.ArrayList;
import java.util.List;

public class Specter {

    static final double PATH_LOSS_EXPONENT = 3.0;
    static final double REFERENCE_DISTANCE = 1.0;
    static final double REFERENCE_RSSI = -40.0;

    static class AccessPoint {
        String ssid;
        double x, y;
        double rssi;

        AccessPoint(String ssid, double x, double y, double rssi) {
            this.ssid = ssid;
            this.x = x;
            this.y = y;
            this.rssi = rssi;
        }

        double estimatedDistance() {
            return REFERENCE_DISTANCE * Math.pow(10.0, (REFERENCE_RSSI - rssi) / (10.0 * PATH_LOSS_EXPONENT));
        }
    }

    static class Position {
        double x, y;

        Position(double x, double y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return String.format("Position(x=%.2f, y=%.2f)", x, y);
        }
    }

    static Position trilaterate(List<AccessPoint> aps) {
        if (aps.size() < 3) {
            throw new IllegalArgumentException("At least 3 access points are required for trilateration.");
        }

        double x1 = aps.get(0).x, y1 = aps.get(0).y, r1 = aps.get(0).estimatedDistance();
        double x2 = aps.get(1).x, y2 = aps.get(1).y, r2 = aps.get(1).estimatedDistance();
        double x3 = aps.get(2).x, y3 = aps.get(2).y, r3 = aps.get(2).estimatedDistance();

        double A = 2 * (x2 - x1);
        double B = 2 * (y2 - y1);
        double C = r1 * r1 - r2 * r2 - x1 * x1 + x2 * x2 - y1 * y1 + y2 * y2;

        double D = 2 * (x3 - x2);
        double E = 2 * (y3 - y2);
        double F = r2 * r2 - r3 * r3 - x2 * x2 + x3 * x3 - y2 * y2 + y3 * y3;

        double det = A * E - B * D;

        if (Math.abs(det) < 1e-10) {
            throw new ArithmeticException("Access points are collinear; cannot trilaterate.");
        }

        double x = (C * E - F * B) / det;
        double y = (A * F - D * C) / det;

        return new Position(x, y);
    }

    static void printSignalMap(List<AccessPoint> aps) {
        System.out.println("\n--- Wireless Signal Map ---");
        for (AccessPoint ap : aps) {
            double dist = ap.estimatedDistance();
            int bars = signalBars(ap.rssi);
            System.out.printf("SSID: %-15s | Pos: (%.1f, %.1f) | RSSI: %.1f dBm | Dist: %.2f m | Signal: %s%n",
                    ap.ssid, ap.x, ap.y, ap.rssi, dist, "█".repeat(bars) + "░".repeat(5 - bars));
        }
    }

    static int signalBars(double rssi) {
        if (rssi >= -50) return 5;
        if (rssi >= -60) return 4;
        if (rssi >= -70) return 3;
        if (rssi >= -80) return 2;
        if (rssi >= -90) return 1;
        return 0;
    }

    public static void main(String[] args) {
        List<AccessPoint> signals = new ArrayList<>();

        signals.add(new AccessPoint("Router_A", 0.0,  0.0,  -55.0));
        signals.add(new AccessPoint("Router_B", 10.0, 0.0,  -65.0));
        signals.add(new AccessPoint("Router_C", 5.0,  8.0,  -70.0));
        signals.add(new AccessPoint("Router_D", 0.0,  10.0, -80.0));

        printSignalMap(signals);

        System.out.println("\n--- Trilateration (using 3 strongest signals) ---");

        signals.sort((a, b) -> Double.compare(b.rssi, a.rssi));
        List<AccessPoint> top3 = signals.subList(0, 3);

        try {
            Position estimated = trilaterate(top3);
            System.out.println("Estimated device position: " + estimated);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

        System.out.println("\n--- All possible trilaterations ---");
        for (int i = 0; i < signals.size() - 2; i++) {
            for (int j = i + 1; j < signals.size() - 1; j++) {
                for (int k = j + 1; k < signals.size(); k++) {
                    List<AccessPoint> combo = List.of(signals.get(i), signals.get(j), signals.get(k));
                    try {
                        Position pos = trilaterate(combo);
                        System.out.printf("  [%s, %s, %s] => %s%n",
                                combo.get(0).ssid, combo.get(1).ssid, combo.get(2).ssid, pos);
                    } catch (Exception e) {
                        System.out.printf("  [%s, %s, %s] => Skipped: %s%n",
                                combo.get(0).ssid, combo.get(1).ssid, combo.get(2).ssid, e.getMessage());
                    }
                }
            }
        }
    }
}
