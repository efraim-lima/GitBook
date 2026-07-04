"""
sample_agent.py — Functional demo agent for the Discord bot middleware.

I/O Protocol:
  Input   : sys.argv[1]          — task string passed by the bot
  Output  : stdout (normal)      — forwarded to Discord as plain text
  Output  : stdout 'QUESTION: …' — bot relays to Discord; user reply piped back
  Input   : stdin                — receives user replies from the bot
  Output  : stderr               — forwarded as a warning block after completion
  Exit    : 0 = success, non-zero = failure
"""
from __future__ import annotations

import json
import sys
import time


def main() -> None:
    if len(sys.argv) < 2:
        print("ERROR: no task provided.", file=sys.stderr)
        sys.exit(1)

    task: str = sys.argv[1]

    # ── Step 1: acknowledge receipt ───────────────────────────────────────────
    print(f"[sample_agent] Task received: {task}", flush=True)
    print("[sample_agent] Running initial analysis…", flush=True)
    time.sleep(1)

    # ── Step 2: ask the user a clarifying question via the QUESTION protocol ──
    # The bot will:
    #   1. Detect the 'QUESTION:' prefix.
    #   2. Relay the question text to Discord, mentioning the original author.
    #   3. Wait for a reply and pipe it to this process's stdin.
    print("QUESTION: What output format do you need? (plain / json / table)", flush=True)

    fmt = sys.stdin.readline().strip().lower() or "plain"
    print(f"[sample_agent] Format selected: {fmt}", flush=True)

    # ── Step 3: simulate work ─────────────────────────────────────────────────
    print("[sample_agent] Processing…", flush=True)
    time.sleep(1)

    # ── Step 4: produce output in the requested format ────────────────────────
    result = {"task": task, "status": "completed", "format": fmt}

    if fmt == "json":
        print(json.dumps(result, indent=2), flush=True)

    elif fmt == "table":
        header = f"{'Field':<20} {'Value'}"
        print(header, flush=True)
        print("-" * 50, flush=True)
        for key, value in result.items():
            print(f"{key:<20} {value}", flush=True)

    else:
        for key, value in result.items():
            print(f"{key}: {value}", flush=True)

    print("[sample_agent] Done.", flush=True)


if __name__ == "__main__":
    main()
