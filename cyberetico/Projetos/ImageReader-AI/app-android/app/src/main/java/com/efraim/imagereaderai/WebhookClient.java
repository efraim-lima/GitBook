package com.efraim.imagereaderai;

import android.util.Base64;

import androidx.annotation.NonNull;

import org.json.JSONObject;

import java.io.IOException;
import java.util.UUID;
import java.util.concurrent.TimeUnit;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;
import okhttp3.ResponseBody;

/**
 * Cliente HTTP para o webhook n8n. Envia a imagem (JPEG em base64) e devolve
 * o texto reconhecido. Contrato descrito em ARQUITETURA.md, seção 3.
 */
public class WebhookClient {

    public interface Callback {
        void onSuccess(String text);
        void onFailure(String reason);
    }

    private static final MediaType JSON = MediaType.get("application/json; charset=utf-8");

    private final String webhookUrl;
    private final OkHttpClient http;

    public WebhookClient(String webhookUrl) {
        this.webhookUrl = webhookUrl;
        this.http = new OkHttpClient.Builder()
                .connectTimeout(15, TimeUnit.SECONDS)
                .readTimeout(60, TimeUnit.SECONDS)   // inferência do Ollama pode demorar
                .writeTimeout(30, TimeUnit.SECONDS)
                .build();
    }

    public void recognize(byte[] jpeg, @NonNull final Callback callback) {
        final String body;
        try {
            String b64 = Base64.encodeToString(jpeg, Base64.NO_WRAP);
            JSONObject payload = new JSONObject();
            payload.put("image_base64", b64);
            payload.put("mime", "image/jpeg");
            payload.put("lang", "por");
            payload.put("client", "android");
            payload.put("request_id", UUID.randomUUID().toString());
            body = payload.toString();
        } catch (Exception e) {
            callback.onFailure("payload_invalido");
            return;
        }

        Request request = new Request.Builder()
                .url(webhookUrl)
                .post(RequestBody.create(body, JSON))
                .build();

        http.newCall(request).enqueue(new okhttp3.Callback() {
            @Override
            public void onFailure(@NonNull Call call, @NonNull IOException e) {
                callback.onFailure("rede: " + e.getMessage());
            }

            @Override
            public void onResponse(@NonNull Call call, @NonNull Response response) {
                try (ResponseBody rb = response.body()) {
                    String raw = rb != null ? rb.string() : "";
                    if (!response.isSuccessful()) {
                        callback.onFailure("http_" + response.code());
                        return;
                    }
                    // Resposta esperada: { "status": "ok", "text": "..." }
                    // Fallback: aceita "response" (formato bruto do Ollama).
                    JSONObject json = new JSONObject(raw);
                    String text = json.optString("text",
                            json.optString("response", ""));
                    callback.onSuccess(text);
                } catch (Exception e) {
                    callback.onFailure("resposta_invalida");
                }
            }
        });
    }
}
