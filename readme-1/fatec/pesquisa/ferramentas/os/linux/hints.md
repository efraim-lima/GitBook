# Hints

Linux é uma ferramenta flexivel que permite instalação de elementos independetemente e também possui diversas distribuições mantidas por empresas e pela comunidade. Uma distro potente e que será estudada mais pra frente é a Security Onion, que possui a ferramenta Sguil.

&#x20;

Sguil, é o console do analista de segurança cibernética em uma versão especial do Linux chamada Security Onion. O Security Onion é um conjunto de ferramentas de código aberto que trabalham juntas para análise de segurança de rede.

&#x20;

A tabela lista algumas ferramentas que são freqüentemente encontradas em um SOC.

<table data-header-hidden data-full-width="true"><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Ferramenta SOC</td><td>Descrição</td></tr><tr><td>Software de captura de pacotes de rede</td><td><ul><li><p></p><ul><li>Uma ferramenta crucial para um analista de SOC, pois permite observar e entender cada detalhe de uma transação de rede.</li><li>Wireshark é uma ferramenta popular de captura de pacotes.</li></ul></li></ul></td></tr><tr><td>Ferramentas de análise de malware</td><td>Essas ferramentas permitem que os analistas executem e observem com segurança a execução de malware sem o risco de comprometer o sistema subjacente.</td></tr><tr><td>Sistemas de detecção de intrusão (IDSs)</td><td><ul><li><p></p><ul><li>Essas ferramentas são usadas para monitoramento e inspeção de tráfego em tempo real.</li><li>Se qualquer aspecto do tráfego atualmente em fluxo corresponder a qualquer uma das regras estabelecidas, uma ação predefinida será executada.</li></ul></li></ul></td></tr><tr><td>Firewalls</td><td>Este software é usado para especificar, com base em regras predefinidas, se o tráfego tem permissão para entrar ou sair de uma rede ou dispositivo.</td></tr><tr><td>Gerenciadores de log</td><td><ul><li><p></p><ul><li>Os arquivos de log são usados para registrar eventos.</li><li>Como uma rede pode gerar um número muito grande de entradas de log, o software do gerenciador de logs é empregado para facilitar o monitoramento de log.</li></ul></li></ul></td></tr><tr><td>Segurança das informações e gerenciamento de eventos (SIEM)</td><td>Os SIEMs fornecem análise em tempo real de alertas e entradas de log geradas por dispositivos de rede, como IDSs e firewalls.</td></tr><tr><td>Sistemas de emissão de bilhetes</td><td>A atribuição de tíquetes de tarefa, edição e gravação é feita através de um sistema de gerenciamento de tíquetes. Os alertas de segurança são frequentemente atribuídos a analistas por meio de um sistema de emissão de bilhetes.</td></tr></tbody></table>

&#x20;

Para invocar um comando através do shell, basta digitar seu nome. O shell tentará encontrá-lo no caminho do sistema e executá-lo.

A tabela lista comandos básicos do Linux e suas funções.

<table data-header-hidden data-full-width="true"><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Comando</td><td>Descrição</td></tr><tr><td>mv</td><td>Move ou renomeia arquivos e diretórios</td></tr><tr><td>chmod</td><td>Modifica as permissões de arquivos</td></tr><tr><td>chown</td><td>Altera o dono de um arquivo</td></tr><tr><td>dd</td><td>Copia os dados de uma entrada para uma saída</td></tr><tr><td>pwd</td><td>Exibe o nome do diretório atual</td></tr><tr><td>ps</td><td>Lista os processos que estão atualmente em execução no sistema</td></tr><tr><td>su</td><td>Simula um login como outro usuário ou para se tornar um superusuário</td></tr><tr><td>sudo</td><td>Executa um comando como um superusuário, por padrão, ou outro usuário nomeado</td></tr><tr><td>grep</td><td>Usado para pesquisar cadeias de caracteres específicas em um arquivo ou outras saídas de comando. Para pesquisar através da saída de um comando anterior, grep deve ser canalizado no final do comando anterior.</td></tr><tr><td>ifconfig</td><td>Usado para exibir ou configurar informações relacionadas à placa de rede. Se emitido sem parâmetros, o ifconfig exibirá a configuração atual da (s) placa (s) de rede. Observação: Embora ainda esteja amplamente em uso, esse comando está obsoleto. Use o endereço IP em vez disso.</td></tr><tr><td>apt-get</td><td>Usado para instalar, configurar e remover pacotes no Debian e seus derivados. Nota: apt-get é um front-end de linha de comando amigável para o dpkg, o gerenciador de pacotes do Debian. O combo dpkg e apt-get é o sistema de gerenciador de pacotes padrão em todas as derivadas Debian Linux, incluindo Raspbian.</td></tr><tr><td>iwconfig</td><td>Usado para exibir ou configurar informações relacionadas à placa de rede sem fio. Semelhante ao ifconfig, o iwconfig exibirá informações sem fio quando emitido sem parâmetros.</td></tr><tr><td>shutdown</td><td>Desliga o sistema, o desligamento pode ser instruído a executar uma série de tarefas relacionadas ao encerramento, incluindo reiniciar, parar, colocar em suspensão ou expulsar todos os usuários conectados no momento.</td></tr><tr><td>passwd</td><td>Usado para alterar a senha. Se nenhum parâmetro for fornecido, passwd altera a senha do usuário atual.</td></tr><tr><td>cat</td><td>Usado para listar o conteúdo de um arquivo e espera o nome do arquivo como parâmetro. O comando cat geralmente é usado em arquivos de texto.</td></tr><tr><td>man</td><td>Usado para exibir a documentação de um comando específico.</td></tr><tr><td>history</td><td>Mostra o histórico de comandos emitidos no terminal em ordem de entrada</td></tr></tbody></table>

