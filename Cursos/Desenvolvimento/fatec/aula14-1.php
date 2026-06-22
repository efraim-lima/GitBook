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
            function processa_formulario(){
                if($_GET["nome"]==""){
                    echo "Nome invalido";
                    echo "<br><a href='javascript:history.back()'> Voltar para o formulário </a>";
                    exit;
                } 
                if ($_GET["valor"]=="") {
                    echo "Valor invalido";
                    echo "<br><a href='javascript:history.back()'> Voltar para o formulário </a>";
                    exit;
                } 
                else {
                    echo "Valor: ".$_GET["nome"];
                    echo "<br>Valor: ".$_GET["valor"];
                }
            }

			?>
        <br>
        <a href="index.php"> Voltar para o índice </a>
		</body>
	</head>
</html>