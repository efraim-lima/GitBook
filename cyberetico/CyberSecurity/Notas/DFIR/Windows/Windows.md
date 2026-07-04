---
Created: 2026-01-05T22:58
Criado em: 2026-01-05T22:58
Criado em 1: 2026-01-05T22:58
Criado por: 2026-01-05T22:58
Module Code: Sistemas Operacionais
---
Para entender sobre os sistemas de arquivos vamos primeiro passar pelo FAT32
**FAT32**
Foi desenhado para suportar partições e arquivos maiores
|   |   |   |
|---|---|---|
|FAT32 File System|Boot Sector|Startup Code|
|||System Information|
||FAT Tables|File Detail Layout|
|||Free Space Management|
||Root Directory|File and Folder Entries|
||Data Area|Physical Content of Files and Folders|
||File and Folder Properties|Names|
|||Sizes|
|||Timestamps|
||System Limitations|Maximum File Size|
|||Maximum Disk Size|
As unidades de memória do FAT32 são chamadas de "clusters" sendo divididos em unidades de 4KB a 32KB, o sistema suporta até 2^32 clusters, podendo suportar um tamanho de até quase 8TB.
Os caminhos dos arquivos são armazenados na tabela FAT. O sistema FAT mantem os arquivos guardados em partes e mantém a informação sobre onde estes arquivos estão armazenados.
A deleção no FAT apenas indica os espaços do arquivo como disponíveis, este processo não apaga fisicamente os conteúdos presentes nos clusters, apenas os torna disponíveis para que sejam sobrescrevidos.
VANTAGENS
- larga abrangência de dispositivos e compatibilidade
- usa poucos recursos do sistema por ter uma estrutura simples
DESVANTAGENS
- tamanho maximo de arquivos de 4GB, tamanho maximo de armazenamento de 8TB
- Segurança e recuperação de dados não são tão avançados quando NTFS
**NTFS**
Sistema de arquivos preferidos para sistemas Windows modernos com foco em performance, segurança e ingridade de dados.
Estrutura mais complexa
|   |   |   |
|---|---|---|
|NTFS File System|Master File Table (MFT)|File Metadata|
|||File and Directory Listings|
||Volume Boot Record|Boot Loader|
|||Volume Information|
||BitLocker (Optional)|Encryption for Data Protection|
||Log File|Transaction Logging for Recovery|
||Indexing Service|Quick File Searches|
||Security Descriptors|Permissions|
|||Ownership|
||Alternate Data Streams|Additional Data Storage|
||File Compression|Native File Compression Mechanism|
**Master File System (MFT)**
Funciona como a FAT, mas neste caso armazena não apenas a posição do arquivo, mas também:
- nomes
- tamanhos
- timestamps
- informações de segurança (permissões)
- metadados
- atributos
Referente aos atributos temos os seguintes:
|   |   |
|---|---|
|Attribute Name|Description|
|$ATTRIBUTE_LIST|Lists the location of all attribute records that do not fit in the MFT record|
|$BITMAP|Attribute for Bitmaps|
|$DATA|Contains the default file data|
|$EA|Extended the attribute index|
|SEA_INFORMATION|Extended attribute information|
|$FILE_NAME|File name|
|$INDEX_ALLOCATION|The type name for a Directory Stream. A string for the attribute code for index allocation|
|$INDEX_ROOT|Used to support folders and other indexes|
|$LOGGED_UTILITY_STREAM|Use by the encrypting file system|
|$OBJECT_ID|Unique GUID for every MFT record|
|$PROPERTY_SET|Obsolete|
|$REPARSE_POINT|Used for volume mount points|
|$SECURITY_DESCRIPTOR|Security descriptor stores ACL and SIDs|
|$STANDARD_INFORMATION|Standard information, such as file times and quota data|
|$SYMBOLIC_LINK|Obsolete|
|$TXF_DATA|Transactional NTFS data|
|$VOLUME_INFORMATION|Version and state of the volume|
|$VOLUME_NAME|Name of the volume|
|SVOLUME VERSION|Obsolete. Volume version|
Atributos também contém informações como:
- Proprietário: Usuário ou grupo proprietário
- Grupo: Usuário ou grupo com permissões de acesso padrão
- DACL (Discritionary Access Control List): Lista que define permissôes para grupos e usuários específicos
- SACL (System Access Control List): Lista definindo permissões para o sistema operacional ou outros componentes do sistema
- Permissões Herdadas (Inherited Permissions): Permissões que são automaticamente aplicadas a subpastas e arquivos (herdadas)
Journaling
O sistema NTFS utiliza Journaling para recuperação do sistema em caso de falhas, isso preserva a integridade dos dados permitindo que eles o sistema possa ser retornado a um ponto do histórico caso pare inesperadamente.
Permissões e Segurança
Como informado anteriormente o sistema conta com recursos de permissão para arquivos e diretórios, podendo contar com gerenciamento de usuários e grupos de forma individual.
Compressão e Criptografia
O sistema conta com recursos de criptografia de arquivos e pastas, fazendo com que o armazenamento possa ser melhor aproveitado assim com a segurança também seja incrementada.
VANTAGENS
- pode ser dividido em partições
- proporciona proteção melhorada com permissões e recursos de segurança
- inclui recursos que otimizam uso de disco e mantêm sua integridade
DESVANTAGENS
- estrutura mais complexa e pouca compatibilidade com sistemas operacionais mais antigos
- pode usar mais recursos do sistema
**exFAT**
O sistema exFAT foi desenhado pela Microsoft para atender a dispositivos portáteis que usam flash drivers e SD cards, melhorando os problemas do FAT32 e incorporando alguns recursos do NTFS
|   |   |   |
|---|---|---|
|exFAT File System|Volume Boot Record|Boot Sector|
|||OEM Parameters|
||FAT (File Allocation Table)|Cluster Allocation|
||Allocation Bitmap|Free Cluster Tracking|
||Upcase Table|Case Sensitivity Information|
||Directory Entry Structure|File and Directory Records|
||File System Metadata|Volume Label|
|||Allocation Unit Size|
||Cluster Heap|Data Storage Area|
||Extended Attributes|Custom Metadata|
||Directory Tree|Hierarchical File System Structure|
Utiliza forma de cluster para armazenar os dados e seus metadados, sendo que o arquivo é alocado dinamicamente.
Neste caso, quando o usuário busca pelo arquivo o sistema procura pelo entrypoint do arquivo (o cluster inicial) e segue a cadeia de clusteres para remontar o arquivo.
O processo de deleção é assim como os outros, o sistema marca os clusteres como disponíveis para gravação.
  
VANTAGENS
- Elimina a limitação de 4GB dos arquivos presente em FAT32
- Mais dispositivos podem suportar este sistema
DESVANTAGENS
- Menos maneiras de proteção de dados que o NTFS
**Comparação entre os sistemas**
|   |   |   |   |
|---|---|---|---|
|**Feature**|**FAT32**|**exFAT**|**NTFS**|
|File Size Limit|4 GB|16 EB|16 EB|
|Partition Size Limit|2 TB|16 EB|256 TB|
|Naming Files|8.3 characters   <br>(limited character   <br>set)|255 characters   <br>(Unicode)|255 characters   <br>(Unicode)|
||Low|Low|High (File   <br>permissions,|
|Security|||encryption)|
|Performance|Fast with small files|Fast with large files|Fast with large files|
||Highest (almost all|High (most of modern|Medium ([[CyberSecurity/Course/tools/operational-systems/windows/windows|windows]],|
|Compatibility|[[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]])|systems)|macOS, [[CyberSecurity/Notas/DFIR/Unix Like/Linux|Linux]])|
||USB drives, memory|External HDDs,|Internal HDDs, SSDs,|
|Usage|cards, older devices|SSDs, flash drives|NAS|