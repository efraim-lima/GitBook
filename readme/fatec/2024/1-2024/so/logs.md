# logs

Vale a pena configurar os logs da máquina, configurando logs específicos para cada ação, mas estruturar de maneira mais convencional com os warns e err, para ter tudo corretaente no lugar correto.

bin refere-se a binários, que são os executáveis do linux. O diretório bin é obrigatório, por conta do LSB (Linix Standard Bas), lá está definido que em todas distros linux é obrigatório ter o diretório bin, nem que seja link simbolico. No linux não temos atalhos, temos links simbolicos, antigamente tinham-se cópias dos arquvs de bin dentro de /usr/bin, agora são links simbólicos. apenas usuários de sistema possuem acesso ao diretório bin, pois antes havia uma cópia dos arquivos em usr/bin para que não houvessem erros. A permissão de edição dos binários no linux parte do pressuposto que o usuário sabe o que está fazendo.

Segundo o LSB deve-se identar os usuários de acordo com o ficheiro "/", que na verdade é um link simbólico oara /usr, pois dessa forma o usuário não vai fazer alterações na raiz do sistema

Antigamente poderiamos acessar o cmd de qualquer servidor através do navegador por conta dos parâmetros dos ficheiros, por exemplo:

http://www.dominio.com/../../winnt/system32/cmd.exe

desse jeito poderiamos acessar o cmd direto do sistema operacional, em servidores eb mais antigos. Para testar isso podemos instalar: windows nt 4.0/IIS 4.0 (sem o service pack 4, apenas até o 3)

nslookup --text=MX // para descobrir qual a url responsável por aquele serviço telnet 25 // usar portas não padrão do telnet

ao dar telnet nunca apontar sem direcionar qual porta quer especificamente, pois pode ter umm ataque reverso configurado para aquela porta.

Sniffer de rede para ataque reverso quando alguém tenta acessar uma porta X

Portas mais importantes para se decorar Todas abaixo de 1024 são portas de entrada

21 FTP&#x20;

22 SSH&#x20;

23 TELNET&#x20;

25 SMTP ou SMTPS

Todo servidor SMTP precisa de um comando EHLO para poder fazer conexão, sem isso ele não permite acesso, seria como um handshake.

diretorio boot tem os arquivos de kernel e modulos de kernel, o processo de bootstrap procura neste diretório o kernel para inicializar

diretorio dev tem os modulos de devices, onde o usuário consegue acessar o dispositivo por meio do dispositivo

etc tem tudo o que é configuravel

home é o diretório padrão do usuŕioa

Quando montamos um dispositivo no sistema unix o SO vai detectar que existe um device conectado via plug and play, montálo em /dev/sd e criaria um link simbólico com /mnt/pendrive



padrão de tamanho do sistema NTFS é de 1kb
