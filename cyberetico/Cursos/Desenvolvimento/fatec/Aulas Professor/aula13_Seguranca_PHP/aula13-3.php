<html><head><title>Meu Site</title></head><body>
<?php
$a=1;
$b=2;
$c=3;
$a=$a+1; 
$b=$c*2;
$c++;
if (($a<$b)&&($b<6)) {
      if ($c-1<=2){
         echo "chegou aqui 1";
      }
   }
   else {    
      if (($b>$a)||(($b>$c)&&($c==4))) {
         echo "chegou aqui 2";
      }
   }
?><body></html>