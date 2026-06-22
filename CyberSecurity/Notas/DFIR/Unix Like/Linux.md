---
Created: 2026-01-05T23:06
Criado em: 2026-01-05T23:06
Criado em 1: 2026-01-05T23:06
Criado por: 2026-01-05T23:06
Module Code: Sistemas Operacionais
---
Em sistemas Unix like temos o advento do Journaling que é o processo de armazenar as alterações do file system em um esquema de [[CyberSecurity/Course/forense/logs/logs|logs]], que fica armazenado numa area do disco dedicada para isso.
Quando o sistema reinicia o file system verifica o ultimo log e correlaciona com o estado atual para validar a integridade do sistema.
Journaling mantem integridade e confiança no sistema assim como proporciona um retorno ao ponto de montagem mais eficiente e de forma consistente. Por fim também reduz o risco da perda de dados, pois loga as alterações ANTES que elas ocorram.
EXT4
Uma evolução clara do EXT3 e EXT2 que possuiam performance semelhante e tamanho de particionamento semelhante (exceto EXT2). Possuindo [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] recursos de Journaling e Logging aprimorados.
![[GetImage.png]]
Btrfs (B-tree File System)
Focado em armazenamentos maiores, mas com maior escalabilidade. Tendo outros recursos como capacidade de snapshots, [[notas/16.0/Backup/Backup|Backup]] e recuperação de dados, gerenciamento dinamico do volume e algoritmos de compressão.
Utiliza o algoritmo B-tree focando em balanceamento da estrutura de dados.
CoW (Copy-on-Writing)
faz uma copia do arquivo em outro volume antes de altera-lo, garantindo sua integridade.
B-Tree
Organiza [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] blocos mantendo performance e escalabilidade
Snapshot e Cloning
Cria uma copia do sistema de arquivos em um tempo especifico permitindo remotagem integra.
Checksums
Mantem Checksums de Dados e Metadados, verificando constantemente a integridade dos arquivos
Alocação Dinamica de Inodes
Mantem identificadores dos objetos do sistema de arquivos
SquashFS
é um sistema voltado para apenas leitura (read-only), muito usado nos live systems ou dispositivos embarcados devido a sua alta capacidade de compressao com [[CyberSecurity/Notas/SOC/Introdução/Ferramentas|Ferramentas]] como Gzip e XZ.
Tmpfs
Permite a execução do sistema em RAM ou memória Swap, de forma a ser leve e também imputável, mas é uma memória temporária, que fara com que [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] dados deixem de existir no reboot ou quando o sistema for desmontado.
Pode ser usado em diretorios como "/tmp”, “/var/tmp”, ou “/[[DEV]]/shm”.
Comparação dos Sistemas de Arquivos
![[GetImage_(1).png]]
![[GetImage_(2).png]]