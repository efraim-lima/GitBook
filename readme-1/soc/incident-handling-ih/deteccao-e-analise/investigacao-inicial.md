# Investigação Inicial

O processo de investigar um incidente parte primeiro de uma construção de base de conhecimento, afinal de contas precisamos conseguir discernir ações legítimas em ambientes seguros de ações maliciosas em ambientes críticos; para isso devemos ter consciência (e produzir uma base de conhecimento --knowledge base) de quais são os servidores principais, os IPs dos hosts na rede, quais são os usuários e quais as suas permissões além de termos uma boa noção de como é o comportamento padrão do ambiente (baseline). Mas calma, é humanamente impossível ter tantas informações na mente, para isso cada organização direcionará de uma forma essa construção.

Mas voltando ao processo de investigação, quando um possível incidente é identificado pode-se adotar uma abordagem que vise responder algumas perguntas: quando, como, o que  e onde.

Para isso podemos averiguar os seguintes elementos, que é uma transcrição quase direta do curso Hack The Box:

* Data/hora em que o incidente foi relatado
* Quem detectou o incidente e/ou quem o denunciou?&#x20;
* Como foi detectado o incidente?&#x20;
* Qual foi o incidente?&#x20;

Monte uma lista de sistemas impactados (se relevante) Documentar quem acessou os sistemas impactados e quais ações foram tomadas. Anote se este é um incidente em andamento ou se a atividade suspeita foi interrompida Localização física, sistemas operacionais, endereços IP e nomes de host, proprietário do sistema, finalidade do sistema, estado atual do sistema (Se houver malware envolvido) Lista de endereços IP, hora e data de detecção, tipo de malware, sistemas impactados, exportação de arquivos maliciosos com informações forenses sobre eles (como hashes, cópias dos arquivos, etc)

Baseando-se nisso fiz o seguinte formulário para facilitar uma investigação:

<table data-full-width="true"><thead><tr><th width="252"></th><th>Data</th><th>Desctrição</th><th>Evidência</th><th>Hash</th><th>Criticidade (5-0)</th></tr></thead><tbody><tr><td>Tipo de Incidente</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Alvo <br>(IP, Usuario, host)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Quem fez <br>(IP, Usuario, host)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>O que <br>(ação do incidente)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Infos<br>(IPs, MAC, OS, Hostname) </td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Malware<br>(data, tipo, sistemas impactados)</td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

Para determinar a criticidade do incidente devemos medir o quanto ele pode impactar o ambiente e determinar uma nota a ele, considerando que 5 é uma criticidade baixa e 0 a mais alta, essa nota deve ser atribuída a cada elemento da tabela, pra assim conseguirmos ter uma nota final de acordo com o peso de cada item da tabela.

Para determinar essa criticidade vamos tomar como base no impacto e os requisitos dessa exploração ao sistema&#x20;

\
