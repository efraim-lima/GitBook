# TCP

Socket: Ip e Porta de origem x Ip e Porta de destino

Seed: a conexão fixada entre IP de destino e IP de origem

UDP connectionless => não orientado à conexão ---> server para DNS services, NTPs services para sincronizar horarios

TCP connectione => orientado à conexão

O processo de conexão TCP (handshake):&#x20;

SYN&#x20;

SYN,ACK&#x20;

ACK&#x20;

PSH, ACK&#x20;

ACK&#x20;

FIN, ACK&#x20;

FIN, ACK&#x20;

ACK

No wireshark o hacker analisa as mensagens com a flag PSH (ou push)

Estudar gerenciamento de serviços

checar os rfcs do tcp e do udpm no site da ietf.org.
