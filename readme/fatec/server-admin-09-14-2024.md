Dentro do Windows server podemos criar uma estrutura de dependẽncias dentro das formas organizacionais baseando-se na estrutura lógica mais apropriada para a organização da empresa como um todo

Quando precisarmos criar alguma estrutura lógica organizacional basta criarmos uma nova OU (Organizational Unit) dentro do domínio que estamos localizados; atenção que estas OUs serão sempre criadas automaticamente com uma proteção de segurança que inibe deleção acidental de OUs dentro do domínio (basta criar como novo)

Ao adicionar uma nova estação de trabalho, no domínio devemos devemos ir em 

``` Configurações >  Sistema > Sobre > Configurações Avançadas do Sistema> Nome do Computador > Alterare adicionar 
```
o usuário naquele ponto especifico, colocando ou removendo o domínio àquela máquina com login de admin (verificar se isso é real)

No samba4 as vezes precisamos delegar e atribuir as permissões necessárias para cada usuário e grupos, isso pode ser feito com o  RSAT


Passo a passo para configurar a descoberta de recursos detro do servidore no sistema
- no servidor, ao fazer a instalação, precisamos configurar pontos cruciais:
    - Instalar os serviços necessários

Ao criar um grupo precisamos ter em vista que ele pode ter alguns escopos de grupo. Estes escopos sao divididos entre local, global e universal, onde o local possui acesso apenas aos recursos de sua OU, o Global possui acesso ao domínio e o universal acesso a todos recursos de todos domínios que se conectem.

Atribuir regras para uma cadeia de grupo permite que todas as permissões sejam dadas para o grupo completo, sendo que todos acabariam tendo acesso às informações e recursos de acordo com suas permissões naquela hierarquia
