# Backup

II) Backup - c'opia de segurança de arquivos sens'iveis ao neg'ocio da empresa -> ARQUIVOS: no linux tudo e um arquivo --> para n'os, arquivo e uma sequencia bin'aria finita de (1011101......1) que possui uma informaç\~ao intr'inseca

\-> Erro de modo comum ---> ao particionar um disco HD de 2 Tb em 2 unidades espelhadas (mirrorred) NÃO temos um backup ---> tendo 2 HDs juntas sendo do mesmo fabricante, NÃO temos um backup (ideal ter de fabricantes diferentes, Wistern Digital e Samsung, por exemplo) O ideal é termos backup em mídias de forma diferente e fisicamente diferentes também.

TIPOS DE BACKUP: Hoje usa-se muito backup nuvem, mas ainda usa-se backup em fita LTO, Digital Tape, com 15Tb de armazenamento ---> Fita LTO tem desvantagem de tempo e de tamanho,

* no quesito tamanho dá para compactar, compactar

HD sao feitas de de ceramica ou latão CRC codigo de reduntancia ciclica quando uma HD sai da fábrica já sai com mapa de badblocks, o que demonstra o quanto de perda de magnetismo que as memórias rígidas possuem.

para recupaeração de HDs muitas vezes precisamos trocar a controladora, trocar o chip da controlaora, tirar da placa que deu problema e colocar na que precisa ser recuperada (cobra-se por Mb recuperado)

no momento de fazer um backup precisamos fazer backup apenas do que é importante. Por exemplo: é importante salvar o .xls e não o excell.

Backup Full -> é uma cópia completa de todos os arquivos sensíveis em um único volume

* desvantagens: tempo de realização, tamanho / espaço (resolve-se com copactação, por exemplo o arquivo .bkp), fica inviável fazer em curtos períodos;
* vantagem: em caso de restore temos apenas um único volume --> quem define a prioridade do que precisa ser armazenado em backup são os stakeholders, que são qualquer indivíduo que tenha importância nos processos; --> backups full são feitos em períodos maiores de tempo, contando a partir do dia 1, podemos fazer um backup no dia 30 novamente, por exemplo...mas se houver perda de dados no dia 18 perdemos tudo o que ocorreu neste interim --> forma mais onerosa de armazenamento, pode ser feita mensalmente ou a cada 2 meses, depende dos stakeholders

Backup Diferencial -> é uma cópia de todos arquivos sensíveis modificados, o CRUD (Create, Read, Update and Delete)

* desvantagens: pode ser mais trabalhoso de recuperar, primeiro o backup full e depois o diferencial mais recente;
* vantagens: menor e mmais rapida que o backup full, pode ser feito e intervalos de tempo menores; --> se consideramos o backup full de 30 em 30 dias, fazemos um diferencial de 10 em 10 dias, pois salvaremos apenas os arquivos alterados neste período --> para recuperar um diferencial precisamos recuperar primeiro o Backup Full mais recente e depois o diferencial anterior, pois o backup diferencial mais recente teria as informações até aquele dia. --> quando falamoss de maior frequencia estamos falando de overclock, ou seja, aumentar a ferquêcia do clock.

Backup Incremental -> copia todos arquivos importantes modificados desde o último backup (seja ele full, != diferencial ou + incremental). É o menor e mais veloz de fazer de todos, é usado para ter menor granularidade

* desvantagens: o restore é mais complexo, precisa pegar o Full, o ultimo diferencial e todos os Incrementais até o ultimo, em forma cronológica
* vantagens: menor e mais rápido --> o primeiro backup incremental depois do full possui as mesmas informações do diferencial

xor: comparar bits entre arquivos que deveriam ser idênticos Backup de menor custo: backup na web

Principais diferencias entre incremental e diferencial: o diferencial se referencia ao full, o incremental ao ultimo

Os backups diferenciais e incrementais acrescentam mais dados em cima do ful, pois armazenam as informações em cima do full, quando é feito mais um full temos a redução de espaço de memória, pois salvamos todas as alterações que estavam armazenadas acima do full (a mais) e salvamos todas as informações como um único backup full.
