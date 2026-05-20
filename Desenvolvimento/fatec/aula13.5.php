<html>
	<head>
	<meta chaset="UTF-8">
	<meta name="description" content="Me site da aula1">
	<meta name="robots" content="robots.txt">
	<meta name="author" content="Efraim Lima">
    <body>
        <form action="aula13.5.php" method="get">
            <select name="UF">
            <option value="" select> Selecione</option>
            <option value="MG"> MG </option> 
            <option value="SP"> SP </option>
            <option value="RJ"> RJ </option>
        </select><br>
        
        <input type="submit" value="Enviar">          
        </form>

        <?php 

			if(isset($_GET['UF'])){
				$UF=$_GET["UF"];
				echo $UF;
				switch($UF){
					case "MG" : echo "mostra MG"; break;
					case "SP" : echo "mostra SP"; break;
					case "RJ" : echo "mostra RJ"; break;
					default : echo "mostra = ".$UF; break;
				}
			}
        ?>
        <br>
        <a href="index.php"> Voltar para o índice </a>
		</body>
	</head>
</html>