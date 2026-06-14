"""
alfred.py — ALFRED concierge agent for the Discord bot middleware.

Invoked by the bot as: python alfred.py "<task>"

I/O Protocol (same as all agents):
  sys.argv[1]          → task string passed by the bot
  stdout (normal line) → forwarded to Discord as plain output
  stdout 'QUESTION: …' → bot relays to Discord; user reply piped back to stdin
  stdin                → receives user replies (already chord-stripped by bot.py)
  stderr               → forwarded as a warning block after completion
  exit 0 / non-zero    → success / failure

Requires (in discord_bot/.env or environment):
  GITHUB_TOKEN        — GitHub personal access token (for GitHub Models API)
  ALFRED_MODEL        — model name (default: gpt-4o-mini)
  WORKSPACE_ROOT      — absolute path to the workspace root (default: parent of .github/)
"""
from __future__ import annotations

import datetime
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

# ── Load .env ─────────────────────────────────────────────────────────────────
_ENV_FILE = Path(__file__).parent / "discord_bot" / ".env"
try:
    from dotenv import load_dotenv
    load_dotenv(_ENV_FILE)
except ImportError:
    pass

# ── Config ────────────────────────────────────────────────────────────────────
GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN", "")
ALFRED_MODEL: str = os.getenv("ALFRED_MODEL", "gpt-4o-mini")
WORKSPACE_ROOT: Path = Path(
    os.getenv("WORKSPACE_ROOT", str(Path(__file__).parent.parent))
).resolve()
_NOTIFY_SCRIPT = Path(__file__).parent / "discord_bot" / "discord_notify.py"
_PYTHON_BIN = os.getenv("PYTHON_EXECUTABLE", sys.executable) or sys.executable

_API_URL = "https://models.inference.ai.azure.com/chat/completions"
_QUESTION_PREFIX = "QUESTION:"
_REPORT_MARKER = "# Activity Report"
_MAX_ROUNDS = 8


# ── Workspace helpers ─────────────────────────────────────────────────────────

def _read_safe(path: Path, max_chars: int = 4000) -> str:
    try:
        text = path.read_text(encoding="utf-8")
        if len(text) > max_chars:
            text = text[:max_chars] + "\n… [truncado]"
        return text
    except Exception:
        return ""


