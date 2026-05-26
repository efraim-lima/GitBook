<html><head><title>Lista Funcionarios</title>
<meta http-equiv="Cache-Control" content="No-Cache">
</head><body>
<?php  

$host		="localhost";  //Endereco do Servidor MySQL
$username	="root";   //Usuario administrador do MySQL
$password	="123456";       //Senha administrador do MySQL Na sua casa não tem senha
$db_name	="jogadores"; //nome da base de dados MySQL
$con=mysqli_connect("$host", "$username", "$password", "$db_name") or die("cannot connect");  //Cria conexao banco de dados
if (mysqli_connect_errno()) {                          //testa se a conexao foi estabelecida corretamente
        echo "Falhou ao conectar ao MySQL: " . mysqli_connect_error();
        exit();
}
$sql = "select id, nome, cargo, email from  funcionarios order by nome";
$result = mysqli_query($con,$sql);    //Roda a query na tabela cadastro usando a conexao e guarda em $result
if (!$result) {
        die("Erro na consulta: " . mysqli_error($con));             //se a query sql for incorreta para aqui
}else{
		while($row = mysqli_fetch_assoc($result)){   		
		    echo $row['id']." = ".$row['nome']." = ".$row['cargo']." = ".$row['email']."<br>";    // AJUSTE O HTML PARA HTML EM FORMATO TABLE e CSS 
		}
		echo "fim de listagem";
		mysqli_close($con); //Fecha a conexao com banco de dados  
}
                 	
?>
</table></body></html>
