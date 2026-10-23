package com.efraim.imagereaderai;

import android.Manifest;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.camera.core.CameraSelector;
import androidx.camera.core.ImageCapture;
import androidx.camera.core.ImageCaptureException;
import androidx.camera.core.ImageProxy;
import androidx.camera.core.Preview;
import androidx.camera.lifecycle.ProcessCameraProvider;
import androidx.camera.view.PreviewView;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import com.google.common.util.concurrent.ListenableFuture;

import java.io.ByteArrayOutputStream;
import java.nio.ByteBuffer;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * Tela única: mostra o preview da câmera, captura uma foto e envia a imagem
 * ao webhook n8n (que delega a leitura à IA visual do Ollama). Exibe o texto
 * reconhecido retornado.
 */
public class MainActivity extends AppCompatActivity {

    private static final String TAG = "ImageReaderAI";
    private static final int REQ_CAMERA = 10;

    private PreviewView previewView;
    private TextView resultView;
    private Button captureButton;

    private ImageCapture imageCapture;
    private ExecutorService cameraExecutor;
    private WebhookClient webhookClient;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        previewView = findViewById(R.id.previewView);
        resultView = findViewById(R.id.resultView);
        captureButton = findViewById(R.id.captureButton);

        cameraExecutor = Executors.newSingleThreadExecutor();
        webhookClient = new WebhookClient(BuildConfig.WEBHOOK_URL);

        captureButton.setOnClickListener(v -> capturePhoto());

        if (hasCameraPermission()) {
            startCamera();
        } else {
            ActivityCompat.requestPermissions(this,
                    new String[]{Manifest.permission.CAMERA}, REQ_CAMERA);
        }
    }

    private boolean hasCameraPermission() {
        return ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
                == PackageManager.PERMISSION_GRANTED;
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions,
                                           @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == REQ_CAMERA
                && grantResults.length > 0
                && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
            startCamera();
        } else {
            Toast.makeText(this, R.string.camera_denied, Toast.LENGTH_LONG).show();
        }
    }

    private void startCamera() {
        ListenableFuture<ProcessCameraProvider> future =
                ProcessCameraProvider.getInstance(this);
        future.addListener(() -> {
            try {
                ProcessCameraProvider provider = future.get();

                Preview preview = new Preview.Builder().build();
                preview.setSurfaceProvider(previewView.getSurfaceProvider());

                imageCapture = new ImageCapture.Builder()
                        .setCaptureMode(ImageCapture.CAPTURE_MODE_MINIMIZE_LATENCY)
                        .build();

                provider.unbindAll();
                provider.bindToLifecycle(this, CameraSelector.DEFAULT_BACK_CAMERA,
                        preview, imageCapture);
            } catch (Exception e) {
                Log.e(TAG, "Falha ao iniciar câmera", e);
            }
        }, ContextCompat.getMainExecutor(this));
    }

    private void capturePhoto() {
        if (imageCapture == null) return;
        setBusy(true);
        resultView.setText(R.string.processing);

        imageCapture.takePicture(cameraExecutor, new ImageCapture.OnImageCapturedCallback() {
            @Override
            public void onCaptureSuccess(@NonNull ImageProxy image) {
                byte[] jpeg = toJpegBytes(image);
                image.close();
                sendToWebhook(jpeg);
            }

            @Override
            public void onError(@NonNull ImageCaptureException exception) {
                Log.e(TAG, "Erro na captura", exception);
                runOnUiThread(() -> {
                    resultView.setText(R.string.capture_error);
                    setBusy(false);
                });
            }
        });
    }

    /** ImageCapture entrega JPEG num único plano — extrai os bytes. */
    private byte[] toJpegBytes(@NonNull ImageProxy image) {
        ByteBuffer buffer = image.getPlanes()[0].getBuffer();
        byte[] bytes = new byte[buffer.remaining()];
        buffer.get(bytes);
        return bytes;
    }

    private void sendToWebhook(byte[] jpeg) {
        webhookClient.recognize(jpeg, new WebhookClient.Callback() {
            @Override
            public void onSuccess(String text) {
                runOnUiThread(() -> {
                    resultView.setText(text == null || text.isEmpty()
                            ? getString(R.string.empty_result) : text);
                    setBusy(false);
                });
            }

            @Override
            public void onFailure(String reason) {
                runOnUiThread(() -> {
                    resultView.setText(getString(R.string.request_error, reason));
                    setBusy(false);
                });
            }
        });
    }

    private void setBusy(boolean busy) {
        captureButton.setEnabled(!busy);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (cameraExecutor != null) cameraExecutor.shutdown();
    }
}
