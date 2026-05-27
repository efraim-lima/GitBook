<html><head><title>Cadastro Duck Tech</title>
<meta http-equiv="Cache-Control" content="No-Cache">
</head><body>
<?php
function processa_formulário(){
   if ($_POST["nome"]==""){
      echo "Nome incorreto";
      echo "<a href='javascript:history.back()'>Voltar</a>";
      exit;
   }
   if ($_POST["endereco"]==""){
      echo "Endereco incorreto";
      echo "<a href='javascript:history.back()'>Voltar</a>";
      exit;
   }
   if ($_POST["email"]==""){
      echo "Email incorreto";
      echo "<a href='javascript:history.back()'>Voltar</a>";
      exit;
   }
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
   if ($_POST["UF"]==""){
      echo "UF incorreto";
      echo "<a href='javascript:history.back()'>Voltar</a>";
      exit;
   }
   if ($_POST["Cargo"]==""){
      echo "Cargo incorreto";
      echo "<a href='javascript:history.back()'>Voltar</a>";
      exit;
   }

   $campos_texto = ["nome", "endereco", "complemento", "cidade", "bairro", "email", "usuario"];
   foreach ($campos_texto as $campo) {
      if (isset($_POST[$campo]) && $_POST[$campo] != "") {
         if ((strrpos($_POST[$campo],"drop")!==false)||
             (strrpos($_POST[$campo],"update")!==false)||
             (strrpos($_POST[$campo],"insert")!==false)||
             (strrpos($_POST[$campo],"delete")!==false)||
             (strrpos($_POST[$campo],"select")!==false)){
                echo ucfirst($campo)." Invalido";
                echo "<a href='javascript:history.back()'>Voltar</a>";
                exit;
         }
      }
   }
}

if ((isset($_POST["nome"]))&&(isset($_POST["email"]))){
    processa_formulário();
}

?>

<?php
$nome         = $_POST["nome"];
$endereco     = $_POST["endereco"];
$numero       = $_POST["numero"];
$complemento  = $_POST["complemento"];
$celular      = $_POST["celular"];
$bairro       = $_POST["bairro"];
$cep          = $_POST["cep"];
$cidade       = $_POST["cidade"];
$uf           = $_POST["UF"];
$email        = $_POST["email"];
$cargo        = $_POST["Cargo"];
$usuario      = $_POST["usuario"];
$senha        = $_POST["senha"];
$departamento = $_POST["Departamento"];

$sql = "INSERT INTO `funcionarios`
(`nome`, `endereco`, `numero`, `complemento`, `celular`, `bairro`, `cep`, `cidade`, `uf`, `email`, `cargo`, `usuario`, `senha`, `departamento`)
VALUES ('".$nome."','".$endereco."','".$numero."','".$complemento."','".$celular."','".$bairro."','".$cep."','".$cidade."','".$uf."','".$email."','".$cargo."','".$usuario."','".$senha."','".$departamento."')";

$host    = "localhost";
$username= "root";
$password= "";
$db_name = "duck_tech";
$con = mysqli_connect("$host", "$username", "$password", "$db_name") or die("cannot connect");
if (mysqli_connect_errno()) {
    echo "Falhou ao conectar ao MySQL: " . mysqli_connect_error();
    exit();
}
$result = mysqli_query($con, $sql);
if (!$result) {
    die("Erro na inclusao: " . mysqli_error($con));
} else {
    mysqli_close($con);
    echo "Funcionário cadastrado com sucesso";
    exit;
}
?></body></html>
