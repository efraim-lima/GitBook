"""
discord_notify.py — Notificador Discord standalone.

Envia mensagens ou arquivos para um canal Discord via API REST.
Usado por alfred.py para postar relatórios e alertas de aprovação
diretamente no servidor, fora do contexto do subprocess do bot.

Uso (linha de comando):
    python discord_notify.py "Mensagem de texto"
    python discord_notify.py --file caminho/para/relatorio.md
    python discord_notify.py --file relatorio.md --channel 123456789

Uso (import):
    from discord_notify import send_message, send_file
    send_message("Texto")
    send_file(Path("relatorio.md"))
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent / ".env")
except ImportError:
    pass

# ── Config ────────────────────────────────────────────────────────────────────
DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN", "")
DEFAULT_CHANNEL_ID: str = os.getenv("STARTUP_CHANNEL_ID", "")
MAX_LEN: int = int(os.getenv("MAX_MESSAGE_LENGTH", "1900"))

_API_BASE = "https://discord.com/api/v10"


# ── Core send ─────────────────────────────────────────────────────────────────

def _post(channel_id: str, content: str) -> bool:
    """POST a single message chunk. Returns True on success."""
    import urllib.error
    import urllib.request

    payload = json.dumps({"content": content}).encode("utf-8")
    req = urllib.request.Request(
        f"{_API_BASE}/channels/{channel_id}/messages",
        data=payload,
        headers={
            "Authorization": f"Bot {DISCORD_TOKEN}",
            "Content-Type": "application/json",
        },
    )
    try:
        urllib.request.urlopen(req, timeout=15)
        return True
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print(f"[discord_notify] HTTP {exc.code}: {body[:200]}", file=sys.stderr)
        return False
    except Exception as exc:
        print(f"[discord_notify] Erro: {exc}", file=sys.stderr)
        return False


def send_message(text: str, channel_id: str = "") -> bool:
    """Envia texto ao Discord, dividindo em chunks se necessário."""
    cid = channel_id or DEFAULT_CHANNEL_ID
    if not cid or not DISCORD_TOKEN:
        print("[discord_notify] DISCORD_TOKEN ou CHANNEL_ID não configurado.", file=sys.stderr)
        return False

    text = text.strip()
    if not text:
        return True

    ok = True
    for i in range(0, len(text), MAX_LEN):
        ok = _post(cid, text[i : i + MAX_LEN]) and ok
    return ok


def send_file(path: Path, header: str = "", channel_id: str = "") -> bool:
    """Lê arquivo e envia conteúdo como mensagem de texto."""
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as exc:
        print(f"[discord_notify] Não foi possível ler {path}: {exc}", file=sys.stderr)
        return False

    prefix = header or f"📄 **`{path.name}`**\n"
    return send_message(prefix + content, channel_id=channel_id)


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Envia mensagem ou arquivo para um canal Discord."
    )
    parser.add_argument("message", nargs="?", help="Texto a enviar")
    parser.add_argument("--file", help="Caminho do arquivo cujo conteúdo será enviado")
    parser.add_argument("--channel", help="ID do canal Discord (padrão: STARTUP_CHANNEL_ID)")
    parser.add_argument("--header", help="Cabeçalho opcional ao enviar arquivo", default="")
    args = parser.parse_args()

    cid = args.channel or DEFAULT_CHANNEL_ID

    if not DISCORD_TOKEN:
        print("[discord_notify] ERRO: DISCORD_TOKEN não configurado.", file=sys.stderr)
        sys.exit(1)
    if not cid:
        print("[discord_notify] ERRO: Canal não especificado (--channel ou STARTUP_CHANNEL_ID).", file=sys.stderr)
        sys.exit(1)

    success = False
    if args.file:
        success = send_file(Path(args.file), header=args.header, channel_id=cid)
    elif args.message:
        success = send_message(args.message, channel_id=cid)
    else:
        # Lê de stdin
        content = sys.stdin.read()
        success = send_message(content, channel_id=cid)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
