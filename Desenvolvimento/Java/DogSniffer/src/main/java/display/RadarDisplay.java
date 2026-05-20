package display;

import cache.CacheEntry;
import cache.SignalCache;
import sensor.SensorData;

import java.text.SimpleDateFormat;
import java.util.*;
import java.util.function.Supplier;

public class RadarDisplay implements Runnable {

    private final SignalCache          cache;
    private final Supplier<SensorData> sensorSupplier;
    private volatile boolean           running;

    private static final int REFRESH_MS  = 500;
    private static final int GRAPH_WIDTH = 50;
    private static final int RADAR_SIZE  = 19;
    private static final double RADAR_MAX_DISTANCE_METERS = 30.0;

    private static final String RESET   = "\033[0m";
    private static final String RED     = "\033[31m";
    private static final String GREEN   = "\033[32m";
    private static final String YELLOW  = "\033[33m";
    private static final String BLUE    = "\033[34m";
    private static final String MAGENTA = "\033[35m";
    private static final String CYAN    = "\033[36m";
    private static final String WHITE   = "\033[37m";
    private static final String BOLD    = "\033[1m";

    private static final String CLEAR_SCREEN = "\033[2J";
    private static final String CURSOR_HOME  = "\033[H";
    private static final String CURSOR_HIDE  = "\033[?25l";
    private static final String CURSOR_SHOW  = "\033[?25h";

    private static final String[] NET_COLORS = {
        CYAN, GREEN, YELLOW, MAGENTA, RED, BLUE, WHITE
    };

    public RadarDisplay(Supplier<SensorData> sensorSupplier) {
        this.cache          = SignalCache.getInstance();
        this.sensorSupplier = sensorSupplier;
        this.running        = true;
    }

