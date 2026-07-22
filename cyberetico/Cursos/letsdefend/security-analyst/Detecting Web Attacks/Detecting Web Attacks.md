# Detecting Web Attacks Overview
## Ferramentas recomentadas 

Ferramenta para fazer scan de aplicações WEB de maneira objetiva desenvolvida pela OWASP: [ZAP](https://www.zaproxy.org)

Boas ferramentas para praticar e desenvolver habilidades relacionadas ao OWASP:
- [OWASP Node.js Goat \| OWASP Foundation](https://owasp.org/www-project-node.js-goat/)

# Formas de Detectar ataques WEB

## SQL Injection:
- **inserção de aspas:** Buscar por `'` ou `"` no final de um parâmetro (ex: `id=1'`). Se o sistema retornar um erro de banco de dados (como _Syntax Error_), o campo provavelmente está vulnerável. Provavelmente a requisição tera um codigo 200 ou então virá seguida de um payload de tamanho incomum.
- **Ataques baseados em tautologia (Sempre Verdadeiro):** Modificar a consulta para que ela sempre retorne um resultado positivo.
    - Exemplo clássico em campos de login: `' OR 1=1 --` ou `' OR '1'='1` [[1](https://www.tandfonline.com/doi/pdf/10.1080/19393555.2021.1995537), [2](https://www.tripwire.com/state-of-security/vert-vuln-school-sql-injection-101), [3](https://ieeexplore.ieee.org/iel7/10389811/10389819/10390153.pdf)]
- **Comentários de código:** Utilizar caracteres que anulam o restante da linha de comando SQL original para ignorar validações subsequentes (como senhas).
    - `--` (Padrão SQL)
    - `#` (MySQL)
    - `/*` (Multi-linha)

## XSS - Cross Site Scripting
Cross site scripting tem 3 formas de se testar.

- Procure por palavras-chave: A maneira mais fácil de detectar ataques XSS é procurar por palavras-chave como "alert" e "script", que são comumente usadas em payloads XSS.
- Conheça os payloads XSS mais usados: Os atacantes tendem a usar os mesmos payloads para procurar vulnerabilidades antes de explorar uma vulnerabilidade XSS. Portanto, familiarizar-se com os payloads XSS mais usados ​​facilitará a detecção de vulnerabilidades XSS. Você pode examinar alguns payloads comumente usados ​​aqui.
- Verifique o uso de caracteres especiais: Verifique os dados provenientes de um usuário para ver se há caracteres especiais comumente usados ​​em payloads XSS, como maior que (>) ou menor que (<).

1. XSS Refletido (Reflected XSS)

O script malicioso vem da requisição HTTP atual (geralmente através de um parâmetro na URL ou em um formulário) e é "refletido" imediatamente na resposta da página. [[1](https://portswigger.net/web-security/cross-site-scripting), [2](https://www.computer.org/publications/tech-news/trends/understand-cross-site-scripting-threats), [3](https://capturethebug.xyz/blogs/Cross-Site-Scripting\(XSS\)), [4](https://blog.openreplay.com/securing-react-with-dompurify/), [5](https://www.jorgeblascoalis.com/assets/papers/galan2010multi.pdf)]

- **Como testar:** Procure por barras de pesquisa, campos de filtros ou mensagens de erro que exibem o que você digitou na tela.
- **Exemplo de URL vulnerável:** `http://exemplo.com<script>alert(1)</script>`
- **Cenário de ataque:** O atacante envia esse link malicioso para a vítima. Quando a vítima clica, o script roda no navegador dela. [[1](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-reflected), [2](https://www.astrill.com/blog/cross-site-scripting/), [3](https://help.accuknox.com/use-cases/dast-xss/), [4](https://github.com/Contrast-Security-OSS/DeveloperLearnGuide/blob/main/docs/Cross%20Site%20Scripting%20\(XSS\).md), [5](https://uwconnect.uw.edu/it?id=kb_article_view&sysparm_article=KB0036739)]

2. XSS Armazenado (Stored / Persistent XSS) [[1](https://xss.js.org/)]

Este é o tipo mais perigoso. O script injetado é salvo permanentemente no servidor da aplicação (como em um banco de dados, fórum, campo de comentários ou perfil de usuário). [[1](https://platform.qa.com/lab/execute-stored-cross-site-scripting-xss-attack/), [2](https://www.pingidentity.com/en/resources/cybersecurity-fundamentals/threats/cross-site-scripting.html), [3](https://attaxion.com/glossary/cwe-79-cross-site-scripting/), [4](https://zerothreat.ai/blog/complete-guide-to-cross-site-scripting), [5](https://kemptechnologies.com/blog/owasp-top-ten-series-cross-site-scripting)]

- **Como testar:** Encontre campos onde os dados inseridos são guardados e exibidos posteriormente para outros usuários (ex: seção de comentários, foto de perfil, cadastro de endereço). [[1](https://verpex.com/blog/cross-site-scripting-xss-prevention-a-detailed-web-security-checklist), [2](https://medium.com/meetcyber/xss-explained-types-examples-and-how-to-prevent-it-9e2dce97f42f), [3](https://medium.com/@zycc2727/ssrf-cross-site-scripting-a54422d0753e)]
- **Exemplo:** Digitar `<script>alert('hackeado')</script>` na caixa de comentários de um blog. [[1](https://abhishekml.medium.com/unmasking-xss-understanding-cross-site-scripting-attacks-fc8be6f8f289), [2](https://www.astrill.com/blog/cross-site-scripting/)]
- **Cenário de ataque:** Sempre que qualquer usuário visitar aquela página de comentários, o script será executado automaticamente no navegador dele. [[1](https://www.20i.com/blog/cross-site-scripting-how-to-protect-your-website/), [2](https://cyberpeace.org/resources/blogs/cross-site-scripting-xss-the-silent-threat-in-everyday-browsing)]

3. XSS Baseado em DOM (DOM-based XSS) [[1](https://github.com/resources/articles/what-is-cross-site-scripting), [2](https://www.fortinet.com/resources/cyberglossary/cross-site-scripting)]

A vulnerabilidade não envolve o servidor. O código malicioso é executado inteiramente no lado do cliente (Client-Side), manipulando a estrutura da página (DOM - Document Object Model) através de scripts legítimos que processam dados de forma insegura. [[1](https://www.theknowledgeacademy.com/blog/what-is-cross-site-scripting-xss/), [2](https://www.invicti.com/learn/dom-based-cross-site-scripting-dom-xss), [3](https://jumpcloud.com/it-index/what-is-cross-site-scripting-xss), [4](https://grsee.com/resources/pentesting/cross-site-scripting-xss-what-it-is-and-how-to-prevent-it/)]

- **Como testar:** Analise o código JavaScript da página procurando por "Fontes" (onde o script lê dados, como `location.search` ou `document.referrer`) que são passadas para "Sumidouros" (funções que renderizam conteúdo, como `element.innerHTML`, `document.write` ou `eval()`). [[1](https://medium.com/@anandrishav2228/dom-based-cross-site-scripting-xss-828c223a80f3), [2](https://www.uprootsecurity.com/blog/dom-xss-explained-examples-testing-payloads), [3](https://grafana.com/blog/trusted-types-how-we-mitigate-xss-threats-in-grafana-10/), [4](https://teampassword.com/blog/cross-site-scripting-xss-what-it-is-and-how-to-defend-against-it)]

## Command Injection
### Detecção de Command Injection: Guia de Análise para Analistas SOC e Logs

Este documento resume as metodologias de identificação de vulnerabilidades e ataques de injeção de comandos com foco na atuação em Centros de Operações de Segurança (SOC) e análise de telemetria[cite: 1].

---

## 1. Mapeamento de Pontos de Entrada e Injeção
Para antecipar e correlacionar os alertas, o analista deve monitorar parâmetros e campos de entrada que a aplicação web utiliza para construir comandos diretamente no sistema operacional do servidor[cite: 1]. Exemplos críticos incluem:
* Mecanismos de upload de arquivos.
* Utilitários integrados de rede (ex: ferramentas de diagnóstico de ping).
* Conversores e geradores automatizados de relatórios em formato PDF.

---

## 2. Indicadores de Ataque com Metacaracteres em Logs Web
Durante a análise de requisições HTTP (cabeçalhos, URIs e corpos de requisição POST), deve-se inspecionar o uso de operadores de shell injetados para concatenar ou desviar a execução original da aplicação[cite: 1]. Os padrões mais comuns incluem:

* **Ponto e Vírgula (`;`):** Utilizado para separar e sequenciar comandos distintos na mesma linha.
* **Pipe (`|`):** Encaminha a saída gerada pelo primeiro comando como entrada do segundo.
* **Operadores E/OU comercial (`&&` ou `||`):** Condicionam a execução de um segundo comando ao sucesso ou falha do primeiro.
* **Crase (`` ` ``) ou `$()`:** Operadores utilizados para substituição de comandos.

> **Exemplo em Log:** Uma requisição contendo parâmetros como `filename.txt; whoami` reflete uma tentativa direta de executar comandos adicionais de forma sequencial.

---

## 3. Investigação de Injeção de Comandos Cega (Blind Command Injection)
Em cenários de ataques "cegos", onde a aplicação não renderiza o resultado do comando injetado na resposta HTTP do usuário, a detecção no SOC deve rastrear sinais indiretos de execução:

### A. Atrasos Baseados em Tempo (Time Delays)
* **Comportamento:** O atacante injeta payloads de temporização como `sleep 5` ou `ping -c 5 127.0.0.1`.
* **Análise no SOC:** Monitoramento do campo `time_taken` (tempo de resposta) nos logs do servidor web (Nginx, Apache, IIS). Desvios exatos correspondentes ao valor do payload (ex: atrasos sistemáticos de 5 segundos) indicam uma exploração bem-sucedida.

### B. Interações Fora da Banda (Out-of-Band - OAST)
* **Comportamento:** O invasor força o servidor a interagir de forma externa com uma infraestrutura sob o seu próprio domínio (ex: `nslookup dominio-do-atacante.com`).
* **Análise no SOC:** Correlação cruzada com os logs de servidores DNS internos ou logs do Firewall de Borda. A ocorrência de requisições externas originadas de servidores de aplicação para domínios anômalos valida o comprometimento.

---

## 4. Assinaturas e Padrões de Terminal a Monitorar
Um pilar crítico para a detecção rápida no SOC é a busca proativa de assinaturas associadas a linguagens específicas de terminais do Linux ou Windows nos payloads recebidos:
* **Comandos de enumeração e navegação:** `dir`, `ls`, `cat`, `type`[cite: 1].
* **Manipulação de arquivos:** `cp`[cite: 1].
* **Shells Reversos:** Padrões com comandos que estabelecem conexões de volta ao atacante de modo a facilitar o controle persistente pós-exploração[cite: 1].

---

## 5. Ferramentas de Automação e Referências de Validação
Para o monitoramento de auditoria e varredura preventiva contínua contra esse tipo de ataque, recomenda-se:
* **Scanners Automatizados:** Emprego de ferramentas como Burp Suite Professional ou OWASP ZAP para simulação exaustiva de casos de teste.
* **Metodologias de Teste Manual:** Consulta ao guia *OWASP Web Security Testing Guide (WSTG)* para análise aprofundada de evasão de filtros.
* **Padrões de Log:** Estudo das assinaturas de ataque em logs de servidores através do portal de inteligência *LetsDefend Blog*.
---

## IDOR - Insecure Direct Object Reference
# Detecção de Insegurança no Objeto de Referência Direta (IDOR): Guia para SOC e Análise de Logs

Este documento resume as metodologias de identificação e detecção de vulnerabilidades e ataques IDOR, com foco no monitoramento de telemetria em Centros de Operações de Segurança (SOC).

---

## 1. O Desafio da Detecção de IDOR
A detecção de ataques IDOR (Insecure Direct Object Reference) apresenta uma complexidade superior se comparada a outras ameaças web. Isso ocorre porque o vetor de ataque não se baseia em assinaturas de payloads conhecidos ou maliciosos, como ocorre em injeções de SQL (SQLi) ou Cross-Site Scripting (XSS). Ademais, a identificação é dificultada pelo fato de que o corpo das respostas HTTP — fundamentais para confirmar se o acesso inadequado foi bem-sucedido — raramente é registrado nos logs por motivos operacionais e de privacidade.

---

## 2. Métodos de Detecção e Análise em Tráfego/Logs do SOC

### A. Análise de Parâmetros e Mapeamento de Padrões Sequenciais
* **Comportamento:** O IDOR pode se manifestar em qualquer parâmetro da requisição. Os atacantes costumam planejar ataques de força bruta visando alcançar múltiplos objetos de forma previsível e sucessiva (valores inteiros sequenciais).
* **Análise no SOC:** Investigação proativa de requisições que apresentem um padrão numérico incremental consecutivo no mesmo parâmetro de ID (ex: `id=1`, `id=2`, `id=3`).

### B. Volumetria e Origem de Requisições
* **Comportamento:** Para exfiltrar dados em massa após descobrir uma falha IDOR, o invasor dispara automações direcionadas para uma única página.
* **Análise no SOC:** Monitoramento do volume de requisições destinadas à mesma página ou endpoint a partir de uma única origem (mesmo endereço IP ou mesma sessão de usuário). Um pico anormal é um forte indicador de força bruta.

### C. Monitoramento da Variabilidade no Tamanho das Respostas (Response Size)
* **Comportamento:** Enquanto o atacante altera sequencialmente os IDs das requisições automatizadas, o servidor retorna os dados de diferentes usuários legítimos.
* **Análise no SOC:** Rastreamento do tamanho dos dados retornados pelo servidor (`bytes_sent` ou `content-length` nos logs). Se as respostas para requisições idênticas em estrutura apresentarem variações significativas de tamanho a cada ID testado, isso indica que o atacante obteve acesso bem-sucedido a informações de terceiros com dimensões únicas.

---

## 3. Validação Proativa e Testes baseados em Matrizes de Acesso

### A. Troca de Papéis e Testes com Proxies
Profissionais de segurança validam o comportamento da aplicação capturando uma requisição legítima do Usuário A e alterando o parâmetro do ID do objeto para o correspondente ao Usuário B. Em seguida, os tokens de autorização são substituídos para verificar se o servidor processará indevidamente a solicitação sem validar a propriedade do objeto.

### B. Extensões de Auditoria Automatizada
* **Autorize (Burp Suite):** Ferramenta utilizada para automatizar e agilizar a verificação de permissões e controle de acesso baseado em funções em múltiplos endpoints.

---

## 4. Ferramentas de Automação e Referências Avançadas
* **DAST Baseado em IA/Automatizado:** Scanners modernos e soluções dinâmicas (como o Aptori) alternam sistematicamente entre tokens de sessão e IDs de objetos para evidenciar falhas de autorização de forma programática.
* **OWASP Testing Guide:** Metodologias completas para localização manual de vulnerabilidades de controle de acesso.
* **Guia Sycope:** Estratégias detalhadas de detecção com foco na análise forense de tráfego HTTP.
* **MDN Web Docs:** Conceitos de remediação estrutural focados no aumento da complexidade de identificadores e mecanismos rígidos de controle de acesso.

## # Detecção de Open Redirect (Redirecionamento Aberto): Guia de Análise para Analistas SOC e Logs

Este documento resume as metodologias de identificação, análise de telemetria e engenharia de detecção para mitigar e responder a ataques de Redirecionamento Aberto (Open Redirect).

---

## 1. O Mecanismo do Ataque e Impacto no SOC
O Open Redirect ocorre quando uma aplicação web aceita uma entrada controlada pelo usuário que especifica uma URL para a qual o sistema redirecionará o navegador, sem a devida validação. 
* **Impacto:** Embora frequentemente classificada como de severidade média ou baixa isoladamente, essa vulnerabilidade é um pilar fundamental para campanhas sofisticadas de **Phishing** e engenharia social, pois permite que um atacante utilize a reputação do domínio legítimo da empresa para mascarar o destino final malicioso.

---

## 2. Mapeamento de Parâmetros de Entrada Sensíveis
A investigação deve iniciar pelo inventário e monitoramento de parâmetros de strings de consulta (*query strings*) que comumente gerenciam fluxos de navegação, autenticação posterior ou retornos de checkout. Exemplos críticos incluem:
* `?next=`
* `?url=`
* `?redirect_url=`
* `?returnTo=`
* `?continue=`
* `?goto=`
* `?checkout_url=`

---

## 3. Técnicas de Evasão (Bypass) e Ofuscação em Logs
Para passar despercebidos por Web Application Firewalls (WAFs) e analistas de SOC, os atacantes não utilizam apenas URLs estruturadas comuns (como `http://attacker.com`). Eles empregam técnicas de bypass para enganar os validadores da aplicação:

* **Manipulação de Barras e Caracteres Especiais:** Uso de barras triplas (`///evil.com`), contra-barras ou o caractere de autenticação básica `@` (`sitelegitimo.com@evil.com`).
* **Codificação de Caracteres (URL Encoding):** Substituição de caracteres críticos por seus equivalentes hexadecimais (ex: `%2f` no lugar de `/`).
* **Bypass de Localhost / IPs:** Utilização de notações alternativas para referenciar loops locais ou fugir de regexes simples:
  * Notação IPv6 abreviada: `http://[::]:25/`
  * Caracteres Unicode equivalentes: `http://①②⑦.⓪.⓪.⓪`
  * Notação CIDR incorreta ou truncada: `http://127.0.0.0`
  * Ignorar pontos por conversão Decimal: `http://2130706433/` (equivalente a `127.0.0.1`)
  * Conversão Hexadecimal: `http://0x7f000001/`

---

## 4. Engenharia de Detecção e Análise de Logs (SIEM/SOC)

### A. Detecção Baseada em Expressões Regulares (Regex)
Para realizar buscas proativas (*threat hunting*) ou criar regras de correlação no SIEM baseadas em logs de servidores web (como Nginx, Apache ou IIS) que registram requisições HTTP GET, pode ser utilizada a seguinte expressão regular baseada no padrão de assinaturas comuns:

```regex
/^.*"GET.*\?.*=(https%3a%2f%2f[a-z0-9-]+%2e[a-z]{2,}).+?.*HTTP\/.*".*$/gm
```




## Detecção de Directory Traversal (Travessia de Diretório): Guia de Análise para Analistas SOC e Logs

Este documento resume as metodologias de identificação, análise de telemetria e engenharia de detecção para mitigar e responder a ataques de Travessia de Diretório (Directory Traversal).

---

## 1. O Mecanismo do Ataque e Alvos Críticos
O Directory Traversal consiste na exploração de falhas de validação de entrada para ler arquivos arbitrários hospedados no servidor de aplicação. O sucesso do exploit depende do acesso a arquivos confidenciais do sistema operacional. Os analistas de SOC devem priorizar alertas que envolvam requisições aos seguintes caminhos populares:

### Alvos em Sistemas Linux
* `/etc/issue`
* `/etc/passwd`
* `/etc/shadow`
* `/etc/group`
* `/etc/hosts`

### Alvos em Sistemas Windows
* `c:/boot.ini`
* `c:/inetpub/logs/logfiles`
* `c:/inetpub/wwwroot/global.asa`
* `c:/inetpub/wwwroot/index.asp`
* `c:/inetpub/wwwroot/web.config`
* `c:/sysprep.inf`

---

## 2. Indicadores de Ataque (Payloads) e Evasão
Os valores-chave que caracterizam esse tipo de ataque baseiam-se na sequência de retrocesso de diretório `../` (dot-dot-slash) ou `..\`. No entanto, para evadir Web Application Firewalls (WAFs), os atacantes utilizam variações de codificação:
* **Codificação Simples:** `%2e%2e%2f`
* **Codificação Dupla:** `%252e%252e%252f`
* **Codificação Unicode:** Uso de caracteres estendidos/Unicode para contornar filtros de strings do WAF antes que a requisição chegue ao interpretador do servidor.

---

## 3. Engenharia de Detecção e Análise de Logs (SIEM/SOC)

### A. Detecção Baseada em Expressões Regulares (Regex)
Para realizar varreduras ou criar regras de correlação em logs de acesso de servidores web (como o Nginx ou Apache), os analistas podem utilizar assinaturas específicas para os payloads descritos.

* **Assinatura Genérica para Travessia Simples (Nginx access.log):**
```regex
/^.*"GET.*\?.*=(%2e%2e%2f).+?.*HTTP\/.*".*$/gm
```














```ccard
type: folder_brief_live
```





 
%% Begin Waypoint %%
- **[[Detecting Web Attacks]]**
	- [[Detecting Web Attacks]]
	- [[OWASP Simple]]
	- [[Web Application  Working]]

%% End Waypoint %%
