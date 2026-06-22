<html><head><title>Meu Site</title>
<meta http-equiv="Cache-Control" content="No-Cache">
</head><body>
<?php
function processa_formulário(){
   if ($_GET["nome"]==""){
      echo "Nome incorreto";
      echo "<a href='javascript:history.back()'>Voltar</a>";
      exit;
   }
   if ($_GET["endereco"]==""){
      echo "Endereco incorreto";
      echo "<a href='javascript:history.back()'>Voltar</a>";
      exit;
   }
   
   //Repita para os outros campos
      if ($_GET["nome"]!=""){
		  if ((strrpos($_GET["nome"],"drop")>0)|| 
		      (strrpos($_GET["nome"],"update")>0)||
			  (strrpos($_GET["nome"],"insert")>0)||
			  (strrpos($_GET["nome"],"delete")>0)||
			  (strrpos($_GET["nome"],"select")>0)||
			  (strrpos($_GET["nome"],"drop")>0)
			  ){
				echo "Nome Invalido";
				echo "<a href='javascript:history.back()'>Voltar</a>";
				exit;
	  }
   }
}
 if ((isset($_GET["nome"]))&&(isset($_GET["email"]))){ 
     processa_formulário();
 }

?> 


<?php 
//$_GET vai capturar o usuario e senha digitados no formulario html para usar na query insert 
$nome    	=$_GET["nome"];
$endereco	=$_GET["endereco"];
//....repita .......... para todosos campos complemento, bairro, cep, cidade, bairro, uf, email, usuario e senha
//....
//OBSERVE que o id não deve ser preenchido pois ele é acrescentado automaticamente. Complete com as variáveis que faltam
$sql="insert into `jogadores`
(`nome`, `endereco`, `numero`, `complemento`, `bairro`, `cidade`,         `cep`,     `uf`,     `email`, `usuario`, `senha`) 
VALUES ('".$nome."','".$endereco."','','','','','','','','','')"; //complete a query com as variáveis do formulário

$host    ="localhost"; //Endereco do Servidor MySQL
$username="root";      //Usuario administrador do MySQL
$password="";          //Senha administrador do MySQL 
$db_name ="empresa"; //nome da base de dados MySQL
$con=mysqli_connect("$host", "$username", "$password", "$db_name") or die("cannot connect");  //Cria conexao banco de dados
if (mysqli_connect_errno()) {                          //testa se a conexao foi estabelecida corretamente
        echo "Falhou ao conectar ao MySQL: " . mysqli_connect_error();
        exit();
}
$result = mysqli_query($con,$sql);    //Roda a query na tabela cadastro usando a conexao e guarda em $result
if (!$result) {
        die("Erro na inclusao: " . mysqli_error($con));             //se a query sql estiver incorreta vai parar aqui
}else{
	mysqli_close($con); //Fecha a conexao com banco de dados  
	echo "cliente cadastrado com sucesso";
	exit;               // Encerra PHP
}
?></table></body></html>