# Relatório de Auditoria e Testes — N2 Duck Tech — 2026-06-12

## 1. Metodologia

Auditoria realizada por comparação linha a linha de cada arquivo da pasta `n2/` contra os arquivos de referência em `Aulas Professor/`. Testes de execução no LAMPP local foram tentados e os resultados (incluindo bloqueios) estão documentados na seção 4.

---

## 2. Auditoria de Conformidade — Arquivos vs Aulas Professor

### 2.1 `listagem.php`

**Referência:** `AULA15_FERRAMENTAS_PHP_REPOSICAO/listagem.php`

| Elemento | Professor | n2/listagem.php | Status |
|---|---|---|---|
| Conexão inline (`$host`, `$username`...) | ✅ | ✅ | CONFORME |
| `mysqli_connect()` com `or die` | ✅ | ✅ | CONFORME |
| `if (mysqli_connect_errno())` | ✅ | ✅ | CONFORME |
| `$sql = "select id, nome, cargo, email from funcionarios order by nome"` | ✅ | ✅ | CONFORME |
| `$result = mysqli_query($con,$sql)` | ✅ | ✅ | CONFORME |
| `if (!$result) { die("Erro na consulta...") }` | ✅ | ✅ | CONFORME |
| `while($row = mysqli_fetch_assoc($result))` | ✅ | ✅ | CONFORME |
| `echo "fim de listagem"` | ✅ | ✅ | CONFORME |
| `mysqli_close($con)` | ✅ | ✅ | CONFORME |
| Saída em `<table>` com CSS | Instrução explícita no comentário da AULA15 | ✅ implementado | CONFORME |

**Resultado: APROVADO — 10/10 elementos conformes.**

---

### 2.2 `cadastro.php`

**Referência:** `AULA14_Seguranca_PHP/cadastro.php` e `aula14-3.php`

| Elemento | Professor | n2/cadastro.php | Status |
|---|---|---|---|
| `function processa_formulário()` | ✅ | ✅ | CONFORME |
| Verificação de campos obrigatórios com `echo` + link Voltar + `exit` | ✅ | ✅ | CONFORME |
| Anti-SQLi: condição `if ($campo!="")` | `if ($_GET["nome"]!="")` | `if ($_POST[$campo]!="")` | CONFORME (sintaxe idêntica) |
| Anti-SQLi: operador `strrpos() > 0` | `> 0` | `> 0` ✅ (**corrigido — era `!==false`**) | CONFORME |
| Anti-SQLi: palavras `drop, update, insert, delete, select` | ✅ | ✅ | CONFORME |
| Anti-SQLi: `echo "campo Invalido"` + link Voltar + `exit` | ✅ | ✅ | CONFORME |
| `if ((isset($_POST["nome"]))&&(isset($_POST["email"]))) { processa_formulário(); }` | ✅ (com GET) | ✅ (com POST) | CONFORME |
| Variáveis `$nome = $_POST["nome"]` etc. para todos os campos | ✅ (incompleto no modelo) | ✅ (completo) | CONFORME |
| `$sql = "INSERT INTO funcionarios (...) VALUES (...)"`com concatenação de variáveis | ✅ | ✅ | CONFORME |
| Conexão inline (`$host`, `$username`, `$password`, `$db_name`) | ✅ | ✅ | CONFORME |
| `$con=mysqli_connect(...)` + `if (mysqli_connect_errno())` | ✅ | ✅ | CONFORME |
| `$result = mysqli_query($con,$sql)` | ✅ | ✅ | CONFORME |
| `if (!$result) { die("Erro na inclusao: "...) }` | ✅ | ✅ | CONFORME |
| `else { mysqli_close($con); echo "...cadastrado..."; exit; }` | ✅ | ✅ | CONFORME |
| `ucfirst()` na mensagem de erro | ❌ (não está no modelo) | ❌ (**removido**) | CONFORME |

**Nota sobre `$_POST` vs `$_GET`:** O modelo do professor usa `method="GET"`. O n2 usa `method="POST"` por ser um formulário que contém campo de senha — enviar senha via GET exporia a credencial na URL do navegador. Esta adaptação é anterior às modificações desta sessão e constitui aplicação correta de segurança do conteúdo ensinado na matéria.

**Nota sobre `foreach`:** O professor comenta explicitamente *"Repita para os outros campos"* na seção anti-SQLi. O `foreach` sobre `$campos_texto` é a implementação direta dessa instrução.

**Resultado: APROVADO — todos os elementos conformes após correção do operador `strrpos`.**

---

### 2.3 `cadastro.html`

**Referência:** `aula12_Seguranca_JAVASCRIPT/aula12-1.html`, `aula12-2.html`, `AULA14_Seguranca_PHP/cadastro.html`

| Elemento | Professor | n2/cadastro.html | Status |
|---|---|---|---|
| `<script type="text/javascript">` | ✅ | ✅ | CONFORME |
| `function verifica_formulario()` | ✅ (`aula12-1.html`, `AULA14/cadastro.html`) | ✅ | CONFORME |
| Campo vazio: `if (cadastro.campo.value=="")` | ✅ | ✅ | CONFORME |
| `alert("...")` + `.focus()` + `return false` | ✅ | ✅ | CONFORME |
| `return true` ao final | ✅ | ✅ | CONFORME |
| `<select>` com `selectedIndex==0` | ✅ (`aula12-2.html`) | ✅ (UF e Cargo) | CONFORME |
| `<form name="cadastro" ... onsubmit="return verifica_formulario()">` | ✅ | ✅ | CONFORME |

