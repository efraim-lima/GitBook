---
description: Primeiro laboratório da trilha SOC Tier 1
---

# Analista de Segurança Jr

Aqui temos a introdução aos desafios de um analista de segurança junior e o primeiro laboratóro que consiste basicamente no processo de analisar um IP encontrado como um IOC, ou seja, um Indicador de Comprometimento.

Para isso vamos detectar o evento que está presente nos logs coletados na ferramenta agregadora de logs.

O log a ser considerado é o de acesso não autorizado, que está marcado em vermelho no print abaixo

<figure><img src="../../../../../../.gitbook/assets/image (3).png" alt=""><figcaption><p>Reprodução da máquinada no laboratório da Try Hack Me</p></figcaption></figure>

Ao analisar o log de acesso não autorizado veremos que temos um número de IPv4, dado relevante que pode nos indicar a origem deste evento, nos ajudando a determiar se este evento é um evento legítmo. Ao selecionar o log seremo redirecionados para um website onde poderemos verificar se este IP ja foi detectado em outros eventos de segurança no passado...existem alguns sites na vida real que realmente proporcionam este tipo de análise e isso pode ser extremamente útil para diversos incidentes.

Sites para busca e análise de IPs com intuito de se detectar se foram identificados como IPs relacionados a atividades suspeitas:

* AbuseIPDB - [https://www.abuseipdb.com](https://www.abuseipdb.com)
* Talos Inteligence - [https://www.talosintelligence.com](https://www.talosintelligence.com)

Após inserirmos o IP detectaremos este como um endereço malicioso...

<figure><img src="../../../../../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Depois disso basta escalar o incidente para uma pessoa responsável pelas atividades que tenha maior autonomia para a investigação, neste caso seria nosso Team Leader, Will Griffin.

<figure><img src="../../../../../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

E com isso ganharemos permissão para bloquear tal IP em nosso firewall internamente, o IP é o coletado acima, ou seja, 221.181.185.159, com isso devemos receber o alerta THM{UNTIL-WE-MEET-AGAIN}

<figure><img src="../../../../../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
