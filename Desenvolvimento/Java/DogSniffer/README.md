# DogSniffer App

## Motivação

Esta ferramenta foi desenvolvida com o objetivo de levantar através de sinais de rádio frequencia (wifi) a posição estivada da origem do sinal.
Foi desenvolvida em Java para fins de aprendizado do desenvolvedor Efraim Lima, mas o objetivo é ter uma forma de tornar este código aplicável a outras plataformas além do Linux.


### Tree map
A estrutura das pastas segue o seguinte tree map:

src/main/java/
├── DogSnifferApp.java              ← sem package (entry point)
├── cache/
│   ├── SignalCache.java            ← estrutura de cache do sinal
│   └── CacheEntry.java             ← getters dos sinais
├── display/
│   └── RadarDisplay.java           ← forma de renderizar visualmente o que tem sido capturado
├── etc/
│   ├── Capture.java                ← vai ser refatorado para os próximos commits
│   ├── NetworkInterfaceSelector.java
│   ├── Configuration.java          ← vamos extrair de NetworkInterfaceSelector
│   └── NetworkSelectionException.java
├── network/
│   ├── NetworkInfo.java            ← coleta de informações das redes (Mac, SSID, segurança, RSSI, etc)
│   └── PacketProcessor.java        ← conecta-se com Capture.java
└── sensor/
    ├── SensorData.java             ← dados do sensor para termos uma boa visão da direção do sinal (sensor ainda não chegou, esta parte está sendo desenvolvida para termos já um pivot)
    └── WitMotionReader.java


### Fim por hora