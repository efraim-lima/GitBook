# MAC Address

MAC ADDRESS (endereço físico)

Todo mac address tem um SSID que é o noma de arede e um BSSID que é o Mac Address

SSID => nme da rede BSSID => endereço MAC (localiza a placa de rede) --> no momento da aula o MAC foi um hexa com base 16 no padrão Unix, ou seja, FF:FF:FF:FF:FF:FF (usando separadores ":"), em máquinas Windows usa-se o padrão FF-FF-FF-FF-FF-FF, em máquinas IOS ou Cisco usa-se o padrão FFFF.FFFF.FFFF.

MAC = endereço físico (placa de rede) IP = endereço lógico (protocolo de endereçamento) -> ambos se correlacionam

Os primeiros 6 dígitos identificam o fabricante e o numero de série (ou seja, os primeiros 64 bytes)

\--> na prova precisamos prestar atenção ao modelo pedido pelo professor no enunciado para inputar o modelo correto. Também precisamos detectar se a máquina interpreta ou não case sensitive.

Endereços wireless possuem um padrão do fabricante IEEE ("ai triple i" em portuingles)

WPA3 com AES-CCMP é a forma de criptogragia mais avançada atualmente

Vamos atacar uma criptogragia WPA2-Personal que é uma tecnologia usada em locais SOHO (Small Office Home Office) de nome "cabrini"

Flags: CAFE:36AB:479X => está no padrão Cisco IOS, mas com ":", que seria do padrão UNIX e possui um X no final, isso está errado.

Os 6 primeiros bytes identificam para onde o pacote está indo e os 6 demais de onde está vindo

A camada data link é dividida em 2 partes: LLC (Lgical Link Control) e MAC O LLC permite o intercêmbio de informação entre IPv4 e IPv6, para casos onde um protocolo precisa se comunicar com o outro

Na camada física tratamos e frequencia, alcance, tipo de conector, cabos, antenas, potencia, NIC

FRAME ethernet e wireless precisam obrigatoriamente saber o que tem dentro dos frames (quadro) --> a camada LLC traz um código hexadecimal sendo que o 0x0800 corresponde ao IPv4, 0x0806 é o ARP, 0x86DD seria o do IPv6, pesquisar sobre code type do frame ethernet.

\-> FRAME ETHERNET - MTU 1500 (Maximum Transmission Unit) ----> possui quantidade maxima de transporte de 1518, caso precise levar menos do que o permitido de dados 1500 (bytes), ele usa o padding para preencher ----> para transportar um único pacote IP precisa-se fragmentá-lo em 44 frames, pois cada pacote IP possui 65000 bits e o frame suporta \~1500 bits

Header da camada física => Preambolo: 56 bits delimitando o tempo => SFD: Start frame delimiter (10101011) informa o momento onde será enviado o endereço de destino e origem Destino Origem Tam/Type Data Padding => verifica erros CRC (Checagem Redundancia Ciclica) => não é mais usado hoje em dia, antes os bits poderiam ser invertidos ma comunicação, o algorítmo é o CRC-32

Antigamente os Hubs possuiam problemas para transmitir pacotes, pois geravam broadcast em toda a rede gerando tráfgo excessivo e desnecessário;

Para isso criaram-se protocolos de Carrier apenas em ambientes com Hub

CSMA-CD -> Carrier Sense Multiple Access With Collision Detecion ---> evita colisões, roda em nível host ---> a placa de rede faz uma analise para evitar colisões entre pacotes

Dentro do switch isso ja não ocorre, pois ele pega um frame e identifica o MAC Address de todos os componentes conectados a ele, podendo enviar o frame para o dispositivo de destino correto. O switch possui uma tabela iMAC, onde armazena todos os endereços MAC dos respectivos computadores, o nome dessa tabela é CAM (Content Address Memory);

Para conseguirmos configurar inicalmente um switch precisamos usar o Cabo Console, para ter acesso ao sistema operacional do Switch através do protocolo UART; Switch 1 => Switch Edge não em configurações, serve para conectar varios computadores em uma LAN Switch 2 => Switch Gerenciavel, tem configurações de gerenciamento e serve para conectarmos uma VLAN, separando um setor de outro na empresa, mas aí precisamos configurar os gateways Switch 3 => Switch Router, usado no núcleo da rede, onde é mais sensível e precisa de mais conexões, geralmente ele é o Gateway principal

ARP (Address Resolution Protocol)

Diferente da tabela CAM (armazena os endereços MAC das maquinas conectadas ao Switch)

O comando ping usa o protocolo ICMP (Internet Control Message Protocol) e opera na camada 3, ele auxilia o protocolo IP a detectar seu caminho na rede. Podemos chamar o processo de pingar um IP enviaremos um comando "echo request" e receberemos como resposta um "echo reply".

O protocolo ARP (0x0806) é outro auxiliar do comando ping (echo request), ele acontece antes do ping, é enviado antes do ping, como broadcast para o switch. O switch, por sua vez, encaminha este broadcast para os demais dispositivos da rede onde apenas o com IP de destino vai responder com seu endereço MAC para o dispositivo de origem e apenas para ele. A partir daí o dispositivo de origem saberá o endereço MAC do dispositivo de destino e aí sim começara a se comunicar usando o protocolo IPv4 (0x0800), lembrando que IPv6 não precisa de ARP.

Em nossos computadores temos a TABELA ARP, onde armazenamos os endereços MAC das máquinas em nossa rede. Podemos descobrir nossa tabela ARP com o comando arp -a. Esta tabela precisa ser limpa de tempos em tempos pois ela é armazenada

"echo" é um tipo de comando que foi no destino e voltou, este é o conceito.

A ARP funciona na camada 3 e serve para o dispositivo saber quais os MAC Address dos dispositivos que já se conectou, assim o dispositivo final consegue saber qual o MAC Address do Gateway Apenas o Router Switch possui tabela ARP, os demais possuem apenas a CAM

ARP Poisoning: CONSULTAR => SEGMA6, lá possuem as instruções para fazer um ARP Poisoning. Acessar o emulador GMS3 O hacker começa a fazer echo request (ping) para todo lado. No caso é uma Raspberry com um cabo de rede conectada à rede do alvo, a Raspberry fica mapeando a rede em busca de dados dos usuários. Ao mesmo tempo ela ataca as tabelas ARP dos dispositivos zerando elas e se passando pelo switch, nisso ele faz spoofing na rede, sendo um MITM e filtrando todo tráfego que passa na rede.

O switch deve ser protegido com senha e chave no hack.

Ao descobrir um alvo grande ele consegue aplicar engenharia social, como os chefes possuem acesso total à rede como admin

hash => uma função que sintetiza irreversívelmente o conteúdo analisado ------> para aplicar hashing no linux: md5sum , sha256sum , sha564sum

Bits divididos entre rampa de subida (bit 1), rampa de descida (bit 0), a rampa é a frequência de cadenciamento de sincronização

LIÇÃO DE CASA: Ir ao site IPv6.br -> site do comite gestor de internet para popularizar o IPv6, algo que é deficitário em nosso curso; baixar o livro Lab de IPv6, ele vem com uma maquina virtual do Core, da Boeng

Ele ensina sobre como funciona o protocolo em detalhes.

\-------> transferir tabela ASCII excell para este diretório
