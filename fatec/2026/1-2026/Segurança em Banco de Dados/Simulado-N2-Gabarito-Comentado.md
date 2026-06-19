# Simulado N2 — Gabarito Comentado
**Disciplina:** Segurança em Bancos de Dados  
**Professor:** Thiago de Jesus Inocêncio  
**Banco utilizado:** `mundo` (cidades, paises, linguas)  
**Pontuação total:** 10 pontos

---

## Schema do banco `mundo` (referência rápida)

```
┌──────────────────────────────────┐
│             paises               │
├──────────────────────────────────┤
│ 🔑 id_pais       CHAR(3)         │
│    id_cidade     INT             │   ← FK para cidades
│    nome          VARCHAR(52)     │
│    codigo_pais   CHAR(2)         │
└──────────┬───────────────────────┘
           │ ON c.id_pais = p.id_pais
           │
┌──────────▼───────────────────────┐     ┌───────────────────────────────┐
│            cidades               │     │           linguas             │
├──────────────────────────────────┤     ├───────────────────────────────┤
│ 🔑 id_cidade  INT                │     │ 🔑 id_lingua   VARCHAR(45)    │
│    id_pais    CHAR(3)  FK        │     │ 🔑 id_pais     CHAR(3)  FK    │
│    nome       VARCHAR(35)        │     │    oficial     ENUM('T','F')  │
│    estado     VARCHAR(40)        │     │    porcentagem DECIMAL(4,2)   │
│    informacoes JSON              │     └───────────────────────────────┘
└──────────────────────────────────┘
```

> **Atenção:** O arquivo `mundo.sql` usa nomes em inglês (`city`, `country`, `countrylanguage`).  
> A prova usa os nomes traduzidos: `cidades`, `paises`, `linguas`.

---

## Questão 1 — SELECT com INNER JOIN (1 ponto)

### Enunciado
> Selecione o nome da cidade (campo `nome` da tabela `cidades`) e o nome do país (campo `nome` da tabela `paises`). Utilize INNER JOIN.

### Resposta

```sql
SELECT c.nome AS cidade,
       p.nome AS pais
FROM cidades c
INNER JOIN paises p
    ON c.id_pais = p.id_pais;
```

### Explicação linha a linha

| Linha | Código | O que faz |
|-------|--------|-----------|
| 1 | `SELECT c.nome AS cidade` | Seleciona a coluna `nome` da tabela `cidades` (apelida como `c`) e renomeia o resultado para `cidade` |
| 2 | `p.nome AS pais` | Seleciona a coluna `nome` da tabela `paises` (apelida como `p`) e renomeia para `pais` |
| 3 | `FROM cidades c` | Define `cidades` como tabela principal; `c` é o alias (apelido) para abreviar nas referências |
| 4 | `INNER JOIN paises p` | Declara o join com a tabela `paises`, apelidada de `p` |
| 5 | `ON c.id_pais = p.id_pais` | Condição de junção: une as duas tabelas pelo campo `id_pais`, que é chave estrangeira em `cidades` e chave primária em `paises` |

### Por que usar alias (`c`, `p`)?
Porque **ambas as tabelas têm uma coluna chamada `nome`**. Sem o prefixo `c.nome` e `p.nome`, o banco retornaria erro de ambiguidade: *"Column 'nome' in field list is ambiguous"*.

### Por que INNER JOIN?
O INNER JOIN retorna **somente** as linhas que possuem correspondência nas duas tabelas. Cidades sem país cadastrado ou países sem nenhuma cidade são excluídos do resultado. É o join mais comum e o mais eficiente quando não há interesse em registros sem correspondência.

### Resultado esperado (10 primeiras linhas)

| cidade | pais |
|--------|------|
| Kabul | Afghanistan |
| Qandahar | Afghanistan |
| Herat | Afghanistan |
| Mazar-e-Sharif | Afghanistan |
| Amsterdam | Netherlands |
| Rotterdam | Netherlands |
| Haag | Netherlands |
| Utrecht | Netherlands |
| Eindhoven | Netherlands |
| Tilburg | Netherlands |

