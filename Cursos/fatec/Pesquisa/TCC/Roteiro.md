Video de demonstração das sugestões implementadas no AgentK

Podemos observar que o trafego está funcionando via HTTPS, com certificado autoassinado o que evidencia neste momento é a presença de um proxy configurado com nginx que ẽ responsável por garantir [[Criptografia]] dos dados via TLS de todos [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] componentes presentes no AgentK.

Depois é apresentado sistema de logon que pode ser por credenciais locais ou SSO, no caso via Google Oauth
 Colocar credenciais

Autenticação disponibilizada pelo Google diretamente
 Principalmente uso de MFA

Ao acessar a interface do AgentK pode-se observar algumas alterações propostas como o ícone de Logout, que veremos funcionando posteriormente.

Em seguida foram implementados alguns testes de prompt para apresentar a funcionalidade do Guardrail, lembrando que a validação dos prompts foi feita com uma IA totalmente local.

04:57 --> Inicio da inserção de prompt 
O primeiro prompt foi de [[Teste]] de conectividade, para indicar o prompt seguro sendo aceito e também a conectividade do AgentK com o ChatGPT.

Podemos ver o processamento da pergunta (ele está um pouco lento devido a IA local conter poucos parâmetros e também recursos mais limitados como mencionado anteriormente)
-  pode-se ver que ele passou sendo uma solicitação segura.

Em seguida foi solicitado a criação de um container com nome [[Teste]] e com imagem do nginx;
- Nisso pode-se observar que o sistema solicitou uma credencial de usuário administrador (essa credencial foi configurada anteriormente no setup da ferramenta e é fruto da análise da IA a partir do prompt)
- ao inserir a credencial o tráfego do prompt é permitido no Streamlit da aplicação e é emitido ao chat GPT
- Como pode ser observado o prompt retornou de maneira eficiente

Para o próximo [[Teste]] o objetivo foi solicitar algo que fugisse às [[CyberSecurity/fatec/2026/1-2026/Desenvolvimento/ATIVIDADES|ATIVIDADES]] do AgentK, neste caso foi solicitado uma receita de bolo.
- Como o veredicto da IA local é incerto o fluxo da aplicação é interrompido

Agora, o [[Teste]] seguinte seria de fazer uma ação mais crítica, como deletar todos [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] recursos. Nisso o retorno do prompt foi UNSAFE que está configurado para ser bloqueado também pelo sistema através das políticas propostas pelo Guardrail.

Para o próximo passo é demostrada a ação de logout do sistema, para indicar o processo rodando eficazmente.

Ao fim de tudo pode-se observar no terminal [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] [[CyberSecurity/Course/forense/logs/logs|logs]] do sistema lado a lado, à esquerda observa-se [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] [[CyberSecurity/Course/forense/logs/logs|logs]] referentes aos prompts recebidos e o veredicto da IA local e à direita pode-se observar [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] [[CyberSecurity/Course/forense/logs/logs|logs]] atrelados ao login e logout do usuário nesta sessão.

Espero ter exemplificado todas as sugestões 