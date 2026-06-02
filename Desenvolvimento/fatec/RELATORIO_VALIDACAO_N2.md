# Relatório de Validação — N2 vs Aulas Professor
**Data:** 25/[[05]]/[[2026]]  
**Diretório analisado:** `[[[[[[[[information-security]]]]/[[[[information-security]]/[[information-security/fatec/fatec|fatec]]/[[information-security/fatec/fatec|fatec]]|[[information-security/fatec/fatec|fatec]]]]/[[[[information-security]]/[[information-security/fatec/fatec|fatec]]/[[information-security/fatec/fatec|fatec]]|[[information-security/fatec/fatec|fatec]]]]|[[[[information-security]]/[[information-security/fatec/fatec|fatec]]/[[information-security/fatec/fatec|fatec]]|[[information-security/fatec/fatec|fatec]]]]]]/[[[[[[reports]]]]/[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]/[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]|[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]]]/1-[[[[[[reports]]]]/[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]/[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]|[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]]]/[[[[[[Estudos Avançados]]]]]]/[[[[[[information-security]]/[[information-security/fatec/fatec|fatec]]/[[information-security/fatec/fatec|fatec]]|[[information-security/fatec/fatec|fatec]]]]/[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]/1-[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]/[[[[Estudos Avançados]]]]/[[[[information-security/fatec/fatec|fatec]]/[[reports/2026/2026|2026]]/1-[[reports/2026/2026|2026]]/[[Estudos Avançados]]/[[fatec/2026/1-2026/Estudos Avançados/N2|N2]]|[[fatec/2026/1-2026/Estudos Avançados/N2|N2]]]]|[[[[information-security/fatec/fatec|fatec]]/[[reports/2026/2026|2026]]/1-[[reports/2026/2026|2026]]/[[Estudos Avançados]]/[[fatec/2026/1-2026/Estudos Avançados/N2|N2]]|[[fatec/2026/1-2026/Estudos Avançados/N2|N2]]]]]]|[[[[[[information-security]]/[[information-security/fatec/fatec|fatec]]/[[information-security/fatec/fatec|fatec]]|[[information-security/fatec/fatec|fatec]]]]/[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]/1-[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]/[[[[Estudos Avançados]]]]/[[[[information-security/fatec/fatec|fatec]]/[[reports/2026/2026|2026]]/1-[[reports/2026/2026|2026]]/[[Estudos Avançados]]/[[fatec/2026/1-2026/Estudos Avançados/N2|N2]]|[[fatec/2026/1-2026/Estudos Avançados/N2|N2]]]]|[[[[information-security/fatec/fatec|fatec]]/[[reports/2026/2026|2026]]/1-[[reports/2026/2026|2026]]/[[Estudos Avançados]]/[[fatec/2026/1-2026/Estudos Avançados/N2|N2]]|[[fatec/2026/1-2026/Estudos Avançados/N2|N2]]]]]]]]/`  
**Referência:** `[[[[[[Aulas Professor]]]]]]/` (aulas 1–3, 5–6, 9, 11–15)

---

## 1. Padrões Identificados nas Aulas Professor

### 1.1 HTML (Aulas 1, 2, 3, 5, 6, 9, 11, 12)

| Padrão | Evidência nas aulas |
|--------|-------------------|
| Estrutura mínima `<html><head><title>` | Todos os arquivos HTML das aulas |
| `<meta charset="UTF-8">` | aula3-1.html, aula13-6.php, entre outros |
| CSS externo via `<link rel="stylesheet">` | Padrão a partir da Aula 5 |
| CSS interno via `<style>` | Aulas 5 e 6 |
| Formulário `<form method="GET/POST" action="arquivo.php">` | aula14/cadastro.html |
| Validação JS com `function verifica_formulario()` e `onsubmit="return ..."` | aula12-1.html, aula14/cadastro.html |
| `<script type="text/javascript">` inline | Aula 11-1, aula 12-1 |
| `<iframe>` para navegação em páginas internas | Padrão de menu da N2 |

### 1.2 PHP (Aulas 13, 14, 15)