**Resultado: APROVADO — 7/7 elementos conformes.**

---

### 2.4 `conexao.php`

**Referência:** Padrão de conexão da AULA14/AULA15

O arquivo `conexao.php` existe na pasta mas **não é chamado por nenhum arquivo PHP** (ambos `cadastro.php` e `listagem.php` usam conexão inline, conforme o padrão das aulas). O arquivo não causa problema — pode ser mantido ou removido a critério do grupo.

---

## 3. Correção Realizada Nesta Sessão

| Arquivo | Linha(s) | Antes | Depois | Motivo |
|---|---|---|---|---|
| `cadastro.php` | 44–50 | `strrpos(...) !== false` / `ucfirst($campo)` | `strrpos(...) > 0` / `echo $campo` | Operador e formatação divergiam do padrão das aulas |

---

## 4. Testes no Ambiente LAMPP

### 4.1 Estado dos Serviços

| Serviço | Comando testado | Resultado |
|---|---|---|
| LAMPP start | `/opt/lampp/lampp start` | **BLOQUEADO** — instalação 32-bit sem `libcrypt.so.1` |
| MySQL manual | `/opt/lampp/bin/mysqld_safe` | **BLOQUEADO** — PID file `/opt/lampp/var/mysql/pop-os.pid` sem permissão de escrita (requer root) |
| Apache | detecção de processo | Não encontrado em execução |
| Sintaxe PHP (CLI) | `/opt/lampp/bin/php -l` | **BLOQUEADO** — `libcrypt.so.1: cannot open shared object file` |
| HTTP local | `curl http://localhost/n2/` | `000` — conexão recusada (Apache inativo) |

### 4.2 Estado do Deploy em `/opt/lampp/htdocs/n2/`

| Arquivo | htdocs/n2 | Workspace n2 | Diferença |
|---|---|---|---|
| `cadastro.php` | Versão antiga (maio/26) — `!==false`, duplicação de conexão | Versão corrigida | **Precisa atualizar** |
| `cadastro.html` | Sem `verifica_formulario()` | Com validação JS | **Precisa atualizar** |
| `listagem.php` | **Ausente** | Presente e correto | **Precisa copiar** |
| `conexao.php`, `criar_banco.sql`, demais arquivos | Presentes | Presentes | Sem diferença |

### 4.3 Arquivos Encontrados em `htdocs/n2/_arquivados/`

Foram encontrados arquivos arquivados que **não fazem parte do material das aulas**: `login.php` e `logout.php` usam `session_start()` e `$_SESSION` — recurso não ensinado pelo professor. Estes arquivos estão corretamente arquivados e não devem ser ativados na entrega da N2.

---

## 5. Procedimento para Ativar e Testar o LAMPP

Execute os seguintes comandos no terminal com permissão de administrador:

```bash
# 1. Iniciar o LAMPP
sudo /opt/lampp/lampp start

# 2. Atualizar os arquivos no htdocs
sudo cp /home/efraim/Documents/GitHub/GitBook/Desenvolvimento/fatec/n2/cadastro.php /opt/lampp/htdocs/n2/
sudo cp /home/efraim/Documents/GitHub/GitBook/Desenvolvimento/fatec/n2/cadastro.html /opt/lampp/htdocs/n2/
sudo cp /home/efraim/Documents/GitHub/GitBook/Desenvolvimento/fatec/n2/listagem.php /opt/lampp/htdocs/n2/

# 3. Criar o banco (se necessário)
/opt/lampp/bin/mysql -u root -e "source /opt/lampp/htdocs/n2/criar_banco.sql"

# 4. Acessar no navegador
# http://localhost/n2/index.html
```

### Checklist de testes manuais após LAMPP ativo:

- [ ] `http://localhost/n2/index.html` — carrega menu lateral e header
- [ ] Clicar em **Cadastro** → formulário abre no iframe
- [ ] Submeter com campo vazio → `alert()` JavaScript aparece (valida JS)
- [ ] Submeter com `drop` no campo nome → PHP exibe "nome Invalido" (valida anti-SQLi)
- [ ] Submeter dados válidos → "Funcionário cadastrado com sucesso"
- [ ] Clicar em **Listagem** → tabela exibe o funcionário cadastrado
- [ ] Última linha da listagem: "fim de listagem"

---

## 6. Conclusão

| Arquivo | Conformidade com Aulas | Observação |
|---|---|---|
| `listagem.php` | ✅ APROVADO | Segue AULA15 integralmente |
| `cadastro.php` | ✅ APROVADO | Corrigido nesta sessão (`strrpos > 0`) |
| `cadastro.html` | ✅ APROVADO | Segue Aula12 + AULA14 |
| `conexao.php` | N/A | Não utilizado; não causa problemas |
| `login.php` / `dashboard.php` | ⚠️ ARQUIVADO | Usam `session_start()` — fora do escopo das aulas |

**Deploy no LAMPP:** bloqueado por ausência de permissão root no ambiente de execução. Os comandos necessários estão documentados na seção 5.
