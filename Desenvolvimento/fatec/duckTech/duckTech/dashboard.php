<?php
// dashboard.php
session_start();

// Verifica se o usuário está logado
if (!isset($_SESSION['usuario_id'])) {
    // Se não estiver logado, redireciona para o menu (ou para uma página de login)
    // Como o formulário de login está no menu lateral, redirecionamos para o menu.html
    // Mas o menu.html carregará o iframe com home.html. Para manter a consistência,
    // podemos redirecionar para uma página de "acesso negado" ou simplesmente mostrar erro.
    // Vamos redirecionar para o menu.html e exibir uma mensagem no iframe?
    // Melhor: exibir uma mensagem de erro e um link para o menu.
    echo "<!DOCTYPE html><html><head><title>Acesso negado</title>";
    echo "<link rel='stylesheet' href='style.css'>";
    echo "<style>body{background:#1C1526;color:white;padding:30px;font-family:Roboto;}</style>";
    echo "</head><body>";
    echo "<div style='max-width:500px;margin:0 auto;background:#2D2540;padding:30px;border-radius:28px;'>";
    echo "<h2 style='color:#F2A413'>Acesso restrito</h2>";
    echo "<p>Você não está logado. Por favor, faça login no menu lateral.</p>";
    echo "<p><a href='menu.html' target='_top' style='color:#F2A413'>Ir para o site</a></p>";
    echo "</div></body></html>";
    exit;
}

// Se está logado, exibe o dashboard
$nome_usuario = $_SESSION['usuario_nome'];
$login_usuario = $_SESSION['usuario_login'];

// Opcional: buscar mais dados do funcionário no banco (email, departamento, etc.)
include 'conexao.php';
$sql = "SELECT email, departamento, cargo, celular FROM funcionarios WHERE id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "i", $_SESSION['usuario_id']);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);
$dados = mysqli_fetch_assoc($result);
mysqli_stmt_close($stmt);
mysqli_close($conn);

$email = $dados['email'] ?? 'não informado';
$departamento = $dados['departamento'] ?? 'não informado';
$cargo = $dados['cargo'] ?? 'não informado';
$celular = $dados['celular'] ?? 'não informado';
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Dashboard - Duck Tech</title>
    <link rel="stylesheet" href="style.css">
    <style type="text/css">
        body {
            background-color: #1C1526;
            font-family: 'Roboto', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 30px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 80vh;
        }
        div#dashboard-card {
            max-width: 600px;
            width: 100%;
            background-color: #2D2540;
            border-radius: 32px;
            padding: 30px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            border: 1px solid #734A19;
        }
        h2 {
            color: #F2A413;
            margin-top: 0;
            text-align: center;
        }
        div#info-dash {
            background-color: #1C1526;
            border-radius: 24px;
            padding: 20px;
            margin: 20px 0;
        }
        div#info-dash p {
            margin: 12px 0;
            font-size: 1.1rem;
        }
        div#info-dash strong {
            color: #F2A413;
        }
        .logout-link {
            text-align: center;
            margin-top: 20px;
        }
        .logout-link a {
            color: #F2A413;
            text-decoration: none;
            background-color: #2D2540;
            padding: 8px 20px;
            border-radius: 40px;
            border: 1px solid #F2A413;
        }
        .logout-link a:hover {
            background-color: #F2A413;
            color: #1C1526;
        }
    </style>
</head>
<body style="background-color:#1C1526;">
    <div id="dashboard-card">
        <h2>Dashboard Duck Tech</h2>
        <div id="info-dash">
            <p><strong>Usuário:</strong> <?php echo htmlspecialchars($nome_usuario); ?></p>
            <p><strong>Login:</strong> <?php echo htmlspecialchars($login_usuario); ?></p>
            <p><strong>Departamento:</strong> <?php echo htmlspecialchars($departamento); ?></p>
            <p><strong>Cargo:</strong> <?php echo htmlspecialchars($cargo); ?></p>
            <p><strong>Email:</strong> <?php echo htmlspecialchars($email); ?></p>
            <p><strong>Celular:</strong> <?php echo htmlspecialchars($celular); ?></p>
        </div>
        <p style="text-align:center;">Bem-vindo ao sistema. Utilize o menu para navegar.</p>
        <div class="logout-link">
            <a href="logout.php" target="_top">Sair do sistema</a>
        </div>
    </div>
</body>
</html>