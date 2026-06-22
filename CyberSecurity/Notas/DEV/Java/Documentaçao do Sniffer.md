---
Created: 2026-03-04T20:02
Criado em: 2026-03-04T20:02
Criado em 1: 2026-03-04T20:02
Criado por: 2026-03-04T20:02
---
Estou iniciando um sniffer de redes wireless, com o objetivo final de coletar a posição de dispositivos wireless em uma sala ou ambientes diversos.
Para este processo tenho um diagrama direcionando o caminho a ser adotado para que possamos tentar alcançar este objetivo. Tentarei desenvolver em pequenas etapas para ter pequenas vitórias no caminho.
![[Diagrama_de_Criao.png]]
  
Para começar, vamos ter que instalar o Pcap4j
```bash
apt-get install libpcap-dev
```
Em seguida foi criado um documetno na path /src/build.gradle com as seguintes dependencias
```bash
dependencies {
    // O núcleo da biblioteca (essencial para capturar pacotes)
    implementation 'org.pcap4j:pcap4j-core:1.8.2'
    
    // Ajuda o Java a entender a estrutura dos pacotes (como IP, TCP, 802.11)
    implementation 'org.pcap4j:pcap4j-packetfactory-static:1.8.2'
    
    // Necessário para o Java conversar com a biblioteca nativa libpcap do seu Arch Linux
    implementation 'net.java.dev.jna:jna:5.13.0'
}
```
Em seguida deve-se começar a desenvolvar a aplicação, primeiro teremos um modulo que coleta as interfaces de redes, para apontar para o Pcap4j afim de coletar [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] pacotes.