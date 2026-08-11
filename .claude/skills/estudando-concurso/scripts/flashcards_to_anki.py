#!/usr/bin/env python3
"""Convert a simple Q&A flashcard file into an Anki-importable TSV.

Anki imports plain text where each line is `front<TAB>back`. This script reads
flashcards written in an easy-to-author Markdown-ish format and emits that TSV,
escaping tabs/newlines so multi-line answers survive the import.

Input format (one card per Q/A pair; blank lines optional):

    Q: What is the prazo for mandado de segurança?
    A: 120 dias, contados da ciência do ato impugnado (Lei 12.016/2009, art. 23).

    Q: ...
    A: ...

You can also use `P:`/`R:` (pergunta/resposta) instead of `Q:`/`A:`.
An answer may span multiple lines until the next `Q:`/`P:` (or EOF).
Optionally add `TAGS: tag1 tag2` after an answer to tag that card.

Usage:
    python3 flashcards_to_anki.py cards.md -o deck.txt
    python3 flashcards_to_anki.py cards.md            # writes cards.anki.tsv
"""
import argparse
import sys
from pathlib import Path

Q_PREFIXES = ("Q:", "P:")
A_PREFIXES = ("A:", "R:")
TAG_PREFIX = "TAGS:"


def clean(text: str) -> str:
    """Collapse a multi-line field into an Anki-safe single line."""
    text = text.strip()
    # Anki uses <br> for line breaks inside a field; tabs would break columns.
    return text.replace("\t", "    ").replace("\n", "<br>")


def parse(lines):
    """Yield (front, back, tags) tuples from the flashcard lines."""
    front, back_lines, tags = None, [], ""
    for raw in lines:
        line = raw.rstrip("\n")
        stripped = line.strip()
        if stripped.startswith(Q_PREFIXES):
            if front is not None:
                yield front, "\n".join(back_lines), tags
            front, back_lines, tags = stripped[2:].strip(), [], ""
        elif stripped.startswith(A_PREFIXES):
            back_lines = [stripped[2:].strip()]
        elif stripped.startswith(TAG_PREFIX):
            tags = stripped[len(TAG_PREFIX):].strip()
        elif front is not None and back_lines:
            back_lines.append(line)  # continuation of a multi-line answer
    if front is not None:
        yield front, "\n".join(back_lines), tags


def main() -> int:
    parser = argparse.ArgumentParser(description="Q&A flashcards -> Anki TSV.")
    parser.add_argument("input", help="Path to the Q&A flashcard file")
    parser.add_argument("-o", "--output", help="Output .tsv/.txt (default: <input>.anki.tsv)")
    args = parser.parse_args()

    src = Path(args.input)
    if not src.exists():
        print(f"error: not found: {src}", file=sys.stderr)
        return 1
    out = Path(args.output) if args.output else src.with_suffix(".anki.tsv")

    rows, skipped = [], 0
    for front, back, tags in parse(src.read_text(encoding="utf-8").splitlines(keepends=True)):
        front, back = clean(front), clean(back)
        if not front or not back:
            skipped += 1
            continue
        row = f"{front}\t{back}"
        if tags:
            row += f"\t{tags}"
        rows.append(row)

    out.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"✅ {len(rows)} cards -> {out}" + (f"  ({skipped} skipped)" if skipped else ""))
    print("Import in Anki: File > Import, field separator = Tab, "
          "allow HTML = yes, map columns Front/Back" + ("/Tags" if any("\t" in r and r.count("\t") == 2 for r in rows) else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
