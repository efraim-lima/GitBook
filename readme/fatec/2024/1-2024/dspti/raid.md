# RAID

RAID - Redundant Array of Independent Disks

Funciona para uptime e disponibilidade, não integridade

Sistemas de Armazenamento:

SAN -> Storage Area Network => focado em disponibilidade

Características importantes do armazenamento: Capacidade -> capacidade de bytes possiveis de manutenção tempo de acesso -> tempo de leitura e escrita

Raid é sistema de backup apenas para disponibilidade composto por uma controladora RAID e a partir de 2 discos, não serve de backup de segurança. O ideal é ter 2 discos de marcas diferentes;

RAID0 | Stripping => Performance O hardware de Raid 0 e 1 é o mesmo (usando sempre mais de um drive) O mesmo arquivo é separado pela metade de forma entrelaçada Velocidade de leitura e escrita muito maior Espaço disponivel maior

RAID1 | Mirroring => Redundância Mesmo hardware do Raid0 O arqivo é escrito em todos os discos, tendo uma cópia do mesmo arquivo em ttodos A velocidade de leitura é identica, mas a de escrita é maior (o dobro) O armazenamento torna-se menor, pois precisa-se reservar os dois discos para

Comparativo Raids

Raid0 | Raid1 Vw => 1s | Vw => 2s Vr => 1s | Vr => 1s Sp => 2T | Sp => Sp

Parity Disk Considere que temos 4 data disks, onde cada um deles possui 1T de armazenamento funcionando em RAID 1, mas o ultimo disco funciona apenas como Parity Disk, ou seja, nele será gravado o backup de tudo o que for escrito, enquanto nos demais a gravação será sequencial. Para identificação dos discos temos identificações baseadas em bits setados (1) e resetados (0). Supondo que um disco falhe e precisemos encontrar qual o id de nossas identificações de disco que falhou basta fazer um xor nos ids sobresalentes que o resultado é o id do que falhou:

Estado inicial ====> Falha em 1 disco ====> XOR 1101 XXXX XXXX 0100 0100 0100 1000 1000 1000 0001 0001 0001 \_\_\_\_\_\_\_\_ XOR: 1101

Quanto mais elementos inseridos em um sistema pode-se coniderar que o MTTR vai diminuir, mesmo que todos tenham um MTBF alto, pois quanto mais elementos inseridos em um sistema, o momento de manutenção (MTTR) vai clustear com o tempo dos demais;

RAID4 - Writing

Comparando os bits mais significativos (o bit mais à esquerda, ou seja, o que vale 128b) faz com que criemos o id de nosso parity disk

RAID5 Ponto de falha:

distancia de Hamming (?) composta por (dH/2)-1

onde: dH = quantidade de elementos únicos, por exemplo, 8 discos;

Portanto se tivermos 8 discos podemos ter até 3 pontos de falha A partir daqui podemos perder até 2 discos, antes poderia-se perder apenas 1 RAID1+0 Mais eficiente Combinação entre o RAID1 (duplica os dados entre dois discos fisicos) e RAID0 (fragmenta entre 2 discos lógicos) RAID0+1 Menos eficiente Combinação dentre o RAID0 (fragmenta os dados entre os discos físicos) e RAID1 (duplica os dados entre os discos lógicos)

Fake RAID => o que conseguimos mudar em nossa BIOS, pois é virtual Hardware RAID => o RAID correto, trabalhando com harwares

NAJOS TIVOLI -> monitoramento de HDDs \*\*estudar mais sobre RAID Acessar Amdahl -> cada ponto do RAID aparenta sinificar a quantidade de particionamento da memoria -> servidor de bancos de dados rodam sgbd(?) -> a partir de 2 discos temos o mirrorring, com 3 discos temos derivados do RAID5 technologi expensive => mais processamento
