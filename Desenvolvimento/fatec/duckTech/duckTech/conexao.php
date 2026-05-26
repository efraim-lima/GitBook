<?php
$host = 'localhost';
$user = 'root';      // padrão XAMPP
$pass = '';          // padrão XAMPP (sem senha)
$db   = 'empresa';   // o banco que você acabou de criar

$conn = mysqli_connect($host, $user, $pass, $db);

if (!$conn) {
    die("Erro de conexão: " . mysqli_connect_error());
}
?>