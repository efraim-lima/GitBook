#!/bin/bash

# Garante que o script seja executado com privilégios de superusuário
if [ "$EUID" -ne 0 ]; then
  echo "Por favor, execute como root (sudo ./setup_inicial.sh)"
  exit 1
fi

echo "=== INICIANDO PROCESSO DE PÓS-INSTALAÇÃO E CONFIGURAÇÃO AVANÇADA ==="

# 1. Atualização Base e Dependências Críticas
echo "[1/11] Atualizando repositórios e instalando dependências base..."
apt-get update -y && apt-get upgrade -y
apt-get install -y curl wget gpg apt-transport-https software-properties-common flatpak psmisc git zsh htop

# 2. Instalação via APT (Repositórios Oficiais)
echo "[2/11] Instalando pacotes nativos..."
apt-get install -y python3 python3-pip virtualbox virtualbox-ext-pack tmux

# 3. Instalação do Docker
echo "[3/11] Instalando Docker Engine..."
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
rm get-docker.sh
usermod -aG docker "$SUDO_USER"

# 4. Instalação do Ollama
echo "[4/11] Instalando Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

# 5. Instalação do Visual Studio Code
echo "[5/11] Configurando repositório e instalando VS Code..."
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | tee /etc/apt/sources.list.d/vscode.list > /dev/null
rm -f packages.microsoft.gpg
apt-get update -y && apt-get install code -y

# 6. Instalação do Navegador Vivaldi
echo "[6/11] Instalando Vivaldi Browser..."
wget -qO- https://repo.vivaldi.com/archive/linux_signing_key.pub | gpg --dearmor | dd of=/usr/share/keyrings/vivaldi-browser.gpg
echo "deb [signed-by=/usr/share/keyrings/vivaldi-browser.gpg arch=$(dpkg --print-architecture)] https://repo.vivaldi.com/archive/deb/ stable main" | tee /etc/apt/sources.list.d/vivaldi.list
apt-get update -y && apt-get install vivaldi-stable -y

# 7. Instalação do Proton VPN
echo "[7/11] Configurando repositório e instalando Proton VPN..."
wget -q -O protonvpn-stable.deb https://repo.protonvpn.com/debian/dists/stable/main/binary-all/protonvpn-stable-release_1.0.3-3_all.deb
dpkg -i protonvpn-stable.deb
rm protonvpn-stable.deb
apt-get update -y && apt-get install proton-vpn-gnome-desktop -y

# 8. Instalações Isoladas via Flatpak (Obsidian e Teams)
echo "[8/11] Configurando Flathub e instalando Flatpaks..."
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install flathub md.obsidian.Obsidian -y
flatpak install flathub com.github.IsmaelMartinez.teams_for_linux -y

# 9. Configuração do Ambiente de Shell (Zsh + Oh My Zsh)
echo "[9/11] Configurando Zsh e Oh My Zsh para o usuário $SUDO_USER..."
chsh -s "$(which zsh)" "$SUDO_USER"
sudo -u "$SUDO_USER" sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# 10. Criação do Daemon Systemd para Atualização em Segundo Plano (Boot)
echo "[10/11] Provisionando daemon de atualização do APT em segundo plano..."
cat << 'EOF' > /etc/systemd/system/apt-update-boot.service
[Unit]
Description=Atualiza a lista de pacotes do APT no boot defensivo
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/bin/bash -c 'while fuser /var/lib/dpkg/lock-frontend >/dev/null 2>&1; do sleep 5; done; apt-get update'
RemainAfterExit=true

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable apt-update-boot.service
systemctl start apt-update-boot.service

# 11. Arquitetura de Painéis Avançados do Tmux (Autostart Gráfico)
echo "[11/11] Construindo scripts de automação do Tmux Dashboard..."

# Criação do script gerenciador de sessões e janelas do Tmux
TARGET_SCRIPT="/usr/local/bin/iniciar_paineis_soc.sh"
cat << 'EOF' > "$TARGET_SCRIPT"
#!/bin/bash
# Aguarda a completa estabilização do ambiente gráfico de usuário
sleep 5

# --- CONFIGURAÇÃO DA SESSÃO 1: SessaoSOC ---
tmux new-session -d -s SessaoSOC -n 'Monitoramento' 'while fuser /var/lib/dpkg/lock-frontend >/dev/null 2>&1; do sleep 2; done; sudo apt-get update; exec zsh'

# Divisões para htop e sockets ativos
tmux split-window -h -t SessaoSOC:0 'htop'
tmux split-window -v -t SessaoSOC:0.1 'watch -n 2 "sudo ss -tunap"'

# Divisões para controle de usuários e permissões de arquivos modificados
tmux split-window -v -t SessaoSOC:0.0 'watch -n 15 "echo \"=== USUARIOS DA MAQUINA ===\"; getent passwd {1000..60000} | cut -d: -f1,3,7; echo \"\n=== PERMISSOES HOME ===\"; ls -la /home/"'
tmux split-window -v -t SessaoSOC:0.2 'watch -n 10 "echo \"=== ULTIMOS ARQUIVOS MODIFICADOS ===\"; find /home -type f -mmin -60 -printf \"%T+ %p\n\" 2>/dev/null | sort -r | head -n 20"'

tmux select-layout -t SessaoSOC tiled

# --- CONFIGURAÇÃO DA SESSÃO 2: SessaoLogs ---
# Janela 1: Logs nominais e de serviços vinculados a ações de usuários
tmux new-session -d -s SessaoLogs -n 'Auditoria' 'sudo journalctl -f -t sudo -t su -t sshd -t systemd-logind 2>/dev/null'

# Janela 2: Logs de criticidade Warning, Critical ou Alertas explícitos
tmux split-window -h -t SessaoLogs:0 'sudo journalctl -f -p 0..4'

# Janela 3: Logs de modificações do ambiente via sockets ou mutações de arquivos
tmux split-window -v -t SessaoLogs:0.1 'sudo journalctl -f --grep="socket|bind|connect|chmod|chown|rm " 2>/dev/null'

tmux select-layout -t SessaoLogs tiled

# Invocação dos emuladores de terminal vinculando as sessões construídas
gnome-terminal --title="SOC Dashboard" -- tmux attach-session -t SessaoSOC &
gnome-terminal --title="SOC Telemetria de Logs" -- tmux attach-session -t SessaoLogs &
EOF

chmod +x "$TARGET_SCRIPT"

# Vinculação no protocolo XDG Autostart para execução no login do usuário comum
AUTOSTART_DIR="/home/$SUDO_USER/.config/autostart"
sudo -u "$SUDO_USER" mkdir -p "$AUTOSTART_DIR"

cat << EOF > "$AUTOSTART_DIR/tmux-dashboard.desktop"
[Desktop Entry]
Type=Application
Exec=$TARGET_SCRIPT
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=SOC Dashboard Tmux
Comment=Inicia automação de painéis operacionais e auditoria de logs
EOF

chown "$SUDO_USER:$SUDO_USER" "$AUTOSTART_DIR/tmux-dashboard.desktop"

echo "=== PROVISIONAMENTO CONCLUÍDO COM SUCESSO! REINICIE O SISTEMA ==="