#!/usr/bin/env python3
"""Download the edital PDF from a concurso notice URL into the shared folder.

Accepts either a direct PDF link or an HTML page (the typical "página do
concurso" of a banca/órgão). For an HTML page it scans the links, ranks the
ones that look like the edital (and its retificações), and downloads them into
the destination folder — by default `Concursos/<slug>/edital/`.

Stdlib only (urllib + html.parser); no external dependencies. Many government
and banca sites block the default urllib User-Agent, so a browser-like UA is
sent. JavaScript-rendered link lists cannot be parsed here — if nothing is
found, fall back to reading the page with WebFetch and passing the direct PDF
URL to this script.

Usage:
    python3 baixar_edital.py <url> --dest Concursos/<slug>/edital
    python3 baixar_edital.py <url> --dest ./edital --all      # grab every PDF
    python3 baixar_edital.py <url> --dest ./edital --list     # only list, no download

Prints one downloaded absolute path per line (for a caller to capture).
"""
import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
from urllib.request import Request, urlopen

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

# Words that make a link more likely to be the notice we want (and its changes).
KEYWORDS = ("edital", "abertura", "retifica", "anexo", "conteudo", "programatic")


class LinkExtractor(HTMLParser):
    """Collect (href, visible_text) pairs from <a> tags."""

    def __init__(self):
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self._href, self._text = href, []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self._href is not None:
            self.links.append((self._href, " ".join(self._text).strip()))
            self._href, self._text = None, []


def fetch(url: str, timeout: int = 45) -> tuple[bytes, str, str]:
    """Return (body, content_type, final_url) following redirects."""
    req = Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urlopen(req, timeout=timeout) as resp:
        return resp.read(), resp.headers.get("Content-Type", ""), resp.geturl()


def is_pdf(body: bytes, content_type: str, url: str) -> bool:
    return (
        body[:5] == b"%PDF-"
        or "application/pdf" in content_type.lower()
        or urlparse(url).path.lower().endswith(".pdf")
    )


def score(href: str, text: str) -> int:
    """Rank a candidate link: higher = more likely the edital PDF."""
    hay = f"{href} {text}".lower()
    s = 0
    if urlparse(href).path.lower().endswith(".pdf"):
        s += 5
    if "download" in hay or "arquivo" in hay:
        s += 1
    s += sum(2 for kw in KEYWORDS if kw in hay)
    # "edital de abertura" is the primary target.
    if "edital" in hay and ("abertura" in hay or "n" in hay):
        s += 2
    return s


def safe_name(url: str, index: int) -> str:
    base = unquote(Path(urlparse(url).path).name) or f"documento_{index}.pdf"
    base = re.sub(r"[^A-Za-z0-9._-]+", "_", base).strip("_")
    if not base.lower().endswith(".pdf"):
        base += ".pdf"
    return base


def download(url: str, dest_dir: Path, index: int) -> Path | None:
    body, ctype, final = fetch(url)
    if not is_pdf(body, ctype, final):
        print(f"  skip (not a PDF): {url}", file=sys.stderr)
        return None
    dest_dir.mkdir(parents=True, exist_ok=True)
    out = dest_dir / safe_name(final, index)
    out.write_bytes(body)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Download edital PDF(s) from a URL.")
    ap.add_argument("url", help="Concurso page URL or direct PDF URL")
    ap.add_argument("--dest", help="Destination folder (e.g. Concursos/<slug>/edital). Required unless --list")
    ap.add_argument("--all", action="store_true", help="Download every PDF found, not just top matches")
    ap.add_argument("--list", action="store_true", help="List candidate PDF links without downloading")
    ap.add_argument("--max", type=int, default=6, help="Max PDFs to download when ranking (default 6)")
    args = ap.parse_args()

    if not args.list and not args.dest:
        ap.error("--dest is required unless --list is used")
    dest = Path(args.dest) if args.dest else Path(".")

    # Case 1: the URL is itself a PDF.
    try:
        body, ctype, final = fetch(args.url)
    except Exception as exc:  # network/SSL/403 etc.
        print(f"error: could not fetch {args.url}: {exc}", file=sys.stderr)
        return 2

    if is_pdf(body, ctype, final):
        if args.list:
            print(final)
            return 0
        dest.mkdir(parents=True, exist_ok=True)
        out = dest / safe_name(final, 1)
        out.write_bytes(body)
        print(out.resolve())
        return 0

    # Case 2: HTML page — extract and rank PDF links.
    parser = LinkExtractor()
    parser.feed(body.decode("utf-8", errors="replace"))
    candidates = []
    seen = set()
    for href, text in parser.links:
        absurl = urljoin(final, href)
        if absurl in seen:
            continue
        # keep only plausible document links (pdf extension, or download route)
        low = absurl.lower()
        if low.endswith(".pdf") or "download" in low or "arquivo" in low:
            seen.add(absurl)
            candidates.append((score(href, text), absurl, text))
    candidates.sort(key=lambda c: c[0], reverse=True)

    if not candidates:
        print("error: no PDF links found on the page. It may be JavaScript-rendered; "
              "read it with WebFetch and pass the direct PDF URL to this script.",
              file=sys.stderr)
        return 3

    if args.list:
        for sc, url, text in candidates:
            print(f"[{sc:>2}] {url}  — {text[:70]}")
        return 0

    chosen = candidates if args.all else candidates[: args.max]
    downloaded = []
    for i, (_sc, url, _text) in enumerate(chosen, 1):
        try:
            out = download(url, dest, i)
        except Exception as exc:
            print(f"  fail: {url}: {exc}", file=sys.stderr)
            continue
        if out:
            downloaded.append(out)

    if not downloaded:
        print("error: found candidate links but none downloaded as a valid PDF.",
              file=sys.stderr)
        return 4
    for out in downloaded:
        print(out.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
