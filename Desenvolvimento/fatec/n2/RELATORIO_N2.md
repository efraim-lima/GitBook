# Relatório de Atividade — 2026-06-12

## Resumo

Análise e implementação de módulos faltantes no projeto N2 (Duck Tech) com base no material de aulas do professor Mardel, habilitando o cadastro funcional via LAMPP e a consulta dinâmica de funcionários.

---

## Diagnóstico — Estado Inicial

| Arquivo | Status | Problema Identificado |
|---|---|---|
| `listagem.php` | **AUSENTE** | Menu do `index.html` aponta para `listagem.php`, mas o arquivo não existia. Só existia `lista.html` estático com dados fixos. |
| `cadastro.php` | **INCOMPLETO** | Duplicava as 5 linhas de conexão já existentes em `conexao.php` (`$host`, `$username`, `$password`, `$db_name`, `mysqli_connect`). O arquivo `conexao.php` existia mas não era utilizado por nenhum script. |
| `cadastro.html` | **INCOMPLETO** | Ausência de validação JavaScript no cliente. O padrão `verifica_formulario()` com `onsubmit` foi ensinado nas Aulas 12 e 14, mas não estava implementado. |

---

## Alterações Realizadas

### 1. CRIADO — `listagem.php`

**Arquivo:** `Desenvolvimento/fatec/n2/listagem.php`  
**Referência nas aulas:** AULA15 (`listagem.php`), AULA14 (`aula14-3.php`), AULA13 (`aula13-5.php`)

**O que foi implementado:**
- `include 'conexao.php'` para reusar a conexão existente (evita duplicação)
- Formulário de pesquisa via `method="GET"` com campo `pesquisa` (padrão ensinado na AULA13/14)
- `isset($_GET["pesquisa"])` para verificação do campo antes do acesso (padrão AULA13)
- Validação anti-SQL Injection com `strrpos()` para `drop`, `update`, `insert`, `delete`, `select` (padrão AULA14)
- `$sql = "select id, nome, cargo, email from funcionarios..."` com filtro opcional `WHERE nome LIKE '%$pesquisa%'`
- `$result = mysqli_query($con, $sql)` (padrão AULA15)
- `while($row = mysqli_fetch_assoc($result))` para iterar e exibir resultados (padrão AULA15)
- Saída em formato `<table>` com `<th>` e `<td>` (conforme orientação do comentário na AULA15: "AJUSTE O HTML PARA HTML EM FORMATO TABLE e CSS")
- `echo "fim de listagem"` (padrão AULA15)
- `mysqli_close($con)` ao final (padrão AULA15)
- CSS visual idêntico ao padrão do projeto (cores `#1C1526`, `#2D2540`, `#F2A413`)

---

### 2. MODIFICADO — `cadastro.php`

**Arquivo:** `Desenvolvimento/fatec/n2/cadastro.php`  
**Referência nas aulas:** AULA14 (`cadastro.php`), `conexao.php` existente

**O que foi alterado:**

| Antes | Depois |
|---|---|
| Repetia `$host`, `$username`, `$password`, `$db_name` e `mysqli_connect()` inline | `include 'conexao.php';` — reutiliza a conexão já definida |
| Bloco `if (mysqli_connect_errno())` duplicado | Removido (já tratado dentro de `conexao.php`) |

A lógica da função `processa_formulário()`, as validações de campos obrigatórios, as verificações anti-SQL Injection, o `mysqli_query()`, o tratamento de erro e o `mysqli_close()` foram **preservados sem alteração**.

---

### 3. MODIFICADO — `cadastro.html`

**Arquivo:** `Desenvolvimento/fatec/n2/cadastro.html`  
**Referência nas aulas:** Aula12 (`aula12-1.html`, `aula12-2.html`), AULA14 (`cadastro.html`)

**O que foi adicionado:**

- Bloco `<script type="text/javascript">` com função `verifica_formulario()` (padrão Aula12)
- Validações de campos de texto vazios com `alert()` + `.focus()` (padrão `aula12-1.html`)
- Validação de `<select>` com `selectedIndex==0` para UF e Cargo (padrão `aula12-2.html`)
- `name="cadastro"` no elemento `<form>` (necessário para acesso JS via `cadastro.campo`)
- `onsubmit="return verifica_formulario()"` no elemento `<form>` (padrão Aula12/AULA14)

---

## Técnicas das Aulas Aplicadas

| Técnica | Aula de Referência | Arquivo Alterado |
|---|---|---|
| `mysqli_connect()` | AULA15 `listagem.php` | `listagem.php` (via `conexao.php`) |
| `mysqli_query()` | AULA15 `listagem.php` | `listagem.php`, `cadastro.php` |
| `mysqli_fetch_assoc()` + `while` | AULA15 `listagem.php` | `listagem.php` |
| `mysqli_close()` | AULA15 `listagem.php` | `listagem.php` |
| `isset($_GET[...])` | AULA13 `aula13-4.php` | `listagem.php` |
| SQL Injection check com `strrpos()` | AULA14 `aula14-3.php` | `listagem.php` |
| Formulário GET + campo de pesquisa | AULA13 `aula13-5.php` | `listagem.php` |
| `include 'conexao.php'` | Módulo existente no n2 | `cadastro.php`, `listagem.php` |
| `function verifica_formulario()` | Aula12 `aula12-1.html` | `cadastro.html` |
| `selectedIndex==0` para `<select>` | Aula12 `aula12-2.html` | `cadastro.html` |
| `onsubmit="return verifica_formulario()"` | Aula12 / AULA14 | `cadastro.html` |

---

## Arquivos NÃO Alterados

- `conexao.php` — funcional e correto para LAMPP (host `localhost`, usuário `root`, senha vazia)
- `criar_banco.sql` — estrutura da tabela `funcionarios` correta e pronta para uso
- `index.html`, `home.html`, `sobre.html`, `header.html`, `style.css` — sem lacunas em relação ao material das aulas
- `lista.html` — mantido (não está linkado no menu; `listagem.php` o substitui funcionalmente)

---

## Como Usar no LAMPP (Linux)

1. Copiar toda a pasta `n2/` para `/opt/lampp/htdocs/n2/`
2. Iniciar o LAMPP: `sudo /opt/lampp/lampp start`
3. Criar o banco: acessar `http://localhost/phpmyadmin` → importar `criar_banco.sql`
4. Acessar o site: `http://localhost/n2/index.html`
5. Cadastrar funcionário via menu **Cadastro**
6. Consultar via menu **Listagem** (campo de pesquisa por nome disponível)

---

## Próximos Passos

- [ ] Testar cadastro e listagem no ambiente LAMPP
- [ ] Enviar para o email do professor conforme prazo da N2
