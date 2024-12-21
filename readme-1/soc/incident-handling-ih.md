# Incident Handling (IH)

O tratamento de incidentes é um ponto importante para uma organização que se preocupa com a prevenção e a redução de volume de incidentes de segurança. Algumas organizações podem tratar disso dentro de casa, outras podem terceirizar este processo.

Agora, para uma boa compreensão do processo de tratamento de incidentes vamos alinhar alguns elementos super importantes para a construção do conhecimento.\
Podemos iniciar a compreensão a partir dos menores fragmentos de um sistema que podem ser analisados e que são constantes ferramentas para quem for atuar na área de segurança: eventos.

Basicamente eventos são elementos compiladas em um sistema que são provenientes de ações tomadas num sistema seja por um usuário ou por aplicações presentes no sistema, geralmente essas ações são transmitidas através de Logs pelos sistemas. A estes elementos podemos chamar de "eventos".

Vamos olhar com mais atenção para os eventos para que possamos compreender como este elemento se apresenta no dia a dia em sistemas.\
\
Eventos geralmente se apresentarão como:

* um usuário que se logou no sistema em seu horario de serviço;
* um usuário clicou em um elemento de um site;
* um usuário está acessando um diretório/arquivo cujo ele deveria realmente ter acesso;

Porém, nem todos eventos podem ser considerados como legítimos e corretos, se tomarmos como contexto os eventos mencionados anteriormente, podemos modificar alguns pontos fundamentais que transformariam estes eventos em eventos suspeitos, assim teríamos:

* um usuário que se logou no sistema FORA seu horario de serviço;
* um usuário clicou em um elemento SUSPEITO de um site;
* um usuário está acessando um diretório/arquivo cujo ele NÃO deveria realmente ter acesso;

Repare que as alterações são sutis e muito semelhantes entre si, mas o que altera é a finalidade da ação e, a partir disso um evento pode caracterizar-se por incidente devido à criticidade que o mesmo impele ao sistema, e para isso temos formas de nos prepararmos e tratarmos tais incidentes, com isso entramos no cerne do Incident Handling (tratamento de incidentes).

PREPARAÇÃO DO ANALISTA

O primeiro estágio, antes de mais nada, dentro do tratamento de incidentes é o processo de preparação, afinal de contas quando um incidente ocorre precisa-se ter um ambiente minimamente preparado mesmo que não seja para se defender, mas para um bom reestabelecimento das atividades (recuperação de desastres) e também para uma mínima coleta e análise forense pós incidente.

Nisso já existem boas práticas a serem seguidas, e debruçaremos sobre estas agora.&#x20;

Para iniciarmos o processo de preparação precisamos nos certificar de ter:

* um time de tratamento de incidentes habilidoso;
* uma força operária bem treinada;
* políticas claras e bem documentadas;
* ferramentas como softwares e equipamentos;

> Como meu objetivo aqui é tratar sempre da parte técnica, vou enfatizar no ponto relacioanda ao ferramental, mais é importante que saiba que as demais partes são tão importantes quanto a ferramental e dispõem de necessidades específicas para sua manutenção, então caso tenha interesse segue link do curso do Hack the Box que me ajudou a construir este material [https://academy.hackthebox.com/module/148/section/1365](https://academy.hackthebox.com/module/148/section/1365).

Um bom ferramental para um bom tratamento de incidentes deve considerar os diversos cenários em que podemos estar inseridos de acordo com as características do incidente que estaremos investigando. Mas algumas das mais mencionadas e referidas são:

* um laptop adicional, para cada membro do time forense, para preservar as provas e evidencias da devida forma (ATENÇÃO: o sistema deve estar configurado apropriadamente para receber malwares e arquivos potencialmente danosos ao sistema e isso deve ser feito de uma forma que preserve quaisquer outros elementos da organização);
* uma boa ferramenta de aquisição e análise de imagens com propósito forense;
* ferramentas de memória e captura;
* ferramentas de captura e análise da resposta em tempo real;
* ferramentas de analise de logs;
* ferramentas de captura e análise de pacotes de rede;
* cabos de rede e switches;
* blocos de nota;
* HDs para imagens forenses;
* cabos de força;
* chaves de fenda, pinças e outras ferramentas relevantes para reparar ou desmontar dispositivos de hardware, se necessário;
* criador do Indicador de Compromisso (COI) e a capacidade de procurar COI em toda a organização;
* formulários de cadeia de custódia;
* softwares de criptografia e hashing;
* sistema de acompanhamento (tracking) de tickets;
* todo o sistema deev estar fora da infraestrutura da empresa

Estes equipamentos devem estar localizados em uma jump bag, dessas que sempre ando com uma versão reduzida em minha bolsa, afinal de contas nunca sabemos quando precisaremos dissecar um desktop por aí (risos).

PREPARAÇÃO DO AMBIENTE

O ambiente empresarial também deve estar pronto para passar por incidentes potencialmente críticos e para isso temos algumas ferramentas que podem auxiliar a transformar o ambiente das organizações mais seguro.

* DMARC: ferramenta para proteção contra phishing, baseada em filtros e regras, evitando contato entre o email potencialmente malicioso e o usuário alvo;
*
