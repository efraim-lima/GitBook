# Agentes Claude Code — Estrutura e Uso

Este documento descreve os subagentes configurados para este repositório (o vault
GitBook/Obsidian + o subprojeto de automação `Work/Automações/Entregaveis`) e como
utilizá-los na CLI do Claude Code.

> **Nota histórica**: estes agentes foram originalmente escritos em
> `.github/agents/*.agent.md` no formato do **VS Code Copilot Chat**. Esse formato
> **não** é lido pelo Claude Code. Os agentes reais para o Claude vivem em
> `.claude/agents/*.md` (este diretório). Os arquivos em `.github/agents/`
> permanecem válidos apenas para o Copilot no VS Code.

---

## 1. Onde os agentes ficam

O Claude Code lê definições de subagentes de dois lugares:

| Local | Escopo | Prioridade |
|-------|--------|-----------|
| `.claude/agents/*.md` | Apenas este projeto | Vence em caso de conflito de nome |
| `~/.claude/agents/*.md` | Todos os projetos | Usado se não houver homônimo no projeto |

Cada arquivo `.md` é **um agente**. O nome do agente vem do campo `name:` no
front-matter YAML, não do nome do arquivo.

### Anatomia de um arquivo de agente

```markdown
---
name: claudio                    # nome usado para invocar
description: Builder/executer... # QUANDO usar — o Claude lê isto para auto-delegar
tools: Read, Write, Edit, Bash, Grep, Glob   # ferramentas permitidas
model: sonnet                    # sonnet | opus | haiku | fable (ou omitir = herda)
---

Corpo em Markdown = o system prompt do agente (o "como ele trabalha").
```

- **`description`** é o campo mais importante: o Claude o usa para decidir
  automaticamente qual agente chamar. Seja específico sobre *quando* usar e
  *quando não* usar.
- **`tools`** restringe o que o agente pode fazer. Omita a linha ptools: Read, Write, Edit, Bash, Grep, Glob   # ferramentas permitidas
tools: Read, Write, Edit, Bash, Grep, Glob   # ferramentas permitidas
ara conceder
  todas as ferramentas. Menos ferramentas = agente mais focado e seguro.
- **`model`** aceita `sonnet`, `opus`, `haiku`, `fable`, ou pode ser omitido para
  herdar o modelo da sessão principal.

---

## 2. O cluster de agentes deste projeto

Quatro agentes, adaptados à natureza real deste repositório (base de conhecimento
Markdown + um pipeline Python de automação). **Foram removidas** as suposições do
framework antigo (`.factory/spec.md`, `pnpm validate`, gates de TDD, `run-e2e.sh`)
porque nada disso existe aqui.

| Agente | Papel | Modelo | Ferramentas |
|--------|-------|--------|-------------|
| **alfred** | Orquestrador/planejador. Separa intenção de execução e delega. | sonnet | Task, Read, Grep, Glob, Bash, TodoWrite |
| **claudio** | Construtor/executor de código (pipeline Python, scripts). | sonnet | Read, Write, Edit, Bash, Grep, Glob |
| **desire** | Automação de apresentações/relatórios (PPTX, placeholders). | sonnet | Read, Write, Edit, Bash, Grep, Glob |
| **severino** | Segurança/DFIR/SOC — revisão de código e autoria de notas. | sonnet | Read, Write, Edit, Bash, Grep, Glob |

### alfred — o orquestrador
Só vale a pena quando a tarefa **cruza vários domínios** (ex.: reestruturar
conteúdo do vault *e* mexer no pipeline de automação). Ele planeja, quebra em
subtarefas e delega para os outros três via a ferramenta `Task`. Não escreve
código nem conteúdo diretamente. Para uma edição de domínio único, chame o agente
específico direto — é mais rápido.

### claudio — o construtor
Implementa mudanças de código, principalmente em `Work/Automações/Entregaveis`
(ingestão → PostgreSQL via `app/db/crud.py` → renderização PPTX). Roda os testes
(`python -m unittest _dev/test_integration.py`) antes de declarar concluído.

