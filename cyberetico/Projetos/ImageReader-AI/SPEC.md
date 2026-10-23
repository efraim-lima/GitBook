---
description: Especificação do projeto ImageReader-AI — app Android (Java) para leitura de texto manuscrito em fotos via IA.
icon: camera
---

# ImageReader-AI — Especificação do Projeto

## 1. Visão geral

Aplicativo Android nativo (Java) que captura uma foto pela câmera do aparelho e
extrai o **texto manuscrito** presente na imagem usando reconhecimento por IA. O
resultado é um texto editável que o usuário pode revisar, copiar e compartilhar.

- **Plataforma:** Android nativo
- **Linguagem:** Java
- **minSdk:** 26 (Android 8.0 Oreo)
- **targetSdk:** 34 (Android 14) — recomendado manter no nível mais recente estável
- **Estratégia de IA:** híbrida (on-device por padrão, nuvem para maior precisão)

## 2. Objetivo

Permitir que o usuário fotografe uma anotação manuscrita (bilhete, quadro,
caderno, formulário preenchido à mão) e obtenha o conteúdo em texto digital
confiável, com opção de operar offline quando possível.

## 3. Escopo

### Dentro do escopo (MVP)
- Captura de foto pela câmera.
- Seleção de imagem existente da galeria.
- Pré-processamento da imagem (recorte, rotação, ajuste de contraste).
- Reconhecimento de texto manuscrito (OCR/HTR).
- Exibição do texto extraído em campo editável.
- Copiar para a área de transferência / compartilhar.
- Modo offline (on-device) e modo online (nuvem).

### Fora do escopo (v1)
- Tradução automática.
- Sincronização em nuvem / conta de usuário.
- Reconhecimento de escrita em tempo real (ink em tela).
- Múltiplos idiomas simultâneos além do padrão configurado.

## 4. Personas e casos de uso

| # | Caso de uso | Fluxo resumido |
|---|-------------|----------------|
| UC1 | Digitalizar bilhete manuscrito | Abrir app → câmera → foto → texto extraído → copiar |
| UC2 | Ler anotação sem internet | Modo offline → on-device HTR → texto (precisão reduzida) |
| UC3 | Ler manuscrito difícil | Modo online → envio à nuvem → texto de alta precisão |
| UC4 | Importar da galeria | Selecionar imagem → extrair texto |

## 5. Requisitos funcionais

- **RF01** — Capturar foto usando CameraX.
- **RF02** — Importar imagem da galeria (Photo Picker / SAF).
- **RF03** — Permitir recorte e rotação antes do reconhecimento.
- **RF04** — Executar reconhecimento on-device por padrão.
- **RF05** — Oferecer reconhecimento na nuvem quando o usuário solicitar ou quando a confiança on-device for baixa.
- **RF06** — Exibir o texto extraído em `EditText` editável.
- **RF07** — Copiar texto e compartilhar via `Intent.ACTION_SEND`.
- **RF08** — Indicar visualmente o nível de confiança / origem do resultado (on-device vs nuvem).
- **RF09** — Tratar ausência de internet degradando para on-device.
- **RF10** — Solicitar permissões de câmera em runtime.
- **RF11** — Enviar a imagem capturada, via requisição HTTP POST, a um **webhook n8n** que orquestra o reconhecimento por IA visual (Ollama). O endpoint deve ser configurável (ambiente local hoje, servidor futuramente).

## 6. Requisitos não funcionais

- **RNF01 — Desempenho:** reconhecimento on-device retorna em ≤ 3 s em aparelho médio.
- **RNF02 — Privacidade:** no modo offline nenhuma imagem sai do aparelho. No modo nuvem, avisar explicitamente que a imagem será enviada a serviço externo.
- **RNF03 — Segurança:** chaves de API nunca embutidas no APK em texto claro; usar backend proxy ou armazenamento seguro. Tráfego apenas HTTPS/TLS.
- **RNF04 — Usabilidade:** fluxo foto→texto em no máximo 3 toques.
- **RNF05 — Confiabilidade:** falha de rede não trava o app; sempre há fallback.
- **RNF06 — Compatibilidade:** funcional de API 26 a API 34.

## 7. Arquitetura

Padrão **MVVM** com camadas claras.

```
UI (Activities/Fragments)
   │  observa
ViewModel  ──►  UseCases (RecognizeTextUseCase)
   │
Repository (OcrRepository)
   ├── OnDeviceRecognizer   (ML Kit)
   └── CloudRecognizer      (API de visão / LLM via backend)
```

- **CameraX** para captura.
- **ML Kit Text Recognition v2** para o caminho on-device.
- **Retrofit + OkHttp** para o caminho de nuvem.
- **Room** (opcional) para histórico local de leituras.
- **WorkManager** para reprocessamento em segundo plano quando a rede voltar.

### Estratégia híbrida
1. Roda on-device primeiro.
2. Calcula confiança média dos blocos reconhecidos.
3. Se confiança < limiar (ex.: 0,6) **e** há internet **e** usuário permitiu nuvem → reenvia à nuvem.
4. Mostra o melhor resultado, marcando a origem.

