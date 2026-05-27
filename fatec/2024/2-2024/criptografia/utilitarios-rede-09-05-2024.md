Utilitarios para camadas especificas de rede

1. **Camada 1 - Física**
   - **[[soc/tools/operational-systems/windows/windows|windows]]**: Não há [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]] específicas para esta camada, mas você pode verificar a interface de rede usando o "Gerenciador de Dispositivos" e verificar o status do hardware.
   - **[[soc/tools/operational-systems/linux/linux|linux]]**: `dmesg` pode mostrar informações sobre o hardware de rede detectado. `ethtool` também pode fornecer detalhes sobre a interface de rede.

2. **Camada 2 - Enlace de Dados**
   - **[[soc/tools/operational-systems/windows/windows|windows]]**: `ipconfig /all` mostra detalhes sobre a configuração da interface de rede, e o "Monitor de Recursos" pode ajudar a visualizar o tráfego.
   - **[[soc/tools/operational-systems/linux/linux|linux]]**: `ifconfig` (ou `ip a` no novo padrão) fornece detalhes sobre as interfaces. `tcpdump` ou `wireshark` podem capturar pacotes para análise de problemas nesta camada.

3. **Camada 3 - Rede**
   - **[[soc/tools/operational-systems/windows/windows|windows]]**: `tracert` (traceroute) pode ser usado para rastrear o caminho dos pacotes até o destino. `ping` verifica a conectividade.
   - **[[soc/tools/operational-systems/linux/linux|linux]]**: `traceroute` e `ping` são utilizados da mesma forma. `mtr` combina a funcionalidade de `ping` e `traceroute` para fornecer informações detalhadas sobre a rota e a latência.

4. **Camada 4 - Transporte**
   - **[[soc/tools/operational-systems/windows/windows|windows]]**: `netstat` fornece informações sobre conexões de rede e [[portas]] abertas. `tcpview` oferece uma interface gráfica para ver conexões [[tcp]] e UDP.
   - **[[soc/tools/operational-systems/linux/linux|linux]]**: `netstat` (ou `ss` para uma versão mais recente e rápida) fornece informações sobre as conexões e [[portas]] abertas. `tcpdump` também pode capturar e analisar o tráfego de transporte.

5. **Camada 5 - Sessão**
   - **[[soc/tools/operational-systems/windows/windows|windows]]**: Não há [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]] específicas para a camada de sessão, mas você pode usar [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]] gerais de rede para observar a configuração e o gerenciamento de sessões de conexão.
   - **[[soc/tools/operational-systems/linux/linux|linux]]**: Similar ao [[soc/tools/operational-systems/windows/windows|windows]], não há [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]] específicas, mas você pode observar o comportamento de sessão usando `tcpdump` ou `wireshark`.

6. **Camada 6 - [[Apresentação]]**
   - **[[soc/tools/operational-systems/windows/windows|windows]]**: Não há [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]] específicas para esta camada, pois é mais voltada para a codificação e decodificação de dados.
   - **[[soc/tools/operational-systems/linux/linux|linux]]**: Similar ao [[soc/tools/operational-systems/windows/windows|windows]], geralmente, a análise é feita em camadas superiores ou com [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]] de [[fatec/Pesquisa/Pesquisa/ferramentas/desenvolvimento|desenvolvimento]] que tratam da codificação e decodificação de dados.

7. **Camada 7 - Aplicação**
   - **[[soc/tools/operational-systems/windows/windows|windows]]**: [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]] como `Wireshark` e `Fiddler` podem ajudar a analisar o tráfego da camada de aplicação. `netsh` também pode ser usado para monitorar e configurar opções de rede.
   - **[[soc/tools/operational-systems/linux/linux|linux]]**: `Wireshark` e `tcpdump` são úteis para capturar e analisar pacotes. `curl` e `wget` ajudam a testar e interagir com serviços da camada de aplicação.

Essas [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]] e utilitários podem ajudar a diagnosticar e resolver problemas em diferentes camadas do modelo [[osi]].
