# Camada de Rede

\-ARP(IPv4) vs NDP(IPv6) \* tarefa para casa

\-Default Gateway

\-Esquema de endereçamento básico -classes IPv4 (IPv6) NAT -os endereços IP não são todos iguais (vídeo) \* tarefa para casa -DHCP -Roteamento estático vc dinâmico (classes IGP vc EGP)

Tamanho (carga) maxima de um pacote IP => 65536 bytes ou 2¹⁶

Tamanho (carga) do frame ethernet (MTU) => 1500 bytes

A carga de um IP precisaria caber dentro do frame ethernet, por conta deste tamanho ele não consegue ser transportado em apenas um frame, precisando ser fragmentado em vários pacotes, de forma a que toda sua carga possa ser enviada independentemente do meio em que a mesma se encontra, para isso temos o MTU (Maximum Transmit Unit)

I sustema de fragmentação do IPv6 não funiona de maneira correta pois os analistas de segurança da informação bloqueiam o ICMP de maneira discriminada, o correto é bloquear apenas i ICMPv4, mas o ICMPv6 deve ser permitido (inclusive é uma gafe bloqueá-lo)

Pegar o livro do IPv6 e fazer os laboratórios na medida do possível, o livro está disponível no site do nic.br.

* Experiência 1.1. Neighbor Discovery Protocol: Neighbor Solicitation e Neighbor Advertisement
* Experiência 1.10. Path MTU Discovery: mensagem ICMPv6 do tipo packet too bi

Pular da experiência 1 e pular para a 3.1

Estudar NDP e comparar ao ARP de acordo com suas funcionalidades

ARP => é o protocolo de descoerta de vizinhança no IPv4, ele detecta qual o dispositivo de destino em uma determinada comunicação na rede.

Como padrão, switches de camada 2 não sabem os numeros IPs de suas máquinas, mas quando enviamos pacotes usando IP teremos apenas os endereços IP, neste momento ocorre que o primeiro host primeiramente envia uma solicitação ARP Request, que possui o endereo IP de origem e destino, ao chegar a um dispositivo de segunda camada (switch) o switch faz um broadcast em todos os dispositivos conectados a ele com o ARP Request contendo o IP de destino que foi enviado pelo host de origem, quando um dispositivo host detecta que o IP de destino é o seu, ele envia a resposta com seu MAC address para o host de destino; a partir de aí começa a conexão par a par entre os dois hosts, fazendo com que ocorra a comunicação entre pacotes, pois a tabela ARP de ambos os dispositivos estava preenchida e agora podem enviar requisições ao switch para o MAC Address específico um do outro.

Para MITM no kali: dsniff

Endereçamento:

192.168.0.10

```
                +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
                |   192    |    168    |    000    |    010    |
                +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
                |           NetId/Prefixo          |  hostId   |
                +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
                |        Rua de uma cidade         |   casa    |
                +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
```



define-se o default gateway por padrão como o primeiro endereço válido da rede, no caso acima seria 192.168.0.1, não muda nada alterar o endereço do gateway padrão.

* 192.168.0.0 => endereço de rede | não pode ser usado&#x20;
* 192.168.0.1 => ideal para configurar o gateway padrão&#x20;
* 192.168.0.n - 2 => endereços que podem ser utilizados&#x20;
* 192.168.0.255 => endereço de broadcast da rede&#x20;
* 127.0.0.1 | ::1 => Endereço de loopback, ou seja, echo no sistema

```
Classes de rede:
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|       |   dec   |      bin      |                                                     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Classe |  Range  | 1 | 2 | 3 | 4 |      Redes     |        Hosts       |    Tamanho    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|   A   |  0-127  | x |   |   |   |     2⁸=256     |   2²⁴=16.777.216   |     Grande    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|   B   | 128-191 | x | x |   |   |   2¹⁶=65.536   |     2¹⁶=65.536     |     Média     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|   C   | 192-223 | x | x | x |   | 2²⁴=16.777.216 |       2⁸=256       |     Pequeno   |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|   D   | 224-239 |   Multicast   |                                                     | 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|   E   | 240-255 |    Estudos    |                                                     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

\*byte mais à esquerda é mais importante
