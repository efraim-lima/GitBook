<html><head><title>Lista Funcionarios Duck Tech</title>
<meta http-equiv="Cache-Control" content="No-Cache">
</head><body>
<?php
$host		="localhost";
$username	="root";
$password	="";
$db_name	="duck_tech";
$con=mysqli_connect("$host", "$username", "$password", "$db_name") or die("cannot connect");
if (mysqli_connect_errno()) {
        echo "Falhou ao conectar ao MySQL: " . mysqli_connect_error();
        exit();
}
$sql = "select id, nome, cargo, email from funcionarios order by nome";
$result = mysqli_query($con,$sql);
if (!$result) {
        die("Erro na consulta: " . mysqli_error($con));
}else{
		while($row = mysqli_fetch_assoc($result)){
		    echo $row['id']." = ".$row['nome']." = ".$row['cargo']." = ".$row['email']."<br>";
		}
		echo "fim de listagem";
		mysqli_close($con);
}
?>
</table></body></html>
