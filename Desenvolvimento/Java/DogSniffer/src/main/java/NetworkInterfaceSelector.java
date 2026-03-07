import org.pcap4j.core.*;
//import org.pcap4j.packet.Packet;
import java.net.InetAddress;
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class NetworkInterfaceSelector {

    private static final int IPV4_ADDRESS_LENGTH = 4;

    public static void main(String[] args) {
        try {
            Configuration config = selectConfiguration();
            System.out.println("Selected configuration: " + config);
            displayResult(config);
        } catch (NetworkSelectionException e) {
            System.err.println("Erro: " + e.getMessage());
            System.exit(1);
        } catch (Exception e) {
            System.err.println("Ocorreu um erro inesperado: " + e.getMessage());
            System.exit(1);
        }
    }

    private static Configuration selectConfiguration() throws NetworkSelectionException {
        try (Scanner userInput = new Scanner(System.in)){
            PcapNetworkInterface device = selectInterface(userInput);
            String ipAddress = selectIpAddress(userInput, device);
            return new Configuration(device, ipAddress);
        } catch (PcapNativeException e) {
            throw new NetworkSelectionException("Erro ao acessar as interfaces de rede: " + e.getMessage());
        }
    }

    private static PcapNetworkInterface selectInterface(Scanner input) throws NetworkSelectionException, PcapNativeException {
        List<PcapNetworkInterface> availableDevices = Pcaps.findAllDevs();
        
        validateDevicesExist(availableDevices);
        displayAvailableInterfaces(availableDevices);

        int userChoice = readNumericInput(input, 1, availableDevices.size());
        return availableDevices.get(userChoice -1);
    }

    private static void validateDevicesExist(List<PcapNetworkInterface> devices) throws NetworkSelectionException {
        if (devices ==null || devices.isEmpty()) {
            throw new NetworkSelectionException("Nenhuma interface encontrada");
        }
    }

    private static void displayAvailableInterfaces(List<PcapNetworkInterface> devices) {
        System.out.println("Interfaces disponívels:\n");

        for (int i = 0; i < devices.size(); i++){
            displayInterfaceSummary(i + 1, devices.get(i));
        }
    }

    private static void displayInterfaceSummary( int number, PcapNetworkInterface device) {
        System.out.println("[ " + number + " ]" + device.getName());
        System.out.println("Description: \n" + device.getDescription());
        System.out.println("IP Addresses: " + device.getAddresses().size());
    }

    private static int readNumericInput(Scanner input, int minimum, int maximum){
        String prompt = "Escolha ("+ minimum + "-" + maximum + "): ";

        while (true){
            System.out.print(prompt);
            String userEntry = input.nextLine().trim();

            try {
                int value = Integer.parseInt(userEntry);
                if (value >= minimum && value <=maximum) {
                    return value;
                }
                return value;
            } catch (NumberFormatException invalidInput){
                System.out.println("Formato Invalido. Por favor, insira um número entre " + minimum + " e " + maximum + ".");
            }
        }
    }


    private static String selectIpAddress (Scanner input, PcapNetworkInterface device) throws NetworkSelectionException {
        List<InetAddress> availableIps = extractIpAddresses(device);

        if (availableIps.isEmpty()) {
            throw new NetworkSelectionException("Interface sem endereço IP");
        }

        displayIpAddresses(device.getName(), availableIps);
        int userChoice = readNumericInput(input, 1, availableIps.size());
        return availableIps.get(userChoice - 1).getHostAddress();
    } 

    private static boolean isIPV4(InetAddress address) {
        return address.getAddress().length ==IPV4_ADDRESS_LENGTH;
    }

    private static List<InetAddress> extractIpAddresses(PcapNetworkInterface device) {
        List<InetAddress> allAddresses = new ArrayList<>();
        for (PcapAddress pcapAddress : device.getAddresses()) {
            allAddresses.add(pcapAddress.getAddress());
        }
        return allAddresses;
    }

    private static void displayIpAddresses(String deviceName, List<InetAddress> addresses) {
        System.out.println("\n=== IPs EM " + deviceName + " ===\n");
        for (int i = 0; i < addresses.size(); i++) {
            System.out.println("[" + (i + 1) + "] " + addresses.get(i).getHostAddress());
        }
    }
    
    private static void displayResult(Configuration config) {
        System.out.println("\n========================================");
        System.out.println("Interface: " + config.getDevice().getName());
        System.out.println("IP: " + config.getIpAddress());
        System.out.println("========================================");
    }
}








        // List<PcapNetworkInterface> devices = Pcaps.findAllDevs();
        // System.out.println("Available network interfaces:");
        
        // for (PcapNetworkInterface device : devices){
        //     //System.out.println(device);
        //     System.out.println("Nome: " + device.getName());
        //     System.out.println("Descrição: " +device.getDescription());
        //     System.out.println("Endereços IP:");
        //     for (PcapAddress ipAddress : device.getAddresses()) {
        //         System.out.println(" - " + ipAddress.getAddress());


class Configuration {
    private final PcapNetworkInterface device;
    private final String ipAddress;

    public Configuration(PcapNetworkInterface device, String ipAddress){
        this.device = device;
        this.ipAddress = ipAddress;
    }

    public PcapNetworkInterface getDevice() {return device;}
    public String getIpAddress() {return ipAddress;}
}

class NetworkSelectionException extends Exception {
    public NetworkSelectionException(String message) {
        super(message);
    }
}