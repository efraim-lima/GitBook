---
Created: 2026-02-25T21:18
Criado em: 2026-02-25T21:18
Criado em 1: 2026-02-25T21:18
Criado por: 2026-02-25T21:18
---
## Infraestrutura básica
Precisamos ter algumas camadas, de forma a proteger nossos ativos em diversas etapas, para isso precisamos partir de um ponto inicial, no caso aqui iniciaremos essa proteção a partir do inventário (se não conhecemos nossos ativos, não sabemos o que podemos proteger).  
  
Abaixo segue uma imagem referenciada no próprio NIST em sua Special Publication 1800-25B (Data Integrity: Identifying and Protecting Assets Against Ransomware and Other Destructive Events)
  
![[/image 32.png|image 32.png]]
  
Após inventariar [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] ativos devemos atrelar [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] [[CyberSecurity/Course/forense/logs/logs|logs]], mas devemos observar com atenção focada também:
- superficie de ataque,
- entrypoints,
- endpoints,
- historico de manutenção,
- ciclo de vida dos equipamentos,
- licenças de [[softwares]],
- políticas de [[Segurança]],
  
Para determinar formas de [[Segurança]] para qualquer ambiente podemos nos referenciar em algumas soluções prontas (não precisamos inventar a roda). Tais soluções podem ser:
- [https://www.nccoe.nist.gov/publication/1800-25/VolB/index.html](https://www.nccoe.nist.gov/publication/1800-25/VolB/index.html)
- S[https://www.isms.online/soc-2/glossary/architecture/](https://www.isms.online/soc-2/glossary/architecture/)
- [https://www.cisecurity.org/controls/cis-controls-list](https://www.cisecurity.org/controls/cis-controls-list)
- [https://attack.mitre.org/](https://attack.mitre.org/)
  
Para fornecer [[Segurança]] para [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] elementos acima podemos utilizar soluções de diversos tipos, podem ser open source, proprietários, etc.
  
## Montagem da arquitetura da rede
Na aula do dia 11/03 pretendemos montar a [[infraestrutura]] segura, a partir da [[infraestrutura]] fornecida pelo professor devemos montar a arquitetura apresentando:
- soluções de [[Segurança]] para cada etapa de [[Segurança]] apresentada no diagrama inicial;
- também precisamos apresentar [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] serviços que determinam [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] processos de [[Segurança]];
- importante listar as funcionalidades de cada etapa e as regras básicas;
- analisar a [[infraestrutura]], precisaremos encontrar vulnerabilidades na implementação (seria uma revisão nossa na infra), apontando também as melhorias necessárias;
- As regras da infra somos nós mesmos que determinamos, só precisamos indicar as interações que ocorrem entre [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] serviços e soluções;
- obrigação: todas soluções de seguranã até Data Domain;
O formato de entrega pode ser uma listagem, o importante é apresentar as soluções para cada camada.