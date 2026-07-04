---
Created: 2026-04-01T17:55
Criado em: 2026-04-01T17:55
Criado em 1: 2026-04-01T17:55
Criado por: 2026-04-01T17:55
---
## Como manter o ambiente seguro
  
### Portas e serviços expostos
Para portas e serviços expostos na infraestrutura do servidor fica evidente que existe a necessidade de hardening do servidor antes deste tipo de teste, pois algumas das vulnerabilidades encontradas com o nmap são fruto de configurações do servidor que devem ser previamente ajustadas antes da instalação do container, para mitigar este tipo de fragilidade no ambiente temos algumas boas práticas que podem ser seguidas de acordo com o artigo “How I secure my linux servers: Best Practices for 2025” <[https://medium.com/codetodeploy/how-i-secure-my-linux-servers-best-practices-for-2025-5e38c6839229](https://medium.com/codetodeploy/how-i-secure-my-linux-servers-best-practices-for-2025-5e38c6839229)> e também podemos seguir dicas provenientes do github “How to secure a linux server” <[https://github.com/imthenachoman/how-to-secure-a-linux-server](https://github.com/imthenachoman/how-to-secure-a-linux-server)>, por fim podemos ter uma visão ampla de como manter o servidor seguro a partir do artigo “Linux security best practices for safe operations” da Suse <[https://www.suse.com/c/linux-security-best-practices-for-safe-operations/](https://www.suse.com/c/linux-security-best-practices-for-safe-operations/)> de forma a termos uma base de quais as principais brechas de um servidor Linux que devem ser fechadas até mesmo antes da instalação do AgentK.
Como o foco deste trabalho não é apenas na parte de segurança do servidor como infraestrutura, mas como software precisamos abordar outras frentes e visões sobre o ambiente.
## Trafego em texto plano HTTP to HTTPS
Para implementar a segurança de tráfego dos dados entre servidor e cliente devemos implementar criptografia nos dados em transito, para isso basta instalarmos o certificado SSL ao servidor e garantir que o ambiente esteja direcionando o tráfego da forma correta pelo caminho correto. Nisso basta instalar o certificado no servidor utilizando o comando
```bash
openssl req -new -x509 -days 90 -newkey rsa:4096 -sha512 -nodes -out agentk.cert -keyout agentk.key
```
![[image 29.png|image 29.png]]
Assim teremos o certificado instalado, mas como o artigo “Nginx Reverse Proxy with TLS Encryption” direciona utilizar o Nginx para complementar o processo de criptografia do trafego vamos utilizar o processo de configuração mencionado.
  
Feito isso seguir os passos seguintes
Ao concluir o processo de encriptar o tráfego e capturar via Wareshark pode-se aferir que o tráfego está fluindo de forma encriptada, sem texto plano nos dados.
Emitindo prompt a partir do ambiente encriptado.
![[image 1 2.png|image 1 2.png]]
Transcrição:

> Você é AgentK, especialista em configurações YAML do Kubernetes e aplicação  
> de boas práticas. Seu papel é guiar na criação, análise e otimização de  
> recursos YAML seguindo padrões de produção. Capacidades:
> 
> - Extrair e analisar YAMLs existentes do cluster
> 
> - Sugerir melhorias e correções baseadas em boas práticas
> 
> - Validar configurações antes da aplicação (client dry-run)
> 
> - Implementar recursos
> 
> - Gerenciar ciclo de vida completo (create/update/delete)  
>     Recursos suportados:  
>     Namespaced: pods, services, deployments, configmaps, secrets, ingresses, pvcs, replicasets, statefulsets, cronjobs, jobs  
>     Cluster-wide: nodes, persistent_volumes, namespaces  
>     Foco em boas práticas:
> 
> - Labels e annotations consistentes
> 
> - Resource limits e requests adequados
> 
> - Configurações de segurança apropriadas
> 
> - Estrutura YAML limpa e legível
> 
> - Imagens com versões específicas  
>     Sempre valide antes de aplicar e sugira melhorias quando identificar  
>     oportunidades. Se for responder com yaml, utilize a formatação  
>     apropriada.
> 
> Teste de conexão
> 
> Conexão  
> recebida! Estou pronto para analisar, validar e otimizar recursos YAML  
> do seu cluster Kubernetes. Como posso ajudar você hoje?
A partir disso podemos analisar no WireShark, seguindo o processo de armazenar o trafego no período de teste para que tenhamos todos pacotes coletados, filtrar o trafego através do filtro ip.addr==<IP do servidor> and tcp.port==443 e procurar pacotes com tamanhos elevados.
Nisso conseguimos encontrar o pacote abaixo:
![[image 2 2.png|image 2 2.png]]
Ai dar Follow no stream conseguimos reparar no tráfego totalmente encriptado e devidamente seguro.
![[image 3 2.png|image 3 2.png]]
  
## Autenticação utilizando KeyCloak e OAuth2
Para uma boa segurança do acesso à ferramenta foi utilizado o Keycloak para ingresso dos usuários e o OAuth2 como complemento ao processo de autenticação do usuário, seguindo as boas práticas recomendadas pelo NIST em sua publicação especial 800-63B [https://pages.nist.gov/800-63-3/sp800-63b.html#:~:text=The ongoing authentication of subscribers,event of loss or theft](https://pages.nist.gov/800-63-3/sp800-63b.html#:~:text=The%20ongoing%20authentication%20of%20subscribers,event%20of%20loss%20or%20theft). e também CISA [https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/require-multifactor-authentication](https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/require-multifactor-authentication) em sua publicação “Multifactor Authentication Provides Extra Security”.
OAuth [https://dev.to/kimmaida/oauth-20-security-best-practices-for-developers-2ba5](https://dev.to/kimmaida/oauth-20-security-best-practices-for-developers-2ba5)
Keycloak [https://www.keycloak.org/guides](https://www.keycloak.org/guides) - [https://www.keycloak.org/server/configuration](https://www.keycloak.org/server/configuration)
Para o design de autentcação foi pensado no seguinte design para o processo:
Usuário → SSH Tunnel (para casos de acesso externo)→ OAuth2 Proxy (4180) → Keycloak (8080) → AgentK (8501)
Nessa arquitetura os componentes terão os seguintes objetivos:
|   |   |
|---|---|
|Componente|Função|
|Keycloak|Gerencia usuários, grupos e autenticação|
|OAuth2 Proxy|Intercepta acessos e valida autenticação|
|SSH Tunnel|Criptografa o tráfego entre o computador e o servidor|
  
Nisso foi criado o processo de autenteicação no ambiente a partir da implementação do keycloak seguindo [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] seguintes passos:  
  
Parte 1 — Ajustar o docker-compose.yaml para o sugerido
  
Parte 2 — Subindo [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] containers  
cd ~/AgentK-MCP  
docker compose up -d  
docker compose ps  
Parte 3 — Configuração do Keycloak  
Acessa o painel em [http://localhost:8080](http://localhost:8080/) com admin / admin123 .  
3.1 — Criar o Realm
1. Clica no dropdown Keycloak no canto superior esquerdo
1. Clica em Create Realm
1. Realm name: agentk
1. Clica em Create  
    3.2 — Criar o Client
1. Clica em Clients → Create client
1. Client ID: oauth2-proxy
1. Client type: OpenID Connect
1. Clica em Next
1. Ativa Client authentication: On
1. Clica em Next
1. Root URL: [http://localhost:4180](http://localhost:4180/)
1. Valid redirect URIs: [http://localhost:4180/oauth2/callback](http://localhost:4180/oauth2/callback)
1. Web origins: [http://localhost:4180](http://localhost:4180/)
1. Clica em Save
1. Vai na aba Credentials e anota o Client Secret gerado  
    3.3 — Atualizar o Client Secret no docker-compose.yml  
    Substitui SEU_CLIENT_SECRET pelo valor gerado:- --client-secret=SEU_CLIENT_SECRET_AQUI  
    Recria o container:  
    docker compose up -d --force-recreate oauth2-proxy  
    3.4 — Criar [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] grupos
1. Clica em Groups → Create group
1. Cria o grupo users
1. Cria o grupo admins  
    3.5 — Criar [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] usuários  
    Criados 8 usuários com Email verified: On e senha teste123321 com Temporary: Off:
  
## Implementacao de estrutura de logs
Abaixo segue o que foi implementado no AgentK para que fosse possível a persistencia de [[CyberSecurity/Course/forense/logs/logs|logs]] no ambiente.
  
```markdown
# Alterações de Logging do Ambiente AgentK
Data: 2026-04-24
## Objetivo
Centralizar e padronizar os logs do cliente e do servidor, com suporte a níveis de log (DEBUG, INFO, WARNING, ERROR, CRITICAL), gravação em arquivo de sistema e rotação de arquivos.
## Arquivos criados
### 1) logs/logging_config.py
Configuração centralizada de logging para todo o projeto.
Implementado:
- Leitura de variáveis de ambiente:
  - AGENTK_LOG_LEVEL
  - AGENTK_LOG_DIR
  - AGENTK_LOG_MAX_MB
  - AGENTK_LOG_BACKUPS
- Resolução de diretório de log:
  - Prioriza AGENTK_LOG_DIR
  - Tenta /var/log/agentk
  - Fallback para diretório local logs/
- Formato padrão de log com timestamp + nível + logger + mensagem
- Handlers:
  - stdout
  - arquivo com rotação (RotatingFileHandler)
- Função pública get_logger(name, log_file)
### 2) server/app/utils/logger.py
Wrapper de logger do servidor.
Implementado:
- Ajuste de path para importar a configuração central em logs/logging_config.py
- Definição de arquivo padrão:
  - AGENTK_SERVER_LOG_FILE (default: agentk-server.log)
- Exposição de logger com nome agentk.server
### 3) client/app/utils/logger.py
Wrapper de logger do cliente.
Implementado:
- Ajuste de path para importar a configuração central em logs/logging_config.py
- Definição de arquivo padrão:
  - AGENTK_CLIENT_LOG_FILE (default: agentk-client.log)
- Exposição de logger com nome agentk.client
## Arquivos alterados
### 4) server/app/main.py
Refatoração do logging antigo para o novo modelo centralizado.
Alterações:
- Removido logging.basicConfig local
- Removido FileHandler local mcp_server.log
- Adicionado import do logger central:
  - from utils.logger import logger
Impacto:
- Servidor passa a usar configuração única e controlada por variáveis de ambiente
### 5) client/app/classes/mcp_client.py
Substituição do debug manual por logging estruturado.
Alterações:
- Removido método _debug_log que gravava em client.log
- Removida flag booleana _debug
- Adicionado import do logger central:
  - from app.utils.logger import logger
- Adicionados logs de operação nos métodos principais:
  - initialize_with_stdio
  - initialize_with_http
  - get_tools
  - get_resources
  - get_prompts
  - call_tool (com tratamento de erro e logger.error)
  - get_resource
  - invoke_prompt
  - cleanup
Impacto:
- Cliente passa a registrar eventos relevantes com níveis apropriados
### 6) docker-compose.yml
Configuração de persistência e compartilhamento de logs no ambiente containerizado.
Alterações no serviço agentk-server:
- Variáveis adicionadas:
  - AGENTK_LOG_LEVEL
  - AGENTK_LOG_DIR=/var/log/agentk
  - AGENTK_LOG_MAX_MB
  - AGENTK_LOG_BACKUPS
  - AGENTK_SERVER_LOG_FILE=agentk-server.log
- Volume adicionado:
  - agentk-logs:/var/log/agentk
Alterações no serviço agentk-client:
- Variáveis adicionadas:
  - AGENTK_LOG_LEVEL
  - AGENTK_LOG_DIR=/var/log/agentk
  - AGENTK_LOG_MAX_MB
  - AGENTK_LOG_BACKUPS
  - AGENTK_CLIENT_LOG_FILE=agentk-client.log
- Volume adicionado:
  - agentk-logs:/var/log/agentk
Resultado:
- Cliente e servidor gravam logs no mesmo diretório de sistema dentro do container
- Persistência via volume Docker agentk-logs
## Níveis de log contemplados
- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL
## Diretório de logs
Prioridade de destino:
1. AGENTK_LOG_DIR (quando definido)
2. /var/log/agentk (quando disponível e gravável)
3. logs/ local do projeto (fallback)
## Rotação de logs
Implementada via RotatingFileHandler:
- Tamanho máximo por arquivo: AGENTK_LOG_MAX_MB (default 10 MB)
- Quantidade de backups: AGENTK_LOG_BACKUPS (default 5)
## Observações
- O arquivo central de configuração permite controle fino de emissão sem alterar código-fonte.
- A separação por arquivo (agentk-server.log e agentk-client.log) facilita troubleshooting.
- Logs continuam sendo emitidos no stdout, útil para observabilidade com docker logs.
```
  
  
  
  
## Guardrails
Foi criada uma ferramenta de guardrail que tem o objetivo de coletar o que foi emitido como prompt no AgentK, validando localmente através de uma LLM local (qwen 2.5/1.5GB) que valida se o prompt se enquadra em alguns padrões como VALIDO, SUSPEITO, NOCIVO e PERIGOSO ([[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] termos divergem, estão em inglês). Foi implementada uma alteração no código do cliente MCP que disponbiliza o prompt para o chatGPT, essa alteração intercepta o prompt antes que seja emitido como requisição ao servidor e ao chatGPT, nessa interceptação ocorre a transferencia do prompt para a LLM local validar a possível intenção do prompt (com base em instruções que são emitidas junto ao processo de análise), a LLM devolve uma resposta curta para o cliente indicando o resultado da analise que, dependendo do resultado emitirá o prompt para o servidor e o chatGPT ou então irá barrar esta emissão pode parecer nociva ou não fizer sentido para o ambiente.
Nisso foi capturado o seguinte resultado:
![[image 4 2.png|image 4 2.png]]
Com essa prova de conceito conseguimos definir que o usuário não consegue emitir [[comandos]] potencialmente nocivos ao ambiente.