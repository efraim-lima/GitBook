# Configuração de Switches 08-27-2024

Aqui temos o processo de configuração de uma rede que utiliza switches camada 2 e o script que pode ser utlizado para esta configuração. Tentarei anexar os scripts aqui e deixar em texto plano também.

{% file src="../../../../../.gitbook/assets/configuracao-switches-08272024.txt" %}

\##SWITCH camada 2

## não possui segurança aprofundada, no caso teremos segurança aplicada ao switches a partir do camada 3

\#configuração dos switches convencionais, lembrar-se de alterar a ID da vlan e o hostname locais em "switchport access vlan XX" e "hostname XXX" respectivamente.

enable
configure terminal
interface range FastEthernet 0/1-5
switchport mode trunk
interface range FastEthernet 0/6-24
switchport access vlan 50
exit
hostname ENG
vlan 10
name DCE
vlan 20
name ADM
vlan 30
name VEN
vlan 40
name FIN
vlan 50
name ENG
vlan 60
name MAN
exit
spanning-tree vlan 10 priority 0
spanning-tree vlan 20 priority 0
spanning-tree vlan 30 priority 0
spanning-tree vlan 40 priority 0
spanning-tree vlan 50 priority 0
spanning-tree vlan 60 priority 0

\#configurar os swithes apenas até a porta 5 e os hosts a partir da 6, para que a comunicação seja restringida naquela vlan para os hosts a partir desta porta

\#vlan do tipo tronco permite que noo mesmo router passem muitas VLANs para garantir que, caso um link caia exista redundancia, o modo ACCESS permite que haja apenas uma VLAN no mesmo, agora o modo TRUNK permite que varias vlans habitem no mesmo switch.

\#CTRL + SHIFT + 6 dá o scape para o ponto de domain server translate (DNS solver)

## Apens para o caso do switch core, acrescentar ao nivel de configure terminal:

interface FastEthernet 0/6
switchport access vlan 10
exit
interface FastEthernet 0/7
switchport access vlan 20
exit
interface FastEthernet 0/8
switchport access vlan 30
exit
interface FastEthernet 0/9
switchport access vlan 40
exit
interface FastEthernet 0/10
switchport access vlan 50
exit
interface FastEthernet 0/11
switchport access vlan 60
exit

\#configuração do router: cada interface precisa ter um IP específico pois estas serão os gateways padrão de cada switch, e estes IPs precisam ser os primeiros IPs úteis de cada cada rede presente em cada switch; imprescindível inserir mais interfaces no roteador para comportar a quantidade de interfaces, no caso foram inseridos 4 Ethernets para comportar as conexões

enable
configure terminal
hostname ROUTER-CORE
interface FastEthernet0/0
ip address 192.168.0.1 255.255.255.192
no shutdown
exit
interface FastEthernet0/1
ip address 192.168.0.65 255.255.255.224
no shutdown
exit
interface Ethernet1/0
ip address 192.168.0.97 255.255.255.224
no shutdown
exit
interface Ethernet1/1
ip address 192.168.0.129 255.255.255.192
no shutdown
exit
interface Ethernet1/2
ip address 192.168.0.193 255.255.255.224
no shutdown
exit
interface Ethernet1/3
ip address 192.168.0.225 255.255.255.224
no shutdown
exit

\#ao final não podemos esquecer: copy running-config startup-config