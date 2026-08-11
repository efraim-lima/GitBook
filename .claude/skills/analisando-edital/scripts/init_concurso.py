#!/usr/bin/env python3
"""Create the shared folder tree for a concurso (public-exam) study project.

The tree lives at the repository root under `Concursos/<slug>/` so that both
agents and the user can reach the same files: the edital, the syllabus
analysis, past-exam PDFs, and study materials.

Usage:
    python3 init_concurso.py "Nome do Concurso 2026" [--root /path/to/repo]

Prints the absolute path of the created concurso folder on the last line so a
caller can capture it.
"""
import argparse
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path


def slugify(name: str) -> str:
    """Turn a concurso name into a filesystem-friendly slug (ascii-kebab)."""
    norm = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    norm = norm.lower()
    norm = re.sub(r"[^a-z0-9]+", "-", norm).strip("-")
    return norm or "concurso"


def find_repo_root(start: Path) -> Path:
    """Walk up from `start` looking for a .git dir; fall back to start."""
    for candidate in [start, *start.parents]:
        if (candidate / ".git").exists():
            return candidate
    return start


SUBDIRS = ["edital", "provas-anteriores", "materiais", "estudos"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Init a concurso study folder.")
    parser.add_argument("name", help="Human name of the concurso, e.g. 'PF Agente 2026'")
    parser.add_argument("--root", help="Repo root (default: auto-detect via .git)")
    args = parser.parse_args()

    root = Path(args.root).resolve() if args.root else find_repo_root(Path.cwd())
    slug = slugify(args.name)
    base = root / "Concursos" / slug

    if base.exists():
        print(f"⚠️  Already exists: {base}", file=sys.stderr)
    for sub in SUBDIRS:
        (base / sub).mkdir(parents=True, exist_ok=True)

    # Seed the analysis note if missing (never overwrite user work).
    analise = base / "analise-edital.md"
    if not analise.exists():
        analise.write_text(
            f"""---
concurso: {args.name}
slug: {slug}
criado: {date.today().isoformat()}
banca:
cargo:
status: analise-pendente
---

# Análise do Edital — {args.name}

> Preencha após ler o edital. Ver o template completo em
> `.claude/skills/analisando-edital/references/modelo-analise.md`.

## Dados gerais
- **Banca:**
- **Cargo(s):**
- **Vagas:**
- **Escolaridade / requisitos:**
- **Remuneração:**
- **Datas-chave:** inscrição · prova · resultado
- **Nº de questões / peso por matéria:**

## Conteúdo programático (escopo exato da prova)

<!-- Uma seção por matéria. Quebre o conteúdo em tópicos atômicos e marque peso. -->

## Provas anteriores localizadas
<!-- Ver provas-anteriores/README.md -->

## Materiais de referência
<!-- Ver materiais/ -->
""",
            encoding="utf-8",
        )

    provas_readme = base / "provas-anteriores" / "README.md"
    if not provas_readme.exists():
        provas_readme.write_text(
            "# Provas anteriores\n\n"
            "PDFs de provas passadas desta banca/cargo. Mantenha um item por arquivo:\n\n"
            "| Arquivo | Ano | Banca | Cargo | Fonte (URL) |\n"
            "|---------|-----|-------|-------|-------------|\n",
            encoding="utf-8",
        )

    print(base)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
