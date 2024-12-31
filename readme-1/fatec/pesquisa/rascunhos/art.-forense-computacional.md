# Art.: Forense Computacional

## Artigo: Forense Computacional

Quando um ataque ocorre em um ambiente o atacante pode procurar esconder seus rastros e algumas formas

Como podemos verificar no artigo de MARCELO CIRILO DE SOUZA, ao deletar quaisquer arquivos, os sistemas operacionais não os excluem definitivamente do sistema operacional, sendo que a primeira camada de segurança do sistema é manter os registros e o arquivo apenas em um espaço diferente da memória de forma tal que conseguimos recuperá-los posteriormente.

O artigo nos indica onde podemos encontrar esses registros afim de recuperá-los, sendo que para Windows o processo consiste na criação de 2 arquivos novos sendo diferenciados pelos prefixos $I e $R na lixeira, que encontra-se na raiz do OS.

> sendo diferenciados pelo prefixo $I, que possui informações como data de exclusão, tamanho do arquivo original e data da exclusão, e o prefixo $R, que contém o conteúdo do arquivo original (Llamas, 2019)
>
> SE SOUZA apud Llamas, 2019

O conceito para Linux é muito mais simples, uma vez que os arquivos não perdem seus nomes originais quando são excluídos e seus metadados serão mantidos em diretórios destinados a isso na lixeira que também se mantém sobre a árvore de diretórios do usuário.

No processo de recuperação de arquivos que foram completamente deletados (esvaziando a lixeira ou "deletando permanentemente") precisaremos contar com ferramentas forenses específicas e, antes de mais nada termos noção dos tamanhos dos clusters em que a memória foi dividida, sendo as padrões NTFS para Windows e ext4 para Linux. No processo de separação dos clusters de memória para ambos os sistemas existe o preenchimento dos blocos de memória de acordo com o tamanho do arquivo que deve ser armazenado naquela parte do disco, mas como nem sempre todo o tamanho íntegro do bloco é utilizado, muitas vezes sobra um espaço que não foi utilizado para aquele armazenamento, o slack space; e neste espaço ainda podemos encontrar vestígios do que foi deletado anteriormente.

Neste momento pode-se fazer uma busca por arquivos de logs deletados utilizando-se da técnica data carving ou data recovery, ou seja, buscar vestígios de um arquivo anteriormente deletado em slack space, como processo de investigar possiveis indícios de dados sobrescritos de forma maliciosa ou intencional.

Para localizar os arquivos possivelmente sobrescritos em memória basta procurarmos por assinturas das extensôes de arquivos nos headers dos arquivos, onde pode-se indicar a extensão do arquivo que foi apagado, (DE SOUZA).&#x20;
