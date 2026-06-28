<?php
// logout.php - Destroi a sessão e redireciona para a página principal
session_start();
session_destroy();

// Redireciona para o menu principal (fora dos iframes)
// Usamos JavaScript para garantir que a página toda seja recarregada
echo "<!DOCTYPE html>";
echo "<html>";
echo "<head>";
echo "<meta charset='UTF-8'>";
echo "<title>Saindo...</title>";
echo "</head>";
echo "<body>";
echo "<script>";
echo "window.top.location.href = 'index.html';"; // Força recarregar a janela principal
echo "</script>";
echo "</body>";
echo "</html>";
exit;
?>