---
description: >-
  Laboratórios e atividades propostas pelo curso Analista de Segurança da
  Informação Junior
---

# Pyramid Of Pain

Atividades Pyramid of Pain

1. Hashing:&#x20;

Primeiro precisamos abrir o arquivo indicado no prório site, que é um relatório do hash do arquivo proveniente do site VirusTotal;

Coletar o nome do arquivo, sendo este:

* Sales\_Receipt 5606.xls

2. IP Addresses:

teremos que acessar um relatório do AnyRun para analisar algumas informações presentes neste relatório e coletar informações como o primeiro IP e o primeiro domínio que o arquivo tentou acessar

* IP: 50.87.136.52:443
* Dominio: craftingalegacy.com

3. Domain names

Ao acessar o relatório do any.run vamos detectar o primeiro domínio suspeito, o termo referente ao endereço usado para acessar os websites.&#x20;

Também vamos responder qual tipo de ataque usa caracteres Unicode para imitar sites legítimos

Por fim prover o site ao qual seríamos redirecionaados após acessar a url, lembrando que basta adicionar um caractere "+" ao fim da url para sabermos isso. URL: [https://tinyurl\[.\]com/bw7t8p4u](https://tinyurl.com/bw7t8p4u)

* Domínio Suspeito: craftingalegacy.com
* Termo: Domain Name
* Tipo de ataque: Punycode attack
* URL do redirect: [\
  https://tryhackme.com/](https://tryhackme.com/)

4. Host Artifacts

Aqui somos solicitados a analisar alguns pontos presentes em um relatório fornecido por um security vendor. Nele analisaremos alguns processos no sistema e precisamos capturar O IP presente em uma requisição POST executada por um arquivo regidle.exe exclusivamente na porta 8080, o nome de um executavel dropado pelo actor e, por fim analisar um report no VirusTotal e detectar quantos vendors trataram o host como malicioso.

* IP: 96.126.101.6
* Aplicação dropada: G\_jugk.exe
* vendors: 9

5. Tools

Aqui basicamente basta ler o texto apresentado e a descrição presente no site da SSDeep \[SSDeep]\([https://ssdeep-project.github.io/ssdeep/index.html](https://ssdeep-project.github.io/ssdeep/index.html)) sobre seus serviços de análise de fuzzy hash values (ou seja, faz o processo de analisar a similaridade entre arquivos distintos), com isso chegaremos às  respostas:

* Fuzzy Hashing
* context triggered piecewise hashes

6. TTPs

Neste modulo teremos que visitar o site do MITTRE ATT\&CK e coletar a quantidade de tecnicas referenciadas pelo campo Exfiltration e também fazer uma pesquisa sobre a ferramenta de acesso remoto usado pelo grupo Chimera, que é baseado na China. Vendo isso teremos as respostas:

* 9
* Cobalt Strike

7. Practical: The Pyramid of Pain

Para concluir os exames precisaremos resolver um puzzle de correlacionar as informações corretas ao campo da Pyramid Of Pain correto, com isso receberemo uma chave para preencher a flag, a chave:

* THM{PYRAMIDS\_COMPLETE}

Para quem quer compreender as respostas deste capítulo:

* The attackers plans and objectives. => TTP
* The attacker has utilised these to accomplish their objective. => Tools
* &#x20;These artefacts can present themselves as C2 traffic for example. => Network
* An attacker has purchased this and used it in a typo-squatting campaign. => Domain names
* These addresses can be used to identify the infrastructure an attacker is using for their campaign. => IP Adresses
* These signatures can be used to attribute payloads and artefacts to an actor. => Hash values