    @Override
    public void run() {
        System.out.print(CURSOR_HIDE);
        try {
            while (running) {
                System.out.print(CLEAR_SCREEN + CURSOR_HOME);

                List<CacheEntry> entries = cache.getAllEntries();
                entries.sort((a, b) ->
                    Double.compare(b.getSmoothedRssi(), a.getSmoothedRssi()));

                printHeader();
                printSensorStatus();
                printRadarWithColumns(entries);
                printSignalGraph(entries);
                printFooter();
                System.out.flush();

                Thread.sleep(REFRESH_MS);
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } catch (Exception e) {
            System.err.println("[Display] Erro: " + e.getMessage());
        } finally {
            System.out.print(CURSOR_SHOW);
            System.out.flush();
        }
    }

    private void printHeader() {
        String time = new SimpleDateFormat("HH:mm:ss").format(new Date());
        System.out.println(BOLD + CYAN +
            "╔══════════════════════════════════════════════════════════════╗\n" +
            "║          📡  DOG SNIFFER — WIFI RADAR                       ║\n" +
            "╚══════════════════════════════════════════════════════════════╝"
            + RESET);
        System.out.printf("  Redes: %s%d%s  |  %s%n%n",
            BOLD + GREEN, cache.size(), RESET, time);
    }

    private void printSensorStatus() {
        SensorData sd = sensorSupplier.get(); // ← busca dado atual via Supplier
        System.out.print(BOLD + "  🧭 Sensor WT901C: " + RESET);
        if (sd.isValid()) {
            System.out.printf(GREEN + "ONLINE" + RESET +
                "  Roll:%s%.1f°%s  Pitch:%s%.1f°%s  Yaw:%s%.1f°%s%n%n",
                YELLOW, sd.getAngleX(), RESET,
                YELLOW, sd.getAngleY(), RESET,
                CYAN + BOLD, sd.getAngleZ(), RESET);
        } else {
            System.out.println(RED + "OFFLINE" + RESET +
                " — ângulos zerados (antena omni ativa)");
            System.out.println();
        }
    }

    private void printRadarWithColumns(List<CacheEntry> entries) {
        SensorData currentSensor = sensorSupplier.get();
        List<String> left = buildLeftPanel(entries);
        List<String> center = buildRadarLines(entries, currentSensor);
        List<String> right = buildRightPanel(entries, currentSensor);

        int leftWidth = 46;
        int maxLines = Math.max(center.size(), Math.max(left.size(), right.size()));

        for (int i = 0; i < maxLines; i++) {
            String leftPart = i < left.size() ? left.get(i) : "";
            String centerPart = i < center.size() ? center.get(i) : "";
            String rightPart = i < right.size() ? right.get(i) : "";

            System.out.printf("%-" + leftWidth + "s%s%s%n", leftPart, centerPart, rightPart);
        }
        System.out.println();
    }

    private List<String> buildLeftPanel(List<CacheEntry> entries) {
        List<String> lines = new ArrayList<>();
        lines.add(BOLD + "  ID  MAC                SSID" + RESET);
        lines.add("  " + "─".repeat(45));

        for (int i = 0; i < entries.size() && i < 8; i++) {
            CacheEntry e = entries.get(i);
            String color = NET_COLORS[i % NET_COLORS.length];
            char id = (char) ('A' + i);
            lines.add(String.format("  %s%c%s  %-17s %-18s",
                color + BOLD, id, RESET,
                trunc(e.getMacAddress(), 17),
                trunc(nvl(e.getSsid()), 18)));
        }
        return lines;
    }

    private List<String> buildRightPanel(List<CacheEntry> entries, SensorData currentSensor) {
        List<String> lines = new ArrayList<>();
        lines.add(BOLD + "  RSSI   Dist    Dir    Protocolo      Intensidade" + RESET);
        lines.add("  " + "─".repeat(53));

        for (int i = 0; i < entries.size() && i < 8; i++) {
            CacheEntry e = entries.get(i);
            int bars = (int) Math.max(0, Math.min(12, (e.getSmoothedRssi() + 100) / 7.0));
            String intensity = "";
            for (int j = 0; j < bars; j++) intensity += "▮";
            for (int j = bars; j < 12; j++) intensity += " ";

            double dir = currentSensor.isValid()
                ? normalizeAngle360(e.getAngleZ() - currentSensor.getAngleZ())
                : normalizeAngle360(e.getAngleZ());

            lines.add(String.format("  %4.0f dBm %5.1fm %5.0f°  %-10s %s",
                e.getSmoothedRssi(), e.getEstimatedDistanceMeters(), dir,
                trunc(nvl(e.getProtocol()), 10), intensity));
        }
        return lines;
    }

    private List<String> buildRadarLines(List<CacheEntry> entries, SensorData currentSensor) {
        int center = RADAR_SIZE / 2;
        int radius = center - 1;

        char[][] grid = new char[RADAR_SIZE][RADAR_SIZE];
        String[][] colorGrid = new String[RADAR_SIZE][RADAR_SIZE];
        for (char[] row : grid) Arrays.fill(row, '·');

        for (int i = 0; i < entries.size() && i < NET_COLORS.length; i++) {
            CacheEntry e = entries.get(i);
            double relativeAngle = currentSensor.isValid()
                ? normalizeAngle360(e.getAngleZ() - currentSensor.getAngleZ())
                : normalizeAngle360(e.getAngleZ());
            double rad = Math.toRadians(relativeAngle);
            double distanceRatio = clamp(e.getEstimatedDistanceMeters() / RADAR_MAX_DISTANCE_METERS, 0.1, 1.0);
            int pointRadius = Math.max(1, (int) Math.round(distanceRatio * radius));

            int col = center + (int) Math.round(Math.sin(rad) * pointRadius);
            int row = center - (int) Math.round(Math.cos(rad) * pointRadius);
            col = Math.max(0, Math.min(RADAR_SIZE - 1, col));
            row = Math.max(0, Math.min(RADAR_SIZE - 1, row));
            grid[row][col] = (char) ('A' + i);
            colorGrid[row][col] = NET_COLORS[i];
        }

        List<String> lines = new ArrayList<>();
        lines.add("  " + BOLD + "RADAR" + RESET + " (N relativo ao sensor)       N");
        lines.add("                           ↑");

        for (int r = 0; r < RADAR_SIZE; r++) {
            StringBuilder row = new StringBuilder();
            row.append(r == center ? "  W ←  " : "         ");
            for (int c = 0; c < RADAR_SIZE; c++) {
                if (r == center && c == center) {
                    row.append(BOLD).append(RED).append("✛").append(RESET).append(" ");
                } else if (colorGrid[r][c] != null) {
                    row.append(colorGrid[r][c])
                       .append(BOLD).append(grid[r][c]).append(RESET).append(" ");
                } else {
                    row.append(BLUE).append(grid[r][c]).append(RESET).append(" ");
                }
            }
            if (r == center) row.append("→ E");
            lines.add(row.toString());
        }

        lines.add("                           ↓");
        lines.add("                           S");
        lines.add("");
        return lines;
    }

    private double normalizeAngle360(double angle) {
        double normalized = angle % 360.0;
        return normalized < 0 ? normalized + 360.0 : normalized;
    }

    private double clamp(double value, double min, double max) {
        return Math.max(min, Math.min(max, value));
    }

    private void printNetworkTable(List<CacheEntry> entries) {
        System.out.println(BOLD +
            "  ID  MAC                SSID               RSSI    ΔRSSI   Dist     Seg        Canal  Tendência"
            + RESET);
        System.out.println("  " + "─".repeat(107));

        for (int i = 0; i < entries.size(); i++) {
            CacheEntry e     = entries.get(i);
            String     color = NET_COLORS[i % NET_COLORS.length];
            int bars = (int) Math.max(0, Math.min(10, (e.getSmoothedRssi() + 100) / 7.0));
            String barColor  = bars >= 7 ? GREEN : bars >= 4 ? YELLOW : RED;

            System.out.printf("  %s%c%s   %-17s %-18s %s%4.0f%s dBm %6s %6.1fm  %-10s %3d    %s%n",
                color + BOLD, (char) ('A' + i), RESET,
                trunc(e.getMacAddress(), 17),
                trunc(nvl(e.getSsid()), 18),
                barColor, e.getSmoothedRssi(), RESET,
                deltaRssi(e),
                e.getEstimatedDistanceMeters(),
                trunc(nvl(e.getSecurity()), 10),
                e.getChannel(),
                trend(e));
        }
        System.out.println();
    }

    private void printSignalGraph(List<CacheEntry> entries) {
        if (entries.isEmpty()) return;

        System.out.println(BOLD + "  📊 HISTÓRICO DE SINAL" + RESET);

        for (int i = 0; i < entries.size() && i < NET_COLORS.length; i++) {
            CacheEntry e = entries.get(i);
            System.out.printf("  %s%c%s=%-20s  ",
                NET_COLORS[i] + BOLD, (char) ('A' + i), RESET,
                trunc(nvl(e.getSsid()), 20));
            if ((i + 1) % 3 == 0) System.out.println();
        }
        System.out.println();

        int    ROWS    = 8;
        int    rssiMax = -30;
        int    rssiMin = -100;
        String[][] graphGrid = new String[ROWS][GRAPH_WIDTH];
        for (String[] row : graphGrid) Arrays.fill(row, " ");

        for (int ni = 0; ni < entries.size() && ni < NET_COLORS.length; ni++) {
            CacheEntry    e     = entries.get(ni);
            String        color = NET_COLORS[ni % NET_COLORS.length];
            char          marker = (char) ('A' + ni);
            List<Integer> hist  = new ArrayList<>(e.getRssiHistory());
            int start = Math.max(0, hist.size() - GRAPH_WIDTH);
            for (int col = 0; col < GRAPH_WIDTH && (start + col) < hist.size(); col++) {
                int rssi    = hist.get(start + col);
                int clamped = Math.max(rssiMin, Math.min(rssiMax, rssi));
                int row     = (int) ((rssiMax - clamped) / (double) (rssiMax - rssiMin) * (ROWS - 1));
                row = Math.max(0, Math.min(ROWS - 1, row));
                graphGrid[row][col] = color + BOLD + marker + RESET;
            }
        }

        for (int r = 0; r < ROWS; r++) {
            int label = rssiMax - (int) (r / (double) (ROWS - 1) * (rssiMax - rssiMin));
            System.out.printf("  %4d dBm |", label);
            for (int c = 0; c < GRAPH_WIDTH; c++) System.out.print(graphGrid[r][c]);
            System.out.println("|");
        }
        System.out.print("           +");
        System.out.print("─".repeat(GRAPH_WIDTH));
        System.out.println("+");
        System.out.printf("           %-25s%s%n%n", "← mais antigo", "mais recente →");
    }

    private String trend(CacheEntry e) {
        List<Integer> h = new ArrayList<>(e.getRssiHistory());
        if (h.size() < 4) return "  ?  ";
        int    half = h.size() / 2;
        double f    = h.subList(0, half).stream().mapToInt(i -> i).average().orElse(0);
        double s    = h.subList(half, h.size()).stream().mapToInt(i -> i).average().orElse(0);
        double d    = s - f;
        if (d > 3)  return GREEN  + "↑ Aprox" + RESET;
        if (d < -3) return RED    + "↓ Afast" + RESET;
        return YELLOW + "→ Estáv" + RESET;
    }

    private String deltaRssi(CacheEntry e) {
        List<Integer> h = new ArrayList<>(e.getRssiHistory());
        if (h.size() < 2) return "  ?  ";
        int last = h.get(h.size() - 1);
        int prev = h.get(h.size() - 2);
        int diff = last - prev;
        String sign = diff > 0 ? "+" : "";
        return String.format("%s%d dB", sign, diff);
    }

    private void printFooter() {
        System.out.println(CYAN + "  " + "─".repeat(64) + RESET);
        System.out.println("  [Ctrl+C para encerrar]  Cache TTL: 5s  |  Refresh: 500ms");
    }

    private String trunc(String s, int max) {
        if (s == null || s.isEmpty()) return "";
        return s.length() <= max ? s : s.substring(0, max - 1) + "…";
    }

    private String nvl(String s) { return s != null ? s : "?"; }

    public void stop() { this.running = false; }
}