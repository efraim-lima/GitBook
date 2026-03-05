# Hints

nformações importantes a serem guardadas para perícias forenses:

\
&#x20;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/WINDOWS







Para dicas de SOC neste sistema operacional: [windows](../../../../../soc/tools/operational-systems/windows/ "mention")

ESTUDAR CMDLETS

* Os dados que o arquivo contém são armazenados no atributo $DATA;
* fluxos de dados alternativos (ADSs) podem ser usados para injetar malwares no sistema pois é facil ocultar dados em um ADS. Ex.: No sistema de arquivos NTFS, um arquivo com um ADS é identificado após o nome do arquivo e dois pontos, por exemplo, Testfile.txt:ADS.
* pra ver se há um arquivo ads no Windows precisamos usar o atributo dir /r.

&#x20;

\
ENCONTRAR DADOS DO FABRICANTE:

* Systeminfo : todos os dados do PC como fabricantes, placas NAT, chipset e afins
* Get-Ciminstance Win32\_Bios | Format-List Serialnumber,Manufacturer,Product: dados como numero de serie do dispositivo

&#x20;

A tabela lista alguns comandos que você pode usar. Digite help seguido do comando para saber mais sobre o comando.

| Comando MS-DOS              | Descrição                                                             |
| --------------------------- | --------------------------------------------------------------------- |
| dir                         | Mostra uma lista de todos os arquivos no diretório atual (pasta)      |
| cd diretório                | Altera o diretório para o diretório indicado                          |
| cd ..                       | Muda o diretório para o diretório acima do diretório atual            |
| cd \\                       | Muda o diretório para o diretório raiz (geralmente C:)                |
| copy fonte de destino       | Copia arquivos para outro local                                       |
| del nome do arquivo         | Exclui um ou mais arquivos.                                           |
| find                        | Procura texto em arquivos                                             |
| mkdir diretório             | Cria um novo diretório.                                               |
| ren nome\_antigo nome\_novo | Renomeia um arquivo                                                   |
| help                        | Exibe todos os comandos que podem ser usados, com uma breve descrição |
| help comando                | Exibe a ajuda extensa para o comando indicado                         |

\
&#x20;

Há dois itens de registro importantes que são usados para iniciar automaticamente aplicativos e serviços:

* HKEY\ \_LOCAL\ \_MACHINE - Vários aspectos da configuração do Windows são armazenados nesta chave, incluindo informações sobre serviços que começam com cada inicialização.
* HKEY\ \_CURRENT\ \_USER - Vários aspectos relacionados ao usuário conectado são armazenados nesta chave, incluindo informações sobre serviços que iniciam somente quando o usuário faz logon no computador.
* HKKEY\_LOCAL\_MACHINE - All of the configuration settings for the hardware and software configured on the computer for all users.
* HKEY\_CURRENT\_USER - Data about the preferences of the currently logged on user, including personalization settings, default devices, and programs, etc.
* HKEY\_CLASSES\_ROOT - Settings about the file system, file associations, shortcuts used when you ask Windows to run a file, or view a directory.
* HKEY\_CURRENT\_CONFIG- Information about the current hardware profile of the machine

&#x20;

Teclar Win + R e acionar:

* netplwiz: verificar se usuários são os corretos;
* msconfig: Ir em opções avançadas de INICIALIZAÇÃO e ver se os processadores estão bloqueados;
* mrt: fazer varredura e limpeza da máquina;

&#x20;

Teclar Ctrl + Shift + Win + B para reiniciar a placa grafica\
&#x20;

Msconfig.exe: Essa ferramenta é usada para exibir e alterar todas as opções de inicialização do computador. Use a caixa de pesquisa para localizar e abrir a ferramenta Msconfig.

* tipos de inicialização diferentes podem ser escolhidos aqui. Geral, Diagnóstico e Seletivo.
* qualquer sistema operacional instalado pode ser escolhido aqui para iniciar.
* todos os serviços instalados estão listados aqui para que possam ser escolhidos para iniciar na inicialização.
* ferramentas comuns do sistema operacional podem ser iniciadas diretamente a partir desta guia

\
&#x20;

RAMMap fornece uma riqueza de informações sobre como o Windows alocou memória do sistema para o kernel, processos, drivers e aplicativos.

\
&#x20;

As chaves do Registro e os valores nas seções podem ser criados, modificados ou excluídos por uma conta com privilégios administrativos. Como mostrado na figura, a ferramenta regedit.exe é usada para modificar o registro.

&#x20;

A tabela lista os cinco ramos do registro do Windows.

