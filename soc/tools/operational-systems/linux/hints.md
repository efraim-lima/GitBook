# Hints

Para ter maior visibilidade de comandos e funcionalidades do sistema operacional: [linux](../../../../fatec/pesquisa/ferramentas/os/linux/ "mention")\
\
Imprescindível ter conhecimento aprofundado sobre o sistema operacional para atuar em uma investigação neste sistema operacional, por isso mantenho essa imagem aqui em meu radar, para sempre ter uma boa visibilidade de como funciona o sistema.

<figure><img src="../../../../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

Os logs de host do Microsoft Windows são visíveis localmente pelo Visualizador de Eventos. O Visualizador de Eventos mantém quatro tipos de logs:

* Logs de aplicativos — Eles contêm eventos registrados por vários aplicativos.
* Registros do sistema — Isso inclui eventos relacionados à operação de drivers, processos e hardware.
* Registros de instalação — Estes registram informações sobre a instalação de software, incluindo atualizações do Windows.
* Registros de segurança — Esses eventos registram relacionados à segurança, como tentativas de logon e operações relacionadas ao gerenciamento e acesso de arquivos ou objetos.
* Logs da linha de comando - Os invasores que obtiveram acesso a um sistema e alguns tipos de malware executam comandos da interface de linha de comando (CLI) em vez de uma GUI. A execução da linha de comando em log fornecerá visibilidade para esse tipo de incidente.

&#x20;

Vários logs podem ter diferentes tipos de eventos. Os logs de segurança consistem apenas em mensagens de falha ou êxito de auditoria. Em computadores Windows, o log de segurança é realizado pelo Local Security Authority Subsystem Service (LSASS), que também é responsável por impor diretivas de segurança em um host Windows. O LSASS é executado como lsass.exe. Ele é frequentemente falsificado por malware. Ele deve estar sendo executado a partir do diretório System32 do Windows. Se um arquivo com esse nome, ou um nome camuflado, como 1sass.exe, estiver em execução ou em execução a partir de outro diretório, ele pode ser malware.

&#x20;

descrições de pacotes do Syslog

Nota: Códigos de instalação entre 15 e 23 (local0-local7) não recebem uma palavra-chave ou nome. Eles podem ser atribuídos a diferentes significados dependendo do contexto de uso. Além disso, vários sistemas operacionais foram encontrados para utilizar ambas as instalações 9 e 15 para mensagens de relógio.

| Value | Gravidade                                                                                                    |
| ----- | ------------------------------------------------------------------------------------------------------------ |
| 0     | Emergência: sistema está inutilizável                                                                        |
| 1     | Alerta: a ação deve ser tomada imediatamente                                                                 |
| 2     | Crítico: condições críticas que devem ser corrigidas imediatamente e indica falha em um sistema              |
| 3     | Erro: uma falha que não é urgente, deve ser resolvida dentro de um determinado tempo                         |
| 4     | Aviso: um erro não existe atualmente; no entanto, um erro ocorrerá no futuro se a condição não for resolvida |
| 5     | Aviso: um evento que não é um erro, mas que é considerado incomum. Não requer ação imediata.                 |
| 6     | Informativo: mensagens emitidas relativas ao funcionamento normal                                            |
| 7     | Depuração: mensagens de interesse para desenvolvedores                                                       |

&#x20;

O valor de Prioridade (PRI) é calculado multiplicando o valor de Facilidade por 8 e, em seguida, adicionando-o ao valor de Gravidade, conforme mostrado abaixo.

Priority = (Facility \* 8) + Severity

O valor Prioridade é o primeiro valor em um pacote e ocorre entre colchetes angulados <>.

&#x20;

Dois arquivos de log importantes para se familiarizar são os logs de acesso do servidor web Apache e os logs de acesso do Microsoft Internet Information Server (IIS). Exemplos de cada um são mostrados abaixo.

#### Log de acesso do Apache

203.0.113.127 – dsmith \[10/Oct/2016:10:26:57 - 0500] "GET /logo\_sm.gif HTTP/1.0" 200 2254 "[http://www.example.com/links.html](http://www.example.com/links.html)" "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"

#### Log de acesso do IIS

