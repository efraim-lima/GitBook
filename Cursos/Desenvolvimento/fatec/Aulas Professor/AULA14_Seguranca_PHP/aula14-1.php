<html><head><title>Meu Site</title></head><body>
<?php
function Converte_Real_Dolar($valorreais)
{
	$cotacaodolarhoje=5.30;
	$dolares=$valorreais/$cotacaodolarhoje;
	return $dolares;
}
if (isset($_GET["valor"])) {
	$valorreais=$_GET["valor"];
	if ($valorreais!="") echo "Dólares: ".Converte_Real_Dolar($valorreais)."<br>";
}
?>
Converte Real para Dólares<BR>
<form method="GET" action="aula14-1.php">
Informe valor em reais (R$): 
<input type="text" name="valor" >
<input type="submit" Value="Envia" >
</form>
</body></html>

