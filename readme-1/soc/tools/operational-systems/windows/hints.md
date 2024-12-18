# Hints

Malware Analysis in SOC

[https://explorer.globe.engineer/search?qd=%5B%7B%22searchbox\_query%22%3A%22malware%20analisys%20SOC%20%22%2C%22search\_id%22%3A%2293f9fe5f-3bea-4390-8928-f0f51e1f3429%22%2C%22index%22%3A0%2C%22type%22%3A%22initial\_searchbox%22%2C%22clicked\_category%22%3Anull%2C%22staged\_image%22%3Anull%7D%5D\&sid=93f9fe5f-3bea-4390-8928-f0f51e1f3429](https://explorer.globe.engineer/search?qd=%5B%7B%22searchbox_query%22%3A%22malware%20analisys%20SOC%20%22%2C%22search_id%22%3A%2293f9fe5f-3bea-4390-8928-f0f51e1f3429%22%2C%22index%22%3A0%2C%22type%22%3A%22initial_searchbox%22%2C%22clicked_category%22%3Anull%2C%22staged_image%22%3Anull%7D%5D\&sid=93f9fe5f-3bea-4390-8928-f0f51e1f3429)

&#x20;

Malware Diagnosis

[https://explorer.globe.engineer/search?qd=%5B%7B%22searchbox\_query%22%3A%22malware%20diagnosis%20in%20PC%20linux%20and%20windows%22%2C%22search\_id%22%3A%224fc49bed-77c0-41fc-a2c1-62a899c59987%22%2C%22index%22%3A0%2C%22type%22%3A%22initial\_searchbox%22%2C%22clicked\_category%22%3Anull%2C%22staged\_image%22%3Anull%7D%5D\&sid=4fc49bed-77c0-41fc-a2c1-62a899c59987](https://explorer.globe.engineer/search?qd=%5B%7B%22searchbox_query%22%3A%22malware%20diagnosis%20in%20PC%20linux%20and%20windows%22%2C%22search_id%22%3A%224fc49bed-77c0-41fc-a2c1-62a899c59987%22%2C%22index%22%3A0%2C%22type%22%3A%22initial_searchbox%22%2C%22clicked_category%22%3Anull%2C%22staged_image%22%3Anull%7D%5D\&sid=4fc49bed-77c0-41fc-a2c1-62a899c59987)

&#x20;

Sysinternals Microsoft

GLPI para gerar tickets de alerta

&#x20;

Desabilitar leitura automática de USB – montar ou montagem automatica

&#x20;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/WINDOWS

* Entrar no editor de registror do windows
*
  * Win + R => regedit => Computer\HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\mountmgr
  *
    * Criar uma DWORD em hexadecimal chamada NoAutoMount
    * Double Click nela
    *
      * Mudar valor de 1 para 0 (disable to enable)
  * Win + R => regedit =>  Computer\HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\USBSTOR
  *
    * Criar um novo valor DWORD chamado "PreventDeviceEnumeration"
    * definir-lo como 1
  * Win + R => regedit => Computer\HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\USBSTOR
  *
    * Criar um novo valor DWORD chamado "PreventAutomaticMounting"
    * Definir-lo como 1
  * Reiniciar o computador para receber as mudanças
* Caso queira montar alguma unidade segura após isto basta digitar Win + X e ir em Gerenciador de Dispositivos

&#x20;

Outra alternativa para montagem de unidades no windows:\
&#x20;

* Abriir terminal ou powershell e acessar configurações de dispositivos de memoria:
*
  * diskpart
  * automount disable
  * mountvol /n
  * mountvol /r
  * Para reabilitar:
  *
    * automount enable
    * | Mountvol /e |   |
      | ----------- | - |
  * Para limpar histórico de unidades montadas anteriormente:
  *
    * automount scrub

&#x20;

Para voltarmos a montar as unidades USB normalmente:

diskpart

list disk

select disk 2

assign letter=E

&#x20;

Por fim vale a pena ainda gerar o AutoPlay:\
-ir em Settings => Devices => AutoPlay => Desabilitar

&#x20;

verificar arquivos de hosts e ver IPs redirecionados

&#x20;

Para montar uma unidade USB desconhecida, recomendo abri-la em uma máquina virtual isolada para isso.\
Dica:

&#x20;

Primeiro instale o "apt install clamav clamav-daemon" e faça um "clamscan -r \<pasta>" ou "clamscan -v \<pasta>"

Caso tenha duvidas da veracidade e qualidade do material recomendo fortemente formatar a mídia com os passos a seguir:\
\
lsblk => listar os dispositivos conectados

umount /dev/\<nome da unidade sd?> => desmonta a unidade sd

sudo dd if=/dev/zero of=/dev/\<nome da unidade sd?> bs=4M status=progress => escreve um tudo em 00 na unidade

sudo mkfs.vfat /dev/\<nome da unidade sd?> => formata para fat32 #mais rápido

sudo mkfs.ext4 /dev/\<nome da unidade sd?>  => formata para ext64

sudo eject /dev/\<nome da unidade sd?> => ejeta o dispositivo

&#x20;

&#x20;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/WINDOWS

Windows ->  C:\Windows\System32\drivers\etc\hosts

As ferramentas comuns que são usadas para monitoramento de segurança de rede incluem:

* Analisadores de protocolo de rede como Wireshark e Tcpdump
* NetFlow
* Sistemas de gerenciamento de eventos e informações de segurança (SIEM)

Também é comum que analistas de segurança confiem em arquivos de log e SNMP (Simple Network Management Protocol) para detecção de comportamento de rede.

Observação: \*\*windump\*\* é uma variante do Microsoft Windows do \*\*tcpdump\*\*. \*\*tshark\*\* é uma ferramenta de linha de comando Wireshark semelhante a \*\*tcpdump\*\*.

Em caso de encontrar o arquivo lsass.exe no Program Files é  preciso deletá-lo, pode ser um malware.

O NetFlow pode monitorar essa conexão de aplicativo rastreando contagens de bytes e pacotes para esse fluxo de aplicativo individual. Em seguida, envia as estatísticas para um servidor externo chamado coletor NetFlow.

Por exemplo, o Cisco Stealthwatch coleta estatísticas do NetFlow para executar funções avançadas, incluindo:

* Costura de fluxo - Ele agrupa entradas individuais em fluxos.
* Desduplicação de fluxo - Filtra entradas duplicadas de vários clientes NetFlow.
* Costura NAT - Simplifica os fluxos com entradas NAT.

Há um canal Cisco Stealthwatch no YouTube que fornece muitos detalhes sobre o Stealthwatch e seus usos.

Os sistemas SIEM incluem as seguintes funções essenciais:

* Análise forense — A capacidade de pesquisar logs e registros de eventos de fontes em toda a organização. Ele fornece informações mais completas para análise forense.
* Correlação — examina logs e eventos de diferentes sistemas ou aplicativos, acelerando a detecção e reação a ameaças de segurança.
* Agregação - A agregação reduz o volume de dados de eventos consolidando registros de eventos duplicados.
* Reporting - Reporting apresenta os dados de eventos correlacionados e agregados em monitoramento em tempo real e resumos de longo prazo.

O SIEM fornece detalhes sobre a origem da atividade suspeita:

* Informações do usuário, como nome de usuário, status de autenticação, localização.
* Informações do dispositivo, como fabricante, modelo, versão do sistema operacional, endereço MAC, método de conexão de rede e localização.
* Informações de postura, como se o dispositivo é compatível com a política de segurança, tem arquivos antivírus atualizados e é atualizado com os patches de SO mais recentes.&#x20;

Teclar Win + R e acionar:

* netplwiz: verificar se usuários são os corretos;
* msconfig: Ir em opções avançadas de INICIALIZAÇÃO e ver se os processadores estão bloqueados

Cuckoo Sandbox é um sandbox popular sistema de análise de malware livre. Ele pode ser executado localmente e ter amostras de malware enviadas a ele para análise. Existem várias outras sandboxes públicas online. Esses serviços permitem que amostras de malware sejam carregadas para análise. Alguns desses serviços são VirusTotal, Joe Sandbox e CrowdStrike Falcon Sandbox.
