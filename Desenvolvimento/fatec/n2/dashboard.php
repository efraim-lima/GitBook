<html><head><title>Duck Tech - Dashboard</title>
<meta http-equiv="Cache-Control" content="No-Cache">
</head><body>
<?php
session_start();
if (!isset($_SESSION["usuario"])){
    echo "Acesso negado. Faca o login primeiro.";
    echo "<a href='javascript:history.back()'>Voltar</a>";
    exit;
}
echo "Usuario: ".$_SESSION["usuario"]."<br>";
echo "Cargo: ".$_SESSION["cargo"]."<br>";
echo "Departamento: ".$_SESSION["departamento"]."<br>";
echo "<br><a href='logout.php'>Sair</a>";
?>
</body></html>
