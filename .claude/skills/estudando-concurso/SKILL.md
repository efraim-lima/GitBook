---
name: estudando-concurso
description: Study assistant for Brazilian public-service exam (concurso público) candidates. Use when the user wants to actually study and master the exam content — building a study schedule/ciclo de estudos from available daily hours, generating banca-style practice questions (Cebraspe C/E, FGV, FCC) and simulados, creating Anki flashcards from text, simplifying dense legal texts and summarizing long material, giving rubric-based feedback on discursive/essay answers, and tutoring by breaking down the step-by-step solution of missed questions. Works from an analise-edital.md produced by the analisando-edital skill and reads/writes the shared Concursos/ folder (one subfolder per concurso).
---

# Estudando Concurso

## Overview

This skill helps a candidate understand and master concurso público content. It
turns an analyzed edital into concrete study action: schedules, practice
material, simplified explanations, essay feedback, and on-demand tutoring. It
pairs with `analisando-edital` — prefer starting from that skill's
`Concursos/<slug>/analise-edital.md`, which defines the exact scope, the banca,
and the priority of each topic.

## Shared folder

Read source material from `Concursos/<slug>/` and write study outputs to
`Concursos/<slug>/estudos/` so the user has the same files. If no concurso
folder exists yet, offer to run the `analisando-edital` skill first, or work
ad hoc from whatever material the user provides.

## Core capabilities

### 1. Planning and structuring the studies
Extract the exact topics from `analise-edital.md` (or from an edital directly).
Given the candidate's **available daily study hours** and the exam date, produce
a **ciclo de estudos** that rotates matérias and schedules spaced reviews
(24h → 7d → 30d). Base the output on `assets/cronograma-template.md`; weight the
rotation toward high-priority, high-difficulty matérias. Save to
`estudos/cronograma.md`.

### 2. Generating practice material
- **Simulados / questions:** create original questions in the **style of the
  specific banca** — Cebraspe Certo/Errado (with penalty logic), FGV
  case-based multiple choice, FCC literal multiple choice. See
  `references/bancas.md`. Each question includes the answer and a short
  justification pinpointing why it is right/wrong. Calibrate against the real
  provas anteriores in `Concursos/<slug>/provas-anteriores/` when available.
- **Flashcards:** analyze a block of text, extract the key concepts, and format
  them as Q/A pairs. Write them to a `.md` file in `Q:`/`A:` format, then run
  `scripts/flashcards_to_anki.py cards.md` to emit an Anki-importable TSV for
  spaced repetition.

### 3. Simplifying complex content
- **Legal translation:** rewrite dense legal text (Direito Administrativo,
  Constitucional, etc.) in direct, accessible language — without losing the
  legal meaning; keep article/law references.
- **Targeted summaries:** condense a long text or a video-lesson transcript to
  its central points, aligned to the topics that actually fall on the exam.

### 4. Correction and evaluation
Give feedback on discursive/essay answers: grammatical correction, textual
cohesion analysis, and argumentation improvements. **Use the banca's correction
criteria** from the edital when present; otherwise use the general rubric in
`references/bancas.md` (conteúdo, coesão/coerência, correção gramatical,
adequação ao comando). Score per criterion, quote specific passages, and suggest
a rewrite.

### 5. On-demand tutor (question resolution)
For calculation/logic subjects (Matemática Financeira, Estatística, Raciocínio
Lógico) and any missed question, reverse-engineer the solution: break it down
step by step and explain the **concept behind the error**, not just the right
answer. Where useful, generate 1–2 similar questions to reinforce the concept.

## Resources

- `scripts/flashcards_to_anki.py` — converts a `Q:`/`A:` flashcard file into an
  Anki-importable TSV (supports multi-line answers and `TAGS:`).
- `references/bancas.md` — per-banca question styles (Cebraspe/FGV/FCC/others)
  and criteria for correcting discursivas.
- `assets/cronograma-template.md` — study-schedule template (ciclo de estudos,
  weekly grid, spaced-review tracker).
