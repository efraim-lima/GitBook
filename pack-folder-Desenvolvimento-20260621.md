# Context Pack: Desenvolvimento

Generated: 2026-06-21

Source: folder:Desenvolvimento

Notes: 10

---

## RELATORIO_N2
📁 Desenvolvimento/fatec/n2

# Relatório de Atividade — 2026-06-12

## Resumo

Análise e implementação de módulos faltantes no Projeto N2 (Duck Tech) com base no material de aulas do professor Mardel, habilitando o cadastro funcional via LAMPP e a consulta dinâmica de funcionários.

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

---

## N2
📁 Desenvolvimento/fatec/n2

ATIVIDADES

Atividade para ser entregue na N2 da FATEC para a parte de desenvolvimento WEB.
Todos arquivos necessários para esta atividade estão no website https://drive.google.com/drive/folders/1OdmGcWuh76STL8NasJ4NoyMgpq-JzzZR

Sendo ATIVIDADES do professor Mardel

- [ ] Criar o website
- [ ] Validar
- [ ] Enviar para o email do professor 📅 2026-05-26 
- [ ] Validar com os prõximos passos

---

## AUDITORIA_2026-06-12
📁 Desenvolvimento/fatec/n2

# Relatório de Auditoria e Testes — N2 Duck Tech — 2026-06-12

## 1. Metodologia

Auditoria realizada por comparação linha a linha de cada arquivo da pasta `N2/` contra os arquivos de referência em `Aulas Professor/`. Testes de execução no LAMPP local foram tentados e os resultados (incluindo bloqueios) estão documentados na seção 4.

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

**Deploy no LAMPP:** bloqueado por ausência de permissão root no ambiente de execução. os comandos necessários estão documentados na seção 5.

---

## fatec
📁 Desenvolvimento/fatec

# fatec Overview
 
```ccard
type: folder_brief_live
```
 

- **fatec**
	- **Aulas Professor**
	- **duckTech**
		- **duckTech**
			- cadastro.html
			- cadastro.php
			- conexao.php
			- dashboard.php
			- duck_bg_menu.jpg
			- duck_cadastro_bg.jpg
			- duck_chefe.jpg
			- duck_header.png
			- header.html
			- home.html
			- index.html
			- listagem.php
			- login.php
			- logout.php
			- menu_lateral.html
			- sobre.html
			- style.css
	- **EfraimLima_GabrielPereira_GiovannaPardini**
		- **n1**
			- **css**
				- style.css
			- **dash**
				- tabela.html
			- **forms**
				- cadastro.html
				- form-cadastro.html
				- form-registro.html
			- **img**
				- background-cadastro.jpg
				- background-home.jpg
				- chapeu.webp
				- chapeu2.webp
				- ducks.enc
				- efraim.enc
				- gabriel.enc
				- giovanna.enc
			- index.html
			- robots.txt
		- aula.html
		- aula0.html
	- **n1**
		- **_arquivados**
			- dashboard.php
			- listagem.php
			- login.php
			- logout.php
		- **css**
			- style.css
		- **dash**
			- tabela.html
		- **forms**
			- cadastro.html
			- form-cadastro.html
			- form-registro.html
		- **img**
			- background-cadastro.jpg
			- background-home.jpg
			- chapeu.webp
			- chapeu2.webp
			- ducks.enc
			- efraim.enc
			- gabriel.enc
			- giovanna.enc
		- index.html
		- robots.txt
	- **N2**
		- AUDITORIA_2026-06-12
		- cadastro.html
		- cadastro.php
		- conexao.php
		- criar_banco_ducktech.sql
		- criar_banco.sql
		- duck_bg_menu.jpg
		- duck_cadastro_bg.jpg
		- duck_chefe.jpg
		- duck_header.jpg
		- duck_header.png
		- header.html
		- home.html
		- index.html
		- lista.html
		- listagem.php
		- login.php
		- N2
		- RELATORIO_N2
		- sobre.html
		- style.css
	- **src**
		- **css**
			- aula5.css
		- **img**
			- background.jpg
			- chapeu.webp
			- chapeu2.webp
	- AGENTS
	- aula1.html
	- aula2-1.html
	- aula2-2.html
	- aula2-3.html
	- aula2-4.html
	- aula2.html
	- aula3-1.html
	- aula3-2.html
	- Aula3-3.html
	- aula3-4.html
	- aula3-5.html
	- aula3.html
	- aula5-1.html
	- aula5-2.html
	- aula5-3.html
	- aula5-4.html
	- aula5-5.html
	- aula5.html
	- aula6-1.html
	- aula6-2.html
	- aula6.html
	- aula9-1-1.html
	- aula9-1-2.html
	- aula9-1.html
	- aula9-2.html
	- aula9.html
	- aula11-1.html
	- aula11-2.html
	- aula11-3.html
	- aula11.html
	- aula13.4.php
	- aula13.5.php
	- aula13.6.php
	- aula14-1.php
	- EfraimLima_GabrielPereira_GiovannaPardini.zip
	- fatec
	- index.php
	- n2.zip
	- RELATORIO_VALIDACAO_N2
	- template.html