> A ordem depende da ordem física das linhas na tabela. Para garantir ordem alfabética, adicione `ORDER BY p.nome, c.nome`.

---

## Questão 2 — Stored Procedure `cidade_pais_info` (1,5 pontos)

### Enunciado
> Qual código você usaria para criar uma Stored Procedure chamada `cidade_pais_info` da consulta da questão 1?

### Resposta

```sql
DELIMITER $$

CREATE PROCEDURE cidade_pais_info()
BEGIN
    SELECT c.nome AS cidade,
           p.nome AS pais
    FROM cidades c
    INNER JOIN paises p
        ON c.id_pais = p.id_pais;
END $$

DELIMITER ;

CALL cidade_pais_info();
```

### Explicação linha a linha

#### Parte 1: Preparação — `DELIMITER $$`

```sql
DELIMITER $$
```

Por padrão, o MySQL/MariaDB usa `;` para sinalizar o fim de um comando.  
O problema: dentro do `BEGIN...END` também existem `;` (um para cada instrução interna).  
Se não mudarmos o delimitador, o client interpretaria o `;` interno como "fim da procedure" antes de ela estar completa.  

**Solução:** trocar o delimitador para `$$` temporariamente. Agora só `$$` termina o comando.

#### Parte 2: Criação — `CREATE PROCEDURE`

```sql
CREATE PROCEDURE cidade_pais_info()
```

- `CREATE PROCEDURE` — instrução DDL que cria a procedure no banco ativo.
- `cidade_pais_info` — nome da procedure (deve ser único no banco).
- `()` — lista de parâmetros. Vazia aqui porque a procedure não recebe argumentos.

#### Parte 3: Corpo — `BEGIN ... END`

```sql
BEGIN
    SELECT c.nome AS cidade,
           p.nome AS pais
    FROM cidades c
    INNER JOIN paises p
        ON c.id_pais = p.id_pais;
END $$
```

- `BEGIN` — abre o bloco de código da procedure.
- O `SELECT` dentro é idêntico à Q1 — a procedure apenas encapsula a consulta.
- `END $$` — fecha o bloco e usa `$$` (o delimitador atual) para sinalizar fim do comando.

#### Parte 4: Restaurar delimitador — `DELIMITER ;`

```sql
DELIMITER ;
```

Volta o delimitador ao padrão `;`. **Obrigatório** após criar a procedure, pois os comandos seguintes precisam usar `;` normalmente.

#### Parte 5: Execução — `CALL`

```sql
CALL cidade_pais_info();
```

Invoca a procedure. Os `()` são obrigatórios mesmo sem parâmetros.

### Vantagens de usar Stored Procedures
- **Reutilização:** o código fica salvo no banco, qualquer aplicação pode chamar `CALL cidade_pais_info()`.
- **Segurança:** pode-se dar permissão de `EXECUTE` a um usuário sem dar `SELECT` direto nas tabelas.
- **Manutenção:** alteração de lógica de negócio em um único lugar.
- **Performance:** procedures são pré-compiladas no banco.

---

## Questão 3 — Conceito RIGHT JOIN (1 ponto)

### Enunciado
> Com base na Figura 2 (diagrama de Venn do RIGHT JOIN), qual das afirmações é verdadeira?

### Resposta: **E**

> "O RIGHT JOIN retorna todas as linhas presentes na tabela2 e as correspondentes na table1."

### Por que cada alternativa está certa ou errada

