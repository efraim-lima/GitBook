# Aula Inaugural 05-08-2024

### Informações sobre atividades e provas

A N1 é prova normal valendo 7 e outra atividade valendo 3. Na N2, teremos um laboratório de SO contendo Administração de SO, Inglês e Empreendedorismo.\
A N2 valerá 7 pontos e todos os grupos precisarão ter ao menos uma pessoa cursando todas as matérias.

A ideia é fazer um projeto criando um servidor para uma empresa "real", onde faremos todo o deploy de maneira semi-real, criando um projeto multidisciplinar com o objetivo de se usar todas as matérias compreendidas em apenas um trabalho.

O professor perguntou a todos se temos conhecimento de script DOS.

### Pentesting com SQLInjection

O primeiro passo é verificar se o formulário está validando os inputs no cliente.\
Uma boa maneira de se validar se o cliente está validando é inserindo um comando simples nos formulários como `\ 'or 1=1' --`, assim saberemos se existe validação no cliente. Caso não haja, podemos tentar montar uma query ao estilo:

```SQL
-- textcode "and password=" .txtsenha
```

Caso esteja validando, basta fazer o download do código fonte baixando seu HTML e buscar pelos form-actions de maneira a compreender os campos do formulário e o que cada um compreende.

De posse deste conhecimento, conseguimos elaborar uma query coerente com a organização deste formulário especificamente, usando o REQBIN. Dessa forma, as queries redirecionarão diretamente para o banco de dados através de uma requisição.

Muitas vezes, os desenvolvedores acham que usar um simples captcha impossibilita uma série de ataques, mas isso é uma falácia, pois esses sistemas podem ser bypassados com facilidade apenas enviando requests diretamente para o servidor.
