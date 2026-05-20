<html>
	<head>        
        <title> Mais aula </title>

        <meta chaset="UTF-8">
        <meta name="description" content="Me site da aula1">
        <meta name="robots" content="robots.txt">
        <meta name="author" content="Efraim Lima">
    </head>
    
    <body>
        <table border=1><tr><td>Índice</td><td>Aluno</td><td>Nota</td></tr>
        <?php
            $indice=0;
            $notas=2.75;

            while ($indice<10) {
                $indice++;
                echo "<tr><td>".$indice."</td><td>Aluno ".$indice."</td><td>".$notas."</td></tr>";
                $notas=$notas+0.25;
            }
        ?>
        </table>
        <br>
        <a href="index.php"> Voltar para o índice </a>
    </body>
</html>