6/14/2016, 16:22:43, 203.0.113.24, -, W3SVC2, WEB3, 198.51.100.10, 80, GET, /home.htm, -, 200, 0, 15321, 159, 15, HTTP/1.1, Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0), -, [http://www.example.com](http://www.example.com)

&#x20;

O SIEM combina as funções essenciais de gerenciamento de eventos de segurança (SEM) e ferramentas de gerenciamento de informações de segurança (SIM) para fornecer uma visão abrangente da rede empresarial usando as seguintes funções:

* Coleta de logs — Os registros de eventos de origens em toda a organização fornecem informações forenses importantes e ajudam a atender aos requisitos de relatórios de conformidade.
* Normalização — Mapeia mensagens de log de diferentes sistemas em um modelo de dados comum, permitindo que a organização se conecte e analise eventos relacionados, mesmo que sejam inicialmente registradas em diferentes formatos de origem.
* Correlação — Isso vincula registros e eventos de sistemas ou aplicativos diferentes, acelerando a detecção e reação a ameaças de segurança.
* Agregação — Isso reduz o volume de dados de eventos consolidando registros de eventos duplicados.
* Relatórios — Apresenta os dados de eventos agregados e correlacionados em monitoramento em tempo real e resumos de longo prazo, incluindo painéis gráficos interativos.
* Conformidade — são relatórios para atender aos requisitos de várias regulamentações de conformidade.

Um SIEM popular é o Splunk, que é feito por um parceiro Cisco. Outra solução SIEM popular é Security Onion com ELK, que consiste nos aplicativos integrados Elasticsearch, Logstash e Kibana.

&#x20;

A tabela lista vários tipos de testes que podem ser realizados.

| Termo                        | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Análise de risco             | <ul><li><p></p><ul><li>Esta é uma disciplina na qual os analistas avaliam o risco representado pelas vulnerabilidades a uma organização específica.</li><li>Uma análise de risco inclui a avaliação da probabilidade de ataques, identifica tipos de possíveis agentes de ameaça e avalia o impacto de explorações bem-sucedidas na organização.</li></ul></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Avaliação de vulnerabilidade | <ul><li><p></p><ul><li>Este teste emprega software para verificar servidores voltados para a Internet e redes internas em busca de vários tipos de vulnerabilidades.</li><li>Essas vulnerabilidades incluem infecções desconhecidas, fraquezas nos serviços de banco de dados voltados para a Web, patches de software ausentes, portas de escuta desnecessárias etc.</li><li>As ferramentas para avaliação de vulnerabilidades incluem a plataforma OpenVAS de código aberto, o Microsoft Baseline Security Analyzer, o Nessus, a Qualys e os serviços FireEye Mandiant.</li><li>A avaliação de vulnerabilidades inclui, mas vai além, a varredura de portas.</li></ul></li></ul>                                                                                                                                                                                                            |
| Teste de penetração          | <ul><li><p></p><ul><li>Esse tipo de teste usa ataques simulados autorizados para testar a força da segurança da rede.</li><li>O pessoal interno com experiência em hackers ou hackers éticos profissionais identifica ativos que podem ser alvo de agentes de ameaças.</li><li>Uma série de explorações é usada para testar a segurança desses ativos.</li><li>Ferramentas de software de exploração simuladas são frequentemente usadas.</li><li>O teste de penetração não só verifica se existem vulnerabilidades, como também explora essas vulnerabilidades para determinar o impacto potencial de uma exploração bem-sucedida.</li><li>Um teste de penetração individual é frequentemente conhecido como teste de caneta.</li><li>Metasploit é uma ferramenta usada em testes de penetração.</li><li>CORE Impact oferece software e serviços de teste de penetração.</li></ul></li></ul> |

A tabela lista exemplos de atividades e ferramentas que são usadas em testes de vulnerabilidade.

| Atividade de                 | Descrição                                                                                                                       | Ferramentas                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Análise de risco             | Indivíduos realizam uma análise abrangente dos impactos dos ataques nos ativos principais da empresa e no funcionamento         | Consultores internos ou externos, quadros de gestão de riscos           |
| Avaliação de vulnerabilidade | Gerenciamento de patches, varreduras de host, varredura de portas, outras verificações de vulnerabilidade e serviços            | OpenVAS, Analisador de Linha de Base da Microsoft, Nessus, Qualys, Nmap |
| Teste de penetração          | Uso de técnicas e ferramentas de hacking para penetrar nas defesas da rede e identificar a profundidade de penetração potencial | Metasploit, CORE Impact, hackers éticos                                 |

&#x20;

Soluções SOAR:

* Fornece ferramentas de gerenciamento de casos que permitem que o pessoal de segurança cibernética pesquise e investigue incidentes, frequentemente integrando inteligência contra ameaças à plataforma de segurança de rede.
* Use inteligência artificial para detectar incidentes e auxiliar na análise e resposta a incidentes.
* Automatize procedimentos complexos de resposta a incidentes e investigações, que são tarefas potencialmente intensas de mão-de-obra executadas pela equipe do centro de operações de segurança (SOC) executando livros de execução. Esses são playbooks que executam ações como acessar e analisar dados relevantes, tomar medidas para isolar sistemas comprometidos e pesquisar ameaças para validar alertas e executar uma resposta a incidentes.
* Oferece painéis e relatórios para documentar a resposta a incidentes para melhorar os principais indicadores de desempenho do SOC e pode melhorar consideravelmente a segurança da rede para as organizações.

O SIEM ajuda a soar o alarme para atividades mal-intencionadas. Os analistas terão que agir sobre a ameaça. A SOAR ajuda os analistas a responder à ameaça.