&#x20;

Muitas ferramentas de linha de comando estão incluídas no Linux por padrão. Para ajustar a operação do comando, os usuários podem passar parâmetros e opções junto com o comando. A tabela lista alguns dos comandos mais comuns relacionados a arquivos e diretórios.

| Comando | Descrição                                                                             |
| ------- | ------------------------------------------------------------------------------------- |
| ls      | Exibe os arquivos dentro de um diretório                                              |
| cd      | Muda o diretório atual                                                                |
| mkdir   | Cria um diretório no diretório atual                                                  |
| cp      | Copia arquivos da origem para o destino                                               |
| mv      | Move os arquivos para um diretório diferente                                          |
| rm      | Remove arquivos                                                                       |
| grep    | Pesquisa cadeias de caracteres específicas em um arquivo ou outras saídas de comandos |
| cat     | Lista o conteúdo de um arquivo e espera o nome do arquivo como parâmetro              |

&#x20;

&#x20;

&#x20;É prática comum deixar o serviço em execução em sua porta padrão. A tabela lista algumas portas comumente usadas e seus serviços. Estes também são chamados de “portas bem conhecidas”.

&#x20;

| Porta   | Descrição                                                      |
| ------- | -------------------------------------------------------------- |
| 20/21   | File Transfer Protocol (FTP)                                   |
| 22      | Secure Shell (SSH)                                             |
| 23      | Serviço de login remoto Telnet                                 |
| 25      | Protocolo SMTP                                                 |
| 53      | Domain Name System (DNS)                                       |
| 67/68   | Protocolo de Configuração Dinâmica de Host (DHCP)              |
| 69      | Protocolo de Transferência Trivial de Arquivo (TFTP)           |
| 80      | Protocolo HTTP                                                 |
| 110     | Protocolo POP3 (Post Office Protocol - Protocolo dos Correios) |
| 123     | Network Time Protocol (NTP)                                    |
| 143     | Protocolo IMAP                                                 |
| 161/162 | Protocolo de Gerenciamento Simples de Rede (SNMP)              |
| 443     | HTTP seguro (HTTPS)                                            |

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

A tabela a seguir compara os comandos de distribuição Arch Linux e Debian / Ubuntu Linux para realizar operações básicas do sistema de pacotes.

| Tarefa                                          | Arch        | Debian/Ubuntu          |
| ----------------------------------------------- | ----------- | ---------------------- |
| Instalar um pacote pelo nome                    | pacman -S   | apt install            |
| Remover um pacote pelo nome                     | pacman -Rs  | apt remover            |
| Update a local package                          | pacman -Syy | apt-get update         |
| Atualize todos os pacotes atualmente instalados | pacman -Syu | atualização do apt-get |

&#x20;

Um processo é uma instância em execução de um programa de computador. Os sistemas operacionais multitarefa podem executar muitos processos ao mesmo tempo.

Bifurcação é um método que o kernel usa para permitir que um processo crie uma cópia de si mesmo. Os processos precisam de uma maneira de criar novos processos em sistemas operacionais multitarefa. A operação bifurcação (fork) é a única maneira de fazer isso no Linux.