| Seção (Hive) do Registro     | Descrição                                                                                                                                                                                                                  |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HKEY\_CURRENT\_USER (HKCU)   | Contém informações sobre o usuário conectado no momento.                                                                                                                                                                   |
| HKEY\_USERS (HKU)            | Contém informações relativas a todas as contas de usuário no host.                                                                                                                                                         |
| HKEY\_CLASSES\_ROOT (HKCR)   | Contém informações sobre registros OLE (vinculação e incorporação de objetos). OLE permite que os usuários incorporem objetos de outros aplicativos (como uma planilha) em um único documento (como um documento do Word). |
| HKEY\_LOCAL\_MACHINE (HKLM)  | Contém informações relacionadas ao sistema.                                                                                                                                                                                |
| HKEY\_CURRENT\_CONFIG (HKCC) | Contém informações sobre o perfil de hardware atual.                                                                                                                                                                       |

\
&#x20;

As chaves do Registro podem conter uma subchave ou um valor. Os diferentes valores que as chaves podem conter são os seguintes:

* REG\ \_BINARY - Números ou valores booleanos
* REG\ \_DWORD - Números maiores que 32 bits ou dados brutos
* REG\ \_SZ - Valores de cadeia

\
&#x20;

Como o registro contém quase toda infomação do sistema operacional e do usuário, é essencial garantir que ele não seja comprometido. Aplicativos potencialmente mal-intencionados podem adicionar chaves do Registro para que elas sejam iniciadas quando o computador for iniciado.

\
&#x20;

O registro também contém a atividade que um usuário executa durante o uso diário normal do computador. Isso inclui o histórico de dispositivos de hardware, incluindo todos os dispositivos que foram conectados ao computador, incluindo o nome, o fabricante e o número de série. Outras informações, como quais documentos um usuário e um programa abriram, onde eles estão localizados e quando foram acessados, são armazenadas no registro.

\
&#x20;

Há quatro níveis de ajuda no Windows PowerShell:

* get-help PS command - Exibe a ajuda básica para um comando
* get-help PS command\ \[\ -examples] - Exibe a ajuda básica para um comando com exemplos
* get-help PS command\ \[\ -detailed] - Exibe ajuda detalhada para um comando com exemplos
* get-help PS command\ \[\ -full] - Exibe todas as informações de ajuda de um comando com exemplos em maior profundidade

\
&#x20;

A Instrumentação de Gerenciamento do Windows (WMI) é usada para gerenciar computadores remotos. Ele pode recuperar informações sobre componentes de computador, estatísticas de hardware e software e monitorar a integridade de computadores remotos. Para abrir o controle WMI a partir do Painel de Controle, clique duas vezes em Ferramentas Administrativas > Gerenciamento do Computador para abrir a janela Gerenciamento do Computador, expanda a árvore Serviços e Aplicativos e clique com o botão direito do mouse no ícone Controle WMI > Propriedades.

\
&#x20;

Estas são as quatro guias na janela Propriedades de Controle WMI:

* Geral - Informações resumidas sobre o computador local e o WMI
* Backup/Restore - Permite backup manual de estatísticas coletadas pelo WMI
* Segurança - Configurações para configurar quem tem acesso a diferentes estatísticas WMI
* Avançado - Configurações para configurar o namespace padrão para WMI

&#x20;

A tabela lista alguns comandos net comuns.

| Comando      | Descrição                                                                     |
| ------------ | ----------------------------------------------------------------------------- |
| net accounts | Define os requisitos de senha e logon para usuários                           |
| net session  | Lista ou desconecta sessões entre um computador e outros computadores na rede |
| net share    | Cria, remove ou gerencia recursos compartilhados                              |
| net start    | Inicia um serviço de rede ou lista os serviços de rede em execução            |
| net stop     | Para um serviço de rede                                                       |
| net use      | Conecta, desconecta e exibe informações sobre recursos de rede compartilhados |
| net view     | Mostra uma lista de computadores e dispositivos de rede na rede               |

&#x20;

A tabela descreve as sete guias no Gerenciador de Tarefas.