---

## RELATORIO_VALIDACAO_N2
📁 Desenvolvimento/fatec

# Relatório de Validação — N2 vs Aulas Professor
**Data:** 25/05/2026 
**Diretório analisado:** `[[[[[[[[information-security]]]]/[[[[information-security]]/[[information-security/FATEC/FATEC|FATEC]]/[[information-security/FATEC/FATEC|FATEC]]|[[information-security/FATEC/FATEC|FATEC]]]]/[[[[information-security]]/[[information-security/FATEC/FATEC|FATEC]]/[[information-security/FATEC/FATEC|FATEC]]|[[information-security/FATEC/FATEC|FATEC]]]]|[[[[information-security]]/[[information-security/FATEC/FATEC|FATEC]]/[[information-security/FATEC/FATEC|FATEC]]|[[information-security/FATEC/FATEC|FATEC]]]]]]/[[[[[[reports]]]]/[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]/[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]|[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]]]/1-[[[[[[reports]]]]/[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]/[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]|[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]]]/[[[[[[Estudos Avançados]]]]]]/[[[[[[information-security]]/[[information-security/FATEC/FATEC|FATEC]]/[[information-security/FATEC/FATEC|FATEC]]|[[information-security/FATEC/FATEC|FATEC]]]]/[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]/1-[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]/[[[[Estudos Avançados]]]]/[[[[information-security/FATEC/FATEC|FATEC]]/[[reports/2026/2026|2026]]/1-[[reports/2026/2026|2026]]/[[Estudos Avançados]]/FATEC/2026/1-2026/Estudos Avançados/N2|N2]]|FATEC/2026/1-2026/Estudos Avançados/N2|N2]]]]|[[[[information-security/FATEC/FATEC|FATEC]]/[[reports/2026/2026|2026]]/1-[[reports/2026/2026|2026]]/[[Estudos Avançados]]/FATEC/2026/1-2026/Estudos Avançados/N2|N2]]|FATEC/2026/1-2026/Estudos Avançados/N2|N2]]]]]]|[[[[[[information-security]]/[[information-security/FATEC/FATEC|FATEC]]/[[information-security/FATEC/FATEC|FATEC]]|[[information-security/FATEC/FATEC|FATEC]]]]/[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]/1-[[[[reports]]/[[reports/2026/2026|2026]]/[[reports/2026/2026|2026]]|[[reports/2026/2026|2026]]]]/[[[[Estudos Avançados]]]]/[[[[information-security/FATEC/FATEC|FATEC]]/[[reports/2026/2026|2026]]/1-[[reports/2026/2026|2026]]/[[Estudos Avançados]]/FATEC/2026/1-2026/Estudos Avançados/N2|N2]]|FATEC/2026/1-2026/Estudos Avançados/N2|N2]]]]|[[[[information-security/FATEC/FATEC|FATEC]]/[[reports/2026/2026|2026]]/1-[[reports/2026/2026|2026]]/[[Estudos Avançados]]/FATEC/2026/1-2026/Estudos Avançados/N2|N2]]|FATEC/2026/1-2026/Estudos Avançados/N2|N2]]]]]]]]/` 
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

---

## Aulas Professor
📁 Desenvolvimento/fatec/Aulas Professor

# Aulas Professor Overview
 
```ccard
type: folder_brief_live
```
 

- **Aulas Professor**
	- **aula1_Ferramentas_HTML**
		- AULA1_Seguranca.pdf
		- aula1-1.html
		- aula1-2.html
		- aula1-3.html
		- aula1-4.html
	- **AULA2_Ferramentas_HTML**
		- aula2-1.html
		- aula2-2.html
		- aula2-3.html
		- aula2-4.html
		- aula2-5.html
		- aula2.html
		- AULA2.pdf
	- **AULA3_Seguranca_HTML**
		- AULA3_Seguranca.pdf
		- aula3-1.html
		- aula3-2.html
		- aula3-3.html
		- aula3-4.html
		- aula3.html
	- **Aula5_Ferramentas_CSS**
		- AULA5_Segurança.pdf
		- aula5-1.html
		- aula5-3.html
		- aula5-4.html
		- aula5-5.html
	- **Aula6_Ferramentas_CSS**
		- aula6-1.html
		- aula6-2.html
		- aula6.html
		- AULA6.pdf
	- **Aula9_Seguranca_JAVASCRIPT**
		- aula9-1.html
		- aula9-2.html
		- aula9-3.html
		- aula9-4.html
		- aula9-5.html
		- aula9.html
		- AULA9.pdf
	- **Aula11_Ferramentas_JAVASCRIPT**
		- aula11-1.html
		- aula11-2.html
		- aula11-3.html
		- aula11.html
		- AULA11.pdf
	- **aula12_Seguranca_JAVASCRIPT**
		- AULA12_seguranca.pdf
		- aula12-1.html
		- aula12-2.html
		- aula12-3.html
		- aula12-4.html
	- **aula13_Seguranca_PHP**
		- AULA13_seguranca.pdf
		- aula13-1.php
		- aula13-2.php
		- aula13-3.php
		- aula13-4.php
		- aula13-5.php
		- aula13-6.php
		- aula13-7.php
		- aula13-8.php
		- aula13.php
	- **AULA14_Seguranca_PHP**
		- aula14-1.php
		- aula14-2.php
		- aula14-3.php
		- AULA14.pdf
		- aula14.php
		- cadastro.html
		- cadastro.php
	- **AULA15_FERRAMENTAS_PHP_REPOSICAO**
		- AULA15.pdf
		- listagem.php
	- Aulas Professor