&#x20;

Quando um processo é bifurcado (fork), o processo do chamador se torna o processo pai, com o processo recém-criado referido como seu filho. Depois da bifurcação, os processos são, até certo ponto, processos independentes; eles têm IDs de processo diferentes, mas executam o mesmo código de programa.

A tabela lista três comandos usados para gerenciar processos.

| Comando  | Descrição                                                                                                                                                                                                                                                                                                                                                                          |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ps       | <ul><li><p></p><ul><li>Usado para listar os processos em execução no computador no momento em que é invocado.</li><li>Ele pode ser instruído a exibir processos em execução que pertencem ao usuário atual ou a outros usuários.</li><li>Embora listar processos não exija privilégios de root, eliminar ou modificar os processos de outros usuários exige.</li></ul></li></ul>   |
| superior | <ul><li><p></p><ul><li>Usado para listar processos em execução, mas ao contrário do ps, top continua exibindo processos em execução dinamicamente.</li><li>Pressione q para sair do topo.</li></ul></li></ul>                                                                                                                                                                      |
| kill     | <ul><li><p></p><ul><li>Usado para modificar o comportamento de um processo específico.</li><li>Dependendo dos parâmetros, kill removerá, reiniciará ou pausará um processo.</li><li>Em muitos casos, o usuário executará ps ou top antes de executar kill.</li><li>Isso é feito para que o usuário possa aprender o PID de um processo antes de executar kill.</li></ul></li></ul> |

&#x20;

Um vetor de ataque Linux comum é seus serviços e processos. Vulnerabilidades são freqüentemente encontradas no código de servidor e processo em execução em computadores conectados à rede.

&#x20;Os invasores geralmente testam portas abertas para avaliar a versão e a natureza do servidor em execução nessa porta.

&#x20;

telnet 209.165.200.224 80

&#x20;

Como acontece com a maioria das vulnerabilidades, manter o computador atualizado e fechar todos os serviços e portas não utilizados é uma boa maneira de reduzir as oportunidades de ataque em um computador Linux.

&#x20;

A remoção do Rootkit pode ser complicada e muitas vezes impossível, especialmente nos casos em que o rootkit reside no kernel; a reinstalação do sistema operacional geralmente é a única solução real para o problema. Os rootkits de firmware geralmente requerem substituição de hardware.

chkrootkit é um programa popular baseado em Linux projetado para verificar o computador em busca de rootkits conhecidos. É um script shell que usa ferramentas comuns do Linux, como strings e grep para comparar as assinaturas de programas principais. Ele também procura discrepâncias à medida que atravessa o sistema de arquivos /proc comparando as assinaturas encontradas lá com a saída de ps.

&#x20;

sudo ./chkrootkit

&#x20;

Embora as ferramentas de linha de comando geralmente sejam projetadas para executar uma tarefa específica e bem definida, muitos comandos podem ser combinados para executar tarefas mais complexas por uma técnica conhecida como piping. Nomeado após seu caractere definidor, o pipe (|), tubulação consiste em encadear comandos juntos, alimentando a saída de um comando na entrada de outro.

&#x20;

Os dois comandos, ls e grep, podem ser canalizado juntos para filtrar a saída de ls. Isto é mostrado na saída do comando ls -l | grep host (filtrará todos elementos que possuirem "host" em seus nomes durante a saida do ls –l) e do comando ls -l | grep file (filtrará todos elementos que possuirem "file" em seus nomes durante a saida do ls –l) .

&#x20;

Embora as ferramentas de l

&#x20;

Instalando, verificando e limpando aplicações no Linux.

* Primeiro inserimos os comandos apt update e apt upgrade para atualizar o sistema;
* Depois instalamos o mlocate usando apt install chkrootkit ou sudo pacman –S mlocate
* (Apache) Depois precisamos fazer sudo updatedb
* (Apache) Agora precisamos fazer locate messages
* Após isso podemos iniciar com o comando sudo chkrootkit
* Seguindo vamos usar piping, fazendo uma pesquisa usando cat /var/log/syslog | grep http \<aqui pode ser a string a ser procurada no sistema>

&#x20;

sudo apt install clamav clamav-daemon

sudo clamscan -r \<path>

&#x20;

_From <_[_https://gemini.google.com/u/0/app/7aa4d22e166a7ca9_](https://gemini.google.com/u/0/app/7aa4d22e166a7ca9)_>_
