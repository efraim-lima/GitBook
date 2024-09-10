Quando colocamos um host automatiacmente na rede e ativamos o DHCP sem ter configurado um servidor DHCP a comuncação será estabelecida pelo protocolo APIPA (nos IPs 169.256.XXX.XXX)

Para o próximo projeto precisamos criar um serviço DHCP a partir de um host ao lado do servidor, o processo deve ser feito também entre os gateways para proporcionar interoperabilidade entre as redes. O host ao lado do servidor deve ser empenhado para garantir que não criamos gargalos na rede por conta de configuração de dhcp. Para isso nós precisamos configurar no roteador um dhcp pool para cada subrede/vlan, isso evita conflitos na rede.


[ROUTER]
enable
configure terminal
username user password pass
ip domain-name fatec.edu.com
crypto key generate rsa general-keys modulus 1024
ip ssh version 2
enable secret pass
login
transport input ssh
exit
service password-encrryption
banner motd @  **** Acesso restrto ****	@

//a partir daqui precisamos ter exclusivamente uma configuração para cada subrede 
ip dhcp excluded-address 192.168.0.1 192.168.0.5 // aqui precisa ser o range equivalente a subrede (vlan marcada ou tagged)
ip dhcp pool DHCP-VEN //nome da subrede dhcp
dns-server 192.168.0.2
network 192.168.0.96 255.255.255.224
exit
ip dhcp excluded-address 192.168.0.1 192.168.0.5 // aqui precisa ser o range equivalente a subrede (vlan marcada ou tagged)
ip dhcp pool DHCP-FIN //nome da subrede dhcp
dns-server 192.168.0.2
network 192.168.0.96 255.255.255.224
exit
ip dhcp excluded-address 192.168.0.1 192.168.0.5 // aqui precisa ser o range equivalente a subrede (vlan marcada ou tagged)
ip dhcp pool DHCP-ADM //nome da subrede dhcp
dns-server 192.168.0.2
network 192.168.0.96 255.255.255.224
exit
ip dhcp excluded-address 192.168.0.1 192.168.0.5 // aqui precisa ser o range equivalente a subrede (vlan marcada ou tagged)
ip dhcp pool DHCP-VEN //nome da subrede dhcp
dns-server 192.168.0.2
network 192.168.0.96 255.255.255.224
exit
ip dhcp excluded-address 192.168.0.1 192.168.0.5 // aqui precisa ser o range equivalete a subrede (vlan marcada ou tagged)
ip dhcp pool DHCP-VEN //nome da subrede dhcp
dns-server 192.168.0.2
network 192.168.0.96 255.255.255.224
exit
copy running-config startup-config // ou apenas write



precisamos excluir o servidor da abrangencia dos ips dhcp, pois serviços como servidores, impressoras, bancos de dados não podem receber um ip dinamicamente a cada reboot do sistema, pois precisam ser enontrados na rede independentemente de seu reboot; para isso um a boa prática em topologias de rede é manter os 5 primeiros IPs de uma rede para esses serviços
