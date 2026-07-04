"""
config.py — Load and validate environment configuration.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

# ── Discord ────────────────────────────────────────────────────────────────────
DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN", "")

AUTHORIZED_USER_IDS: frozenset[int] = frozenset(
    int(uid.strip())
    for uid in os.getenv("AUTHORIZED_USER_IDS", "").split(",")
    if uid.strip().isdigit()
)

# ── Agents ─────────────────────────────────────────────────────────────────────
# AGENTS_DIR may be absolute or relative.
# Relative paths are resolved from the directory that contains this file,
# so the bot works correctly regardless of the working directory at launch.
_bot_dir: Path = Path(__file__).parent
AGENTS_DIR: Path = (
    _bot_dir / os.getenv("AGENTS_DIR", "..")
).resolve()

PYTHON_BIN: str = os.getenv("PYTHON_EXECUTABLE", "").strip() or sys.executable

# ── Startup notification ───────────────────────────────────────────────────────
# Optional: if set, the bot sends a startup message to this channel when ready.
STARTUP_CHANNEL_ID: int | None = (
    int(os.getenv("STARTUP_CHANNEL_ID", "").strip())
    if os.getenv("STARTUP_CHANNEL_ID", "").strip().isdigit()
    else None
)

# ── Workspace ─────────────────────────────────────────────────────────────────
# Root directory of the GitBook workspace. Used by alfred.py to locate
# Tasks.md, context/, and reports/.
_default_workspace = str(Path(__file__).parent.parent.parent)
WORKSPACE_ROOT: Path = Path(
    os.getenv("WORKSPACE_ROOT", _default_workspace)
).resolve()

# ── Session security: chord prefix ────────────────────────────────────────────
# Replies to active agent sessions are only accepted when the message starts
# with this chord sequence (case-insensitive).  Strip it before forwarding.
CHORD_PREFIX: str = os.getenv("CHORD_PREFIX", "EM7 FM7 Am7")

# ── Behaviour ──────────────────────────────────────────────────────────────────
REPLY_TIMEOUT: float = float(os.getenv("REPLY_TIMEOUT_SECONDS", "120"))
MAX_MESSAGE_LENGTH: int = int(os.getenv("MAX_MESSAGE_LENGTH", "1900"))


def validate() -> None:
    """Exit with a descriptive error if required settings are missing."""
    errors: list[str] = []

    if not DISCORD_TOKEN:
        errors.append("DISCORD_TOKEN is not set")

    if not AUTHORIZED_USER_IDS:
        errors.append(
            "AUTHORIZED_USER_IDS is not set or contains no valid integer IDs"
        )

    if not AGENTS_DIR.is_dir():
        errors.append(
            f"AGENTS_DIR '{AGENTS_DIR}' does not exist or is not a directory"
        )

    if errors:
        for msg in errors:
            print(f"[Config] ERROR: {msg}", file=sys.stderr)
        sys.exit(1)
