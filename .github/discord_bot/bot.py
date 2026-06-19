"""
bot.py — Discord client entry point.

Command:
    @Bot delegate <agent_id> <task>

Examples:
    @Bot delegate sample_agent summarize the last error logs
    @Bot delegate alfred review the Tasks.md file
"""
from __future__ import annotations

import asyncio
import sys

import discord

import config
import runner

# ── Startup validation ─────────────────────────────────────────────────────────
config.validate()

# ── Discord client ─────────────────────────────────────────────────────────────
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

_DELEGATE_CMD = "delegate"


# ── Events ─────────────────────────────────────────────────────────────────────

@bot.event
async def on_ready() -> None:
    assert bot.user is not None
    print(f"[Bot] Online  : {bot.user} (ID: {bot.user.id})")
    print(f"[Bot] Auth IDs: {config.AUTHORIZED_USER_IDS}")
    print(f"[Bot] Agents  : {config.AGENTS_DIR}")

    # ── Startup notification (channel) ────────────────────────────────────────
    if config.STARTUP_CHANNEL_ID:
        channel = bot.get_channel(config.STARTUP_CHANNEL_ID)
        if channel and hasattr(channel, "send"):
            await channel.send(  # type: ignore[union-attr]
                f"🟢 **ALFRED** está online e operacional.\n"
                f"Pronto para receber comandos via `@{bot.user.name} delegate alfred <tarefa>`."
            )

    # ── Startup DM to every authorized user ───────────────────────────────────
    for uid in config.AUTHORIZED_USER_IDS:
        try:
            # Try to find the member via shared guilds first (more reliable).
            member = None
            for guild in bot.guilds:
                member = guild.get_member(uid)
                if member:
                    break
            # Fallback to fetch_user if not found in cache.
            target = member or await bot.fetch_user(uid)
            await target.send(
                f"👋 **ALFRED aqui.**\n"
                f"Estou online e pronto para receber seus comandos no servidor.\n"
                f"Use `@{bot.user.name} delegate alfred <tarefa>` em qualquer canal."
            )
            print(f"[Bot] DM enviado para user ID {uid}")
        except Exception as exc:
            print(f"[Bot] Não foi possível enviar DM para user ID {uid}: {exc}")


@bot.event
async def on_message(message: discord.Message) -> None:
    # Never respond to our own messages.
    if message.author == bot.user:
        return

    assert bot.user is not None
    channel = message.channel
    author = message.author

    # ── Route reply to an active agent session ─────────────────────────────────
    session = runner.get_session(channel.id)
    if session and author.id == session.author_id:
        # Only route if the message is NOT a new bot command.
        if bot.user not in message.mentions:
            raw = message.content.strip()
            prefix = config.CHORD_PREFIX.strip()

            # Validate chord prefix (case-insensitive).
            if not raw.upper().startswith(prefix.upper()):
                await channel.send(
                    f"🔒 {author.mention} — resposta rejeitada. Autenticação necessária."
                )
                return

            # Strip the chord prefix and any leading whitespace before forwarding.
            payload = raw[len(prefix):].strip()
            await session.reply_queue.put(payload)
            return

    # ── All commands require an @mention ──────────────────────────────────────
    if bot.user not in message.mentions:
        return

    # ── Authorization ─────────────────────────────────────────────────────────
    if author.id not in config.AUTHORIZED_USER_IDS:
        await channel.send(f"🚫 {author.mention} — not authorized.")
        return

    # ── Parse: @Bot delegate <agent_id> <task> ────────────────────────────────
    # Strip the bot mention (both <@ID> and <@!ID> forms), then split.
    content = message.content
    for mention_str in (f"<@{bot.user.id}>", f"<@!{bot.user.id}>"):
        content = content.replace(mention_str, "")
    content = content.strip()

    parts = content.split(maxsplit=2)

    if len(parts) < 3 or parts[0].lower() != _DELEGATE_CMD:
        await channel.send(
            "**Usage:** `@Bot delegate <agent_id> <task>`\n"
            "**Example:** `@Bot delegate sample_agent analyze the error logs`"
        )
        return

    _, agent_id, task = parts[0], parts[1], parts[2]

    agent_path = runner.resolve_agent_path(agent_id)
    if agent_path is None:
        await channel.send(
            f"❌ Agent `{agent_id}` not found.\n"
            f"Expected file: `{config.AGENTS_DIR}/{agent_id}.py`"
        )
        return

    # Fire-and-forget; runner manages its own session lifecycle.
    asyncio.create_task(
        runner.execute(channel, author, agent_path, task)  # type: ignore[arg-type]
    )


# ── Entry point ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if not config.DISCORD_TOKEN:
        sys.exit("[Bot] DISCORD_TOKEN is missing — check your .env file.")
    bot.run(config.DISCORD_TOKEN)
