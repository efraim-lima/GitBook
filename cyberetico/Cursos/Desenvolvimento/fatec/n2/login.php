<html><head><title>Duck Tech - Login</title>
<meta http-equiv="Cache-Control" content="No-Cache">
<style>
body { background-color: #1C1526; color: #F2F2F2; padding: 30px; }
a { color: #F2A413; }
</style>
</head><body>
<?php
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
   if ($_POST["usuario"]!=""){
      if ((strrpos($_POST["usuario"],"drop")>0)||
          (strrpos($_POST["usuario"],"update")>0)||
          (strrpos($_POST["usuario"],"insert")>0)||
          (strrpos($_POST["usuario"],"delete")>0)||
          (strrpos($_POST["usuario"],"select")>0)){
             echo "Usuario Invalido";
             echo "<a href='javascript:history.back()'>Voltar</a>";
             exit;
      }
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
    $encontrou=0;
    while($row = mysqli_fetch_assoc($result)){
        $encontrou=1;
        echo "Usuario: ".$row['nome']."<br>";
        echo "Cargo: ".$row['cargo']."<br>";
        echo "Departamento: ".$row['departamento']."<br>";
    }
    if ($encontrou==0){
        echo "Usuario ou senha invalidos";
        echo "<a href='javascript:history.back()'>Voltar</a>";
    }
    mysqli_close($con);
}
?>
</body></html>
