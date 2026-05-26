<html>
	<head>
	<meta chaset="UTF-8">
	<meta name="description" content="Me site da aula1">
	<meta name="robots" content="robots.txt">
	<meta name="author" content="Efraim Lima">
    <body>
			<form action="aula13.4.php" method="get">
				<input type="text" name="valor" placeholder="Digite seu numero">
				<input type="submit" value="Enviar">
			<?php 

			if(isset($_GET['valor'])){
				$a=$_GET["valor"];

				switch($a){
					case "1" : echo "mostra 1"; break;
					case "2" : echo "mostra 2"; break;
					default : echo "mostra = ".$a; break;
				}
			}

			?>
        <br>
        <a href="index.php"> Voltar para o índice </a>
		</body>
	</head>
</html>