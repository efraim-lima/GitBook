---
Created: 2026-03-09T20:25
Criado em: 2026-03-09T20:25
Criado em 1: 2026-03-09T20:25
Criado por: 2026-03-09T20:25
---
Exemplo em aula
INDUSTRIA AUTOMOBILISTICA
## Folha de pagamentos -RH - periodicidade mensal - nota 3
Venda de Contratos - MKT - peiodicidade diária - nota 2  
cliente não se duplica e não se exclui, seu id é um valor dinamico que não se repete -> primary key, non duplicate  
por isso geralmente mantem-se um campo de 10 char para isso
O cadastro do cliente é uma saída de Venda CTR (tabela de [[CLIENTES]])  
Ao ter sido feito o cadastro da venda é feito o cadastro do contrato em outra tabela diferente (não pode ser alterado e nem alterado) -> primary key, non duplicate.
Cada parcela deve ser inserida em outra tabela -> foreign key
Nota 2 | detalhe: observar pelo negócio e não pela [[Segurança]], não puxar a sardinha para a sua área, mas olhar pelo olhar do negócio
## ================  
Recebimentos - Financeiro (Contas a Receber) Débito Diário - periodicidade diária - Nota 5
parte de Recebimentos (Contas a Receber), sendo de finanças e debito direto precisa-se indicar qual o ponto de foco, no caso sendo da venda de contratos.
Sendo débito direto, o processo é feito no dia anterior (com a parcela que sera debitada no dia seguinte).  
A baixa do debito direto é feita a partir do envio dos dados para o banco e não na devolutiva do banco e quando há a devolutiva de débito do banco é feito o processo de recomposição dos pagamentos (pode levar dias), nisso é feita a recomposiçao do pgto com o debito e quando há discrepância pode ser verificado a fraude ou a inadimplência
Nota 5 | Aqui, mesmo que atrelado às vendas de contratos (no caso que não era o objetivo principal do negócio), o fato de rodar um volume alto de dinheiro a classificação é alta, mesmo que atralada a um sistema que não é tão importante na pontuação
  
## PDS
1º passo: mapeamento dos ativos
2º passo: classificar
  
Plano Diretor de [[Segurança]] te o objetivo de mapear a relação entre ativos e processos que precisam ser assegurados.
Isso está relacionado ao GSI principalmente ao Estudo de Perímetros, onde se agrupa [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] principais gestores da parte técnica tática, onde serão levantadas informações topológicas, físicas e tecnológicas. Neste processo é feita a identificação tambḿe dos ativos, infra-estrutura, tecnologias, aplicações, informações e pessoas.
Tudo deve ser relacionado, inclusive identificando o funcioamento, relação de troc de informações e fluxo de dados.
  
  
=======================================================
a visão do todo é o que nos faz ser diferenciados podemos ser a estrela de belem ou a vaca do prezépio