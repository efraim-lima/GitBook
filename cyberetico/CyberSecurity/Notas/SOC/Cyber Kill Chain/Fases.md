---
Created: 2026-01-20T23:15
Criado em: 2026-01-20T23:15
Criado em 1: 2026-01-20T23:15
Criado por: 2026-01-20T23:15
---
# 🔍 Reconhecimento
O processo de reconhecimento, por parte do atacante, consiste em coletar informações provenientes do alvo…essa coleta pode ser passiva ou ativa.
## 1️⃣ Reconhecimento Passivo
Processo de coletar informações sem contato direto com o sistema alvo. O atacante basicamente procura por informações presentes em redes sociais, emails, site, sistemas da empresa, etc.
## 2️⃣ Reconhecimento Ativo
Ja o reconhecimento ativo é o processo de coletar informações com contato direto com o sistema alvo. Neste ponto o atacante coleta informações interagindo com o sistema, enviando um form, enviando requisições ao servidor e observando as respostas obtidas por tais respostas.
  
🥷 Alguns tipos de infrormações que um atacante pode obter
- versão do sistema
- informações sobre fontes abertas
- endereços de email dos integrantes da organização
- informações internas ou pessoais dos colaboradores
- dispositivos conectados a internet
- vulnerabilidades em servidores abertos para internet
- fornecedores da organização
  
🛡️ Para [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] defensores existem algumas ações que podem ser adotadas
- detectar pontos que divulgam informações via [[Pentest]]
- coletar informações sobre vazamentos da organização com fontes de threat [[intel]]
- [[Evitar]] disponibilização de dados da empresa
- monitorar trafego da organização
- manter [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] sistemas atualizados para [[Evitar]] ameaças
# 🔫 Armamento
Neste momento o atacante ja coletou as informações necessárias sobre o sistema e começa a coletar [[CyberSecurity/Notas/SOC/Introdução/Ferramentas|Ferramentas]] que possam explorar as vulnerabilidades e falhas para que seu objetivo final seja alcançado.
  
🥷 neste momento o atacante deve ter a posse das [[CyberSecurity/Notas/SOC/Introdução/Ferramentas|Ferramentas]]
- criar malware
- desenvolver exploits
- criar conteudo malicioso para [[phishing]]
- identificar a melhor ferramenta para o [[CYBER]] ataque
  
🛡️ ao lado do defensor o processo de ser voltado para previnir o ataque em si
- verificar o sistema de forma regular
- buscar por vulnerabilidades expostas
- instalar atualizações de [[Segurança]]
- avaliar o ataque de ataques cibernéticos
- criar um bom playbook de resposta a incidentes
# 📦 Entrega
Etapa onde o atacante executa o plano de ataque, inicando as [[CyberSecurity/fatec/2026/1-2026/Desenvolvimento/ATIVIDADES|ATIVIDADES]] como envio de emails, [[CyberSecurity/Course/tools/malwares|malwares]], mensagens, etc.
  
🥷 O atacante envia [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] artefatos a serem deflagrados no ataque
- enviar URL maliciosa por email ou redes sociais
- enviar malware como arquivo anexado
- enviar malware através do website
- instalar um malware de forma fisica
  
🛡️ para [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] defensores resta monitorar o ambiente para [[Evitar]] que ocorra o avanço para proximas etapas
- Treinar o time para ter uma postura defensiva ao receber mensagens, emails, ligações ou [[Solicitações]]
- adotar uma postura investigativa em emails (anexos, metadados, origem/destino);
- monitorar e analisar com o objetivo de detectar anomalias e determinar as causas iniciais
# 💣 Exploração
Tendo entregado o artefato, o atacante precisa garantir que este material será executado e mantido no ambiente
  
🥷 Garantir que o artefato será executado
- executar o exploit, ransomware ou malware
  
🛡️ Processo mais difícil e complexo comparado com as outras etapas,
- Garantir que o treinamento dos funcionarios em não abrir arquivos, emails estranhos tenha sido implementado
- monitorar as operações do sistemas e detectar anomalias
- rastrear as vulnerabilidades do sistema
- acompanhar atualizaçẽos de [[Segurança]]
- organizar as autorizações dos ativos e contas
# 📩 Instalação
Rodar o malware não basta, o artefato pode ser instalado e sua persistência deve ser mantida (atualmente existem formas de malware que rodam apenas em runtime memory, mas de qualquer forma pode ser feito necessário uma rotina de execução)
  
🥷 Garantir que o artefato será mantido no sistema de forma oculta para que o atacante possa voltar posteriormente
- instalar o malware no dispositivo da vitima
- colocar um backdoor no sistema
- instalar um shell reverso
- adicionar serviço, regras de firewall ou task agendada para garantir a persistencia no sistema
  
🛡️ aqui para [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] defensores o processo resume-se a Threat Hunting, pois se o atacante chegou até esta etapa ele não pode mais ser detectado
- Monitorar a rede em todos ativos
- utilizar EDR para certificar alterações em configurações
- Restringir acessos a arquivos críticos
- Monitorar acesso
- Acesso admin apenas para uso exclusivo e pontual
- Monitorar processos e [[CyberSecurity/fatec/2026/1-2026/Desenvolvimento/ATIVIDADES|ATIVIDADES]] em busca de detecção de ação suspeita
- Validar executaveis e permitir a execução apenas dos que tiverem assinatura valida
- Procurar por anomalias em todas [[CyberSecurity/fatec/2026/1-2026/Desenvolvimento/ATIVIDADES|ATIVIDADES]] monitoradas do sistema em busca da causa raiz
# 🎮 Comando e Controle C2
Particularmente minha etapa preferida, sendo o momento onde o atacante completou boa parte das [[CyberSecurity/fatec/2026/1-2026/Desenvolvimento/ATIVIDADES|ATIVIDADES]] cruciais e pode implementar seu servidor de comando e controle, onde poderá ter controle remoto do sistema
  
🥷 O atacante precisa apenas criar a ponte entre o sistema vitima e seu ambiente remoto, não precisa tomar ações específicas.
- configurar e implementar ações necessárias para estabelecer controle do sistema
  
🛡️ O time de defesa precisa apenas garantir que as boas praticas das [[CyberSecurity/fatec/2026/1-2026/Desenvolvimento/ATIVIDADES|ATIVIDADES]] reconhecem e previnem trafego de C2 na rede
- bloquear IPs de servidores C2 ja conhecidos (CTI, FIrewalls, etc)
- detectar trafego de rede que possam ser servidores C2
# 🎯 Ações e Objetivos
Esta é, de fato, a ação do atacante que mais ele deseja atingir e que mais planejou fazer.
  
🥷 As ações do atacante podem mudar de acordo com [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] seus reais objetivos
- encriptar dados do sistema via ransomware
- exfiltrar informações sensíveis
- gerar danos devido a exclusão de arquivos
- escalar privilegios para aumentar o ambito do ataque
- coletar credenciais de usuários para acessar outros recursos do sistema
- alterar ou manipular inforações no sistema
  
🛡️ Como outras etapas anteriores aqui dependemos de uma boa monitoria do sistema.
- detectar anomalias no trafego de rede
- detectar acessos via rede de fontes externas
- restringir acesso à rede para fontes externas
- restringir acesso a arquivos e diretórios criticos
- usar produtos de DLP (Data Loss Prevention) para previnir o vazamento
- Detectar acesso não autorizado pela parte dos usuários