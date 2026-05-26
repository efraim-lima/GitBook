<?php
// cadastro.php
include 'conexao.php';

// Inicializa variável de erro
$erro = false;
$msg_erro = "";

// Verifica se o formulário foi enviado
if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    // ==========================================
    // 1. Receber e sanitizar os dados
    // ==========================================
    $nome        = trim($_POST['nome'] ?? '');
    $endereco    = trim($_POST['endereco'] ?? '');
    $complemento = trim($_POST['complemento'] ?? '');
    $bairro      = trim($_POST['bairro'] ?? '');
    $cidade      = trim($_POST['cidade'] ?? '');
    $uf          = $_POST['uf'] ?? '';
    $cep         = trim($_POST['cep'] ?? '');
    $email       = trim($_POST['email'] ?? '');
    $celular     = trim($_POST['celular'] ?? '');
    $cargo       = $_POST['cargo'] ?? '';
    $departamento= $_POST['departamento'] ?? '';
    $usuario     = trim($_POST['usuario'] ?? '');
    $senha       = $_POST['senha'] ?? '';

    // ==========================================
    // 2. Validações (as mesmas do JavaScript, mas em PHP)
    // ==========================================
    // Caracteres especiais proibidos
    $caracteres_proibidos = array('*', '#', '!', '@', '<', '>');

    function tem_caractere_especial($texto, $proibidos) {
        foreach ($proibidos as $c) {
            if (strpos($texto, $c) !== false) return true;
        }
        return false;
    }

    // Campos obrigatórios
    if (empty($nome))       { $erro = true; $msg_erro .= "Campo Nome é obrigatório.<br>"; }
    if (empty($endereco))   { $erro = true; $msg_erro .= "Campo Endereço é obrigatório.<br>"; }
    if (empty($bairro))     { $erro = true; $msg_erro .= "Campo Bairro é obrigatório.<br>"; }
    if (empty($cidade))     { $erro = true; $msg_erro .= "Campo Cidade é obrigatório.<br>"; }
    if (empty($email))      { $erro = true; $msg_erro .= "Campo Email é obrigatório.<br>"; }
    if (empty($celular))    { $erro = true; $msg_erro .= "Campo Celular é obrigatório.<br>"; }
    if (empty($usuario))    { $erro = true; $msg_erro .= "Campo Usuário é obrigatório.<br>"; }
    if (empty($senha))      { $erro = true; $msg_erro .= "Campo Senha é obrigatório.<br>"; }

    // Validação de UF (select)
    $ufs_validas = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'];
    if (!in_array($uf, $ufs_validas)) {
        $erro = true; $msg_erro .= "Selecione um estado (UF) válido.<br>";
    }

    // Caracteres especiais nos campos textuais
    if (tem_caractere_especial($nome, $caracteres_proibidos))     { $erro = true; $msg_erro .= "Nome contém caracteres inválidos (* # ! @ < >).<br>"; }
    if (tem_caractere_especial($endereco, $caracteres_proibidos)) { $erro = true; $msg_erro .= "Endereço contém caracteres inválidos.<br>"; }
    if (tem_caractere_especial($cidade, $caracteres_proibidos))   { $erro = true; $msg_erro .= "Cidade contém caracteres inválidos.<br>"; }
    if (tem_caractere_especial($bairro, $caracteres_proibidos))   { $erro = true; $msg_erro .= "Bairro contém caracteres inválidos.<br>"; }

    // Validação de email (presença de @ e . após o @)
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $erro = true; $msg_erro .= "Email inválido. Deve conter @ e um ponto após o @.<br>";
    }

    // Celular apenas números
    if (!ctype_digit($celular)) {
        $erro = true; $msg_erro .= "Celular deve conter apenas números.<br>";
    }

    // Anti SQL Injection: verifica palavras proibidas
    $palavras_proibidas = ['select', 'update', 'insert', 'drop', 'delete', 'alter', 'create'];
    function tem_sql_injection($texto, $proibidas) {
        $texto_lower = strtolower($texto);
        foreach ($proibidas as $palavra) {
            if (strpos($texto_lower, $palavra) !== false) return true;
        }
        return false;
    }
    if (tem_sql_injection($nome, $palavras_proibidas) || tem_sql_injection($endereco, $palavras_proibidas) ||
        tem_sql_injection($cidade, $palavras_proibidas) || tem_sql_injection($bairro, $palavras_proibidas) ||
        tem_sql_injection($usuario, $palavras_proibidas)) {
        $erro = true; $msg_erro .= "Palavras suspeitas (SELECT, UPDATE, etc.) não são permitidas.<br>";
    }

    // ==========================================
    // 3. Se houver erro, exibe mensagem e link voltar
    // ==========================================
    if ($erro) {
        echo "<!DOCTYPE html><html><head><title>Erro no Cadastro</title>";
        echo "<link rel='stylesheet' href='style.css'>";
        echo "<style>body{background:#1C1526;color:white;padding:30px;font-family:Roboto;}</style>";
        echo "</head><body>";
        echo "<div style='max-width:600px;margin:0 auto;background:#2D2540;padding:30px;border-radius:28px;'>";
        echo "<h2 style='color:#F2A413'>Erro no formulário</h2>";
        echo "<p>$msg_erro</p>";
        echo "<p><a href='javascript:history.back()' style='color:#F2A413'>← Voltar e corrigir</a></p>";
        echo "</div></body></html>";
        exit;
    }

    // ==========================================
    // 4. Se passou, criptografa a senha e insere no banco
    // ==========================================
    $senha_hash = password_hash($senha, PASSWORD_DEFAULT); // 60+ caracteres

    $sql = "INSERT INTO funcionarios (nome, endereco, complemento, bairro, cidade, uf, cep, email, celular, cargo, departamento, usuario, senha)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

    $stmt = mysqli_prepare($conn, $sql);
    mysqli_stmt_bind_param($stmt, "sssssssssssss", 
        $nome, $endereco, $complemento, $bairro, $cidade, $uf, $cep, $email, $celular, $cargo, $departamento, $usuario, $senha_hash);

    if (mysqli_stmt_execute($stmt)) {
        // Sucesso: redireciona para listagem
        header("Location: listagem.php");
        exit;
    } else {
        // Erro no banco (ex: usuário duplicado)
        echo "<div style='background:#2D2540; padding:30px; border-radius:28px; max-width:600px; margin:auto;'>";
        echo "<h2 style='color:#F2A413'>Erro ao cadastrar</h2>";
        echo "<p>" . mysqli_error($conn) . "</p>";
        echo "<p><a href='javascript:history.back()'>Voltar</a></p>";
        echo "</div>";
    }

    mysqli_stmt_close($stmt);
    mysqli_close($conn);
} else {
    // Se acessar cadastro.php diretamente sem POST, redireciona para o formulário
    header("Location: cadastro.html");
    exit;
}
?>