# Gerenciamento de Servidores 08312024 ...

Os arquivos de configuração de senhas dos servidores e estações do Windows encontram-se em diretórios no OS, e estes dados podem ser alterados via software no sistema operacional, de forma a alterar as senhas.

Workgoroup (pode administrar seus recursos próprios) => Arquivo SAM (SAM/LOCAL/WINDOWS10) Dominio => Arquivo NTDS

C:\Windows\NTDS => pasta onde armazenaremos o database e os logs C:\Windows\SYSVOL => onde colocamos scripts de usuários, como mapeamento de redes e serviços

* aqui podemos simplesmente seguir dando next ou mudar os diretórios padrão destes elementos durante a configuração de gerenciamento de serviços.

Imprescindível saber que existem outros elementos que podem interferir na configuração de serviços no sistema como firewall e hardware

CRIANDO CONFIGURAÇÕES DO AD

Primeiro precisamos configurar as redes das maquinas virutais para rodarem na rede interna e poderem se comunicar entre si.

Depois basta entrarmos nas configurações de placa de rede do windows em ambos os dispositivos virtauais (control panel > Redes e comunicação > Gerenciar Dispositivos > Propriedade > Configurações de IPv4.

Uma configuração imprescindível aqui é mexer nas regras do firewall ou então liberar o ICMP echo para que possamos pingar ambas as máquinas e testar se a rede está disponível, dessa forma podemos conectar.

enviar email par lucas.rocha50@fatec.sp.gov.br com o texto presente e fazer o trabalho todo novamente so que com o domínio sendo no nosso nome.

### Manage

Na parte de gerenciamento nós instalamos e configuramos serviços e recursos.

Ao configurar um servidor via windows server precisamos primeiros instlar um software no servidor, para iniciar os serviços necessários para a rede. Para isso devemos ir em Gerenciar > Adicionar Recursos (Manage > Add Roles and Features).

Os serviços que adicionamos em aula:

* serviços de DNS
* Active Directory Domain Services
* Active Directory Lightweight Directory Services

Após isso podemos adicionar os outros recursos, neste adicionei o Bitlocker Drive Encryption para poder encriptar os servidores.

Após isso basta irmos nas notificações do Server Manager e selecionar "Promote this server to a domain controller" ou "Promover este seridor a um controle de domínio" e seguir as etapas para definir se este servidor será master, parte de uma forest ou nova forest, setar a versão de dommínios mais antigos na rede...

Selecionamos nova forest e criamos um domínio raís "fatec.com", com as cofigurações para microsoft 2016 e a senha padrão P@st3l,configurando o DNS dando next em tudo (um processo legal seria analizar o script ao fim para facilitar o processo de detecção defalhas. Essas configurações reiniciarão o sistema e farão com que entremos com conta de domínios.

### Tools

Na parte de ferramentas nós podemos acessar e trabalhar com os serviços instalados anteriormente. Neste momento iremos na parte de ferramentas e acessaremos usuários e computadores (Tools > Active Directory Users and Computers); selecionaremos nosso domínio (no caso fatec.com) na coluna da esquerda e iremos no diretório Users, a partir daqui poderemos criar um novo usuário e determinar que sua senha seja alterada no próxio login.

Neste ponto precisaremos apenas ir na maquina host do Windows e procurar a parte de configurações avançadas do sistema para alterar os dados de domínio