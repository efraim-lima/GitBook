# Camada de Transporte

Processo para analisar processos suspeitos.

Encontrando portas registradas no linux:

/etc/servces

Encontrando os sockets conectados na rede: sudo netstat -putan sudo ss -putan'

Analisando os logs dos ultimos processos: sudo tail -f auth.log

Os hackers atacam os sites por meio de proxy Random Socks Server -> Proxy Chains, são maquinas na rede que estão aleatoriamente na rede e ficam ligadas apenas em horários especificos, assim desligam estes servidores e não podem mais ser identificados

Camada 8 da OSI = Usuário

Antes de ocorrer o processo de conexão entre cliente e servidor ocorre o processo 3 way handshake.

Como um nmap sabe que uma porta em um servidor está aberta? O nmap tem uma base de dados com as 1000 portas mais acessadas.

O nmap padrão atua usando o SYN flood (inundação), que significa enviar 1000 pacotes para as portas e aguarda as respostas

RTT (Round Trip Time) => o tempo que leva para enviar um SYN MSS e receber um SYN ACK MSS ou RST ACK

MSS (Maximum Segment Size) MYU (Maximum Transport Unit) H (Headers) => cada Header custa 20bytes

Tamanho da carga util dos pacotes = MSS - (H + H) Logo, carga util = MSS bytes - 40bytes

Para transportar dados muito grandes pela rede, o TCP fragmenta os pacotes e identifica o Sequence Number de cada frame para que possa ser novamente identificado na chegada e os dados (informação) sejam remontados no fim garantindo sua integridade.

O TCP mantém uma copia dos dados no buffer do emissor, aguarda o ACK por uma quantidade de tempo de RTT (Round Trip Time) O RTT trabalha em cima da media movel exponencial ponderada e adiciona o coeficiente de "cagaço"

O processo de investigar os processos no servidor é feito durante o handshake

No wireshark vale a pena fazer o diagrama de fluxo da conexão

CRUD:

Estamos entrando no conceito de Create Read Update e Delete Para cada etapa do CRUD temos um referencial de método no HTTP. Por exemplo:

* C - POST&#x20;
* R - GET&#x20;
* U - PUT, PATCH, POST&#x20;
* D - DELETE

O processo de encapsulamento proporciona um problema de Overhead na comunicação (que é o preenchimento do pacote por protocolos de comunicação)

Proxima aula pegar o ROADMAP



Acessar o documeto RFC 2460 -> https://www.rfc-editor.org/rfc/rfc2460

Next Header e Protocol identificam o que tem dentro do pacote, é uma inspeção do que o mesmo está carregando.
