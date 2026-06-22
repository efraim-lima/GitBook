---
Created: 2026-03-12T21:59
Criado em: 2026-03-12T21:59
Criado em 1: 2026-03-12T21:59
Criado por: 2026-03-12T21:59
---
## Temas a serem divididos e compilados
|   |   |
|---|---|
|Foco principal|[[Tarefas]] sugeridas|
|Levantamento de técnicas|Mapear ataques (prompt injection, tool poisoning, supply chain, exfiltracao de dados, etc.), relacionar a tecnicas de guardrails, sanitização, auditoria, autenticação, políticas de acesso e outras aue possam ser eficientes para mitigar ataques mais conhecidos|
|Modelagem de [[Segurança]]|Detalhar arquitetura segura de MCP (fluxos, [[tools]], papéis), desenhar estratégias de monitoramento e auditoria ([[soc/forense/logs/logs|logs]], SIEM, SOAR).|
|Indicadores de saúde|Definir indicadores e fórmula de pontuação de [[Segurança]], relacionar cada indicador às técnicas de [[Mitigação]].|
|Seleção de ataques|Buscar repositórios de prompt injection, selecionar payloads para laboratório, documentar cenários de [[Teste]].|
|Tool poisoning e cenários|Levantar técnicas de tool poisoning, fechar o conjunto de ataques (prompt injection + tool poisoning + supply chain), finalizar plano de testes.|
|Guardrails e sanitização|Implementar guardrails de input/[[output]] e sanitização, separar claramente dados x instruções, validar outputs de [[tools]].|
|Controles contra injeção|Implementar defesas específicas contra prompt injection e context poisoning (validação adicional, filtros, avaliador secundário).|
|Tool & supply chain|Implementar controles contra tool poisoning (versionamento, revisão de descrições, confirmação explícita) e medidas de supply chain em repositórios.|
|Acesso e privilégios|Implementar autenticação da interface, RBAC, políticas de acesso a servidor e interface, limitar [[tools]] e secrets disponíveis para a IA.|
|[[Pentest]] – planejamento|Planejar cenário de [[Pentest]] (escopo, técnicas, dados de [[Teste]]), preparar ambiente de testes e [[scripts]].|
|[[Pentest]] – execução|Executar ataques de prompt injection, tool poisoning, exploração de RBAC e supply chain contra o ambiente; coletar [[soc/forense/logs/logs|logs]].|
|Análise e indicadores|Consolidar resultados do [[Pentest]], calcular [[notas]] dos indicadores, escrever relatório técnico de [[Pentest]].|
|Redação [[notas/16.0/Backup/TCC/TCC|TCC]] – corpo|Escrever fundamentação teórica, arquitetura proposta, laboratório e metodologia, implementação das técnicas de [[Mitigação]].|
|Redação [[notas/16.0/Backup/TCC/TCC|TCC]] – resultados|Documentar resultados, discussão, indicadores, conclusão do [[notas/16.0/Backup/TCC/TCC|TCC]]; montar figuras/tabelas e anexos.|
|Revisão e entrega|Revisar conteúdo e normas, ajustar detalhes, preparar versão final e entregar à banca.|
Para o [[notas/16.0/Backup/TCC/TCC|TCC]], precisamos levar em conta as seguintes acoes
Pegar a arquitetura do agentK e selecionar um ataque especifico e focar nele,
- selecionar uma vulnerabilidade e blindar
    
    - politica de acesso do servidor em si ([[infraestrutura]])
        
        - descobrir uma forma de violar as politicas de acesso
        
        - virtualizacao do servidor (Mitigacao)
        
        - quantidade de recursos que o servidor tem acesso (Observar)
        
    
    - separacao do ambiente servidor MCP e agentes (nao rodar na mesma maquina)
        
        - virtualizacao do servidor (Mitigacao)
        
        - quantidade de recursos que o servidor tem acesso (Observar)
        
        - politica de acesso da aplicacao AgentK (diferente do servidor)
        
    
    - DOS no GPT (exaurir [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] tokens)
        
        - bloqueio temporario atrav’es do comportamento (ideia do Felipe)
            
            - colocar um SIEM para [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] prompts de IA
                
                - como coletar [[CyberSecurity/Course/forense/logs/logs|logs]] de prompt do MCP (nao sei como)
                
            
        
        - levantar formas de mitigar
        
    
- separar em times onde uma dupla fez o [[Pentest]] e a outra dupla valida (rodizio)
    
    - todos conseguem participar e todos conseguem validar [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] resultados
    
- precisamos conseguir dividir [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] dias para conseguir tracionar as [[CyberSecurity/fatec/2026/1-2026/Desenvolvimento/ATIVIDADES|ATIVIDADES]] (ter um norte por semana)
    
    - colocar uma meta por semana
        
        - [[Pentest]]
        
        - mitigacao do [[Pentest]]
        
        - documento
        
        - escrever pro [[notas/16.0/Backup/TCC/TCC|TCC]]
        
        - gravar o laboratorio