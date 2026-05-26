<html>
	<!-- Para rodar o PHP devemos ir no terminal e rodar nosso servidor antes, que indexará o index.php antes de tudo mais -->
	<!-- Comando: php -S localhost:8000 -->
	<head>
	<meta chaset="UTF-8">
	<meta name="description" content="Me site da aula1">
	<meta name="robots" content="robots.txt">
	<meta name="author" content="Efraim Lima">
		<body>
			<?php 
			$i = 0;
			$arquivos = scandir(".");


			for ($i=0; $i<count($arquivos); $i++){
				$arquivo = $arquivos[$i];
				echo "<a href='".$arquivo."'>".$arquivo."</a><br>";
			}
			?>
		</body>
	</head>
</html>