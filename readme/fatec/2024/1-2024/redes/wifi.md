# WiFi

Topologias de wifi:

BSS: Basic service set => em casas em em SOHO ad-hoc -> rede itinerante, vem dos conceitos militares onde todos conseguem se comunicar entre si, sendo capaz de detectar se os soldados estão em ação.

BSS with AP: BSS com Access Point

Wi-fi Direct

ESS: Exteded Service Set => para escolas, campus, sites e plantas --> aqui é importante ter uma área de sobreposição entre um AP e outro, para que o algoritmo da placa de rede possa definir qual rede utilizará no processo. Para isso a placa de rede possui 3 tipos de algoritmos: o mais agressivo (que muda de AP conforme a maior potencia), o mais preguiçoso (que muda de AP apenas na ultima situação, quando o sinal está muito baixo) e o que . O processo de o dispositivo sair de um AP para outro na mesma rede sendo que estão extendidas chamamos de fastroaming.

backhaul: transmissão de internet via ar

LOS: Antenas de microondas e airfider, pode chegar a velocidades equivalentes a fibra ótica, opera em pares de antenas, onde uma está pareada completamente a altura e direção.

A airfider é full duplex, contando com EDX e EAX, podendo ter que contar com antena de redirecionamento para contornar obstáculos que encontram-se no meio do caminho do sinal, pois

Em areas bachaul existe uma área chamada de backhaul, que é a area espacial compreendida entre uma antena e outra, caso haja um obstáculo neste meio o desempenho será afetado, até mesmo arvores em periodo de primavera e verão podem atrapalhar, pois acumulam mais agua.

pesquisar: antena pringles

Mesh: é a amplificação da rede de um AP com o uso de microcontroladores, alguns como o Google Mash podem direcionar a rede para a posição onde seu host está conectado, filtrar a dependência de pacotes que cada um está tend, podendo emitir mais sinal para o que mais demanda.

802.11i

Segurança wireless.

Antigamente tinham hackers que acessavam as redes wifis anotando apenas o BSSID com giz nas paredes dos locais e se conectando àquelas redes.

WPA2 Enterprise: usado junto a um servidor de autenticação, para detectar a credeciais deste user é usado o protocolo EAP. Isso é Determinado pelo usuaruio e o padrão AAA (Accounting, Authorization and Authentication); isso tudo pode ser condigurado em um servidor RADIUS conectado à rede, até mesmo através de uma RaspberryPi

\---> Miscrosoft Active Directory, SAMBA 4 (inclusive o AD não detecta que é Linux)

Em casa: configurar um WPA2 Enterprise, servidor Radius e 2 hosts