| Alternativa | Afirmação | Análise |
|-------------|-----------|---------|
| A ❌ | Retorna apenas as linhas da table1 | Errado. Isso seria o LEFT JOIN excluindo não-matches, ou um filtro manual. |
| B ❌ | Retorna apenas as linhas que estão em ambas as tabelas | Errado. Isso descreve o INNER JOIN. |
| C ❌ | Retorna todas as linhas da table1, independente de correspondências na table2 | Errado. Isso descreve o LEFT JOIN. |
| D ❌ | Exclui todas as linhas que estão na table2 | Errado. É o oposto do correto. |
| E ✅ | Retorna todas as linhas da tabela2 e as correspondentes na table1 | **CORRETO.** Define exatamente o comportamento do RIGHT JOIN. |

### Explicação visual dos JOINs

```
INNER JOIN         LEFT JOIN          RIGHT JOIN
  ┌──┬──┐           ┌──┬──┐            ┌──┬──┐
  │  │██│           │██│██│            │  │██│
  │  │██│           │██│██│            │  │██│
  └──┴──┘           └──┴──┘            └──┴──┘
 (só a interseção)  (toda a esquerda)  (toda a direita)
```

### Comportamento prático no banco `mundo`

```sql
-- RIGHT JOIN: todos os países aparecem, mesmo sem cidades cadastradas
SELECT c.nome AS cidade, p.nome AS pais
FROM cidades c
RIGHT JOIN paises p ON c.id_pais = p.id_pais;
-- Resultado: países sem cidades aparecem com cidade = NULL

-- LEFT JOIN: todas as cidades aparecem, mesmo sem país cadastrado
SELECT c.nome AS cidade, p.nome AS pais
FROM cidades c
LEFT JOIN paises p ON c.id_pais = p.id_pais;
-- Resultado: cidades sem país aparecem com pais = NULL
```

### Regra de ouro para a prova

> **RIGHT JOIN** = toda a tabela da **direita** (depois do `RIGHT JOIN`) está garantida no resultado.  
> **LEFT JOIN** = toda a tabela da **esquerda** (antes do `LEFT JOIN`, no `FROM`) está garantida no resultado.  
> `FROM tabela_A RIGHT JOIN tabela_B` ≡ `FROM tabela_B LEFT JOIN tabela_A`

---

## Questão 4 — Executar Stored Procedure (1 ponto)

### Enunciado
> Qual comando deveria ser utilizado para executar a procedure `cidade_pais_info` criada na questão 2?

### Resposta: **D**

```sql
CALL cidade_pais_info();
```

### Por que cada alternativa está errada

| Alternativa | Comando | Análise |
|-------------|---------|---------|
| A ❌ | `EXECUTE cidade_pais_info;` | `EXECUTE` é usado para **prepared statements** (`PREPARE stmt FROM ...; EXECUTE stmt;`), não para procedures. |
| B ❌ | `EXEC cidade_pais_info;` | `EXEC` é o comando do **SQL Server** (Microsoft). Não existe no MySQL/MariaDB. |
| C ❌ | `RUN cidade_pais_info;` | `RUN` não é um comando SQL padrão. Não existe em nenhum SGBD mainstream. |
| D ✅ | `CALL cidade_pais_info();` | **CORRETO.** `CALL` é o comando padrão MySQL/MariaDB para executar stored procedures. Os `()` são obrigatórios. |
| E ❌ | `CALL PROCEDURE cidade_pais_info;` | `CALL PROCEDURE` não é sintaxe válida. O correto é apenas `CALL nome_procedure()`. |

### Variações do CALL com parâmetros

```sql
-- Sem parâmetros (Q4)
CALL cidade_pais_info();

-- Com parâmetro IN
CALL buscar_cidades_por_pais('BRA');

-- Com parâmetro OUT
CALL contar_cidades('BRA', @total);
SELECT @total;  -- lê o valor de saída

-- Com parâmetros IN e OUT
CALL procedure_mista('BRA', @resultado);
```

---

## Questão 5 — COUNT + GROUP BY + ORDER BY (1,5 pontos)

### Enunciado
> Qual consulta você utilizaria para contar a quantidade de cidades que existem em cada país, ordenando pelo país com maior número de cidades? Utilize INNER JOIN, GROUP BY e ORDER BY.

