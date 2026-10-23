---
description: Arquitetura do ImageReader-AI — app Android → webhook n8n → Ollama (IA visual). Entradas, saídas e implantação local/servidor.
icon: sitemap
---

# ImageReader-AI — Arquitetura

Documento de arquitetura do fluxo de reconhecimento de texto manuscrito:
**App Android → Webhook n8n → Ollama (modelo de visão)**.

## 1. Visão de componentes

```
┌────────────────────┐        HTTP POST (JSON)        ┌────────────────────┐
│   App Android      │  multipart/base64 da imagem    │      n8n           │
│   (Java, CameraX)  │ ─────────────────────────────► │  (Webhook node)    │
│                    │                                 │                    │
│  captura foto      │                                 │  1. recebe imagem  │
│  envia ao webhook  │ ◄───────────────────────────── │  2. monta prompt   │
│  exibe texto       │        HTTP 200 (JSON)          │  3. chama Ollama   │
└────────────────────┘        { "text": ... }          │  4. devolve texto  │
                                                        └─────────┬──────────┘
                                                                  │ HTTP local
                                                                  ▼
                                                        ┌────────────────────┐
                                                        │      Ollama        │
                                                        │  /api/generate     │
                                                        │  modelo: moondream │
                                                        │  (visão, leve)     │
                                                        └────────────────────┘
```

### Papéis
- **App Android** — captura a foto, codifica a imagem e faz um POST ao webhook. Apenas cliente HTTP; não conhece o Ollama.
- **n8n** — orquestrador. Recebe a imagem, monta o prompt de OCR/HTR, chama o Ollama, trata erros e devolve JSON limpo ao app.
- **Ollama** — servidor de inferência local. Roda um modelo de visão leve (`moondream`) e retorna o texto reconhecido.

## 2. Ambientes

| Fase | n8n | Ollama | URL base no app |
|------|-----|--------|-----------------|
| **Local (hoje)** | máquina do dev, porta `5678` | máquina do dev, porta `11434` | `http://<IP-LAN-da-maquina>:5678` |
| **Servidor (futuro)** | servidor dedicado | servidor dedicado (ou host) | `https://<dominio-ou-ip-do-servidor>` |

> No modo local, o celular e a máquina precisam estar **na mesma rede Wi-Fi**.
> Usar o IP da LAN da máquina (ex.: `192.168.0.10`), nunca `localhost`
> (que, no celular, aponta para o próprio aparelho).

## 3. Contrato da API (App ↔ n8n)

### Requisição — App → Webhook n8n

- **Método:** `POST`
- **URL:** `{BASE_URL}/webhook/imagereader`
- **Content-Type:** `application/json`

```json
{
  "image_base64": "<imagem JPEG codificada em base64>",
  "mime": "image/jpeg",
  "lang": "por",
  "client": "android",
  "request_id": "uuid-v4-gerado-no-app"
}
```

Alternativa (recomendada para imagens grandes): `multipart/form-data` com o campo
`file` contendo o binário JPEG — evita o overhead de ~33% do base64.

### Resposta — Webhook n8n → App

- **Sucesso:** `HTTP 200`

```json
{
  "status": "ok",
  "text": "conteúdo manuscrito reconhecido",
  "model": "moondream",
  "request_id": "uuid-v4-ecoado",
  "elapsed_ms": 2140
}
```

- **Erro:** `HTTP 4xx/5xx`

```json
{
  "status": "error",
  "reason": "modelo_indisponivel | imagem_invalida | timeout",
  "request_id": "uuid-v4-ecoado"
}
```

## 4. Contrato interno (n8n ↔ Ollama)

O n8n chama o Ollama via HTTP Request node.

### Requisição — n8n → Ollama

- **Método:** `POST`
- **URL:** `http://localhost:11434/api/generate` (Ollama na mesma máquina do n8n)

```json
{
  "model": "moondream",
  "prompt": "Extraia fielmente todo o texto manuscrito desta imagem. Responda apenas com o texto, sem comentários.",
  "images": ["<mesma imagem em base64>"],
  "stream": false
}
```

### Resposta — Ollama → n8n

```json
{
  "model": "moondream",
  "response": "texto reconhecido...",
  "done": true
}
```

O n8n extrai `response`, envelopa no contrato da seção 3 e devolve ao app.

## 5. Fluxo n8n (nós)

1. **Webhook** (`POST /webhook/imagereader`) — recebe a imagem.
2. **Function / Set** — valida payload, monta o prompt e o corpo do Ollama.
3. **HTTP Request** — chama `http://localhost:11434/api/generate`.
4. **Function / Set** — extrai `response`, formata a resposta final.
5. **Respond to Webhook** — retorna o JSON de saída (seção 3).
6. (Opcional) **Error Trigger / IF** — trata timeout e modelo indisponível.

## 6. Entradas e saídas (resumo)

| Fronteira | Entrada | Saída |
|-----------|---------|-------|
| App → n8n | imagem (base64/multipart) + metadados | — |
| n8n → app | — | texto reconhecido + status |
| n8n → Ollama | modelo + prompt + imagem | — |
| Ollama → n8n | — | texto bruto (`response`) |

## 7. Modelo de IA — escolha por baixo consumo

| Modelo Ollama | Tamanho aprox. | Uso de recurso | Nota |
|---------------|----------------|----------------|------|
| **moondream** | ~1,7 GB | **baixo** | Recomendado para o MVP. Visão leve. |
| llava-phi3 | ~2,9 GB | médio | Boa qualidade, ainda enxuto. |
| llama3.2-vision:11b | ~7,9 GB | alto | Maior precisão, exige mais RAM/GPU. |

Instalação do modelo recomendado:

```bash
ollama pull moondream
```

## 8. Requisitos de rede e segurança

- **Local:** app e máquina na mesma LAN; liberar a porta `5678` (n8n) no firewall da máquina.
- **Servidor (futuro):**
  - Expor o n8n atrás de **HTTPS/TLS** (proxy reverso: Nginx/Caddy).
  - Autenticação no webhook (token/header secreto) para impedir uso externo.
  - Não expor o Ollama (`11434`) publicamente — apenas o n8n o acessa, na rede interna.
- Ollama processa **localmente**; nenhuma imagem sai para provedores de IA de terceiros.

## 9. Configuração no app

A URL base é configurável (não fixa no código). No scaffold, o valor padrão vem
de `WEBHOOK_URL` em `app/build.gradle` (campo `buildConfigField`), sobrescrevível
em tempo de build ou em uma tela de configurações futura.

## 10. Evolução

| Fase | Mudança arquitetural |
|------|----------------------|
| MVP local | App → n8n local → Ollama local |
| Servidor | Mesmo fluxo, n8n+Ollama no servidor, HTTPS + auth no webhook |
| Escala | Fila (ex.: n8n + worker), cache de resultados, múltiplos modelos por confiança |
