[[Desenvolvimento]]

# DogSniffer App

## Motivação

Esta ferramenta foi desenvolvida com o objetivo de levantar através de sinais de rádio frequencia ([[wifi]]) a posição estivada da origem do sinal.
Foi desenvolvida em [[Java]] para fins de aprendizado do desenvolvedor Efraim Lima, mas o objetivo é ter uma forma de tornar este código aplicável a outras plataformas além do [[soc/tools/operational-systems/linux/linux|linux]].


### Tree map
A estrutura das pastas segue o seguinte tree map:

src/main/[[Java]]/
├── DogSnifferApp.[[Java]]              ← sem package (entry point)
├── cache/
│   ├── SignalCache.[[Java]]            ← estrutura de cache do sinal
│   └── CacheEntry.[[Java]]             ← getters dos sinais
├── display/
│   └── RadarDisplay.[[Java]]           ← forma de renderizar visualmente o que tem sido capturado
├── etc/
│   ├── Capture.[[Java]]                ← vai ser refatorado para [[fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] próximos commits
│   ├── NetworkInterfaceSelector.[[Java]]
│   ├── Configuration.[[Java]]          ← vamos extrair de NetworkInterfaceSelector
│   └── NetworkSelectionException.[[Java]]
├── network/
│   ├── NetworkInfo.[[Java]]            ← coleta de informações das redes (Mac, SSID, segurança, RSSI, etc)
│   └── PacketProcessor.[[Java]]        ← conecta-se com Capture.[[Java]]
└── sensor/
    ├── SensorData.[[Java]]             ← dados do sensor para termos uma boa visão da direção do sinal (sensor ainda não chegou, esta parte está sendo desenvolvida para termos já um pivot)
    └── WitMotionReader.[[Java]]


### Fim por hora