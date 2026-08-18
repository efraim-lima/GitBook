# Terminal
#tmux #linux #segurança #monitoramento #admin #sistema #CLI #terminal 

Tmux é um utilitario para uso via terminal, ele tem diversos recursos que auxiliam na divisão de abas do terminal, disposição e ajuda bastante na produtividade.

Com isso tem algumas coisas que podemos fazer com ele, no caso eutenho construido um dashboard para uso no tmux.

## Cockpit
Construí um cockpit que me ajuda a monitorar a máquina assim que inicio (vou implementar uma rotina cron para iniciar sempre que houver uma nova sessão -- talvez um deamon).

### btop
O btop é um substituto do htop, funciona semelhantemente, mas com alguns recursos a mais. Ele está rodando com o comando:

``` bash
sudo gtop
```

### gping
O gping subsitui o ping, indicando um grafico de performance da velocidade de resposta ao longo do tempo, eu gosto de configurar um tempo para a emissão dos pacotes ICMP para não caracterizar os pings como varredura ou DOS. 

``` bash
sudo gping --watch-interval 1.5 google.com yahoo.com registro.br
```

### last
Utilizo o last para verificar os acessos em minha máquina, deste modo posso verificar os usuários que acessaram minha máquina, o que pode me indicar algum tipo de acesso indevido em meu sistema.

``` bash
sudo last -a | less
```

O uso do pipe "|" e do less é para que eu possa verificar as ultimas entradas.
Para investigar falhas de acesso eu uso o lastb, assim consigo verificar se tem ocorrido algum tipo de bruteforce no ambiente.

```bash
sudo lastb | less
```


### wavemon
Uso o wavemon para ter um diagnóstico de minha rede, assim tenho acesso a alguns recursos que me auxiliam no monitoramento da qualidade de minha rede wireless, depois pretendo unir a um outro projeto meu para contra-espionagem.

``` bash
sudo wavemon
```

### iptop
O iftop serve para monitorar o tráfego de rede em tempo real por conexão. Ele escuta uma placa de rede específica e mostra quem está enviando e recebendo dados, ordenando os dispositivos que mais estão consumindo a sua internet ou banda local naquele exato momento.

Antes de todar o iftop precisamos saber qual interface de rede vamos monitorar.

```bash
sudo ip addr show
```

Com isso basta utilizarmos o iftop para monitorar a rede do ambiente.

```bash 
sudo iftop -i <interface>
```


## Gerenciamento de sessões
Para gerenciar sessões do tmux eu utilizo um utilitário bem objetivo...o tmuxp, com ele basta salvar uma sessão e suas configurações usando:

```bash 
tmuxp freeze -o ~/.config/tmuxp/mysession.yaml
```

E depois basta restaurar a sessão usando

```bash
tmuxp load mysession
```


