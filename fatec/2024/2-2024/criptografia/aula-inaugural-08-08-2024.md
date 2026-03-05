# Aula Inaugural 08-08-2024

### Notas gerais

O curso de criptografia possuirá apresentações de seminários antes das provas contendo conteúdos específicos que abordem a matéria como um todo, por exemplo:

* Forense Computacional
* Vulnerabilidades de Criptografia
* Formas de Criptografia
* CTF
* Web Hacking
* Engenharia Social
* Desenvolvimento de Exploits
* Aplicações de Segurança com Python
* Segurança na Nuvem
* Wifi Hacking
* Aplicações com Criptografia usando CTF

As apresentações terão critérios para a apresentação, sendo um tempo de 20 a 30 minutos e contendo uma apresentação PowerPoint.

### Conteúdo

A segurança da informação possui não apenas o CID, mas também o cubo da segurança da informação, que consiste de:

* **1ª face** - Princípios de Segurança: Confidencialidade, Integridade, Disponibilidade
* **2ª face** - Estado dos Dados: Processamento, Armazenamento (em repouso), Transmissão
* **3ª face** - Contramedidas ou Tecnologias: Tecnologia, Políticas e Processos, Pessoas

Na parte de estados dos dados, teremos um processo de criptografia para cada etapa.

* https://threatmap.checkpoint.com
* https://threatmap.fortiguard.com
* https://cvedetails.com
* https://exploit-db.com

Algo que pode ser útil em conceito de processos é: primeiro fazer uma leitura de serviços presentes na rede usando o nmap e, a partir do levantamento dos serviços, basta usar o https://exploit-db.com para verificar se aquele serviço e aquela versão possuem alguma vulnerabilidade.

Cert.br apresenta estatísticas de riscos na internet compiladas em forma de dados.

Publicações de segurança com repercussão na mídia podem ser encontradas nos sites da Security Report e IBRASPD.

Pesquisar sobre os 10 mandamentos da ética profissional e de computadores.

Uma boa ferramenta para fazermos testes e laboratórios de pentesting, seja em rede, seja em web e muitos outros recursos, é acessando os laboratórios da Wargames através do website: https://overthewire.org/wargames/

### TEÓRICO

A primeira forma de cifra da história foi através dos sistemas monoalfabéticos, como o ROT13 e a cifra de César.

Análise da cifra de César: **Para encriptar** l' = (l + ch) mod 26\
**Para decriptar** l = (l' - ch) mod 26

l = letra\
ch = caracteres\
mod 26 = modulado pelas 26 letras do alfabeto

Depois, criaram-se os modos de criptografia em modos polialfabéticos (Vigenère), que podem ser representados por um cálculo, mas é mais fácil termos uma visão em tabela do mesmo, pois essa criptografia consiste em criar múltiplos alfabetos diferentes, deslocando sempre uma letra para frente no próximo, assim conseguimos determinar como seria a mensagem a partir da posição pré-determinada. Um exemplo de como seria o alfabeto:

```
abcdefghijklmnoprst  
bcdefghijklmnopqstu  
cdefghijklmnopqrtuv  
defghijklmnopqrsuvx  
efghijklmnopqrstvxw  
fghijklmnopqrstuxwy  
ghijklmnopqrstuvwyz  
...
```

Posteriormente, começaram a criar dispositivos criptográficos, como a máquina Enigma durante a Segunda Guerra Mundial, onde Alan Turing conseguiu desenvolver uma máquina que resolvesse a Enigma e o considerado primeiro computador criado.

Um processo de criptoanálise é através de métodos estatísticos que determinam a ocorrência de cada letra em um determinado idioma, de forma a se estabelecer padrões em alguns idiomas.

Desenvolveram em 1920 o teste kappa e o teste phi, que podem ser utilizados para decriptar textos; o teste kappa determina a probabilidade de cada letra aparecer em um evento único (ou seja, 1/26 ou 0.0385), já o teste phi analisa a incidência de cada caráter em um dado idioma, o tamanho da mensagem, um phi randômico e, a partir disso, determinar se o texto é transposto ou substituído.

* **Estudar teste phi**

Existem ferramentas de decriptografia de cifra de César.

Existe uma forma de codificação nomeada base64 que se baseia nos bytes, mas como em base64 as letras necessitam apenas de 6 bits, com isso a outra letra subsequente já se iniciaria nos 2 últimos bits do mesmo byte, fazendo com que a resposta seja sempre menor do que a pergunta, com isso sempre podem acabar sobrando alguns bits no final da mensagem que frequentemente precisam ser completados por "==", caracterizando claramente uma cifra em base64.

Podemos fazer um teste disso no Linux através do comando: `echo -n "Texto a ser encriptado" | base64`