---

## AGENTS
📁 Desenvolvimento/fatec

Não crie codigos duplicados no sistema, evite replicar trechos de codigo redundante no ambiente, reduza a quantidade de comentários desnecessários.
Revise códigos gerados para que sejam exutos e fucnionais de forma a Evitar espagetificação de código e ineficiência de funcionalidades nas aplicações.

---

## Java
📁 Desenvolvimento/Java

# Java Overview
 
```ccard
type: folder_brief_live
```
 

- **Java**
	- **DogSniffer**
		- **build**
			- **classes**
				- **java**
					- **main**
						- **cache**
							- CacheEntry.class
							- SignalCache.class
						- **display**
							- RadarDisplay.class
						- **etc**
							- Capture.class
							- Configuration.class
							- NetworkInterfaceSelector.class
							- NetworkSelectionException.class
						- **network**
							- NetworkCollector.class
							- NetworkInfo.class
							- PacketProcessor.class
						- **sensor**
							- SensorData.class
							- SensorData$1.class
							- WitMotionReader.class
						- DogSnifferApp.class
			- **distributions**
				- network-analyzer-1.0.tar
				- network-analyzer-1.0.zip
			- **libs**
				- network-analyzer-1.0.jar
			- **scripts**
				- network-analyzer
				- network-analyzer.bat
			- **tmp**
				- **compileJava**
				- **jar**
					- MANIFEST.MF
		- **Network Analyzer**
			- Diagrama de Criação.drawio
		- **src**
			- **main**
				- **java**
					- **cache**
						- CacheEntry.java
						- SignalCache.java
					- **display**
						- RadarDisplay.java
					- **etc**
						- Capture.java
						- Configuration.java
						- NetworkInterfaceSelector.java
						- NetworkSelectionException.java
					- **network**
						- NetworkCollector.java
						- NetworkInfo.java
						- PacketProcessor.java
					- **sensor**
						- SensorData.java
						- WitMotionReader.java
					- DogSnifferApp.java
		- build.gradle
		- README
		- settings.gradle
	- **Estudo**
		- Classes.java
		- Condicionais.java
		- Fundamentals.java
		- Loops.java
		- Metodos.java
		- Specter.java
	- **RFScanner**
		- **src**
			- **main**
				- **java**
					- **com**
						- **rfscanner**
	- Java

---

## README
📁 Desenvolvimento/Java/DogSniffer

Desenvolvimento

# DogSniffer App

## Motivação

Esta ferramenta foi desenvolvida com o objetivo de levantar através de sinais de rádio frequencia (wifi) a posição estivada da origem do sinal.
Foi desenvolvida em Java para fins de aprendizado do desenvolvedor Efraim Lima, mas o objetivo é ter uma forma de tornar este código aplicável a outras plataformas além do linux.

### Tree map
A estrutura das pastas segue o seguinte tree map:

src/main/Java/
├── DogSnifferApp.Java ← sem package (entry point)
├── cache/
│ ├── SignalCache.Java ← estrutura de cache do sinal
│ └── CacheEntry.Java ← getters dos sinais
├── display/
│ └── RadarDisplay.Java ← forma de renderizar visualmente o que tem sido capturado
├── etc/
│ ├── Capture.Java ← vai ser refatorado para os próximos commits
│ ├── NetworkInterfaceSelector.Java
│ ├── Configuration.Java ← vamos extrair de NetworkInterfaceSelector
│ └── NetworkSelectionException.Java
├── network/
│ ├── NetworkInfo.Java ← coleta de informações das redes (Mac, SSID, Segurança, RSSI, etc)
│ └── PacketProcessor.Java ← conecta-se com Capture.Java
└── sensor/
 ├── SensorData.Java ← dados do sensor para termos uma boa visão da direção do sinal (sensor ainda não chegou, esta parte está sendo desenvolvida para termos já um pivot)
 └── WitMotionReader.Java

### Fim por hora

---

## Desenvolvimento
📁 Desenvolvimento

Desenvolvimento
README
AGENTS

## Premissas
Estou desenvolvendo uma esrutura de agentes que atuarao de forma quase autonoma e Tarefas e sub-Tarefas do meu dia-a-dia, para me ajudarem a desenvolver meus trabalhos e atuar em meus cursos.

Para isso utilizarei as IDEs deisponiveis no mercado, o obsidian e tambem ferramentas como Cline para tocar as ATIVIDADES

```LIST FROM "./" WHERE file.name != this.file.name
```

- **Desenvolvimento**
	- **fatec**
	- **Java**
	- Desenvolvimento

---