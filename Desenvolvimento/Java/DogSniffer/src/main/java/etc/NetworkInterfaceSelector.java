package etc;

import org.pcap4j.core.*;
//import org.pcap4j.packet.Packet;
import java.net.InetAddress;
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * NetworkInterfaceSelector cuida de toda a interação com o usuário
 * para escolher qual interface de rede usar.
 *
 * Não mudamos a lógica — só adicionamos "package etc;" no topo
 * e garantimos que Configuration e NetworkSelectionException
 * estão no mesmo package, então não precisamos importá-las.
 */

public class NetworkInterfaceSelector {

    private static final int IPV4_ADDRESS_LENGTH = 10;


    public static Configuration selectConfiguration() throws NetworkSelectionException {
        try (Scanner userInput = new Scanner(System.in)){
            PcapNetworkInterface device = selectInterface(userInput);
            String ipAddress = selectIpAddress(userInput, device);
            return new Configuration(device, ipAddress);
        } catch (PcapNativeException e) {
            throw new NetworkSelectionException("Erro ao acessar as interfaces de rede: " + e.getMessage());
        } catch (Exception e) {
            throw new NetworkSelectionException("Erro inesperado durante a seleção: " + e.getMessage());
        }
    }

    private static PcapNetworkInterface selectInterface(Scanner input) 
            throws NetworkSelectionException, PcapNativeException {
        List<PcapNetworkInterface> availableDevices = Pcaps.findAllDevs();
        
        validateDevicesExist(availableDevices);
        displayAvailableInterfaces(availableDevices);

        int userChoice = readNumericInput(input, 1, availableDevices.size());
        return availableDevices.get(userChoice -1);
    }

    private static void validateDevicesExist(List<PcapNetworkInterface> devices) 
            throws NetworkSelectionException {
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
        System.out.println("[" + number + "] - " + device.getName());
        System.out.println("Description: " + device.getDescription());
        System.out.println("IP Addresses: " + device.getAddresses().size());

        for (PcapAddress pcapAddress : device.getAddresses()){
            System.out.println("- " + pcapAddress.getAddress());
        };

        System.out.println("\n");
    }

    private static int readNumericInput(Scanner input, int minimum, int maximum){
        String prompt = "Escolha ("+ minimum + "-" + maximum + "): ";

        while (true){
            System.out.print(prompt);
            String userEntry = input.nextLine().trim();

            try {
                int value = Integer.parseInt(userEntry);
                if (value >= minimum && value <= maximum) {
                    return value;
                } else {
                    System.out.println("Número fora do intervalo. Por favor, insira um número entre " + minimum + " e " + maximum + ".");
                }
            } catch (NumberFormatException invalidInput){
                System.out.println("Formato Invalido. Por favor, insira um número entre " + minimum + " e " + maximum + ".");
            }
        }
    }


    private static String selectIpAddress (Scanner input, PcapNetworkInterface device) 
            throws NetworkSelectionException {
        List<InetAddress> availableIps = extractIpAddresses(device);

        if (availableIps.isEmpty()) {
            System.out.println("[Aviso] Interface sem IP (modo monitor detectado). Continuando...");
            //throw new NetworkSelectionException("Interface sem endereço IP");
            return "N/A";
        }

        displayIpAddresses(device.getName(), availableIps);
        int userChoice = readNumericInput(input, 1, availableIps.size());
        return availableIps.get(userChoice - 1).getHostAddress();
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
    
    public static void displayResult(Configuration config) {
        System.out.println("\n========================================");
        System.out.println("Interface: " + config.getDevice().getName());
        System.out.println("IP: " + config.getIpAddress());
        System.out.println("========================================");
    }
}