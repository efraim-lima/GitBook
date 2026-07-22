# Arquitetura de Agentes com uso de Harness

Para estruturar uma instrução de gerenciamento de memória de longo prazo que maximize a eficiência de tokens e mantenha a legibilidade humana, você deve implementar o conceito de Harness Engineering focado em persistência de estado e hidratação seletiva.
Abaixo está a instrução estruturada para o seu agente, dividida por pastas e técnicas de otimização:
Instrução de Arquiteto: Gerenciamento de Memória de Longo Prazo
Sua Missão: Gerenciar a continuidade do conhecimento entre sessões "frias" (onde o agente não tem memória nativa), utilizando o repositório como a única fonte da verdade e minimizando o consumo de tokens através de compressão e divulgação progressiva.

## 1. Estrutura da Memória (Arquivos Físicos)

Toda memória deve residir no diretório .factory/ (ou agentic/) para garantir persistência:

- .factory/session-log.md (Memória de Curto/Médio Prazo): Registro narrativo do que foi feito, o que quebrou e decisões tomadas.
- .factory/memory-bank/ (Memória de Longo Prazo):
- state.json: Dados estruturados e listas de tarefas (JSON resiste melhor à corrupção que Markdown).
- concepts.lean: Base de conhecimento técnica comprimida no formato LEAN (economiza ~44% de tokens).
- .factory/intent.md: Contrato imutável de intenções e metas do projeto para evitar desvios comportamentais.

## 2. Estratégia de Criação de Memória (Ao final da tarefa)

Sempre que concluir uma atividade ou antes de um Context Reset, execute este protocolo:
Resumo Recursivo (Human-Ready): Escreva no session-log.md uma frase concisa (máximo 2 sentenças) sobre o progresso. Use um tom narrativo para que um humano entenda o "estado da arte" atual.
Compactação Técnica: Se o histórico de conversas estiver "poluído", gere um resumo técnico removendo "tokens parasitas" (polidez e redundâncias).
Atualização de Estado: Atualize o state.json mudando apenas os status de tarefas de incompleto para completo. Nunca remova ou reordene itens para preservar o histórico de commits como auditoria.

## 3. Estratégia de Consulta Eficiente (Consumo de Tokens)

Para consultar a memória sem explodir a janela de contexto, utilize estas técnicas:
Hidratação Seletiva (Divulgação Progressiva): Não carregue toda a memória. Leia primeiro o CLAUDE.md (ponteiro) e depois apenas a seção específica da especificação ou log relevante para a tarefa atual.
Padrão de Alias de Evidência: Em vez de citar documentos inteiros, use IDs curtos (ex: E001, F002) que apontam para uma tabela de referência no RAG. Isso reduz o custo de input em até 75%.
Prompt Caching: Posicione os arquivos de instrução estática (como intent.md e regras base) no início do prompt para aproveitar descontos de cache de até 90% em provedores como Anthropic e OpenAI.

## 4. Scripts e Processamento Offline (Opcional)

Se houver capacidade de processamento local, prefira scripts determinísticos em vez de IA para tarefas de manutenção de memória:
Script de Limpeza (Post-Build): Execute um script Python que use regex para remover metadados de sistema ou logs de erro repetitivos antes de salvar o log de sessão.
Linter de Memória: Use um linter para garantir que os arquivos Markdown na pasta de memória não excedam 100 linhas, forçando a IA a decompor o conhecimento em novos subarquivos.
RAG Local: Para grandes bases de dados, use um banco vetorial local (como FAISS ou Chroma). O agente deve consultar apenas os top-k fragmentos mais relevantes em vez de ler toda a documentação

## Tree Map

A estrutura centraliza a "inteligência" no diretório .factory/ (ou agentic/) e as habilidades no diretório skills/, mantendo a raiz do projeto limpa com "arquivos de ponteiro".

``` bash
/
├── CLAUDE.md              # Ponteiro para o Claude Code [2, 5, 6]
├── AGENTS.md              # Padrão AAIF (GitHub Copilot, Cursor, Devin) [5, 7]
├── .factory/              # Infraestrutura do Harness (Memória e SDD) [1, 3, 8]
│   ├── spec.md            # Especificação Comportamental (Fonte da Verdade) [1, 2, 9]
│   ├── intent.md          # Contrato de Intenção Organizacional [1, 2]
│   ├── discovery.md       # Mapa do Codebase (Essencial para Brownfield) [3, 10]
│   ├── session-log.md     # Memória Narrativa (Handoff entre sessões) [1, 2, 11]
│   ├── memory-bank/       # Registros de Estado [1]
│   │   ├── state.json     # Checklist de tarefas e progresso imutável [1, 12, 13]
│   │   └── concepts.lean  # Base de conhecimento técnica comprimida [1, 14]
│   └── adr/               # Architecture Decision Records (Imutáveis) [15, 16]
├── skills/                # Habilidades Modulares e Testáveis [17-19]
│   └── [nome-da-skill]/
│       ├── SKILL.md       # Instruções + Metadados YAML [17, 20-22]
│       ├── scripts/       # Código executável e utilitários [17, 21, 23]
│       ├── references/    # Documentação de apoio (carregada sob demanda) [17, 21]
│       └── evals/         # Suítes de avaliação para a skill [17, 24, 25]
└── .github/               # Scaffolding específico para agentes GitHub (Spec Kit) [26]
    └── prompts/           # Templates de prompts (specify, plan, tasks) [26]
```