| Padrão | Evidência nas aulas |
|--------|-------------------|
| `<meta http-equiv="Cache-Control" content="No-Cache">` | aula14/cadastro.php, aula15/listagem.php |
| Conexão: `mysqli_connect("$host","$username","$password","$db_name") or die(...)` | aula14/cadastro.php, aula15/listagem.php |
| Teste de conexão: `if (mysqli_connect_errno()) { ... exit(); }` | aula14/cadastro.php, aula15/listagem.php |
| Leitura de POST: `$_POST["campo"]` direto | aula14/cadastro.php |
| Validação de campos com função `processa_formulário()` | aula14-3.php, aula14/cadastro.php |
| Anti-injection com `strrpos($_POST["campo"], "drop/update/insert/...")` | aula14-3.php, aula14/cadastro.php |
| `if ((isset($_POST["a"]))&&(isset($_POST["b"]))) { processa_formulário(); }` | aula14/cadastro.php |
| `INSERT INTO` com concatenação de variáveis | aula14/cadastro.php |
| `$result = mysqli_query($con,$sql)` | aula14/cadastro.php, aula15/listagem.php |
| `if (!$result) { die("Erro..."); }else{ ... }` | aula14/cadastro.php, aula15/listagem.php |
| `while($row = mysqli_fetch_assoc($result))` | aula15/listagem.php |
| `echo "fim de listagem"` + `mysqli_close($con)` | aula15/listagem.php |
| `session_start()`, `$_SESSION["chave"]`, `session_destroy()` | aula13 (sessões PHP) |
| `isset($_SESSION["chave"])` para proteger páginas | Padrão de sessão das aulas |
| `header("Location: arquivo.php")` para redirecionamento | Padrão PHP |

---

## 2. Análise Arquivo por Arquivo — N2

### 2.1 index.html ✅ CONFORME

| Critério | Status | Evidência |
|----------|--------|-----------|
| Estrutura `<html><head><title>...</title></head><body>` | ✅ | Linha 1–9 |
| `<meta charset="UTF-8">` | ✅ | Linha 3 |
| `<link rel="stylesheet" href="style.css">` | ✅ | Linha 7 |
| CSS interno `<style>` com personalizações visuais | ✅ | Linhas 18–107 |
| `<iframe>` para navegação de menu + conteúdo | ✅ | Padrão de menu com iframes |
| Formulário de login `method="POST" action="login.php"` | ✅ | Área de login no menu lateral |
| `<input type="submit">` funcional | ✅ | Botão LOGIN |
| Links de navegação para todas as páginas | ✅ | home, sobre, listagem, cadastro |

**Referência:** Padrão de menu com iframe das aulas, formulário POST da aula 14.

---

### 2.2 header.html ✅ CONFORME

| Critério | Status | Evidência |
|----------|--------|-----------|
| Estrutura HTML básica | ✅ | `<html><head>...<body>` |
| `<link rel="stylesheet" href="style.css">` | ✅ | Presente |
| Imagem com `<img src="duck_header.png">` | ✅ | Tag img com alt e src |
| CSS interno para layout do header | ✅ | `<style>` com background gradiente |

**Referência:** Padrão de imagem e CSS das Aulas 5/6.

---

### 2.3 home.html ✅ CONFORME

| Critério | Status | Evidência |
|----------|--------|-----------|
| Estrutura HTML básica | ✅ | `<html>...<body>` |
| `<link rel="stylesheet" href="style.css">` | ✅ | Presente |
| CSS interno `<style>` | ✅ | Personalizações de card |
| Conteúdo institucional em parágrafo | ✅ | Texto de apresentação |

**Referência:** Padrão de conteúdo e CSS das Aulas 5/6.

---

### 2.4 sobre.html ✅ CONFORME

| Critério | Status | Evidência |
|----------|--------|-----------|
| Estrutura HTML completa com `<head>` e `<body>` | ✅ | Estrutura correta |
| `<link rel="stylesheet" href="style.css">` | ✅ | Presente |
| CSS interno para layout | ✅ | Container e tipografia |
| Uso de `<table>` para layout de conteúdo lado a lado | ✅ | Texto + imagem em colunas |
| Imagem `<img src="duck_chefe.jpg">` | ✅ | Tag img com alt |

**Referência:** Uso de tabelas para layout, padrão HTML das Aulas 1–3.

---

### 2.5 lista.html ✅ CONFORME