### Resposta

```sql
SELECT p.nome AS pais,
       COUNT(c.id_cidade) AS total_cidades
FROM paises p
INNER JOIN cidades c
    ON p.id_pais = c.id_pais
GROUP BY p.id_pais, p.nome
ORDER BY total_cidades DESC;
```

### Explicação linha a linha

| Linha | Código | O que faz |
|-------|--------|-----------|
| 1 | `SELECT p.nome AS pais` | Seleciona o nome do país como coluna de agrupamento |
| 2 | `COUNT(c.id_cidade) AS total_cidades` | Conta quantas cidades existem para cada grupo (país). `id_cidade` é PK de `cidades`, nunca é NULL, portanto conta todas |
| 3 | `FROM paises p` | `paises` como tabela principal (LEFT no JOIN) |
| 4 | `INNER JOIN cidades c` | Une com `cidades` — só países com ao menos uma cidade aparecem |
| 5 | `ON p.id_pais = c.id_pais` | Condição de junção pelo campo `id_pais` |
| 6 | `GROUP BY p.id_pais, p.nome` | Agrupa os resultados por país. `p.id_pais` garante unicidade; `p.nome` está presente porque aparece no SELECT (regra do GROUP BY) |
| 7 | `ORDER BY total_cidades DESC` | Ordena pelo total calculado, do maior para o menor (`DESC` = decrescente) |

### Por que `GROUP BY p.id_pais, p.nome` e não só `GROUP BY p.nome`?

- `p.id_pais` é a **chave primária** — garante que dois países com mesmo nome (ex: "Congo") sejam tratados separadamente.
- `p.nome` é necessário no `GROUP BY` porque aparece no `SELECT` sem função de agregação. MySQL com `ONLY_FULL_GROUP_BY` (modo padrão) exige isso.

### Entendendo o COUNT

```sql
COUNT(*)          -- conta todas as linhas do grupo, incluindo NULLs
COUNT(c.id_cidade)  -- conta só linhas onde id_cidade não é NULL (recomendado aqui)
COUNT(DISTINCT c.id_cidade)  -- conta valores únicos (irrelevante aqui, pois id_cidade é PK)
```

### Resultado esperado (top 10)

| pais | cidades |
|------|---------|
| China | 363 |
| India | 341 |
| United States | 274 |
| Japan | 248 |
| Brazil | 245 |
| Russian Federation | 189 |
| Mexico | 169 |
| Philippines | 136 |
| Germany | 93 |
| Indonesia | 85 |

### Como adicionar filtro de mínimo de cidades (HAVING)?

```sql
-- Só países com mais de 100 cidades
SELECT p.nome AS pais,
       COUNT(c.id_cidade) AS total_cidades
FROM paises p
INNER JOIN cidades c ON p.id_pais = c.id_pais
GROUP BY p.id_pais, p.nome
HAVING total_cidades > 100     -- HAVING, não WHERE, pois filtra agregado
ORDER BY total_cidades DESC;
```

---

## Questão 6 — Criar View `paises_sumario` (1,5 pontos)

### Enunciado
> Com base na consulta da questão 5, informe o código de criação de uma View chamada `paises_sumario`.

### Resposta

```sql
CREATE VIEW paises_sumario AS
SELECT p.nome AS pais,
       COUNT(c.id_cidade) AS total_cidades
FROM paises p
INNER JOIN cidades c
    ON p.id_pais = c.id_pais
GROUP BY p.id_pais, p.nome
ORDER BY total_cidades DESC;

-- Verificar o conteúdo
SELECT * FROM paises_sumario;
```

### Explicação linha a linha

| Linha | Código | O que faz |
|-------|--------|-----------|
| 1 | `CREATE VIEW paises_sumario AS` | Cria uma visão (View) chamada `paises_sumario`. O `AS` inicia a definição da consulta que a View representa |
| 2–8 | `SELECT ... ORDER BY ...` | A query da Q5 — exatamente igual. A View **armazena essa definição**, não os dados |