def _load_workspace_context() -> str:
    """Carrega Tasks.md e arquivos de contexto recentes para o prompt."""
    parts: list[str] = []

    # Tasks.md — tenta Work/Tasks.md e Tarefas.md
    for candidate in [
        WORKSPACE_ROOT / "Work" / "Tasks.md",
        WORKSPACE_ROOT / "Tarefas.md",
    ]:
        if candidate.exists():
            content = _read_safe(candidate)
            parts.append(f"### {candidate.relative_to(WORKSPACE_ROOT)}\n```\n{content}\n```")
            break

    # Últimos 3 arquivos de contexto modificados
    context_dir = WORKSPACE_ROOT / "Work" / "context"
    if context_dir.exists():
        recent = sorted(
            context_dir.glob("*.md"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )[:3]
        for cf in recent:
            content = _read_safe(cf, 2000)
            parts.append(f"### context/{cf.name}\n```\n{content}\n```")

    return "\n\n".join(parts) if parts else "_Nenhum contexto de workspace encontrado._"


def _save_report(content: str) -> Path | None:
    """Salva relatório em reports/YYYY/MM/DD_report.md e retorna o caminho."""
    today = datetime.date.today()
    report_dir = WORKSPACE_ROOT / "reports" / str(today.year) / f"{today.month:02d}"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"{today.isoformat()}_report.md"
    try:
        report_path.write_text(content, encoding="utf-8")
        return report_path
    except Exception as exc:
        print(f"[alfred] Erro ao salvar relatório: {exc}", file=sys.stderr)
        return None


def _notify_discord(text: str) -> None:
    """Envia mensagem diretamente ao Discord via discord_notify.py."""
    if not _NOTIFY_SCRIPT.exists():
        return
    try:
        subprocess.run(
            [_PYTHON_BIN, str(_NOTIFY_SCRIPT), text],
            timeout=20,
            check=False,
        )
    except Exception as exc:
        print(f"[alfred] Falha no discord_notify: {exc}", file=sys.stderr)


# ── System prompt ─────────────────────────────────────────────────────────────

def _build_system_prompt(workspace_ctx: str) -> str:
    today = datetime.date.today().isoformat()
    return f"""Você é ALFRED, agente concierge e orquestrador principal do workspace de Efraim Lima.

Data de hoje: {today}
Workspace: {WORKSPACE_ROOT}

## Identidade
- Nome: ALFRED
- Papel: Concierge e Orquestrador de Workflow
- Língua padrão: pt-BR

## Contexto do Workspace
{workspace_ctx}

## Regras de Operação

### Delegação
| Tipo de Tarefa | Agente |
|---|---|
| Desenvolvimento, scripts, automação, engenharia de dados, revisão de código | **CLAUDIO** |
| Design, apresentações, slides, formatação visual | **DESIRE** |
| Segurança da informação, pentest, compliance, auditoria, análise de vulnerabilidades | **SEVERINO** |

NÃO execute desenvolvimento ou design diretamente. Sempre delegue ao especialista correto.

### Decisões Críticas
Quando uma decisão crítica/irreversível for necessária:
1. Suspend a execução.
2. Envie uma pergunta de aprovação via protocolo QUESTION:.
3. NÃO prossiga até o usuário responder com **APPROVED**.

### Protocolo de Perguntas
- Quando precisar de esclarecimento ou aprovação, prefixe com exatamente: QUESTION: <pergunta>
- Apenas UMA pergunta por resposta.

### Relatórios
Ao concluir um ciclo de workflow, gere um relatório neste formato exato:

# Activity Report — {today}

## Resumo
{{Uma frase descrevendo o ciclo concluído.}}

## Tarefas Processadas
| Tarefa | Agente | Status | Fonte |
|--------|--------|--------|-------|

## Decisões Tomadas
{{Lista de decisões com fonte.}}

## Decisões Pendentes
{{Decisões aguardando APPROVED.}}

## Próximas Ações
{{Próximos passos concretos com agente responsável.}}

### Padrões de Escrita
- Terceira pessoa ou construções impessoais
- Sem primeira pessoa, sem julgamentos de valor
- Cite sempre a fonte de cada afirmação técnica
"""


# ── Connectivity ──────────────────────────────────────────────────────────────

def _check_internet() -> bool:
    try:
        urllib.request.urlopen("https://api.github.com", timeout=5)
        return True
    except Exception:
        return False


# ── LLM call ──────────────────────────────────────────────────────────────────

def _call_llm(messages: list[dict]) -> str:
    if not GITHUB_TOKEN:
        return (
            "⚠️ `GITHUB_TOKEN` não encontrado.\n"
            "Adicione ao `discord_bot/.env`:\n```\nGITHUB_TOKEN=seu_token_aqui\n```"
        )

    payload = json.dumps({
        "model": ALFRED_MODEL,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 2048,
    }).encode("utf-8")

    req = urllib.request.Request(
        _API_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"].strip()
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return f"❌ Erro da API ({exc.code}): {body[:400]}"
    except Exception as exc:
        return f"❌ Falha na requisição: {exc}"


# ── Output ────────────────────────────────────────────────────────────────────

def _emit(text: str) -> None:
    print(text, flush=True)


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    if len(sys.argv) < 2:
        print("ERRO: nenhuma tarefa fornecida.", file=sys.stderr)
        sys.exit(1)

    task: str = sys.argv[1]

    # Verifica conectividade
    if not _check_internet():
        _emit("🔴 **ALFRED** sem conexão com a internet. Verifique a rede.")
        sys.exit(1)

    _emit("🟢 **ALFRED** online — carregando contexto do workspace…")

    # Carrega contexto do workspace
    workspace_ctx = _load_workspace_context()
    system_prompt = _build_system_prompt(workspace_ctx)

    _emit("📋 Contexto carregado. Processando tarefa…")

    messages: list[dict] = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": task},
    ]

    report_content: str | None = None

    for _ in range(_MAX_ROUNDS):
        response = _call_llm(messages)

        # Detecta protocolo QUESTION: (pode estar em qualquer posição)
        if _QUESTION_PREFIX in response:
            parts = response.split(_QUESTION_PREFIX, 1)
            pre_text = parts[0].strip()
            question_text = parts[1].strip()

            if pre_text:
                _emit(pre_text)

            # Protocolo QUESTION: — runner.py retransmite ao Discord e
            # encaminha a resposta (já sem o chord prefix) de volta ao stdin.
            _emit(f"{_QUESTION_PREFIX} {question_text}")

            user_reply = sys.stdin.readline().strip()
            if not user_reply:
                _emit("_(sem resposta — encerrando diálogo)_")
                break

            messages.append({"role": "assistant", "content": response})
            messages.append({"role": "user", "content": user_reply})
            continue

        # Resposta final — emite e verifica se contém relatório
        _emit(response)

        if _REPORT_MARKER in response:
            # Extrai conteúdo do relatório a partir do marcador
            report_start = response.index(_REPORT_MARKER)
            report_content = response[report_start:]

        break

    else:
        _emit("⚠️ Número máximo de rodadas de clarificação atingido.")

    # Salva e notifica relatório se foi gerado
    if report_content:
        report_path = _save_report(report_content)
        if report_path:
            _emit(f"\n📁 Relatório salvo em `{report_path.relative_to(WORKSPACE_ROOT)}`")
            # Envia diretamente ao canal Discord (fora do stdout do subprocess)
            _notify_discord(
                f"📊 **Relatório ALFRED — {datetime.date.today().isoformat()}**\n\n"
                + report_content[:1800]
            )


if __name__ == "__main__":
    main()
