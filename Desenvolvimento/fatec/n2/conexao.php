<html><head><title>Conexao Duck Tech</title>
<meta http-equiv="Cache-Control" content="No-Cache">
</head><body>
<?php
$host    ="localhost";
$username="root";
$password="";
$db_name ="duck_tech";
$con=mysqli_connect("$host", "$username", "$password", "$db_name") or die("cannot connect");
if (mysqli_connect_errno()) {
        echo "Falhou ao conectar ao MySQL: " . mysqli_connect_error();
        exit();
}
?>
</body></html>
