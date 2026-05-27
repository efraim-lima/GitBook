<html><head><title>Duck Tech - Login</title>
<meta http-equiv="Cache-Control" content="No-Cache">
</head><body>
<?php
session_start();
function processa_login(){
   if ($_POST["usuario"]==""){
      echo "Usuario incorreto";
      echo "<a href='javascript:history.back()'>Voltar</a>";
      exit;
   }
   if ($_POST["senha"]==""){
      echo "Senha incorreta";
      echo "<a href='javascript:history.back()'>Voltar</a>";
      exit;
   }
}
if ((isset($_POST["usuario"]))&&(isset($_POST["senha"]))){
    processa_login();
}
?>

<?php
$usuario =$_POST["usuario"];
$senha   =$_POST["senha"];
$sql="select id, nome, cargo, departamento from funcionarios where usuario='".$usuario."' and senha='".$senha."'";

$host    ="localhost";
$username="root";
$password="";
$db_name ="duck_tech";
$con=mysqli_connect("$host", "$username", "$password", "$db_name") or die("cannot connect");
if (mysqli_connect_errno()) {
        echo "Falhou ao conectar ao MySQL: " . mysqli_connect_error();
        exit();
}
$result = mysqli_query($con,$sql);
if (!$result) {
        die("Erro na consulta: " . mysqli_error($con));
}else{
    if(mysqli_num_rows($result)>0){
        $row = mysqli_fetch_assoc($result);
        $_SESSION["usuario"]      = $row["nome"];
        $_SESSION["cargo"]        = $row["cargo"];
        $_SESSION["departamento"] = $row["departamento"];
        mysqli_close($con);
        header("Location: dashboard.php");
        exit;
    }else{
        mysqli_close($con);
        echo "Usuario ou senha invalidos";
        echo "<a href='javascript:history.back()'>Voltar</a>";
        exit;
    }
}
?>
</body></html>
