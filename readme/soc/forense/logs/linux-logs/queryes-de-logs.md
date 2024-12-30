# Queryes de LOGs

O processo de análise de LOGs infere que precisamos reconstruir uma cadeia de eventos com o objetivo de se compreender a linha de tempo do que ocorreu e ter uma melhor visibilidade de como pode ter ocorrido um incidente, levantando cada etapa do incidente seja antes ou depois do mesmo ocorrer. Portanto é importante saber correlacionar os eventos detectados com etapas de um incidente, isso trará clareza e consciência de cada etapa e também a possiblidade de inferir qual foi a intenção da ação do atacante no ambiente.&#x20;

A partir disso é interessante correlacionar o framework Cyber Kill Chain, que descreve as etapas de um ataque cibernético e queryes especificas que podemos inputar no Linux que levantarão eventos que podem ser associados a cada etapa do incidente.&#x20;

Abaixo está uma lista detalhada dos IDs de eventos relevantes para o Windows, categorizados por cada etapa da Cyber Kill Chain.\


Queries de Análise de Logs para Análise Forense em Cada Etapa do Cyber Kill Chain

#### 1. Reconhecimento

* **Query**: Identificar tentativas de varredura de portas, com o uso de um nmap, por exemplo.
  * **Comando**: `grep "Failed password" /var/log/auth.log`
* **Query**: Detectar acessos a serviços de rede não autorizados.
  * **Comando**: `grep "connection" /var/log/syslog | grep "unauthorized"`

#### 2. Intrusão&#x20;

* **Query**: Verificar logs de acesso a arquivos críticos.
  * **Comando**: `grep "access" /var/log/audit/audit.log`
* **Query**: Identificar comandos executados por usuários não autorizados.
  * **Comando**: `cat /var/log/auth.log | grep "sudo"`
* Query: Verificar logs de e-mail indicando e-mails suspeitos com anexos.
  * **Comando**: `cat /var/log/mail.log | grep "sudo"`        >:???????????????????????

#### 3. Expansão

* **Query**: Monitorar alterações em permissões de arquivos e diretórios.
  * **Comando**: `ausearch -f /etc/passwd`
* **Query**: Analisar logs de escalonamento de privilégios.
  * **Comando**: `grep "sudo" /var/log/auth.log`
* **Query:** Analisar criação de serviços, scripts ou binários registrados em \`/var/log/syslog\` ou \`/var/log/auth.log\`. >>>>>>:::::::::::::::?????????????????????????
* **Query:** Verificar gatilhos específicos para criação de tarefas agendadas
  * **Comando**: `cat /etc/crontab | grep "sudo"`

#### 4. Coleta de Informações

* **Query**: Identificar acessos a dados sensíveis.
  * **Comando**: `grep "read" /var/log/audit/audit.log | grep "/path/to/sensitive/data"`
* **Query**: Verificar logs de exportação ou cópia de dados.
  * **Comando**: `grep "cp" /var/log/syslog`

#### 5. Comando e Controle

* **Query**: Detectar conexões com servidores externos suspeitos.
  * **Comando**: `grep "CONNECT" /var/log/syslog | grep "suspicious_IP"`
* **Query**: Analisar logs de execução de scripts ou comandos remotos.
  * **Comando**: `grep "bash" /var/log/auth.log`

#### 6. Ação

* **Query**: Identificar logs relacionados a ações maliciosas, como exclusão de arquivos.
  * **Comando**: `grep "delete" /var/log/audit/audit.log`
* **Query**: Monitorar logs de serviços críticos que foram paralisados ou reiniciados.
  * **Comando**: `grep "service stop" /var/log/syslog`

#### 7. Exfiltração

* **Query**: Verificar transferências suspeitas de dados.
  * **Comando**: `grep "scp" /var/log/auth.log`
* **Query**: Analisar logs de tráfego de rede para detectar padrões anômalos.
  * **Comando**: `tcpdump -i eth0 port not 22`

Essas queries são fundamentais para a análise forense em sistemas Linux, permitindo identificar e investigar atividades suspeitas em cada etapa do Cyber Kill Chain, contribuindo para uma resposta rápida e eficaz a incidentes de segurança.\
\
Referências:\
[https://www.trendmicro.com/vinfo/br/security/news/cybercrime-and-digital-threats/a-look-at-linux-threats-risks-and-recommendations](https://www.trendmicro.com/vinfo/br/security/news/cybercrime-and-digital-threats/a-look-at-linux-threats-risks-and-recommendations)

[https://www.lasca.ic.unicamp.br/paulo/papers/2002-Pericia-marcelo.reis-forense.tecnicas.procedimentos.pdf](https://www.lasca.ic.unicamp.br/paulo/papers/2002-Pericia-marcelo.reis-forense.tecnicas.procedimentos.pdf)

h[ttp://repositorio.ufla.br/jspui/bitstream/1/5543/1/MONOGRAFIA\_Per%C3%ADcia%20forense%20de%20rede%20teoria%20e%20pr%C3%A1tica.pdf](http://repositorio.ufla.br/jspui/bitstream/1/5543/1/MONOGRAFIA_Per%C3%ADcia%20forense%20de%20rede%20teoria%20e%20pr%C3%A1tica.pdf)

