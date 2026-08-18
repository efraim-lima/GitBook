# Resumo dirigido das normas — DATAPREV 2026 · Perfil 5

Resumo focado em concurso (FGV) das normas ISO/NIST citadas no edital do Perfil 5.
Cada norma traz: **objetivo**, **pontos que a banca cobra** e **pegadinhas**.
Fonte da cobrança: Anexo I do edital (ver `../analise-edital.md`).

---

## Família ISO/IEC 27000 (Segurança da Informação)

### ISO/IEC 27001:2022 — Requisitos do SGSI
- **Objetivo:** especifica os **requisitos** para estabelecer, implementar, manter
  e melhorar continuamente um **Sistema de Gestão de Segurança da Informação
  (SGSI)**. É a norma **certificável** da família.
- **Cobra:** ciclo de melhoria contínua (**PDCA**); abordagem baseada em **risco**;
  contexto da organização, liderança, planejamento, apoio, operação, avaliação de
  desempenho e melhoria (estrutura de alto nível — Anexo SL); o **Anexo A** lista os
  controles (referenciados na 27002).
- **Pegadinha:** 27001 = **requisitos** (o "o quê", certificável). Não confundir com
  27002 (o "como", controles). Versão do edital: **2022** (Anexo A com 93 controles
  em 4 temas: Organizacional, Pessoas, Físico, Tecnológico).

### ISO/IEC 27002:2022 — Controles de segurança da informação
- **Objetivo:** **código de práticas** / guia de implementação dos **controles** de
  segurança da informação. **Não é certificável**.
- **Cobra:** na versão **2022**, são **93 controles** organizados em **4 temas**
  (antes eram 114 controles em 14 seções na versão 2013). Introduz 5 **atributos**
  para categorizar controles (tipo de controle, propriedades de SI, conceitos de
  cibersegurança, capacidades operacionais, domínios de segurança).
- **Pegadinha:** mudou de nome/estrutura em 2022; "Código de prática para controles
  de segurança da informação". A 27001 diz o que exigir; a 27002 detalha os controles.

### ISO/IEC 27005:2019 — Gestão de riscos de segurança da informação
- **Objetivo:** diretrizes para o **processo de gestão de riscos** de segurança da
  informação, apoiando os requisitos da 27001.
- **Cobra:** etapas do processo — **definição de contexto → identificação →
  análise → avaliação → tratamento** do risco, com **comunicação** e **monitoramento
  e análise crítica** permeando tudo. Opções de tratamento: **modificar (mitigar),
  reter (aceitar), evitar, compartilhar (transferir)** o risco.
- **Pegadinha:** 27005 é **específica de SI**; a 31000 é **genérica**. A 27005 se
  alinha à 31000.

---

## ISO 31000:2018 — Gestão de riscos (diretrizes)
- **Objetivo:** norma **genérica** de gestão de riscos, para qualquer tipo de risco
  organizacional (não só SI). Fornece **princípios, estrutura e processo**.
- **Cobra:**
  - **Princípios:** a gestão de riscos cria e protege valor; é **integrada**,
    **estruturada e abrangente**, **personalizada**, **inclusiva**, **dinâmica**,
    baseada na **melhor informação disponível**, considera **fatores humanos e
    culturais** e busca **melhoria contínua**.
  - **Processo:** escopo/contexto/critérios → **avaliação de riscos** (identificação,
    análise, avaliação) → **tratamento** → registro e relato; com **comunicação e
    consulta** + **monitoramento e análise crítica**.
- **Pegadinha:** 31000 **não é certificável** (é diretriz, "guidelines"). Não
  confundir processo (identificar/analisar/avaliar) com princípios.

---

## Continuidade de negócios

### ISO 22301:2020 — Sistema de Gestão de Continuidade de Negócios (SGCN)
- **Objetivo:** especifica **requisitos** para implantar e manter um **SGCN** —
  proteger a organização de incidentes disruptivos e permitir a retomada.
- **Cobra:** conceitos-chave —
  - **BIA (Business Impact Analysis):** identifica atividades críticas e impactos ao
    longo do tempo.
  - **RTO (Recovery Time Objective):** tempo máximo tolerável para retomar a atividade.
  - **RPO (Recovery Point Objective):** perda máxima tolerável de dados (ponto de
    recuperação).
  - **MTPD/MTDA:** período máximo tolerável de disrupção.
  - Estratégias de continuidade, planos de resposta, testes/exercícios.
