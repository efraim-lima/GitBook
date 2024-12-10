# Linux

Para analisar logs no linux:

&#x20;

cd /var/log

cat auth.logs | grep "string" | grep "string2" | cut -d " " -f 11 | sort | uniq

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

uniq -d

wc -l

<table><thead><tr><th width="153">Comando</th><th width="258">Descrição</th><th>Exemplo</th></tr></thead><tbody><tr><td>ifconfig</td><td>Apresenta informações das interfaces e podemos configurar as interfaces também</td><td>ifconfig<br>ifconfig [Interface] [IP]</td></tr><tr><td>ip</td><td>Assim como infconfig, serve para apresentar informações de rede das interfaces e para configurar tais interfaces também</td><td>ip -a<br>ip addr add [IP] dev [Interface]<br>ip link set [Interface] up<br>ip route add [NetID] via [gateway IP]</td></tr><tr><td>iwconfig</td><td>Aqui podemos configurar uma rede wireless no dispositivo</td><td>iwconfig [Interface] essid [SSID]</td></tr><tr><td>nmtui</td><td>Um editor de rede que utiliza uma interface de usuário baseada em terminal</td><td>nmtui<br>nmtui-connect<br>nmtui-edit</td></tr><tr><td>ethtool</td><td>apresentar ou mudar configurações na placa de rede</td><td>ethtool [Interface]</td></tr><tr><td>route</td><td>Conseguimos aqui editar as tabelas de roteamento, para configurar o alcance de nossa rede</td><td>route<br>route add default gw [gateway IP]<br>route add nat [IP] subnetmask [mascara de rede] gw [gatewayIP]</td></tr><tr><td>mtr</td><td>Ferramenta de diagnóstico da rede</td><td>mtr [website]</td></tr><tr><td>ping</td><td>utilitãrio eficiente para testar conexão com as redes</td><td>ping [website/IP]</td></tr><tr><td>fping</td><td>para pingar multiplos IPs</td><td>fping -a -g [IP][IP]</td></tr><tr><td>traceroute</td><td>apresenta os saltos ocorridos entre os nós de rede</td><td>traceroute [website/IP]</td></tr><tr><td>netstat</td><td></td><td></td></tr><tr><td>iperf</td><td></td><td></td></tr><tr><td>ss</td><td></td><td></td></tr><tr><td>nc</td><td></td><td></td></tr><tr><td>nload</td><td></td><td></td></tr><tr><td>hostname</td><td></td><td></td></tr><tr><td>hostnamectl</td><td></td><td></td></tr><tr><td>dig</td><td></td><td></td></tr><tr><td>nslookup</td><td></td><td></td></tr><tr><td>resolvconf</td><td></td><td></td></tr><tr><td>nmcli</td><td></td><td></td></tr><tr><td>host</td><td></td><td></td></tr><tr><td>iptables</td><td></td><td></td></tr><tr><td>iftop</td><td></td><td></td></tr><tr><td>iptraf</td><td></td><td></td></tr><tr><td>ufw</td><td></td><td></td></tr><tr><td>tcpdump</td><td></td><td></td></tr><tr><td>ssh-keygen</td><td></td><td></td></tr><tr><td>sshd</td><td></td><td></td></tr><tr><td>telnet</td><td></td><td></td></tr><tr><td>scp</td><td></td><td></td></tr><tr><td>wget</td><td></td><td></td></tr><tr><td>curl</td><td></td><td></td></tr><tr><td>nmap</td><td></td><td></td></tr><tr><td>lsof</td><td></td><td></td></tr><tr><td>ethtool</td><td></td><td></td></tr><tr><td>arp</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></tbody></table>







