<html><head><title>Meu Site</title>
<meta charset="UTF-8"></head><body>
<table border=1><tr><td>Índice</td><td>Aluno</td><td>Nota</td></tr>
<?php 
$notas=2.75;
for( $indice=1;$indice<=30;$indice++){ 
 echo 
 "<tr><td>".$indice."</td><td>Aluno".$indice."</td><td>".$notas."</td></tr>";
 $notas=$notas+0.25;
}
?>
</table>
</body></html>
