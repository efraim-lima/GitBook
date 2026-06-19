"""
runner.py — Async subprocess executor with bidirectional Discord ↔ agent I/O.

Agent I/O protocol (agent side):
  sys.argv[1]          → task string
  stdout (normal line) → forwarded to Discord as plain output
  stdout 'QUESTION: …' → bot relays to Discord; pipes user reply back to stdin
  stdin                → receives user replies piped by the bot
  stderr               → forwarded as a warning block after completion
  exit 0 / non-zero    → success / failure
"""
from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import discord

import config

# Lines starting with this prefix trigger the question protocol.
_QUESTION_PREFIX = "QUESTION:"


# ── Session ────────────────────────────────────────────────────────────────────

@dataclass
class _AgentSession:
    channel_id: int
    author_id: int
    agent_name: str
    reply_queue: asyncio.Queue[str] = field(default_factory=asyncio.Queue)


# Active sessions: one per channel (channel_id → session).
_sessions: dict[int, _AgentSession] = {}


def get_session(channel_id: int) -> Optional[_AgentSession]:
    return _sessions.get(channel_id)


# ── Path resolution ────────────────────────────────────────────────────────────

def resolve_agent_path(agent_id: str) -> Optional[Path]:
    """
    Safely map <agent_id> to AGENTS_DIR/<agent_id>.py.

    Security:
      - Only alphanumeric, dash (-), and underscore (_) characters are accepted.
      - The resolved path is verified to be a child of AGENTS_DIR to prevent
        path traversal (e.g. '../../../etc/passwd').
    """
    safe_id = "".join(c for c in agent_id if c.isalnum() or c in "-_")
    if safe_id != agent_id or not safe_id:
        return None

    candidate = (config.AGENTS_DIR / f"{safe_id}.py").resolve()

    try:
        candidate.relative_to(config.AGENTS_DIR)
    except ValueError:
        return None

    return candidate if candidate.is_file() else None


# ── Helpers ────────────────────────────────────────────────────────────────────

async def _send_chunks(
    channel: discord.abc.Messageable, text: str
) -> None:
    """Split *text* into Discord-safe code blocks and send each."""
    text = text.strip()
    if not text:
        return
    limit = config.MAX_MESSAGE_LENGTH
    for i in range(0, len(text), limit):
        await channel.send(f"```\n{text[i : i + limit]}\n```")


# ── Executor ───────────────────────────────────────────────────────────────────

async def execute(
    channel: discord.TextChannel,
    author: discord.Member | discord.User,
    agent_path: Path,
    task: str,
) -> None:
    """
    Execute *agent_path* as an async subprocess, bridging its I/O with Discord.

    Only one agent may run per channel at a time.
    """
    channel_id = channel.id

    if channel_id in _sessions:
        await channel.send(
            "⚠️  An agent is already running in this channel. "
            "Wait for it to complete."
        )
        return

    session = _AgentSession(
        channel_id=channel_id,
        author_id=author.id,
        agent_name=agent_path.stem,
    )
    _sessions[channel_id] = session

    await channel.send(
        f"▶ **`{agent_path.stem}`** started — requested by {author.mention}"
    )

    try:
        proc = await asyncio.create_subprocess_exec(
            config.PYTHON_BIN,
            str(agent_path),
            task,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        assert proc.stdout is not None
        assert proc.stdin is not None

        stdout_buf: list[str] = []

        async def _flush() -> None:
            if stdout_buf:
                await _send_chunks(channel, "\n".join(stdout_buf))
                stdout_buf.clear()

        # Stream stdout line-by-line.
        async for raw_line in proc.stdout:
            line = raw_line.decode("utf-8", errors="replace").rstrip()

            if line.startswith(_QUESTION_PREFIX):
                # Flush buffered output before asking the question.
                await _flush()

                question = line[len(_QUESTION_PREFIX):].strip()
                await channel.send(
                    f"🤖 **Agent question for {author.mention}:** {question}\n"
                    f"_(reply here within {int(config.REPLY_TIMEOUT)} s)_"
                )

                try:
                    reply = await asyncio.wait_for(
                        session.reply_queue.get(),
                        timeout=config.REPLY_TIMEOUT,
                    )
                except asyncio.TimeoutError:
                    reply = ""
                    await channel.send(
                        "⏱ No reply received — sending empty response to agent."
                    )

                proc.stdin.write((reply + "\n").encode("utf-8"))
                await proc.stdin.drain()

            else:
                stdout_buf.append(line)

        await _flush()

        # Capture remaining stderr after stdout EOF.
        _, stderr_data = await proc.communicate()
        if stderr_data:
            stderr_text = stderr_data.decode("utf-8", errors="replace").strip()
            if stderr_text:
                limit = config.MAX_MESSAGE_LENGTH
                await channel.send(
                    f"⚠️ **stderr:**\n```\n{stderr_text[:limit]}\n```"
                )

        rc = proc.returncode
        icon = "✅" if rc == 0 else "❌"
        await channel.send(
            f"{icon} **`{agent_path.stem}`** finished (exit code {rc})."
        )

    except Exception as exc:
        await channel.send(f"💥 **Execution error:** `{exc}`")
        raise

    finally:
        _sessions.pop(channel_id, None)
