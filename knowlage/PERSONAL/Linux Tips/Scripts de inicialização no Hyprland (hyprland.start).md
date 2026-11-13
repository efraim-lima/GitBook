# Scripts de inicialização no Hyprland (hyprland.start)
#linux #hyprland #wayland #dotfiles #lua #teclado #automação #CLI

Este guia documenta o padrão para criar **scripts que ajustam o Hyprland em runtime** no boot da sessão — úteis sempre que a configuração *declarativa* não dá conta (ou não aplica retroativamente) e você precisa rodar um `hyprctl` de verdade depois que a sessão sobe.

O exemplo trabalhado é o que motivou a nota: forçar um **teclado wireless US** para o grupo de layout `us`, enquanto o teclado embutido ABNT2 do laptop continua no `br`.

## Quando usar este padrão

Este setup usa a **configuração nativa em Lua do Hyprland** (0.55+), onde existe um objeto global `hl` (`hl.config{}`, `hl.bind()`, `hl.dsp.*`, `hl.on()`, `hl.exec_cmd()`). A regra de bolso:

- **Dá para declarar?** Prefira `hl.config{}` (ex.: `input`, `general`, `decoration`, regras de janela).
- **Precisa de uma ação em runtime** que o config declarativo não expressa, ou que só vale depois que um dispositivo/monitor aparece? → **script + hook no `hyprland.start`**.

Um caso concreto onde o declarativo *falha*: o bloco `device{}` no Lua nativo **não aplica retroativamente** a dispositivos já conectados. Setar `kb_layout` por dispositivo ali não muda um teclado que já estava plugado. A solução confiável é chamar `hyprctl switchxkblayout` via script.

## Passo a passo

### 1. Descobrir o nome exato do dispositivo

Use o JSON do `hyprctl` — é estável e fácil de filtrar:

```bash
hyprctl devices -j | jq -r '.keyboards[] | "\(.name) | main=\(.main) | \(.active_keymap)"'
```

Atenção: um mesmo periférico costuma expor **vários nós** (consumer-control, system-control, virtuais). O que importa é o de `main=true`. No caso do receptor wireless, o nome útil era `hs6209-2.4g-wireless-receiver-keyboard` (e não o irmão `...-receiver` sem `-keyboard`).

### 2. Entender o índice do layout

O layout global aqui é `kb_layout = "br,us"`, ou seja uma **lista indexada**: índice `0 = br`, índice `1 = us`. O comando que troca o layout de **um dispositivo específico** é:

```bash
hyprctl switchxkblayout <device> <índice>   # ou: next | prev
```

Então `hyprctl switchxkblayout hs6209-2.4g-wireless-receiver-keyboard 1` joga só aquele teclado para `us`. Se você mudar a ordem do `kb_layout` global, o índice muda junto — documente essa suposição no script.

### 3. Escrever o script

Boas práticas que valem para qualquer script deste tipo:

- **`set -euo pipefail`** para falhar cedo e de forma previsível.
- **Retry na enumeração**: no boot (e no hotplug) o dispositivo pode ainda não existir quando o `hyprland.start` dispara. Repita algumas vezes com `sleep`.
- **Sair com `exit 0` quando o dispositivo não existe** (desligado/desconectado) — não é erro, e evita poluir o log da sessão.
- **Idempotência**: rodar o script duas vezes deve dar o mesmo resultado.

Exemplo real (`~/.config/hypr/scripts/kb-layout-per-device.sh`):

```bash
#!/usr/bin/env bash
set -euo pipefail

DEVICE="hs6209-2.4g-wireless-receiver-keyboard"
US_INDEX=1          # índice do `us` dentro do kb_layout global "br,us"
RETRIES=10          # enquanto o teclado é enumerado no boot/hotplug
SLEEP=1

for _ in $(seq "$RETRIES"); do
    if hyprctl devices -j | grep -q "\"${DEVICE}\""; then
        hyprctl switchxkblayout "$DEVICE" "$US_INDEX"
        exit 0
    fi
    sleep "$SLEEP"
done
exit 0
```

Torne-o executável:

```bash
chmod +x ~/.config/hypr/scripts/kb-layout-per-device.sh
```

### 4. Pendurar no evento `hyprland.start`

No Lua nativo, `hl.on("hyprland.start", fn)` registra um callback para quando a sessão sobe, e `hl.exec_cmd` executa um comando. Adicione em um arquivo que já é `require`do (aqui foi o `input.lua`):

```lua
hl.on("hyprland.start", function()
    hl.exec_cmd(os.getenv("HOME") .. "/.config/hypr/scripts/kb-layout-per-device.sh")
end)
```

### 5. Testar sem deslogar

```bash
# roda o script na mão
~/.config/hypr/scripts/kb-layout-per-device.sh

# confere o resultado por dispositivo
hyprctl devices -j | jq -r '.keyboards[] | select(.name|test("hs6209.*keyboard|at-translated")) | "\(.name): \(.active_keymap)"'
```

Resultado esperado: o wireless em `English (US)` e o laptop em `Portuguese (Brazil)`.

> Observação: `hyprctl keyword ...` é **rejeitado** neste setup (`"keyword can't work with non-legacy parsers"`), porque o parser Lua nativo não é o legado. Para aplicar mudanças de config, edite os arquivos `.lua` (o framework recarrega ao salvar) ou use `hyprctl reload`. Já comandos de **ação** como `switchxkblayout`, `dispatch`, `switchxkblayout` seguem funcionando normalmente.

## Generalizando

O mesmo padrão (**script idempotente com retry + hook no `hyprland.start`**) serve para qualquer ajuste que o config declarativo não resolve de forma retroativa, por exemplo:

- Posicionar/ligar monitores que aparecem tarde (`hyprctl keyword monitor` → aqui via `dispatch`/script).
- Mover janelas de apps que sobem no autostart para workspaces específicos.
- Reaplicar estado de periféricos após suspensão/hotplug.

## Ressalva de manutenção

Os arquivos `input.lua`, `hyprland-gui.lua` e `conf/keybindings/default.lua` fazem parte dos **dotfiles ML4W** (e alguns são gerados por GUI). Um update desses dotfiles pode sobrescrever edições. Se isso acontecer, reaplique o `hl.on(...)` no `input.lua` e confirme que o script continua em `~/.config/hypr/scripts/`. Para blindar, considere mover customizações para um arquivo próprio (ex.: `~/.config/hypr/custom.lua`, que o `hyprland.lua` tenta carregar) que a ferramenta não toca.

## Arquivos relacionados

- Config de teclado: `~/.config/hypr/input.lua` (layout global `br,us`, toggle `grp:win_space_toggle` = Super+Space) e `~/.config/hypr/hyprland-gui.lua` (variant `abnt2`).
- Script: `~/.config/hypr/scripts/kb-layout-per-device.sh`.
