<html><head><title>Meu Site</title></head><body>
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
   //Repita aqui para os outros campos do formulário
   //PROCESSAMENTO ANTI-SQL INJECTION
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
if ((isset($_GET["nome"]))&&(isset($_GET["endereco"])))
  {
     processa_formulário();
 }
?> 
 <form action="aula14-3.php" method="GET">
 Nome:<input type="text" name="nome">
 Endereco:<input type="text" name="endereco">
 <input type="submit" name="Enviar">
 </form>
</body></html>