### O que é uma View?

Uma View é uma **consulta salva** que se comporta como uma tabela virtual.

```
┌─────────────────────────────────────────────┐
│  CREATE VIEW paises_sumario AS SELECT ...   │
│                                             │
│  Não armazena dados físicos!                │
│  Armazena apenas a definição da query.      │
│  A cada SELECT na View, a query é executada.│
└─────────────────────────────────────────────┘
```

### Vantagens das Views

| Vantagem | Explicação |
|----------|------------|
| **Simplificação** | Oculta queries complexas — o usuário faz `SELECT * FROM paises_sumario` em vez de reescrever o JOIN+GROUP BY |
| **Segurança** | Permite dar `GRANT SELECT` na View sem expor as tabelas base |
| **Abstração** | Se a estrutura das tabelas mudar, só a View precisa ser atualizada |
| **Reutilização** | Vários relatórios podem usar a mesma View |

### Comandos úteis com Views

```sql
-- Listar views do banco atual
SHOW FULL TABLES WHERE Table_type = 'VIEW';

-- Ver a definição de uma View
SHOW CREATE VIEW paises_sumario;

-- Atualizar uma View (não precisa dropar antes)
CREATE OR REPLACE VIEW paises_sumario AS
SELECT p.nome AS pais,
       COUNT(c.id_cidade) AS total_cidades
FROM paises p
INNER JOIN cidades c ON p.id_pais = c.id_pais
GROUP BY p.id_pais, p.nome;

-- Remover uma View
DROP VIEW IF EXISTS paises_sumario;
```

---

## Questão 7 — Filtrar a View com WHERE (1,5 pontos)

### Enunciado
> Informe a consulta SQL para utilizar a View `paises_sumario` criada na questão 6 filtrando os países com exatamente 8 cidades.

### Resposta

```sql
SELECT *
FROM paises_sumario
WHERE total_cidades = 8;
```

### Explicação linha a linha

| Linha | Código | O que faz |
|-------|--------|-----------|
| 1 | `SELECT *` | Seleciona todas as colunas da View (`pais` e `total_cidades`) |
| 2 | `FROM paises_sumario` | Usa a View como se fosse uma tabela. Por baixo, o banco executa a query definida na View |
| 3 | `WHERE total_cidades = 8` | Filtra apenas os grupos em que o total de cidades é exatamente 8 |

### Por que `WHERE` aqui funciona, se `total_cidades` é um agregado?

Normalmente, `COUNT()` exige `HAVING` para filtragem. Mas aqui a agregação **já foi feita dentro da View** — ao consultar `paises_sumario`, o banco entrega um resultado com colunas `pais` (texto) e `total_cidades` (número inteiro). Do ponto de vista da query externa, `total_cidades` é uma coluna comum, então `WHERE` funciona normalmente.

```
View (query interna executa):
  SELECT p.nome, COUNT(c.id_cidade)   → devolve: pais / total_cidades
  FROM paises INNER JOIN cidades
  GROUP BY ...

Query externa enxerga:
  paises_sumario = tabela com colunas (pais, total_cidades)
  → WHERE total_cidades = 8  é válido
```

### Resultado esperado

| pais | cidades |
|------|---------|
| Greece | 8 |
| Yugoslavia | 8 |
| Kenya | 8 |
| Tunisia | 8 |
| Bolivia | 8 |

5 países com exatamente 8 cidades cadastradas no banco `mundo`.

### Variações úteis para a prova

```sql
-- Países com mais de 100 cidades
SELECT * FROM paises_sumario WHERE total_cidades > 100;

-- Países com entre 5 e 10 cidades
SELECT * FROM paises_sumario WHERE total_cidades BETWEEN 5 AND 10;

-- Top 3 países com mais cidades
SELECT * FROM paises_sumario LIMIT 3;

-- Usar a View em um JOIN com outra tabela
SELECT ps.pais, ps.total_cidades, l.id_lingua
FROM paises_sumario ps
INNER JOIN linguas l ON l.id_pais = (
    SELECT id_pais FROM paises WHERE nome = ps.pais LIMIT 1
)
WHERE l.oficial = 'T';
```

