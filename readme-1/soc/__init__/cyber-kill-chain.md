---
description: >-
  Este é um conceito trazido do ambiente militar que refere-se a uma sequência
  de processos empenhados para o sucesso de um ataque
---

# Cyber Kill Chain

Cyber Kill Chain é um processo que determina o ciclo de vida de um ataque, descrevendo como cada etapa se manifesta perante o ambiente;

Podemos desmembrar o Cyber Kill Chain em algumas etapas:\
\
<mark style="color:green;">**Recon**</mark>

Este é o estágio inicial, onde o atacante escolhe seu alvo e começa a investigar, coletar informações de forma ativa ou passiva e performar scans para coletar informações de antivírus, firewalls, sistemas operacionais e tecnologias de rede;

&#x20;

<mark style="color:green;">**Weaponize**</mark>

Neste momento o malware que deve infectar o alvo é desenvolvido, levando em consideração que deve ser extremamente leve e indetectável pelas ferramentas de antivírus do sistema

&#x20;

<mark style="color:green;">**Delivery**</mark>

Momento de entrega do Malware, onde o atacante já estudou e se preparou, agora ele precisa buscar acesso aos sistemas. A entrega pode ser feita de diversas formas, mas as mais comuns são por e-mails de phishing, onde o usuário é levado a uma página externa falsificada pelo atacante, nessa página o atacante pode optar por coletar credenciais, transmitir payloads para instalar ferramentas no sistema ou explorar vulnerabilidades do sistema para ganhar o acesso

&#x20;

<mark style="color:green;">**Exploit**</mark>

Neste momento o atacante vai explorar as vulnerabilidades do sistema de fato, geralmente ocorre quando o payload é entregue ao sistema e acionado. Neste momento o atacante pretende ganhar acesso e/ou controle do sistema atacado.

&#x20;

<mark style="color:green;">**Install**</mark>

Na instalação o estágio inicial é executado e já está rodando na máquina comprometida, mas para compreendermos melhor como a fase de instalação chega ao alvo podemos compreender melhor as metas e a natureza deste comprometimento.

* Droppers: Os droppers podem entregar o malware ao sistema alvo, esta ferramenta é uma pequena peça designada para instalar o malware no sistema e executar. Podendo ser entregue por anexos de e-mail, sites maliciosos ou táticas de engenharia social;
* Backdoors: Os backdoors são malwares desenvolvidos parar porporcionar acesso contínuo ao sistema comprometido, ele pode ser instalado no processo de exploitation ou através de um dropper sendo util para executar ataques furtivos ou roubar data do sistema comprometido;
* Rootkits: Já os rootkits são um tipo de malware que é desenvolvido para ocultar a presença do atacante no sistema comprometido e são muitas vezes utilizados no estágio de instalação para evadir a detecção por parte dos antivirus e outras ferramentas de segurança. Os rootkits também são instalados pelo atacante durante a fase de exploitation e entregues ao sistema a partir de um dropper;

&#x20;

C² (C\&C)

Neste momento o atacante já conseguiu estabelecer acesso remoto ao ambiente comprometido, onde pode ocorrer de grupos de hackers mais avançados desenvolverem ferramentas separadas para o processo de manter sua presença na rede e reduzir os riscos de erradicação de seu ataque;

&#x20;

Action

Durante a etapa de ação, o atacante irá fazer o processo de exfiltração de dados, encriptação dos dados no sistema ou seja lá qual for, de acordo com os interesses do atacante;

&#x20;

O processo de manejamento de incidentes de segurança pode ser dividido entre três etapas separadas:

* Preparação
* Detecção
* Análise

&#x20;

Poderemos verificar este processo no campo a seguir: [incident-handling.md](__init__-1/incident-handling.md "mention")
