Falar brevemente sobre hashing

Primeiro falar sobre o paradigma do aniversário, onde a probabilidade de 2 pessoas fazerem aniversário na mesma sala excede os 50% quando houverem 23 pessoas na mesma sala e isso vai aumentando gradativamente até chegarmos em uma probabilidade de 100% comm 100 pessoas em uma sala.

 As vulnerabilidades de MD5 foram descobertas devido à sua estrutura e à forma como manipula os dados, permitindo a construção de pares de mensagens diferentes que geram o mesmo hash, o que foi formalmente demonstrado em 2004.

- 2¹²⁸ possibilidades, mas apenas 23 entradas são necessárias para ter uma probabilidade maior que 50% de uma colisão (aproximadamente 1 em 365).

Ou seja: Ao gerar 1000 hashes, as chances de colisão se tornam significativas, apesar de existirem bilhões de combinações possíveis.

 Já no SHA1 a estrutura permite a manipulação de bits de maneira a gerar hashes idênticos.

 Em 2017, o ataque "SHAttered" gerou duas imagens diferentes com o mesmo hash SHA-1, mostrando que, mesmo com um espaço maior (160 bits), a colisão pode ser encontrada com um número razoável de entradas, explorando as fraquezas estruturais

depois apresentar como isso afeta os algoritmos sha1 e md5 pois eles possuem pouca variabilidade de permutas para poder fazer uma extensão maior de variabilidade de outputs, o que inevitavelmente fará com que tenhamos elementos semelhantes no output que não representam semelhança no input.

apresentar o teste em python3:

crypy 
fornece uma interface para funções de hashing criptográfico usadas principalmente para armazenar senhas. Ela é uma interface para a função crypt do sistema Unix, 


import crypt
crypt.crypt("5dUD&66", "br")
'brokenOz4KxMc'
crypt.crypt("O!>',%$", "br")
'brokenOz4KxMc'

presente em https://github.com/corkami/collisions

também apresentar os testes do hello e erase, presentes no website: https://www.mscs.dal.ca/~selinger/md5collision/

C:\TEMP> md5sum hello.exe
cdc47d670159eef60916ca03a9d4a007
C:\TEMP> .\hello.exe
Hello, world!

(press enter to quit)
C:\TEMP> 
C:\TEMP> md5sum erase.exe
cdc47d670159eef60916ca03a9d4a007
C:\TEMP> .\erase.exe
This program is evil!!!
Erasing hard drive...1Gb...2Gb... just kidding!
Nothing was erased.

(press enter to quit)
C:\TEMP> 

por fim informar que outro ponto importante é em como isso torna senhas de aplicações inseguras e até mesmo verificaçao de arquivos (apresentar como é feita essa verifiação com base em seu resumo hash)