## 8. Reconhecimento de texto manuscrito

Manuscrito ("handwriting"/HTR) é mais difícil que texto impresso. Opções:

| Camada | Tecnologia | Observação |
|--------|-----------|------------|
| On-device | ML Kit Text Recognition v2 | Bom para impresso; manuscrito legível funciona parcialmente. Offline, grátis. |
| On-device (alt.) | ML Kit Digital Ink | Feito para traços de caneta, não foto — só se houver captura de ink. |
| Nuvem | Google Cloud Vision (`DOCUMENT_TEXT_DETECTION`) | Forte em manuscrito. |
| Nuvem (LLM) | Modelo de visão (ex.: Claude / GPT-4o) | Excelente em manuscrito difícil e contexto; custo por chamada. |

**Recomendação MVP:** on-device com ML Kit v2 + nuvem com um modelo de visão LLM
(melhor qualidade em manuscrito). O acesso à nuvem deve passar por um **backend
proxy** próprio para proteger a chave de API.

## 9. Dependências (Gradle)

```gradle
// CameraX
implementation "androidx.camera:camera-camera2:1.3.x"
implementation "androidx.camera:camera-lifecycle:1.3.x"
implementation "androidx.camera:camera-view:1.3.x"

// ML Kit — reconhecimento de texto on-device
implementation "com.google.mlkit:text-recognition:16.0.x"

// Rede (caminho nuvem)
implementation "com.squareup.retrofit2:retrofit:2.11.x"
implementation "com.squareup.okhttp3:okhttp:4.12.x"

// Histórico local (opcional)
implementation "androidx.room:room-runtime:2.6.x"
```

## 10. Permissões (AndroidManifest)

```xml
<uses-permission android:name="android.permission.CAMERA"/>
<uses-permission android:name="android.permission.INTERNET"/>
<!-- Galeria: usar Photo Picker (sem permissão de armazenamento em API 33+) -->
```

## 11. Telas (UI)

1. **Home / Câmera** — visor CameraX, botão capturar, botão galeria, toggle offline/online.
2. **Recorte** — ajuste da imagem antes do OCR.
3. **Resultado** — texto editável, indicador de origem/confiança, botões copiar/compartilhar/reprocessar na nuvem.
4. **Configurações** — idioma, permitir nuvem, limpar histórico.

## 12. Segurança e privacidade

- Chave da API de nuvem **fora do APK** — usar backend proxy próprio.
- Consentimento explícito antes de enviar imagem à nuvem.
- Sem envio de imagem no modo offline.
- Comunicação somente TLS.
- Não persistir imagens sensíveis sem consentimento; permitir apagar histórico.

## 13. Testes

- **Unitários:** lógica de decisão híbrida (limiar de confiança), parsing de resposta da nuvem.
- **Instrumentados:** fluxo câmera→resultado (Espresso).
- **Manuais:** amostras de manuscrito variado (legível, cursivo, baixa luz).

## 14. Roadmap

| Fase | Entregas |
|------|----------|
| MVP | Câmera, OCR on-device, texto editável, copiar/compartilhar |
| v1.1 | Caminho de nuvem + backend proxy, decisão híbrida |
| v1.2 | Histórico (Room), recorte avançado, pré-processamento |
| v2.0 | Multi-idioma, tradução, exportar PDF |

## 15. Riscos

| Risco | Mitigação |
|-------|-----------|
| Precisão baixa em manuscrito on-device | Fallback para nuvem; orientar boa iluminação |
| Custo das chamadas de nuvem | Cache; usar nuvem só sob demanda/baixa confiança |
| Vazamento de chave de API | Backend proxy, nunca embutir no APK |
| Privacidade de imagens | Consentimento, modo offline padrão, apagar histórico |

## 16. Integração via webhook n8n + Ollama

O caminho de nuvem/servidor deste projeto **não** chama um provedor de IA
externo diretamente. Em vez disso, o app envia a imagem a um **webhook n8n**, que
orquestra o fluxo e delega o reconhecimento visual a um modelo do **Ollama**
rodando na máquina.

- **Hoje (local):** n8n e Ollama rodam na máquina do desenvolvedor. O app aponta
  para o IP local da máquina na rede (ex.: `http://192.168.x.x:5678/webhook/...`).
- **Depois (servidor):** o mesmo n8n + Ollama passam a rodar em um servidor
  dedicado; muda apenas a URL base configurada no app.

O contrato de entradas e saídas, o diagrama de componentes e os detalhes de
implantação estão documentados em [`ARQUITETURA.md`](ARQUITETURA.md).

### Modelo de IA (Ollama)
Prioriza **baixo consumo de armazenamento e processamento** com capacidade
visual. Recomendado: `moondream` (~1,7 GB, leve). Alternativas: `llava-phi3`,
`llama3.2-vision` (mais pesado, maior precisão).
