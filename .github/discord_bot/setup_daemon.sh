#!/usr/bin/env bash
# setup_daemon.sh — Instala o Alfred Discord Bot como daemon no Linux.
#
# Estratégias suportadas (em ordem de preferência):
#   1. systemd --user  (mais robusto, gerencia restart e resume)
#   2. XDG Autostart   (.desktop em ~/.config/autostart/ — funciona sem terminal)
#   3. cron @reboot    (fallback mínimo)
#
# NOTA: Se rodando dentro de Flatpak/sandbox, os arquivos são escritos
# no filesystem real (~/) mas os comandos systemctl precisam ser executados
# em um terminal do SISTEMA (fora do Flatpak).
#
# Uso:
#   chmod +x setup_daemon.sh
#   ./setup_daemon.sh          # instala
#   ./setup_daemon.sh --remove # remove tudo

set -euo pipefail

# ── Paths ──────────────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOT_SCRIPT="$SCRIPT_DIR/bot.py"
PYTHON_BIN="${PYTHON_EXECUTABLE:-$(command -v python3 2>/dev/null || echo python3)}"
SERVICE_NAME="alfred-bot"
SERVICE_DIR="$HOME/.config/systemd/user"
SERVICE_FILE="$SERVICE_DIR/$SERVICE_NAME.service"
RESUME_FILE="$SERVICE_DIR/${SERVICE_NAME}-resume.service"
AUTOSTART_DIR="$HOME/.config/autostart"
AUTOSTART_FILE="$AUTOSTART_DIR/$SERVICE_NAME.desktop"
LOG_DIR="$HOME/.local/share/alfred-bot"

# ── Remove mode ────────────────────────────────────────────────────────────────
if [[ "${1:-}" == "--remove" ]]; then
    echo "[setup] Removendo daemon $SERVICE_NAME…"
    systemctl --user stop    "$SERVICE_NAME.service" 2>/dev/null || true
    systemctl --user disable "$SERVICE_NAME.service" 2>/dev/null || true
    rm -f "$SERVICE_FILE" "$RESUME_FILE" "$AUTOSTART_FILE"
    systemctl --user daemon-reload 2>/dev/null || true
    echo "[setup] Arquivos removidos."
    exit 0
fi

# ── Checks ─────────────────────────────────────────────────────────────────────
if [[ ! -f "$BOT_SCRIPT" ]]; then
    echo "[setup] ERRO: bot.py não encontrado em $BOT_SCRIPT" >&2
    exit 1
fi

mkdir -p "$LOG_DIR"

# ── Detecta ambiente ───────────────────────────────────────────────────────────
IN_FLATPAK=false
if [[ "$(cat /proc/1/comm 2>/dev/null)" == "bwrap" ]] || \
   [[ -n "${FLATPAK_ID:-}" ]] || \
   [[ "$(cat /etc/os-release 2>/dev/null)" == *"Flatpak"* ]]; then
    IN_FLATPAK=true
fi

HAS_SYSTEMCTL=false
command -v systemctl &>/dev/null && HAS_SYSTEMCTL=true

# ── Escreve service file systemd (sempre, mesmo sem systemctl disponível) ──────
mkdir -p "$SERVICE_DIR"

cat > "$SERVICE_FILE" <<EOF
[Unit]
Description=Alfred Discord Bot — Concierge Agent
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory=$SCRIPT_DIR
ExecStart=$PYTHON_BIN $BOT_SCRIPT
Restart=always
RestartSec=10
StandardOutput=append:$LOG_DIR/bot.log
StandardError=append:$LOG_DIR/bot.err

[Install]
WantedBy=default.target
EOF

# Serviço de resume após suspend
cat > "$RESUME_FILE" <<EOF
[Unit]
Description=Reinicia Alfred Bot após suspend/hibernate
After=suspend.target hibernate.target hybrid-sleep.target

[Service]
Type=oneshot
ExecStart=systemctl --user restart $SERVICE_NAME.service

[Install]
WantedBy=suspend.target hibernate.target hybrid-sleep.target
EOF

echo "[setup] ✅ Arquivos de serviço escritos em $SERVICE_DIR/"

# ── Ativa via systemctl se disponível ─────────────────────────────────────────
if $HAS_SYSTEMCTL; then
    systemctl --user daemon-reload
    loginctl enable-linger "$USER" 2>/dev/null || true
    systemctl --user enable "$SERVICE_NAME.service"
    systemctl --user enable "${SERVICE_NAME}-resume.service" 2>/dev/null || true
    systemctl --user stop   "$SERVICE_NAME.service" 2>/dev/null || true
    systemctl --user start  "$SERVICE_NAME.service"
    echo "[setup] ✅ systemd --user: serviço ativado e iniciado."
    echo "  Status  : systemctl --user status $SERVICE_NAME"
    echo "  Logs    : journalctl --user -u $SERVICE_NAME -f"
else
    # ── XDG Autostart (.desktop) ───────────────────────────────────────────────
    mkdir -p "$AUTOSTART_DIR"
    cat > "$AUTOSTART_FILE" <<EOF
[Desktop Entry]
Type=Application
Name=Alfred Discord Bot
Comment=ALFRED concierge agent — Discord middleware
Exec=$PYTHON_BIN $BOT_SCRIPT
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
EOF
    echo "[setup] ✅ XDG Autostart instalado em $AUTOSTART_FILE"
    echo "         O bot iniciará automaticamente no próximo login gráfico."
fi

# ── Instruções para ambiente Flatpak / sem systemctl no PATH ──────────────────
if $IN_FLATPAK; then
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo " AÇÃO NECESSÁRIA — Terminal do SISTEMA (fora do VS Code)"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo " O VS Code está rodando dentro de Flatpak. Execute estes"
    echo " comandos em um terminal normal (ex: GNOME Terminal, Konsole):"
    echo ""
    echo "   loginctl enable-linger \$USER"
    echo "   systemctl --user daemon-reload"
    echo "   systemctl --user enable alfred-bot.service"
    echo "   systemctl --user enable alfred-bot-resume.service"
    echo "   systemctl --user start alfred-bot.service"
    echo ""
    echo " Verificar depois:"
    echo "   systemctl --user status alfred-bot"
    echo "   journalctl --user -u alfred-bot -f"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
fi

echo ""
echo "[setup] Logs      : $LOG_DIR/"
echo "[setup] Configuração: $SCRIPT_DIR/.env"
echo "[setup] Remover   : $0 --remove"

