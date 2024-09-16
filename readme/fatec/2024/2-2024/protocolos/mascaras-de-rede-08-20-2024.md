# Máscaras de Rede 08-20-2024

Uma maneira legal de se calcular as mascaras conriga e extrair o decimal a partir do binario, calcular o restante e a partir disso fazer o processo de calcular o restante.

Exemplo: IP: 192.168.0.128/26 BIN: 11111111.11111111.11111111.11000000

Calculando os binarios do ultimo octeto teremos 128 + 64 = 192, ou seja nossa mascara de rede em decimal e: 255.255.255.192, agora basta calcular quantos bits abertos temos fazendo a subtraçao do limite de IPs (255.255.255.255) da nossa mascara de rede em decimal. Abaixo segue uma tabela ilustrativa do processo passo a passo.

| Descrição                            | IP                                   |
| ------------------------------------ | ------------------------------------ |
| Enderço de Rede + Máscara em binário | 192 . 168 . 0 . 0 /26                |
| Máscara Binário                      | 11111111.11111111.11111111.11000000  |
| Máscara Binário reversa              | 00000000.00000000.00000000.00111111  |
| Máscara de Rede em decimal           | 255.255.255.192                      |
| Calculo de hosts na rede             | 255.255.255.255 - 255.255.255.192    |
| IPs disponíveis                      | 0.0.0.63                             |
| Brodcast da rede                     | 192.168.0.63                         |

Chegaremos ao numero de IPs disponiveis naquela mascara, mas precisamos compreender que 2 IPs nao podem ser utilizados, nem o endereço de broadcast (ultimo endereço da rede) e nem o endereço de rede (primeiro endereço). Com isso saberemos que podemos adicionar 61 dispositivos nesta rede.