| Critério | Status | Evidência |
|----------|--------|-----------|
| Estrutura HTML básica | ✅ | `<html>...<body>` |
| `<link rel="stylesheet" href="style.css">` | ✅ | Presente |
| CSS interno com estilos de tabela | ✅ | `<style>` no cabeçalho |
| `<table>` com `<th>` e `<td>` para listagem | ✅ | Tabela de funcionários estática |
| Dados de exemplo coerentes com a proposta | ✅ | Pato Donald, Pato Douglas, Pato Donaldo |

**Referência:** Padrão de tabelas e CSS da Aula 13-6/13-7.

---

### 2.6 cadastro.html ✅ CONFORME

| Critério | Status | Evidência |
|----------|--------|-----------|
| Estrutura HTML com `<head>` e `<body>` | ✅ | Estrutura completa |
| `<link rel="stylesheet" href="style.css">` | ✅ | Presente |
| CSS interno com personalizações visuais | ✅ | Container e inputs estilizados |
| `<form method="post" action="cadastro.php">` | ✅ | Envio para arquivo PHP |
| Campos: nome, endereço, número, complemento, celular, bairro, cep, cidade, UF, email, cargo, usuário, senha, departamento | ✅ | Todos presentes com `name` correto |
| `<select>` para UF com todos os estados | ✅ | 27 estados listados |
| `<select>` para Cargo e Departamento | ✅ | Opções específicas Duck Tech |
| `<input type="submit">` | ✅ | Botão de envio |

**Referência:** Estrutura de formulário da aula14/cadastro.html e padrão de validação da aula12-1.html.

---

### 2.7 style.css ✅ CONFORME

| Critério | Status | Evidência |
|----------|--------|-----------|
| Arquivo CSS externo referenciado pelos HTMLs | ✅ | Todos os HTMLs fazem `<link rel="stylesheet" href="style.css">` |
| Estilização de `body`, `a:link`, `a:visited`, `a:hover`, `a:active` | ✅ | Padrão de links das aulas |
| Fonte sans-serif definida | ✅ | `font-family: 'Roboto', sans-serif` |

**Referência:** Padrão de CSS externo das Aulas 5 e 6.

---

### 2.8 cadastro.php ✅ CONFORME

| Critério | Status | Evidência |
|----------|--------|-----------|
| `<html><head><title>` + `<meta http-equiv="Cache-Control" content="No-Cache">` | ✅ | Linha 1–2 |
| Função `processa_formulário()` com validação de campos obrigatórios | ✅ | Validação de nome, endereço, email, usuário, senha |
| Anti-injection com `strrpos()` para keywords SQL | ✅ | drop, update, insert, delete, select |
| `if ((isset($_POST["nome"]))&&(isset($_POST["email"]))) { processa_formulário(); }` | ✅ | Linha 46–48 |
| `$_POST["campo"]` direto para captura dos dados | ✅ | Todos os campos capturados |
| `INSERT INTO funcionarios (campos) VALUES (...)` | ✅ | Query completa com todos os campos |
| `mysqli_connect("$host","$username","$password","$db_name") or die("cannot connect")` | ✅ | Padrão exato das aulas |
| `if (mysqli_connect_errno()) { echo "Falhou..."; exit(); }` | ✅ | Teste de conexão |
| `$result = mysqli_query($con, $sql)` + `if (!$result) die(...)` else { ... } | ✅ | Tratamento de erro da query |
| `mysqli_close($con)` após uso | ✅ | Fechamento da conexão |

**Referência direta:** `AULA14_Seguranca_PHP/cadastro.php` — estrutura idêntica.

---

### 2.9 login.php ✅ CONFORME

