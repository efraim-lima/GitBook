[[CyberSecurity/fatec/Pesquisa/TCC/README|README]]
[[CyberSecurity/fatec/Pesquisa/TCC/__init__|__init__]]
[[__init__]]

```Waypoint

```

Para este arquivo foi utilizado como referencia o nosso [[notas/16.0/Backup/TCC/TCC|TCC]], para consulta basta acessar o link no final deste manterial.



Para uma apresentação nota 10, lembre-se: o slide é um **recurso visual** para a plateia, não uma "cola" para você. Use fontes sem serifa (Arial, Calibri) com tamanho **24 a 32 para textos** e **mínimo 18 para gráficos**.

--------------------------------------------------------------------------------

[[Roteiro]] Estruturado para Apresentação de [[notas/16.0/Backup/TCC/TCC|TCC]]

Slide 1: Capa e Identificação (30s a 1min)

- **Tópicos:** Título do [[CyberSecurity/fatec/Pesquisa/Trabalho/Trabalho|Trabalho]]; Nomes dos autores; Orientador; Instituição.
- **Texto Curto:** "Recomendações de [[Segurança]] para o uso do MCP AI integrado à plataforma de orquestração de containers."
- **Sugestão de Imagem:** Logotipos oficiais ([[CyberSecurity/information-security/fatec/fatec|fatec]], CPS, Governo de SP) dispostos de forma equilibrada.
- **Descrição:** Este slide estabelece o tom formal. Ao falar, agradeça à banca pelo tempo e à instituição pelo suporte. **Dica:** Não leia o slide, apenas se apresente e anuncie o tema com firmeza.

Slide 2: Contexto e Problema de [[CyberSecurity/fatec/Pesquisa/Pesquisa|Pesquisa]] (1 a 2 min)

- **Tópicos:** Ascensão dos Agentes de IA e do protocolo MCP; Lacuna de [[Segurança]] em servidores comunitários; Riscos de execução de instruções nocivas.
- **Texto Curto:** "Como reduzir riscos de acesso não autorizado e execução de [[comandos]] nocivos em servidores MCP?".
- **Sugestão de Imagem:** Tabela 1 do [[CyberSecurity/fatec/Pesquisa/Trabalho/Trabalho|Trabalho]] listando CVEs críticas (como a CVE-[[2025]]-65720) para ilustrar a gravidade real.
- **Descrição:** Contextualize que o MCP é o "USB-C para IA", mas que a falta de autenticação forte permite ataques de RCE e Injeção de Interface.

Slide 3: Objetivos e Hipótese (1 min)

- **Tópicos:** Objetivo Geral; Objetivos Específicos; Hipótese de Redução de Risco.
- **Texto Curto:** "A defesa em camadas reduz de forma relevante a superfície de ataque observável em uma implementação MCP".
- **Sugestão de Imagem:** Ícones que representem [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] pilares da [[Segurança]] (Escudo para Hardening, Lupa para Auditoria, Robô para Guardrail).
- **Descrição:** Segundo as fontes, você pode ler [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] objetivos integralmente, pois a escolha das palavras aqui é técnica e rigorosa.

Slide 4: Metodologia Experimental (1 a 2 min)

- **Tópicos:** Abordagem qualitativa e aplicada; Divisão em três grupos: **Baseline (A)**, **Hardening (B)** e **Guardrail (C)**.
- **Texto Curto:** "Experimentação controlada via framework STRIDE para mapeamento de ameaças".
- **Sugestão de Imagem:** O "Diagrama da implementação das soluções propostas" (Figura 2), que mostra visualmente o fluxo do usuário até o cluster K8s.
- **Descrição:** Explique que o laboratório foi montado em Ubuntu Server com Docker para garantir a reprodutibilidade dos testes.

Slide 5: Implementação: Camada de Hardening (2 min)

- **Tópicos:** Proxy Reverso (Nginx); Identidade Centralizada (Keycloak); Isolamento de rede via Docker Compose.
- **Texto Curto:** "Transição de um estado vulnerável para uma arquitetura Zero Trust".
- **Sugestão de Imagem:** Prints das Figuras 3 e 15: Configuração de RBAC no Keycloak e a restrição de [[portas]] após o hardening.
- **Descrição:** Destaque que a remoção do mapeamento direto de [[portas]] (porta 8501) impediu que atacantes ignorassem a camada de login.

Slide 6: Implementação: Camada de Guardrail Gateway (2 min)

- **Tópicos:** Interceptação semântica; LLM Local (Qwen 2.5); Classificação de Intenções (SAFE, RISKY, UNSAFE).
- **Texto Curto:** "Controle de Acesso Baseado em Risco: Human-in-the-loop para ações críticas".
- **Sugestão de Imagem:** Figura 7, mostrando o pop-up de solicitação de senha administrativa para prompts categorizados como RISKY.
- **Descrição:** Explique que a LLM local garante privacidade e baixa latência, detectando tentativas sofisticadas de _Prompt Injection_.

Slide 7: Resultados: Eficácia do Guardrail (4 min - O coração do [[notas/16.0/Backup/TCC/TCC|TCC]])

- **Tópicos:** Levantamento estatístico; 391 frases testadas; Eficácia de bloqueio global de 95,65%.
- **Texto Curto:** "O sistema neutralizou com sucesso a maioria dos prompts que fugiam à política de [[Segurança]]".
- **Sugestão de Imagem:** Tabela 5 ("Eficácia de bloqueio"), destacando [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] altos percentuais de sucesso para categorias críticas.
- **Descrição:** Use este slide para demonstrar domínio. Explique que mesmo desvios semânticos resultaram em bloqueio, garantindo a integridade do cluster.

Slide 8: Resultados: Impacto na [[Segurança]] (CVSS) (2 min)

- **Tópicos:** Comparação de Score de Risco; Redução média de 89%; Eliminação de tráfego em texto claro.
- **Texto Curto:** "Score de vulnerabilidade reduzido de 8.1 (Elevado) para 0.9 (Mínimo)".
- **Sugestão de Imagem:** Um gráfico de barras comparativo baseado na Tabela 6, mostrando a queda drástica do risco em cada categoria.
- **Descrição:** Enfatize que a aplicação de TLS 1.3 e auditoria estruturada mitigou falhas que permitiam ataques de _Man-in-the-Middle_.

Slide 9: Conclusões e Guia de Boas Práticas (1 a 2 min)

- **Tópicos:** Confirmação da hipótese; Checklist de implementação segura; Limitações e Trabalhos [[futuros]].
- **Texto Curto:** "A [[Segurança]] em agentes de IA depende da validação explícita de entrada e contexto em múltiplas camadas".
- **Sugestão de Imagem:** Uma lista visual estilizada com [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] "Princípios Norteadores" (Menor privilégio, Zero Trust, Auditoria).
- **Descrição:** Mencione que o [[CyberSecurity/fatec/Pesquisa/Trabalho/Trabalho|Trabalho]] preenche uma lacuna acadêmica em língua portuguesa e sugira a integração de GPUs em trabalhos [[futuros]] para melhorar a latência da LLM.

Slide 10: Encerramento e Agradecimentos (30s)

- **Tópicos:** "Obrigado pela atenção!"; Contatos.
- **Texto Curto:** "Dúvidas ou considerações?"
- **Sugestão de Imagem:** Foto da equipe ou um fundo limpo com [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] contatos.
- **Descrição:** Coloque-se à disposição para a arguição. Demonstre satisfação e sentimento de dever cumprido.


![[Recomendações de [[Segurança]] para o uso do MCP AI integrado à plataforma de orquestração de containers.docx.pdf]]