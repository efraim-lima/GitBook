<html><head><title>Meu Site</title></head><body>
<?php
$num = 10;                    // int
$str = "20";                    // String
$soma = $num + $str; 		// $soma será 30 porque a operação é matemática
$texto = "123 casa";
$numero = (int)$texto;       // $numero será 123
echo intval(42)."<br>";      // 42
echo intval(4.7)."<br>";     // 4
$var = "122.367";
$var2=(float)$var;                                //var2 é um float
echo sprintf("%05.2f",$var2)."<br>"; // 122.37 arredondado
$string = "Este é um teste de string";
echo sprintf("%s",$string)."<br>";           //Este é um teste de String
echo str_replace(' ', '_', $string)."<br>"; //Este_é_um_teste_de_String
echo substr($string,0,10)."<br>";         //Este_é_um
echo strrpos($string,"teste")."<br>";                //11
echo strlen($string);                        //26


?>

</form></body></html>

