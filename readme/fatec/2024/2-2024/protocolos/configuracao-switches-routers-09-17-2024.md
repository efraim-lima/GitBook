# Configurando serviço DHCP na rede com um roteador 

enable
configure terminal
username Efraim password 12345
ip domain-name efraim.com.br
crypto key generate rsa general-keys modulus 1024
ip ssh version 2
enable secret pastel
line vty 0 4
password pastelaria
login
transport input ssh
exit
banner motd @ *** ACESSO RESTRITO FATEC SCS *** @
line console 0
password pastel2
login
exit
service password-encryption
interface gig0/0
no shutdown
exit
interface gig0/0.10
encapsulation dot1q 10
ip address 192.168.0.1 255.255.255.192
exit
interface gig0/0.20
encapsulation dot1q 20
ip address 192.168.0.65 255.255.255.224
exit
interface gig0/0.30
encapsulation dot1q 30
ip address 192.168.0.97 255.255.255.224
exit
interface gig0/0.40
encapsulation dot1q 40
ip address 192.168.0.129 255.255.255.192
exit
interface gig0/0.50
encapsulation dot1q 50
ip address 192.168.0.193 255.255.255.224
exit
interface gig0/0.60
encapsulation dot1q 60
ip address 192.168.0.225 255.255.255.224
exit
ip dhcp excluded-address 192.168.0.1 192.168.0.5
ip dhcp excluded-address 192.168.0.65 192.168.0.69
ip dhcp excluded-address 192.168.0.97 192.168.0.101
ip dhcp excluded-address 192.168.0.129 192.168.0.133
ip dhcp excluded-address 192.168.0.193 192.168.0.197
ip dhcp excluded-address 192.168.0.225 192.168.0.229
ip dhcp excluded-address 192.168.0.62
ip dhcp excluded-address 192.168.0.94
ip dhcp excluded-address 192.168.0.126
ip dhcp excluded-address 192.168.0.190
ip dhcp excluded-address 192.168.0.222
ip dhcp excluded-address 192.168.0.254
ip dhcp pool DHCP-DCE
default-router 192.168.0.1
dns-server 192.168.0.2
network 192.168.0.0 255.255.255.192
exit
ip dhcp pool DHCP-ADM
default-router 192.168.0.65
dns-server 192.168.0.2
network 192.168.0.64 255.255.255.224
exit
ip dhcp pool DHCP-VEN
default-router 192.168.0.97
dns-server 192.168.0.2
network 192.168.0.96 255.255.255.224
exit
ip dhcp pool DHCP-FIN
default-router 192.168.0.129
dns-server 192.168.0.2
network 192.168.0.128 255.255.255.192
exit
ip dhcp pool DHCP-ENG
default-router 192.168.0.193
dns-server 192.168.0.2
network 192.168.0.192 255.255.255.224
exit
ip dhcp pool DHCP-MAN
default-router 192.168.0.225
dns-server 192.168.0.2
network 192.168.0.224 255.255.255.224
end
copy running-config startup-config



