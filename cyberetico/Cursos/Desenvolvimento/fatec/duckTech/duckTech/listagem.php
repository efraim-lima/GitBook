<?php
// listagem.php
include 'conexao.php';

$sql = "SELECT id, nome, cargo, departamento, email, celular FROM funcionarios ORDER BY id";
$result = mysqli_query($conn, $sql);
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Listagem de Funcionários - Duck Tech</title>
    <link rel="stylesheet" href="style.css">
    <style type="text/css">
        body {
            background-color: #1C1526;
            font-family: 'Roboto', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 30px;
        }
        div#container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: #2D2540;
            border-radius: 28px;
            padding: 25px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            border: 1px solid #734A19;
        }
        h2 {
            color: #F2A413;
            text-align: center;
            margin-top: 0;
        }
        table#tabela-func {
            width: 100%;
            border-collapse: collapse;
            background-color: #2D2540;
            border-radius: 16px;
            overflow: hidden;
            margin-top: 20px;
        }
        table#tabela-func th, table#tabela-func td {
            border: 1px solid #734A19;
            padding: 12px;
            text-align: left;
            color: #F2F2F2;
        }
        table#tabela-func th {
            background-color: #F2A413;
            color: #1C1526;
        }
        .sem-registros {
            text-align: center;
            color: #A67721;
            padding: 30px;
        }
    </style>
</head>
<body style="background-color:#1C1526;">
    <div id="container">
        <h2> Funcionários Duck Tech</h2>
        <table id="tabela-func">
            <thead>
                <tr><th>ID</th><th>Nome</th><th>Cargo</th><th>Departamento</th><th>Email</th><th>Celular</th></tr>
            </thead>
            <tbody>
                <?php if (mysqli_num_rows($result) > 0): ?>
                    <?php while ($row = mysqli_fetch_assoc($result)): ?>
                    <tr>
                        <td><?php echo $row['id']; ?></td>
                        <td><?php echo htmlspecialchars($row['nome']); ?></td>
                        <td><?php echo htmlspecialchars($row['cargo']); ?></td>
                        <td><?php echo htmlspecialchars($row['departamento']); ?></td>
                        <td><?php echo htmlspecialchars($row['email']); ?></td>
                        <td><?php echo htmlspecialchars($row['celular']); ?></td>
                    </tr>
                    <?php endwhile; ?>
                <?php else: ?>
                    <tr><td colspan="6" class="sem-registros">Nenhum funcionário cadastrado ainda.</td></tr>
                <?php endif; ?>
            </tbody>
        </table>
    </div>
</body>
</html>
<?php mysqli_close($conn); ?>