| Critério | Status | Evidência |
|----------|--------|-----------|
| `<html><head><title>` + `<meta http-equiv="Cache-Control" content="No-Cache">` | ✅ | Linha 1–2 |
| `session_start()` no início | ✅ | Linha 5 |
| Função `processa_login()` com `isset()` e validação de campos | ✅ | Linhas 6–17 |
| `if ((isset($_POST["usuario"]))&&(isset($_POST["senha"]))) { processa_login(); }` | ✅ | Linhas 18–20 |
| `$_POST["campo"]` direto | ✅ | `$usuario`, `$senha` |
| `SELECT ... FROM funcionarios WHERE usuario='...' AND senha='...'` | ✅ | Query de autenticação |
| `mysqli_connect("$host","$username","$password","$db_name") or die(...)` | ✅ | Conexão no padrão |
| `if (mysqli_connect_errno()) { ... exit(); }` | ✅ | Teste de conexão |
| `$result = mysqli_query($con,$sql)` | ✅ | Presente |
| `if (!$result) die(...)` else `{ if(mysqli_num_rows($result)>0) { ... } }` | ✅ | Estrutura condicional |
| `$_SESSION["usuario"] = $row["nome"]` – gravação de sessão | ✅ | Variáveis: usuario, cargo, departamento |
| `mysqli_close($con)` + `header("Location: dashboard.php")` | ✅ | Redirecionamento após login |
| Mensagem de erro + link voltar para credenciais inválidas | ✅ | Padrão das aulas |

**Referência direta:** Padrão de sessão das aulas 13 + conexão/query da aula 14/15.

---

### 2.10 dashboard.php ✅ CONFORME

| Critério | Status | Evidência |
|----------|--------|-----------|
| `<html><head><title>` + `<meta http-equiv="Cache-Control" content="No-Cache">` | ✅ | Linha 1–2 |
| `session_start()` | ✅ | Linha 5 |
| `if (!isset($_SESSION["usuario"])) { echo "..."; exit; }` | ✅ | Proteção de acesso |
| `echo $_SESSION["usuario"]` – uso dos dados da sessão | ✅ | Exibe usuario, cargo, departamento |
| Link para `logout.php` | ✅ | `<a href='logout.php'>Sair</a>` |

**Referência direta:** Padrão de dashboard protegido por sessão das aulas 13.

---

### 2.11 logout.php ✅ CONFORME

| Critério | Status | Evidência |
|----------|--------|-----------|
| `<html><head><title>` + `<meta http-equiv="Cache-Control" content="No-Cache">` | ✅ | Linha 1–2 |
| `session_start()` | ✅ | Linha 5 |
| `session_destroy()` | ✅ | Linha 6 |
| Mensagem de confirmação + link voltar | ✅ | Padrão echo + link das aulas |

**Referência direta:** Padrão de encerramento de sessão PHP das aulas 13.

---

### 2.12 listagem.php ✅ CONFORME

| Critério | Status | Evidência |
|----------|--------|-----------|
| `<html><head><title>` + `<meta http-equiv="Cache-Control" content="No-Cache">` | ✅ | Linha 1–2 |
| `mysqli_connect("$host","$username","$password","$db_name") or die(...)` | ✅ | Padrão exato |
| `if (mysqli_connect_errno()) { ... exit(); }` | ✅ | Presente |
| `select id, nome, cargo, email from funcionarios order by nome` | ✅ | Query de listagem |
| `$result = mysqli_query($con,$sql)` | ✅ | Presente |
| `if (!$result) { die("Erro..."); }else{ while($row = mysqli_fetch_assoc($result)) { echo ... } }` | ✅ | Estrutura idêntica à aula 15 |
| `echo "fim de listagem"` | ✅ | Presente |
| `mysqli_close($con)` | ✅ | Presente |

**Referência direta:** `AULA15_FERRAMENTAS_PHP_REPOSICAO/listagem.php` — estrutura idêntica.

---

### 2.13 conexao.php ✅ CONFORME

| Critério | Status | Evidência |
|----------|--------|-----------|
| `<html><head><title>` + `<meta http-equiv="Cache-Control" content="No-Cache">` | ✅ | Presente |
| Variáveis `$host`, `$username`, `$password`, `$db_name` | ✅ | Padrão das aulas |
| `mysqli_connect("$host","$username","$password","$db_name") or die(...)` | ✅ | Padrão exato |
| `if (mysqli_connect_errno()) { ... exit(); }` | ✅ | Presente |

**Referência direta:** Padrão de conexão da aula 14/15.

---

### 2.14 criar_banco.sql ✅ CONFORME

| Critério | Status | Evidência |
|----------|--------|-----------|
| `CREATE DATABASE IF NOT EXISTS duck_tech` | ✅ | Banco `duck_tech` referenciado em todos os PHP |
| `USE duck_tech` | ✅ | Presente |
| `CREATE TABLE IF NOT EXISTS funcionarios` | ✅ | Tabela com todos os campos do cadastro.php |
| Campos: id (AUTO_INCREMENT), nome, endereco, numero, complemento, celular, bairro, cep, cidade, uf, email, cargo, usuario, senha, departamento | ✅ | Todos os campos do INSERT presente |

