# Portas

Processos se comunicam através de portas na rede, por exemplo: a padrão de web client é a 80, a padrão de ssh é a 22

Um servico de servidor rodando dentro do system control pode ser chamado tanto pelo nome do serviço quanto pelo nome de daemon (daemon service), o que indica que o mesmo está rolando como um processo a parte no sistema.

As portas são maneiras de diferenciar serviços dentro da rede (direcionando pacotes para os locais corretos).

Estudar um pouco de iptables e ufw.

Desligar o verificar o ufw: sudo ufw disable / status

Para saber se uma porta está livre ou não, no linux:

cat /etc/services sudo tail -f /etc/log/auth.log

etc -> arquivos de configuração do linux