- **Pegadinha:** **22301 é certificável (requisitos)**; **22313 são orientações
  (guidance) para uso da 22301** — não é certificável. Distinguir **RTO** (tempo)
  de **RPO** (dados).

### ISO 22313 — Orientações para a 22301
- **Objetivo:** guia de **implementação** do SGCN da 22301. Explica "como", sem
  criar novos requisitos.

---

## Frameworks NIST / MITRE

### NIST Cybersecurity Framework (CSF) v1.1
- **Objetivo:** framework voluntário para **gerenciar riscos de cibersegurança**.
  Composto por **Core, Tiers (níveis de implementação) e Profiles**.
- **Cobra — as 5 funções do Core (na ordem):**
  1. **Identify** (Identificar) — ativos, riscos, governança.
  2. **Protect** (Proteger) — salvaguardas, controle de acesso, treinamento.
  3. **Detect** (Detectar) — monitoração, detecção de eventos/anomalias.
  4. **Respond** (Responder) — resposta a incidentes, comunicação, mitigação.
  5. **Recover** (Recuperar) — restauração, melhorias, resiliência.
- **Pegadinha:** a versão do edital é a **v1.1** → **NÃO** inclui a função
  **"Govern"**, que só aparece na **CSF 2.0**. Se a questão listar "Govern", é
  distrator para a v1.1. Não confundir com o PDCA.

### NIST SP 800-61 — Guia de tratamento de incidentes de segurança
- **Objetivo:** guia de referência para **resposta a incidentes** de segurança
  computacional (Computer Security Incident Handling Guide).
- **Cobra — o ciclo de vida em 4 fases:**
  1. **Preparação** (Preparation) — capacitar equipe (CSIRT), ferramentas, políticas.
  2. **Detecção e Análise** (Detection & Analysis) — identificar e qualificar o incidente.
  3. **Contenção, Erradicação e Recuperação** (Containment, Eradication & Recovery) —
     isolar, remover a causa e restaurar operações.
  4. **Atividade Pós-Incidente** (Post-Incident Activity) — **lições aprendidas**.
- **Pegadinha:** "isolar a máquina" = **Contenção** (fase 3), não detecção. A fase 4
  é onde entram as lições aprendidas. Ciclo é iterativo (detecção↔contenção).

### MITRE ATT&CK (framework, não norma — cobrado no item 27)
- **Objetivo:** base de conhecimento de **táticas, técnicas e procedimentos (TTPs)**
  de adversários, baseada em observações reais.
- **Cobra:** **táticas** = o "porquê" (objetivo) do atacante, ex.: Initial Access,
  Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access,
  Discovery, **Lateral Movement**, Collection, Exfiltration, Impact. **Técnicas** = o
  "como".
- **Pegadinha:** não confundir com a **Cyber Kill Chain** (Lockheed Martin, 7 fases
  lineares). ATT&CK é matriz de táticas/técnicas, não linear.

---

## Tabela-relâmpago (revisão rápida)

| Norma/Framework | É o quê | Certificável? | Palavra-chave |
|-----------------|---------|---------------|---------------|
| ISO 27001:2022 | Requisitos do SGSI | **Sim** | "requisitos", PDCA, Anexo A |
| ISO 27002:2022 | Controles (código de prática) | Não | 93 controles, 4 temas |
| ISO 27005:2019 | Gestão de risco de **SI** | Não | processo de risco em SI |
| ISO 31000:2018 | Gestão de risco **genérica** | Não | princípios+estrutura+processo |
| ISO 22301:2020 | SGCN (continuidade) | **Sim** | BIA, RTO, RPO |
| ISO 22313 | Guia da 22301 | Não | orientações |
| NIST CSF v1.1 | Framework de ciber | — | Identify/Protect/Detect/Respond/Recover (sem Govern) |
| NIST SP 800-61 | Resposta a incidentes | — | 4 fases (contenção = isolar) |
| MITRE ATT&CK | TTPs de adversário | — | táticas (Lateral Movement) |

> Fixar as **pegadinhas em negrito** — é onde a FGV separa quem decorou de quem
> entendeu. Gerar flashcards destes pontos ou puxar questões das provas em
> `../provas-anteriores/`.