**Referência:** Estrutura necessária para suportar todas as queries presentes nos PHP das aulas 14/15.

---

## 3. Resumo de Conformidade

| Arquivo | Tipo | Aula de Referência Principal | Conformidade |
|---------|------|------------------------------|-------------|
| index.html | HTML | Aulas 1–3, Menu com iframe | ✅ CONFORME |
| header.html | HTML | Aula 5/6 (CSS + imagem) | ✅ CONFORME |
| home.html | HTML | Aula 5/6 (CSS interno) | ✅ CONFORME |
| sobre.html | HTML | Aula 1/2 (tabela de layout) | ✅ CONFORME |
| lista.html | HTML | Aula 13-6/7 (tabela estática) | ✅ CONFORME |
| cadastro.html | HTML | Aula 12/14 (form + JS validação) | ✅ CONFORME |
| style.css | CSS | Aula 5/6 | ✅ CONFORME |
| cadastro.php | PHP | Aula 14 — cadastro.php | ✅ CONFORME |
| login.php | PHP | Aula 13 (sessão) + Aula 14 (conexão) | ✅ CONFORME |
| dashboard.php | PHP | Aula 13 (sessão protegida) | ✅ CONFORME |
| logout.php | PHP | Aula 13 (session_destroy) | ✅ CONFORME |
| listagem.php | PHP | Aula 15 — listagem.php | ✅ CONFORME |
| conexao.php | PHP | Aula 14/15 (conexão padrão) | ✅ CONFORME |
| criar_banco.sql | SQL | Estrutura necessária Aula 14/15 | ✅ CONFORME |

**Total: 14/14 arquivos em conformidade com os padrões das Aulas Professor.**

---

## 4. Observações Técnicas

### Diferença aceitável — `strrpos()` em `cadastro.php`
- **Aulas Professor** usam: `strrpos($_POST["nome"],"drop") > 0`
- **n2/cadastro.php** usa: `strrpos($_POST["nome"],"drop") !== false`
- A versão do n2 é **mais correta** — o operador `!== false` detecta palavras no início da string (índice 0), que a versão do professor não detectaria. Não é uma divergência de padrão; é uma correção do comportamento esperado.

### Arquivos exclusivos da N2 (sem correspondente nas aulas, mas coerentes)
- `criar_banco.sql` — script de criação do banco; não há equivalente nas aulas mas é necessário para a atividade funcionar
- `duck_header.png`, `duck_chefe.jpg` — recursos visuais; referenciados nos HTML como `<img src="...">`, padrão da Aula 3

---

## 5. Conclusão

Todos os **14 arquivos** presentes no diretório `n2/` foram analisados e validados.  
A estrutura e o código seguem os padrões pedagógicos estabelecidos nas pastas `Aulas Professor/aula13_Seguranca_PHP`, `Aulas Professor/AULA14_Seguranca_PHP` e `Aulas Professor/AULA15_FERRAMENTAS_PHP_REPOSICAO`, com as seguintes atividades cobertas:

| Atividade Proposta | Arquivo em n2 | Status |
|---|---|---|
| Conexão PHP com MySQL | `cadastro.php`, `login.php`, `listagem.php`, `conexao.php` | ✅ |
| Criação do banco e tabela | `criar_banco.sql` | ✅ |
| Cadastro de funcionários (INSERT) | `cadastro.php` | ✅ |
| Validação de formulário em PHP | `cadastro.php` (`processa_formulário()`), `login.php` (`processa_login()`) | ✅ |
| Proteção contra SQL Injection | `cadastro.php` (`strrpos()` com keywords SQL) | ✅ |
| Listagem dinâmica (SELECT) | `listagem.php` | ✅ |
| Sistema de login | `login.php` | ✅ |
| Sessão com `session_start()` | `login.php`, `dashboard.php`, `logout.php` | ✅ |
| Dashboard protegido | `dashboard.php` (`isset($_SESSION["usuario"])`) | ✅ |
| Logout do sistema | `logout.php` (`session_destroy()`) | ✅ |
