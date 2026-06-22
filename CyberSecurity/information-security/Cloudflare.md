#Assuntos abordados no evento

- AI Guardrails
- AI Gateway
- MCP Servers

## AI Security Report
COnseguimos ter uma cobertura referente a quais IAs estão sendo utilizadas, volume de requisições, volume de requisições, quais IAs são aprovadas, negadas, em revisão e que precisam de revisão.
-- o objetivo é 

## Visualisação 
### Teams Resources
Em Teams Resources podemos observar quais IAs são permitidas ou não, configurando quais IAs são liberadas. Neste processo estamos apenas criando uma flag, mas não estamos bloqueando de fato, para bloquear devemos ir em Firewall Policies, inde criamos regras que podem ser utilizadas para tomar decisões em momentos que o usuário estiver utilizando as IAs (funciona no navegador, inclusive).

Por exemplo:
- redirecionar o usuário (em caso de browser isolado) de uma IA nao aprovada para outra devidamente liberada,
- logar prompts que tenham sido considerado
- emitir um popup em casos onde o user esteja usando o ARP,
- restringir conteúdos a serem emitidos (dados sensíveis como CPF, PLL, Informações financeiras

### HTTP Request Logs
Aqui podemos ver como [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] colaboradores 
- interagem em seus prompts,
- o que enviaram que inflinge as politicas da empresa
- ver [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] prompts
- ver quem emitiu

## Governança de AI
Agentes perdem informações que servem para auditoria e monitoramento de agentes MCP, a melhor forma de fazer.
llm.txt: serve para redirecionar bots (como um robots.txt) que redireciona bots para o servidor MCP de uma aplicação quando um agente faz uma varredura no ambiente em busca de APIs ou [[tools]] para se conectar.

### Workers Observability MCP Server
Possui diversas [[tools]] que permitem observabilidade e capilaridde na cobertura do ambiente.

- portais de MCP server: faz append de todas as funções de todos [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] agentes, workers, documentações e funções no ambiente de forma a permitir que um agente tenha acesso a todo o ambiente disponibilizado pela Cloudflare, permitindo que haja [[Segurança]], accounting e auditoria no uso dos agentes, uma vez que o portal centraliza o trafego de agentes em um só local
-- utiliza ZeroTrust para acesso ao ambiente, inclusive com uso de OAuth
-- o portal permite a configuração de DOminio, [[CyberSecurity/Course/forense/logs/logs]], servidores MCP participantes (o cadastro desses servidores ẽ feito fora), politicas de acesso e testar o portal a partir de AI playground, claude desktop ou outros [[CLIENTES]];
-- em workers tem um agente que pode ser utilizado para aplicar em um modelo de forma rapida e otimizada;

## Protect AI-powered Apps
Ao dizer bom dia para um chatbot de empresas pode-se ocorrer o direcionamento do usuário a um banco de dados vetorizado a partir de RAG para direcionar a resposta mais efetiva para o usuário a partir de sua pergunta.
A Cloudflare utiliza um modelo para combater outro modelo atacante, tendo [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] modelos rodando na rede anycast, cada POP da Cloudflare roda todos [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] serviços e permite que em cada node, cada ponto possa ter o mesmo nível de proteçao e capilaridade.

Um atacante procura impelir prompt injection ao sistema, a clouflare consegue bloquear isso nativamente no sistema assim como envenenar o modelo com informações erradas ou dados sensíveis

O WAF da cloudflare consegue rankear o nível de probabilidade de um elemento ser prompt injection

### AI Firewall
Funciona quando um endpoint é configurado como uma LLM endpoint, tendo uma flag sendo setada (cf-llm)

### AI Gateway
É o Guardrail da CLoudflare, serve para [[CLIENTES]] que não possuem WAF da Cloudflare, com essa ferramenta podemos setar algumas regras:
- coleta de [[CyberSecurity/Course/forense/logs/logs]]
- cache de respostas
- auth gateway
- limite de requisições

A aplicação de IA passará pelo gateway da Cloudflare, onde é feita a implementação do Guardrail (regras de conteudo sexual, dafamar, eleições, prompt injection), implementar DLP (evitando envio de dados sensiveis ou documentos --para casos de modelos multimodais)  e tudo isso feito de forma proxiada na rede

Dentro do AI Gateway pode-se criar rotas dinamicas, funcionando como um fallback de modelo, ou balanceador de carga para caso um modelo caia, caso haja exaustão de tokens por exemplo.
O AI Gateway serve também como um orqustrador de modelos, podendo redirecionar prompts para modelos diferenciados.
A cloudflare consegue cachear as respostas do modelo, reduzindo o custo de interações desnecessárias com IA.

Basicamente [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] modelos da CLoudflare atuam no trafego HTTP (sim, HTTP) pegando Requests e Responses em HTTP e filtrando o json neste meio termo, lembrando que o tráfego está sendo proxiado pela cloudflare, sendo uma solução impressionante no processo de [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/desenvolvimento|desenvolvimento]] da empresa.

A Gateway consegue ler imagens subidas para modelos multimodais (limite de 15Mb) em busca de subida de PIIs ou dados sensíveis. Mas a ferramenta consegue fazer a leitura de dados via OCR tanto para DLP quanto para [[Evitar]] alimentar modelos com dados sensíveis.

Um agente de IA pode ser subido no Worker da Cloudflare e direcionar seus agentes e [[tools]] para o MCP Server Portal, sendo o [[CyberSecurity/fatec/Pesquisa/Trabalho/Trabalho]] de hard code direcionado apenas no processo de criar a VPS com o servidor.

Importante:
Cloudflare não conecta com outros players que tenham ZTNA ou SASE 
