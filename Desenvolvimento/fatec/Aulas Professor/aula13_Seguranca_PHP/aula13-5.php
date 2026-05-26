<html><head><title>Meu Site</title>
</head><body>
<form method="GET" action="aula13-5.php">
UF: <select name="UF">
<option value=""    select>Selecione</option>
<option value="MG" >MG</option>
<option value="SP"  >SP</option>
</select><br>
<input type="submit" Value="Envia" >
</form>
<?php
if (isset($_GET["UF"])) { /*Se não usar o isset ele gera um warning */
    $UF=$_GET["UF"];
	switch($UF) {
	  case "MG" : echo "MG"; break;
	  case "SP" : echo "SP"; break;
	  default : echo "Estado Incorreto";
	}
}
?>
</body></html>


