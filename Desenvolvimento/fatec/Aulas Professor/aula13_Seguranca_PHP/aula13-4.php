<html><head><title>Meu Site</title></head><body>
<form action="aula13-4.php">
<input type="text" name="valor" value="">
<input type="submit" value="ENVIAR">
</form>
<?php
if (isset($_GET["valor"])) { /*Se não usar o isset ele gera um warning */
     $a=$_GET["valor"];
	switch($a) {
	  case "1" : echo "mostra 1"; break;
	  case "2" : echo "mostra 2"; break;
	  default : echo "valor padrao";
	}
}
?>
</body></html>

