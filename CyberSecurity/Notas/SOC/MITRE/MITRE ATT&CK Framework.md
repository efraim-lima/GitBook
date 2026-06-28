---
Created: 2026-01-18T21:10
Criado em: 2026-01-18T21:10
Criado em 1: 2026-01-18T21:10
Criado por: 2026-01-18T21:10
---
# \#️⃣ Matrizes do MITRE ATT&CK
A Matriz do MITRE é uma forma de visualização que classifica e facilita a forma de identificar cyber ataques.
A Matris comumente dividida entre 3 tipos:
- Enterprise
- Mobile
- ICS (Industrial Control Systems)
  
### 🏦 Enterprise
Possui a maioria dos sistemas digitais inclusos e mais comuns do que as outras matrizes. Usado para compreender ataques em grandes organizações.
  
Focado nas seguintes diretrizes (sub-matrizes):
- PRE
- Windows
- macOS
- Linux
- Cloud
- Network
- Containers

> [!info] Matrix - Enterprise | MITRE ATT&CK®  
> Below are the tactics and techniques representing the MITRE ATT&CK® Matrix for Enterprise.  
> [https://attack.mitre.org/matrices/enterprise/](https://attack.mitre.org/matrices/enterprise/)  
  
### 📱 Mobile
Na parte de Mobile tempos os principais TTPs referentes aos sistemas Android e IOS

> [!info] Matrix - Mobile | MITRE ATT&CK®  
> Below are the tactics and techniques representing the MITRE ATT&CK® Matrix for Mobile.  
> [https://attack.mitre.org/matrices/mobile/](https://attack.mitre.org/matrices/mobile/)  
  
### 🏭 ICS (Industrial Control Systems)
Nesta parte o foco é em sistemas de controle industrial, sendo a parte

> [!info] Matrix - ICS | MITRE ATT&CK®  
> Below are the tactics and techniques representing the MITRE ATT&CK® Matrix for ICS.  
> [https://attack.mitre.org/matrices/ics/](https://attack.mitre.org/matrices/ics/)  
  
## \#️⃣ Matrizes
### 🗒️ Taticas
Correspondente aos Indices das colunas, as taticas sção uma das principais partes atreladas ao MITRE, sendo a forma como descobrimos o comportamento dos grupos de cyber ataque.
![[image 33.png|image 33.png]]
  
Referente às taticas temos diferenciação delas entre os tipos de matrizes, no caso temos os seguintes comportamentos (taticas) para as devidas matrizes.
|   |   |   |
|---|---|---|
|==[Enterprise](https://attack.mitre.org/tactics/enterprise/)==|==[Mobile](https://attack.mitre.org/tactics/mobile/)==|==[ICS](https://attack.mitre.org/tactics/ics/)==|
|Reconhecimento  <br>Desenvolvimento de Recursos  <br>Acesso Inicial  <br>Execução  <br>Persistência  <br>Escalonamento de Privilégios  <br>Evasão de Defesa  <br>Acesso a Credenciais  <br>Descoberta  <br>Movimentação Lateral  <br>Coleta  <br>Comando e Controle  <br>Exfiltração  <br>Impacto|Acesso Inicial  <br>Execução  <br>Persistência  <br>Escalonamento de Privilégios  <br>Evasão de Defesa  <br>Acesso a Credenciais  <br>Descoberta  <br>Movimentação Lateral  <br>Coleta  <br>Comando e Controle  <br>Exfiltração  <br>Impacto  <br>Efeitos de Rede  <br>Efeitos de Serviço Remoto|Acesso Inicial  <br>Execução  <br>Persistência  <br>Escalonamento de Privilégios  <br>Evasão  <br>Descoberta  <br>Movimentação Lateral  <br>Coleta  <br>Comando e Controle  <br>Inibir Função de Resposta  <br>Prejudicar o Controle do Processo  <br>Impacto|
Além dessas informações acho interessante mencionar que o MITTRE ATT&CK disponibiliza informações pertinentes não apenas aos TTPs, mas também a toda uma cadeia relacionada a detecção, analise e mitigação de eventos cibernéticos, passando pelo processo de mitigação de ameças, identificação de grupos de cyber criminosos de acordo com seu comportamento (técnicas e softwares utilizados).  
  
Pontos importantes para analise posteriormente:  
O que revela a motivação de um ataque são suas táticas  
O conceito que explica como o atacante performa suas ações são as técnicas  
O que expressa os métodos utilizados são os procedimentos  
## Divisão dos IDs
## 1. Táticas (Tactics)
As táticas representam o **"porquê"** de um ataque (o objetivo tático).
- **Formato:** `TA` seguido de 4 dígitos.
- **Exemplo: TA0001** (Initial Access).
- **Lógica:** Elas são as categorias de alto nível (as colunas da matriz) que cobrem todo o ciclo de vida do ataque, desde o acesso inicial até a exfiltração ou impacto.
## 2. Técnicas (Techniques)
As técnicas representam **"como"** um adversário atinge um objetivo tático.
- **Formato:** `T` seguido de 4 dígitos.
- **Exemplo: T1059** (Command and Scripting Interpreter).
- **Lógica:** É a ação técnica específica. Uma mesma técnica pode aparecer em várias táticas diferentes.
## 3. Subtécnicas (Sub-techniques)
Introduzidas para dar mais granularidade sem poluir a matriz principal, elas detalham **variações específicas** de uma técnica.
- **Formato:** ID da Técnica + `.` + 3 dígitos.
- **Exemplo: T1059.001** (PowerShell).
- **Lógica:** O ponto final separa a técnica "mãe" da sua variação. No exemplo, a técnica é "Intérprete de Comandos" e a subtécnica especifica que o uso foi via PowerShell.
## 4. Grupos (Groups)
Identificam atores de ameaças ou clusters de atividades (APT, grupos cibercriminosos).
- **Formato:** `G` seguido de 4 dígitos.
- **Exemplo: G0007** (APT28).
- **Lógica:** Reúne as técnicas e softwares que um grupo específico costuma utilizar historicamente.
## 5. Software
Identifica ferramentas, malwares ou utilitários usados por adversários.
- **Formato:** `S` seguido de 4 dígitos.
- **Exemplo: S0154** (Cobalt Strike).
- **Lógica:** Diferencia ferramentas legítimas usadas para fins maliciosos (como o PsExec) de malwares proprietários.
  
|   |   |   |   |
|---|---|---|---|
|||||
|||||
|||||
|||||
|||||
|||||