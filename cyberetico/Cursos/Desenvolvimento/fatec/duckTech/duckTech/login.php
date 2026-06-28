<?php
// login.php
include 'conexao.php';

// Inicia a sessão
session_start();

$erro = false;
$msg_erro = "";

// Verifica se o formulário foi enviado
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $usuario = trim($_POST['usuario'] ?? '');
    $senha   = $_POST['senha'] ?? '';

    // Valida campos vazios
    if (empty($usuario)) {
        $erro = true;
        $msg_erro = "Usuário é obrigatório.";
    } elseif (empty($senha)) {
        $erro = true;
        $msg_erro = "Senha é obrigatória.";
    }

    if (!$erro) {
        // Busca o usuário no banco de dados
        $sql = "SELECT id, nome, usuario, senha FROM funcionarios WHERE usuario = ?";
        $stmt = mysqli_prepare($conn, $sql);
        mysqli_stmt_bind_param($stmt, "s", $usuario);
        mysqli_stmt_execute($stmt);
        $result = mysqli_stmt_get_result($stmt);

        if ($row = mysqli_fetch_assoc($result)) {
            // Verifica a senha (hash)
            if (password_verify($senha, $row['senha'])) {
                // Senha correta: cria variáveis de sessão
                $_SESSION['usuario_id']   = $row['id'];
                $_SESSION['usuario_nome'] = $row['nome'];
                $_SESSION['usuario_login'] = $row['usuario'];

                // Redireciona para o dashboard (dentro do mesmo iframe)
                header("Location: dashboard.php");
                exit;
            } else {
                $erro = true;
                $msg_erro = "Usuário ou senha inválidos.";
            }
        } else {
            $erro = true;
            $msg_erro = "Usuário não encontrado.";
        }
        mysqli_stmt_close($stmt);
    }

    // Se houve erro, exibe mensagem e link voltar
    if ($erro) {
        echo "<!DOCTYPE html><html><head><title>Erro no Login</title>";
        echo "<link rel='stylesheet' href='style.css'>";
        echo "<style>body{background:#1C1526;color:white;padding:30px;font-family:Roboto;}</style>";
        echo "</head><body>";
        echo "<div style='max-width:500px;margin:0 auto;background:#2D2540;padding:30px;border-radius:28px;'>";
        echo "<h2 style='color:#F2A413'>Acesso negado</h2>";
        echo "<p>$msg_erro</p>";
        echo "<p><a href='javascript:history.back()' style='color:#F2A413'>← Voltar e tentar novamente</a></p>";
        echo "</div></body></html>";
        exit;
    }
} else {
    // Se acessou login.php diretamente sem POST, redireciona para o menu (página inicial)
    header("Location: menu.html");
    exit;
}
?>