---

## Questão 8 — GRANT SELECT na View (1 ponto)

### Enunciado
> Qual é o comando SQL correto para conceder a permissão de leitura da View `paises_sumario` para um usuário chamado `fatecuser` que executará a partir de qualquer IP?

### Resposta (gabarito adaptado do professor)

```sql
GRANT SELECT ON mundo.paises_sumario TO 'fatecuser'@'%';
```

### Análise de cada alternativa

#### A ❌ — `GRANT SELECT ON VIEW ecommerce.informacoes_frete TO 'usuario'@'10.106.1.24'`
Problemas:
1. `ON VIEW` — sintaxe **inválida** no MySQL/MariaDB. O correto é `ON banco.objeto` (sem a palavra VIEW).
2. Banco errado: `ecommerce` em vez de `mundo`.
3. Usuário errado: `usuario` em vez de `fatecuser`.
4. Host restrito a um IP fixo em vez de `'%'` (qualquer IP).

#### B ❌ — `GRANT VIEW ON ecommerce.informacoes_frete TO 'fatecuser'@'%'`
Problemas:
1. `GRANT VIEW ON` — sintaxe **inválida**. `VIEW` não é um privilégio; o privilégio sobre uma View é `SELECT`, `INSERT`, etc.
2. Banco e objeto errados.

#### C ❌ — `ALLOW SELECT ON ecommerce.informacoes_frete TO 'usuario'@'10.106.1.24'`
Problemas:
1. `ALLOW` — **não existe** no MySQL/MariaDB. O comando é `GRANT`.
2. Banco, objeto e usuário errados.

#### D ❌ — `GRANT SELECT ON ecommerce.informacoes_frete TO 'usuario'@'10.106.1.24'`
Problemas:
1. Banco errado: `ecommerce` em vez de `mundo`.
2. Objeto errado: `informacoes_frete` em vez de `paises_sumario`.
3. Usuário errado: `usuario` em vez de `fatecuser`.
4. Host restrito a IP fixo.
> **Atenção:** A sintaxe `GRANT SELECT ON banco.objeto TO 'user'@'host'` está **correta**. O erro aqui são os valores errados nos campos.

#### E ❌ — `GRANT ACCESS ON ecommerce.informacoes_frete TO 'fatecuser'@'10.105.1.24'`
Problemas:
1. `GRANT ACCESS` — `ACCESS` **não é um privilégio** válido no MySQL/MariaDB.
2. Banco e objeto errados.
3. Host com IP fixo (10.105.1.24) em vez de `'%'`.

#### ✅ Resposta correta

```sql
GRANT SELECT ON mundo.paises_sumario TO 'fatecuser'@'%';
```

- `GRANT SELECT` — concede apenas permissão de leitura.
- `ON mundo.paises_sumario` — especifica o banco (`mundo`) e o objeto (`paises_sumario`).
- `TO 'fatecuser'@'%'` — para o usuário `fatecuser` conectando de **qualquer IP** (`%` é wildcard).

### Estrutura geral do GRANT

```sql
GRANT <privilégio(s)>
ON <banco>.<objeto>
TO '<usuario>'@'<host>';
```

### Tabela de privilégios MySQL

| Privilégio | O que permite |
|------------|---------------|
| `SELECT` | Leitura (SELECT) |
| `INSERT` | Inserção de dados |
| `UPDATE` | Atualização de dados |
| `DELETE` | Exclusão de dados |
| `EXECUTE` | Executar Stored Procedures |
| `CREATE` | Criar tabelas/bancos |
| `DROP` | Remover tabelas/bancos |
| `ALL PRIVILEGES` | Todos os privilégios acima |