| Guias do gerenciador de tarefas | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Processos                       | <ul><li><p></p><ul><li>Lista todos os programas e processos que estão em execução no momento.</li><li>Exibe a utilização da CPU, da memória, do disco e da rede de cada processo.</li><li>As propriedades de um processo podem ser examinadas ou encerradas se ele não estiver se comportando corretamente ou tiver parado.</li></ul></li></ul>                                                                                                                                                                                                                                                      |
| Desempenho                      | <ul><li><p></p><ul><li>Uma exibição de todas as estatísticas de desempenho fornece uma visão geral útil do desempenho da CPU, memória, disco e rede.</li><li>Clicar em cada item no painel esquerdo irá mostrar estatísticas detalhadas desse item no painel direito.</li></ul></li></ul>                                                                                                                                                                                                                                                                                                            |
| Histórico de aplicativos        | <ul><li><p></p><ul><li>O uso de recursos por aplicativo ao longo do tempo fornece informações sobre aplicativos que estão consumindo mais recursos do que deveriam.</li><li>Clique em Opções e Mostrar histórico de todos os processos para ver o histórico de todos os processos executados desde que o computador foi iniciado.</li></ul></li></ul>                                                                                                                                                                                                                                                |
| Inicializar                     | <ul><li><p></p><ul><li>Todos os aplicativos e serviços que iniciam quando o computador é inicializado são mostrados nesta guia.</li><li>Para desativar o início de um programa na inicialização, clique com o botão direito do mouse no item e escolha Desativar.</li></ul></li></ul>                                                                                                                                                                                                                                                                                                                |
| Usuários                        | <ul><li><p></p><ul><li>Todos os usuários que estão conectados ao computador são mostrados nesta guia.</li><li>Também são mostrados todos os recursos que os aplicativos e processos de cada usuário estão usando.</li><li>Nesta guia, um administrador pode desconectar um usuário do computador.</li></ul></li></ul>                                                                                                                                                                                                                                                                                |
| Detalhes                        | <ul><li><p></p><ul><li>Semelhante à guia Processos, essa guia fornece opções de gerenciamento adicionais para processos, como definir uma prioridade para que o processador dedique mais ou menos tempo a um processo.</li><li>A afinidade da CPU também pode ser definida, o que determina qual núcleo ou CPU um programa usará.</li><li>Além disso, um recurso útil chamado Analisar cadeia de espera mostra qualquer processo para o qual outro processo está aguardando.</li><li>Esse recurso ajuda a determinar se um processo está simplesmente aguardando ou está parado.</li></ul></li></ul> |
| Serviços                        | <ul><li><p></p><ul><li>Todos os serviços que são carregados são mostrados nesta guia.</li><li>O ID do processo (PID) e uma breve descrição também são mostrados juntamente com o status de Executando ou Parado.</li><li>Na parte inferior, há um botão para abrir o console Serviços que fornece gerenciamento adicional de serviços.<br> </li></ul></li></ul>                                                                                                                                                                                                                                      |

A tabela descreve as cinco guias do Monitor de Recursos.

| Guias do Monitor de Recursos | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Visão geral                  | <ul><li><p></p><ul><li>A guia exibe o uso geral de cada recurso.</li><li>Se você selecionar um único processo, ele será filtrado em todas as guias para mostrar somente as estatísticas desse processo.</li></ul></li></ul>                                                                                                                                                                                                                                                                                                                      |
| CPU                          | <ul><li><p></p><ul><li>O PID, o número de threads, qual CPU o processo está usando e o uso médio da CPU de cada processo é mostrado.</li><li>Informações adicionais sobre quaisquer serviços em que o processo se baseia e os identificadores e módulos associados podem ser vistas expandindo as linhas inferiores.</li></ul></li></ul>                                                                                                                                                                                                         |
| Memória                      | <ul><li><p></p><ul><li>Todas as informações estatísticas sobre como cada processo usa memória são mostradas nesta guia.</li><li>Além disso, uma visão geral do uso de toda a RAM é mostrada abaixo da linha Processos.</li></ul></li></ul>                                                                                                                                                                                                                                                                                                       |
| Disco                        | Todos os processos que estão usando um disco são mostrados nesta guia, com estatísticas de leitura/gravação e uma visão geral de cada dispositivo de armazenamento.                                                                                                                                                                                                                                                                                                                                                                              |
| Rede                         | <ul><li><p></p><ul><li>Todos os processos que estão usando a rede são mostrados nesta guia, com estatísticas de leitura/gravação.</li><li>Mais importante ainda, as conexões TCP atuais são mostradas, juntamente com todas as portas que estão escutando.</li><li>Esta guia é muito útil ao tentar determinar quais aplicativos e processos estão se comunicando pela rede.</li><li>Permite saber se um processo não autorizado está acessando a rede, ouvindo uma comunicação e o endereço com o qual está se comunicando.</li></ul></li></ul> |

\
&#x20;

nslookup and netstat

O Sistema de Nomes de Domínio (DNS, Domain Name System) também deve ser testado porque é essencial encontrar o endereço dos hosts traduzindo-o a partir de um nome, como uma URL. Use o comando nslookup para testar o DNS. Digite nslookup [cisco.com](http://cisco.com/) no prompt de comando para localizar o endereço do servidor Web Cisco. Quando o endereço é retornado, você sabe que o DNS está funcionando corretamente. Você também pode verificar quais portas estão abertas, onde elas estão conectadas e qual é seu status atual. Digite netstat na linha de comando para ver detalhes das conexões de rede ativas, conforme mostrado na saída do comando. O comando netstat será examinado mais adiante neste módulo.

&#x20;

C:\Users\USER >netstat

&#x20;

&#x20;

Ir até virtualização da maquina e ajustar manualmente início e fim da memória para o tamanho da RAM para aliviar a %PAGE FILE SYS

&#x20;

Organizar a estrutura de memoria do Windows constantemente

&#x20;

&#x20;

ADICIONAR ARQUIVOS AO PATH DO SISTEMA

&#x20;

Acessar o terminal e digitar:

setx Path "%Path%;C:\Program Files\\\<PROGRAMA>\\"
