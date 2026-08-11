---
name: analisando-edital
description: Analyzes Brazilian public-service exam announcements (editais de concurso público). Use when the user shares an edital PDF/URL or names a concurso and wants to understand exactly what the exam covers — extracting the conteúdo programático into atomic study topics, identifying the banca, cargo, dates, question weights and required legislation, organizing reference study materials, and finding and saving past exam PDFs (provas anteriores). Sets up a shared Concursos/ folder (one subfolder per concurso) that both the agent and the user can access.
---

# Analisando Edital

## Overview

This skill turns a Brazilian concurso público edital into an actionable study
foundation: a precise breakdown of what the exam covers, a shared folder of
organized materials, and a collection of past-exam PDFs. Its output feeds the
companion skill `estudando-concurso`, which builds schedules, questions, and
flashcards from the analysis.

## Shared folder convention

All artifacts live at the **repository root** under `Concursos/<slug>/` so the
agent and the user share the exact same files:

```
Concursos/<slug>/
├── analise-edital.md      # the syllabus breakdown (main deliverable)
├── edital/                # the edital PDF + any retificações
├── provas-anteriores/     # past-exam PDFs + README.md manifest
├── materiais/             # reference study materials
└── estudos/               # study outputs (cronograma, simulados, flashcards)
```

Create this tree with the bundled script — never hand-craft the folders:

```bash
python3 scripts/init_concurso.py "Nome do Concurso 2026"
```

It auto-detects the repo root via `.git`, slugifies the name, seeds
`analise-edital.md` and the `provas-anteriores/README.md` manifest, and prints
the created path.

## Workflow

### 1. Set up the shared folder
Run `scripts/init_concurso.py` with the concurso's human name. Confirm the
printed path with the user before populating it. This creates
`Concursos/<slug>/edital/` where the notice PDF will be saved.

### 2. Obtain the edital (URL is the primary path)
The common case: **the user passes the URL of the public tender notice**
(the "página do concurso"). Download the PDF into the shared folder with the
bundled script — it accesses the page, finds the edital link(s), and saves the
file so the study skill can use it:

```bash
python3 scripts/baixar_edital.py "<url>" --dest "Concursos/<slug>/edital"
```

- The URL may be a **direct PDF** or an **HTML page**; the script handles both.
  For a page it ranks links and downloads the edital de abertura plus any
  retificações (add `--all` to grab every PDF, `--list` to preview links first).
- It prints each saved absolute path. Confirm the PDF is the real notice.
- **If it finds nothing** (JavaScript-rendered pages, logins, portals), read the
  page with WebFetch to locate the direct `.pdf` URL, then re-run the script
  with that URL. As a last resort, save the file the user provides directly.

If instead the user gives only a concurso name (no URL), search for the official
edital PDF using `references/fontes-provas.md`, then download it the same way.

### 3. Analyze the edital
Read the edital and fill `analise-edital.md` following the full template in
`references/modelo-analise.md`. The core job is to **eliminate ambiguity about
scope**: break the conteúdo programático into atomic, studyable topics, and
capture:
- banca, cargo, vagas, requisitos, remuneração, datas-chave;
- exam structure: number of questions, weight and minimum score per matéria,
  question type (multiple-choice vs. Certo/Errado — note Cebraspe's penalty
  where a wrong answer cancels a right one);
- every law/súmula/norma the edital cites (the source of truth for questions);
- discursiva/redação rules and the banca's correction criteria, if any.

### 4. Organize study materials
Collect reference materials (apostilas, legislation texts, links) into
`materiais/`. Prefer the exact legislation cited by the edital.

### 5. Find and save past exams
Search for provas anteriores using `references/fontes-provas.md` (banca sites
first, then aggregators like PCI Concursos / QConcursos). Prefer the **same
banca and cargo**. Download each PDF into `provas-anteriores/`, name it
`AAAA_<banca>_<orgao>_<cargo>.pdf`, and record it in the manifest
(`provas-anteriores/README.md`) with its source URL. Use the historical
incidence of topics to set the priority (A/M/B) column in the analysis.

### 6. Hand off
Point the user (and the `estudando-concurso` skill) at the completed
`analise-edital.md` as the basis for planning, simulados, and flashcards.

## Resources

- `scripts/init_concurso.py` — creates the shared `Concursos/<slug>/` tree and
  seeds the analysis note and manifest. Idempotent; never overwrites files.
- `scripts/baixar_edital.py` — given the tender-notice URL (page or direct PDF),
  downloads the edital PDF(s) into the destination folder. Stdlib only;
  browser-like User-Agent; `--all` / `--list` / `--max` flags.
- `references/modelo-analise.md` — full template for `analise-edital.md`.
- `references/fontes-provas.md` — where to find editais and past-exam PDFs, plus
  search strategy and naming/verification best practices.
