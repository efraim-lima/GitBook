# Aula inaugural 08-06-2024

## **PROTOCOLOS DE REDES**

## Aula inaugural

Introdução a alguns conceitos de redes e de processos em que os protocolos se desenrolam nos meios e no sistema como um todo, por exemplo, como analisarmos cada nó na rede para sabermos qual o caminho físico que os pacotes estão fazendo quando usamos o traceroute (tracert) e qual a relação dos IPs com os nós na rede real (cabeada, basicamente);

Apresentou as ferramentas como ip address detail, que apresentam dados dos nós de forma física.

Quando for enviar o projeto para o professor via email, usar no assunto do email "SEGNA3" para identificar a turma e no corpo os integrantes.

Máscaras de IP ######################

O processo de conversão de máscara de IP de decimal para binário é dado da seguinte forma:

Temos bits "fechados" e bits "abertos" que determinam qual é a máscara vigente no IP.

IP 192.168.15.0/22 Máscara Bin: 11111111.11111111.11111100.00000000 Máscara Dec: 255.255.252.0 IP 192.168.15.0/20 Máscara Bin: 11111111.11111111.11110000.00000000 Máscara Dec: 255.255.240.0

Para entendermos melhor:

* **/20** é referente à quantidade de 1 na máscara de redes
* **Bin** é a representação binária da quantidade de bits fechados e abertos que determinam a máscara de rede daquele IP
* **Dec** é a representação decimal da máscara de rede, para chegarmos a este cálculo basicamente precisamos calcular o valor de cada byte da máscara binária, para isso precisamos ter em mente a distribuição dos valores de cada bit, com isso vamos ver o exemplo abaixo, onde vemos um byte (composto por 8 bits) e acima o valor que representa cada bit, vamos ver o exemplo do ip 192.168.15.0/22

```bash
**192.168.15.0/22**
Máscara Bin: 11111111.11111111.11111100.00000000
```

Para calcular a máscara decimal partiremos da máscara binária, como o valor de cada bit decimal ativo seria correspondente ao seu valor basta somar suas representações, por exemplo, no primeiro e no segundo octeto possuímos todos os bits ativos, portanto basta somar suas posições, por exemplo:

```
Valor:   128   64   32   16   8   4   2   1
Bits:     1     1    1    1   1   1   1   1
```

Somando 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 teremos 255, portanto conseguimos saber que os dois primeiros octetos serão 255, portanto nossa máscara começaria com "255.255", a partir disso conseguimos inferir que o último octeto será 0 já que não temos bits ativos, ou seja "00000000". Agora só precisamos calcular o terceiro octeto para termos seu valor decimal. Vamos somar o valor de seus bits ativos:

```
Valor:    128   64   32   16   8   4   2   1
Bits:      1     1    1    1   1   1   0   0
```

Agora sim, somando todos os bits ativos (ou subtraindo a soma dos inativos do valor 255, o valor fechados do byte) chegaremos a: 128 + 64 + 32 + 16 + 8 + 4 = 252, ou então, pela lógica reversa: 255 - (2 + 1) = 252.

Sendo assim teremos nossa máscara de rede final como: 255.255.252.0 e o compilado de representação de máscaras sendo:

|         |                                     |
| ------- | ----------------------------------- |
| IP      | 192.168.15.0/22                     |
| Binário | 11111111.11111111.11111100.00000000 |
| Decimal | 255.255.252.0                       |

Algo que vale se prestar atenção é que a máscara de redes vai definir quantos IPs teremos na rede, quanto mais "0" houverem na máscara, maior disponibilidade de hosts teremos na rede e vice-versa.

Atividade do dia:

* Criar uma topologia de rede constando 2 hosts que sejam de classe B (ou seja, IPs compreendidos entre 172.16.0.0 e 172.31.255.255) mas sem ser sua máscara padrão, sendo máscara /23 (a máscara padrão desta classe é 255.255.0.0 ou /16)
* Precisa-se ter 2 switches conectados entre si usando 2 cabos Gigabit
* Numa ponta precisa-se de 2 Servidores sendo um DNS, outro Web e um host
* Alterar o HTML do servidor de maneira a apresentar seu nome no website
* Resolver o endereço do website através do servidor DNS
* Indicar a quantidade de endereços úteis na rede
