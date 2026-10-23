# ImageReader-AI — App Android (scaffold MVP)

App Android nativo (Java) que captura uma foto da câmera e envia a imagem a um
**webhook n8n**, que delega a leitura do texto manuscrito à IA visual do
**Ollama** rodando na sua máquina.

> Escopo deste scaffold: **apenas** capturar a imagem da câmera e enviá-la à IA
> visual. Reconhecimento, orquestração e prompt ficam no n8n/Ollama.
> Arquitetura completa em [`../ARQUITETURA.md`](../ARQUITETURA.md).

## Estrutura

```
app-android/
├── settings.gradle
├── build.gradle
├── gradle.properties
└── app/
    ├── build.gradle
    └── src/main/
        ├── AndroidManifest.xml
        ├── java/com/efraim/imagereaderai/
        │   ├── MainActivity.java      # câmera (CameraX) + captura + UI
        │   └── WebhookClient.java     # POST da imagem ao webhook n8n
        └── res/
            ├── layout/activity_main.xml
            └── values/{strings,themes}.xml
```

## Pré-requisitos

- Android Studio (ou Gradle 8.7+ e Android SDK 34).
- Aparelho/emulador Android 8.0+ (API 26).
- Ollama e n8n rodando na máquina (ver `../ARQUITETURA.md`).

## Configuração da URL do webhook

Definida em `app/build.gradle` via `buildConfigField "WEBHOOK_URL"`:

- **Emulador:** `http://10.0.2.2:5678/webhook/imagereader` (10.0.2.2 = host).
- **Aparelho físico:** trocar para o IP da sua máquina na LAN, ex.:
  `http://192.168.0.10:5678/webhook/imagereader` (mesma rede Wi-Fi).

> `usesCleartextTraffic="true"` está ligado para permitir HTTP local. Ao migrar
> para servidor, use HTTPS e remova essa flag.

## Build e execução

```bash
# gerar o gradle wrapper na primeira vez (se não usar o Android Studio)
gradle wrapper --gradle-version 8.7

# compilar o APK de debug
./gradlew assembleDebug

# instalar em um aparelho/emulador conectado
./gradlew installDebug
```

Ou abrir a pasta `app-android/` no Android Studio e rodar (Run ▶).

## O que o app faz

1. Mostra o preview da câmera (CameraX).
2. Ao tocar em **Capturar e ler**, tira a foto (JPEG).
3. Codifica em base64 e faz `POST` ao webhook n8n.
4. Exibe o texto retornado pelo Ollama.

## Próximos passos (fora deste scaffold)

- Construir o fluxo n8n (webhook → Ollama `moondream`) — ver `../ARQUITETURA.md`.
- Recorte/rotação antes do envio.
- Modo offline (ML Kit) e decisão híbrida — ver `../SPEC.md`.
- Tela de configurações para a URL base.