### Tabela de hosts MySQL

| Host | Significado |
|------|-------------|
| `'%'` | Qualquer IP (qualquer host) |
| `'localhost'` | Apenas conexão local (não via rede) |
| `'127.0.0.1'` | Apenas IP de loopback |
| `'192.168.1.%'` | Qualquer IP da rede 192.168.1.0/24 |
| `'10.106.1.24'` | Um único IP específico |

### Aplicar + verificar + revogar

```sql
-- Aplicar (forçar releitura das permissões)
FLUSH PRIVILEGES;

-- Ver o que o usuário pode fazer
SHOW GRANTS FOR 'fatecuser'@'%';

-- Revogar permissão
REVOKE SELECT ON mundo.paises_sumario FROM 'fatecuser'@'%';

-- Criar o usuário (se ainda não existir) antes de dar GRANT
CREATE USER 'fatecuser'@'%' IDENTIFIED BY 'senha_segura_123!';
```

---

## Resumo das Respostas

| # | Tipo | Pontos | Resposta |
|---|------|--------|---------|
| Q1 | Dissertativa | 1,0 | `SELECT c.nome AS cidade, p.nome AS pais FROM cidades c INNER JOIN paises p ON c.id_pais = p.id_pais;` |
| Q2 | Dissertativa | 1,5 | `DELIMITER $$ CREATE PROCEDURE cidade_pais_info() BEGIN ... END $$ DELIMITER ;` |
| Q3 | Múltipla escolha | 1,0 | **E** — RIGHT JOIN retorna todas as linhas da tabela da direita + correspondentes da esquerda |
| Q4 | Múltipla escolha | 1,0 | **D** — `CALL cidade_pais_info();` |
| Q5 | Dissertativa | 1,5 | `SELECT p.nome, COUNT(c.id_cidade) ... GROUP BY p.id_pais, p.nome ORDER BY total_cidades DESC;` |
| Q6 | Dissertativa | 1,5 | `CREATE VIEW paises_sumario AS SELECT ... (query da Q5)` |
| Q7 | Dissertativa | 1,5 | `SELECT * FROM paises_sumario WHERE total_cidades = 8;` |
| Q8 | Múltipla escolha | 1,0 | **GRANT SELECT ON mundo.paises_sumario TO 'fatecuser'@'%';** |

---

## O que pode cair na prova N3

Com base nos tópicos cobrados no Simulado N2 e no conteúdo das aulas posteriores:

| Probabilidade | Tópico | Aula | Dica |
|---------------|--------|------|------|
| 🔴 Alta | Stored Procedures com parâmetros IN/OUT | Aula 11 | Saber a sintaxe com `DECLARE` e `INTO` |
| 🔴 Alta | Views — criação, consulta e `CREATE OR REPLACE` | Aula 12 | Saber que Views não armazenam dados |
| 🔴 Alta | GRANT/REVOKE — privilégios e hosts | Aula 3 | Decorar: `GRANT priv ON banco.obj TO 'user'@'host'` |
| 🟡 Média | HAVING vs WHERE | Aula 10 | WHERE = antes de agrupar; HAVING = depois |
| 🟡 Média | Subqueries (IN, EXISTS) | Aula 7 | Saber colocar SELECT dentro de WHERE |
| 🟡 Média | CASE WHEN / IF dentro de SELECT | Aula 10 | Expressões condicionais em colunas calculadas |
| 🟢 Baixa | Funções de String e Data | Aula 9 | `CONCAT`, `DATE_FORMAT`, `NOW()` |
| 🟢 Baixa | Tipos de dados (ENUM, JSON, DECIMAL) | Aula 2 | ENUM('T','F'), DECIMAL(4,2) = 4 dígitos total, 2 decimais |

---

*Gerado por ALFRED em 2026-06-12 com base em `[Correcao] - Simulado N2.pdf` e nas Aulas 01–12 da disciplina.*
