<html>
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