# Art.: Forense Computacional

## Artigo: Forense Computacional

Quando um ataque ocorre em um ambiente o atacante pode procurar esconder seus rastros e algumas formas

Como podemos verificar no artigo de CIRILO DE SOUZA, ao deletar quaisquer arquivos, os sistemas operacionais não os excluem definitivamente do sistema operacional, sendo que a primeira camada de segurança do sistema é manter os registros e o arquivo apenas em um espaço diferente da memória de forma tal que conseguimos recuperá-los posteriormente.

O artigo nos indica onde podemos encontrar esses registros afim de recuperá-los, sendo que para Windows o processo consiste na criação de 2 arquivos novos sendo diferenciados pelos prefixos $I e $R na lixeira, que encontra-se na raiz do OS.

> sendo diferenciados pelo prefixo $I, que possui informações como data de exclusão, tamanho do arquivo original e data da exclusão, e o prefixo $R, que contém o conteúdo do arquivo original (Llamas, 2019)
>
> SE SOUZA apud Llamas, 2019

O conceito para Linux é muito mais simples, uma vez que os arquivos não perdem seus nomes originais quando são excluídos e seus metadados serão mantidos em diretórios destinados a isso na lixeira que também se mantém sobre a árvore de diretórios do usuário.