### desire — automação de entregáveis
Especialista no fluxo `gerar_apresentacao.py` / `update_presentation.py`: sincroniza
dados em placeholders de um template `.pptx` **sem nunca alterar o design visual**.
Se não houver template, ele para e pergunta.

### severino — segurança
Revisa código/infra em busca de problemas de segurança (tratamento de segredos em
`.env`/`app/config.py`, injeção em ingestão/CRUD) e escreve/audita notas de
segurança em `cyberetico/`, `readme-1/` (dfir), `knowlage/`. Não roda payloads
destrutivos sem autorização explícita.

---

## 3. Como usar na CLI

### Opção A — deixar o Claude delegar sozinho (automático)
Basta descrever a tarefa. Se ela casar com a `description` de um agente, o Claude
principal delega automaticamente. Exemplos de prompt:

```
Revise o tratamento de credenciais em app/config.py em busca de vazamento de segredos.
→ Claude tende a acionar severino

Adicione uma função de ingestão para uma nova fonte de dados no pipeline.
→ Claude tende a acionar claudio
```

### Opção B — pedir um agente pelo nome (explícito)
Nomeie o agente diretamente no prompt para forçar a escolha:

```
Use o severino para auditar a segurança do módulo de ingestão.
Peça ao claudio para implementar a nova função de upsert e rodar os testes.
Use o alfred para planejar a reorganização do SUMMARY.md junto com uma revisão de segurança.
```

### Opção C — verificar / gerenciar agentes
```bash
# Listar os arquivos de agente do projeto
ls .claude/agents/

# O antigo wizard interativo /agents foi REMOVIDO do Claude Code.
# Para criar/editar um agente: peça ao Claude ("crie um subagente que...")
# ou edite os arquivos .md diretamente neste diretório.
```

> **Importante**: o comando `/agents <nome>` **não** invoca um agente — aquele era
> um assistente de criação que foi descontinuado. Para *usar* um agente, escreva um
> prompt normal (Opção A ou B), não um slash command.

---

## 4. Como o Claude escolhe um agente

1. Você envia um prompt.
2. O Claude principal compara a tarefa com o campo `description` de cada agente.
3. Se houver correspondência clara (ou se você nomear o agente), ele delega via a
   ferramenta `Task`, passando um recorte da tarefa — não o prompt inteiro.
4. O subagente roda em seu **próprio contexto isolado**, com apenas as ferramentas
   do seu front-matter, e devolve um resumo do resultado ao Claude principal.
5. O Claude principal relata a você.

Como o contexto é isolado, o subagente **não** enxerga o histórico da conversa —
inclua no pedido tudo o que ele precisa saber (arquivos, escopo, objetivo).

---

## 5. Notas específicas deste repositório

- **`Work/` é um repositório git aninhado separado** (`Work/.git`). `git status` /
  `git log` na raiz não cobrem o `Work/`. Os agentes checam os dois de forma
  independente.
- **Não editar**: blocos `%% Waypoint %%`, blocos Dataview `ccard`, e diretórios
  `.smart-env/` (dados do plugin Smart Connections) — são gerados por plugins.
- **Governança obsoleta**: `.github/AGENTS.md` e `.github/CLAUDE.md` descrevem um
  fluxo genérico pnpm/TDD/spec-driven que **não existe** aqui. Ignorar. O
  `CLAUDE.md` da raiz é a fonte autoritativa.
- Único alvo real de build/teste: `Work/Automações/Entregaveis` (Python,
  `unittest`, `uv run`).

---

## 6. Editando ou criando novos agentes

Para ajustar um agente, edite o `.md` correspondente e salve — a mudança vale na
próxima invocação (subagentes recarregam a cada chamada). Para criar um novo:

1. Crie `.claude/agents/<nome>.md`.
2. Preencha o front-matter (`name`, `description`, `tools`, `model`).
3. Escreva o system prompt no corpo.
4. Verifique com `ls .claude/agents/`.

Ou simplesmente peça ao Claude: *"crie um subagente chamado X que faz Y"*.
