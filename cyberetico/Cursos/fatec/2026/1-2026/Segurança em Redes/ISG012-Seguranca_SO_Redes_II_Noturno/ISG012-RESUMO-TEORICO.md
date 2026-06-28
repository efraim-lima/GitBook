# ISG012 — Resumo do Conteúdo Teórico

> **Disciplina:** ISG012 — [[Segurança]] em [[CyberSecurity/Notas/PENTESTING/Windows/Sistemas Operacionais|Sistemas Operacionais]] e Redes II  
> **Turno:** Noturno  
> **Compilado em:** [[reports/2026/2026|2026]]-06-02  
> **Finalidade:** Referência rápida para revisão e [[CyberSecurity/fatec/Pesquisa/Pesquisa|Pesquisa]] futura  

---

## Módulo 01 — Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica

Segurança em Sistemas Operacionais e Redes de
Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à 
Segmentação Lógica

Objetivo da Aula
• Abrange a compreesão e a aplicação dos princípios fundamentais de arquitetura 
de redes seguras, distinguindo entre modelos tradicionais de perímetro e 
abordagens modernas como Zero Trust e Defense in Depth;
• Estabelece os fundamentos teóricos e práticos necessários para o projeto de 
infraestruturas de rede resilientes. O foco reside na transição de arquiteturas 
baseadas em perímetro fixo para modelos dinâmicos baseados em 
segmentação e desconfiança implícita;
• Ao compreender estes paradigmas, o aluno estará apto a identificar 
vulnerabilidades estruturais em redes planas(1) e propor soluções de isolamento 
lógico que minimizem a superfície de ataque lateral. 
______
(1) Redes planas (ou flat networks) são infraestruturas de rede onde todos os dispositivos 
compartilham o mesmo domínio de broadcast, geralmente operando em uma única VLAN ou sub-rede 
IP, sem qualquer segmentação lógica ou física entre eles. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Objetivo da Aula
• Compreender a evolução histórica das arquiteturas de segurança de redes;
• Diferenciar modelos de perímetro tradicionais de abordagens modernas;
• Aplicar conceitos de Defense in Depth e Zero Trust em cenários reais;
• Projetar segmentação lógica utilizando VLANs e zonas de segurança;
• Implementar DMZs como estratégia de contenção de serviços expostos;
• Utilizar subnetting como ferramenta de microssegmentação;
• Analisar trade-offs entre complexidade e segurança em arquiteturas 
segmentadas.
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
O Modelo de Perímetro Tradicional
• A arquitetura de perímetro, predominante nas décadas de 1990 e 2000, opera 
sob a premissa de "castelo e fosso": recursos robustos de segurança protegem 
a fronteira externa, enquanto o interior da rede goza de confiança implícita;
• Este modelo presume que ameaças externas são o único vetor de risco, 
estabelecendo firewalls na borda como sentinelas absolutas;
• Entretanto, a mobilidade dos dispositivos, a nuvem híbrida e a sofisticação de 
ameaças internas tornaram este paradigma obsoleto, uma vez que um único 
comprometimento na borda expõe toda a rede interna. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Perímetro vs. Zero Trust
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
O Modelo de Perímetro Tradicional
• Conceito Central: "Hard outside, soft inside" – proteção concentrada na borda;
• Limitação Crítica: Confiança implícita em tráfego interno após autenticação 
inicial;
• Vetores de Falha: Ameaças internas, malware lateral e dispositivos BYOD(1) 
comprometidos;
• Insuficiência: Não endereça adequadamente segmentação entre sistemas 
críticos;
• Legado: Ainda presente em infraestruturas legadas, exigindo modernização 
gradual.
______
(1) Malware Lateral (Lateral Movement) e dispositivos BYOD são dois vetores críticos que tornam o 
modelo de perímetro tradicional obsoleto:
– Movimentação lateral é a técnica utilizada por atacantes para se deslocarem de um sistema 
comprometido inicial para outros sistemas dentro da mesma rede, expandindo seu acesso e 
buscando ativos de maior valor (crown jewels);
– BYOD (Bring Your Own Device) é a política que permite funcionários utilizarem dispositivos 
pessoais (smartphones, tablets, laptops) para acessar recursos corporativos (email, Wi-Fi, 
arquivos). 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Defense in Depth (Defesa em Profundidade)
• Defense in Depth constitui uma estratégia de segurança que emprega múltiplas 
camadas de controles defensivos ao longo do caminho de dados, garantindo 
que a falha de um único mecanismo não resulte em comprometimento total;
• Inspirada em táticas militares, esta abordagem integra controles físicos, técnicos 
e administrativos, criando redundância protetiva;
• Cada camada – desde o perímetro externo até o núcleo dos dados – incorpora 
mecanismos de prevenção, detecção e resposta, dificultando a progressão de 
atacantes através da infraestrutura.
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Defense in Depth (Defesa em Profundidade)
• Princípio: Nenhum controle é infalível; redundância estratégica é essencial;
• Camadas Típicas: Políticas → Perímetro → Rede → Endpoint → Aplicação → 
Dados;
• Abordagem: Prevenção (firewalls) + Detecção (IDS) + Resposta (contenção);
• Vantagem: Retardamento do atacante e redução do impacto de brechas; 
isoladas;
• Implementação: Controles complementares, não apenas repetitivos 
(diversidade defensiva).
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Defense in Depth (Defesa em Profundidade) – Camadas de proteção
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
O Paradigma Zero Trust
• Zero Trust ("Nunca Confie, Sempre Verifique") representa uma ruptura 
epistemológica em relação aos modelos baseados em localização;
• Este framework elimina o conceito de "rede confiável", exigindo verificação 
contínua e estrita de identidade, dispositivo e contexto para cada solicitação de 
acesso, independentemente da origem;
• Desenvolvido inicialmente pelo Forrester Research e posteriormente adotado 
pelo NIST(1), o Zero Trust opera sob o pressuposto de que a rede já está 
comprometida, impondo microssegmentação e privilégio mínimo como 
contramedidas padrão.
______
(1) O NIST (National Institute of Standards and Technology) é o instituto federal de padronização dos 
Estados Unidos que desenvolve e publica diretrizes técnicas obrigatórias para agências 
governamentais e amplamente adotadas como referência global em segurança da informação, 
incluindo a norma SP 800-207 que define a arquitetura Zero Trust 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
O Paradigma Zero Trust
• Verificação Explícita: Autenticação e autorização contínuas para cada acesso;
• Uso de Microssegmentação: Isolamento granular entre workloads(1) e usuários;
• Privilégio Mínimo: Acesso concedido estritamente ao necessário (least privilege);
• Assunção de Brecha: Proteções projetadas assumindo que o perímetro já foi 
violado;
• Inspeção Profunda: Análise de tráfego cifrado(2) e comportamental (padrões de 
comunicação - volume, frequência, destinos) em tempo real.
_____
(1) Workloads são unidades executáveis de processamento — abrangendo,  entre outros, máquinas 
virtuais e containers — que consomem recursos computacionais e são tratadas como entidades 
independentes para orquestração, escalabilidade e aplicação de políticas de segurança em arquiteturas 
modernas. 
(2) Pressupõe cenários corporativos controlados onde a organização controla os endpoints e pode 
instalar certificados raiz próprios
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Segmentação de Rede – Conceitos Fundamentais
• A segmentação lógica de redes consiste na divisão arquitetural de uma 
infraestrutura IP em zonas isoladas, controladas por políticas de tráfego 
específicas;
• Esta prática contém o raio de explosão de incidentes de segurança, impedindo 
movimentação lateral de ameaças;
• A segmentação pode ser física (cabeamento separado) ou lógica (VLANs, 
subnets), sendo a última preferível por flexibilidade e custo-redução;
• Zonas de segurança distintas – como Management, Internal, DMZ e External – 
exigem controles diferenciados baseados na criticidade dos ativos hospedados. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Segmentação de Rede – Conceitos Fundamentais
• Propósito: Contenção de breaches(1) e redução da superfície de ataque lateral;
• Métodos: VLANs (camada 2), Subnetting (camada 3), Microssegmentação(2) 
(camada 7);
• Zonas Típicas: Management (administração), Internal (usuários), DMZ (serviços 
públicos);
• Políticas: Default-deny entre zonas, com regras explícitas de necessidade 
operacional;
• Benefício: Isolamento de sistemas legados e dados críticos em silos protegidos.
_____
(1) Contenção de breaches é a estratégia de limitar o raio de propagação de um incidente de 
segurança através de barreiras arquiteturais (VLANs, subnets, firewalls), impedindo que a 
comprometimento de um sistema se espalhe lateralmente para ativos críticos, mesmo após a violação 
inicial do perímetro.
(2) Microsegmentação é a divisão granular de uma rede em segmentos de segurança extremamente 
pequenos (frequentemente até nível de workload, container ou processo individual), onde políticas de 
acesso "default-deny" são aplicadas dinamicamente baseadas em identidade e contexto, não em 
endereços IP estáticos, permitindo contenção precisa de ameaças mesmo dentro de uma mesma VLAN 
tradicional. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
VLANs (Virtual Local Area Networks)
• VLANs constituem tecnologia de camada 2 do modelo OSI que permite a 
criação de domínios de broadcast lógicos independentes da topologia física da 
infraestrutura;
• Através do tagging 802.1Q, switches conseguem segregar tráfego, criando 
segmentos virtuais que funcionam como redes separadas;
• Esta segmentação impede que dispositivos em VLANs distintas comuniquem-se 
diretamente, exigindo roteamento inter-VLAN controlado por firewalls ou Layer 3 
switches, o que possibilita aplicação de políticas de segurança granulares entre 
departamentos ou funções. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
 Implementação e Segurança
• Padrão: IEEE 802.1Q – tagging de quadros(1) Ethernet com identificador de VLAN (1-4094);
• Tipos: VLANs de dados, de voz (QoS)(2), de management e nativas (segurança 
aprimorada);
• Isolamento: Broadcast storms(3) contidos dentro de VLANs específicas;
• Roteamento: Inter-VLAN requer dispositivo de camada 3 (router ou L3 switch);
• Hardering: VLAN hopping prevention(4) (desativar trunking dinâmico, pruning(5) adequado).
_______
(1) Tagging de quadros é a técnica de inserção de um identificador de 4 bytes (campo TCI no padrão IEEE 
802.1Q) no cabeçalho Ethernet para vincular um quadro a uma VLAN específica, permitindo que switches 
transmitam tráfego de múltiplas VLANs sobre um mesmo enlace físico (trunk) mantendo o isolamento lógico 
entre segmentos. 
(2) VLANs de voz (Voice VLANs)são VLANs dedicadas exclusivamente ao tráfego de VoIP (Voice over IP), 
configuradas com QoS (Quality of Service)para garantir prioridade máxima.
(3) Broadcast storms são eventos de colapso de rede causados por uma avalanche exponencial de pacotes de 
broadcast/multicasting que saturam a banda e processamento dos equipamentos, geralmente decorrentes de 
loops de camada 2 ou ausência de segmentação (VLANs), tornando a comunicação impossível em todo o 
domínio de broadcast.
(4) Hopping prevention é o conjunto de contramedidas de segurança em switches que inclui a desativação do 
trunking dinâmico (DTP), a configuração explícita de portas como access ou trunk e o isolamento da VLAN 
nativa, impedindo que atacantes realizem ataques de VLAN hopping via spoofing de switches ou 
encapsulamento duplo de quadros 802.1Q.
(5) Pruning é a técnica de filtragem dinâmica aplicada em troncos (trunks) VLAN que suprime o 
encaminhamento de tráfego de broadcast/multicast para VLANs não utilizadas em determinados links, 
otimizando largura de banda e recursos de switching ao evitar que quadros alcancem switches desprovidos de 
portas ativas naquela VLAN específica. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
  Zona Desmilitarizada - Demilitarized Zone (DMZ)
• A Zona Desmilitarizada (DMZ) representa uma sub-rede perimetral projetada 
para hospedar serviços acessíveis externamente (web, email, DNS) enquanto 
isola a rede interna corporativa;
• Posicionada entre a Internet não-confiável e a rede privada, a DMZ opera sob 
premissas de máxima restrição: servidores aqui alojados não podem iniciar 
conexões para a rede interna, apenas responder a solicitações legitimadas;
• Comprometimentos em serviços de DMZ não garantem acesso à rede 
corporativa devido às regras de firewall unidirecionais e ausência de rotas 
diretas para segmentos internos sensíveis. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
  DMZ – Arquitetura e Controles
• Posicionamento: Entre firewall externo (Internet) e firewall interno (rede corporativa);
• Regra de Ouro: Nunca permitir conexões originadas na DMZ destinadas à rede interna;
• Serviços Típicos: Web servers, proxies reversos, servidores de email relay(1), DNS 
externos;
• Hardening: Sistemas mínimos, patching rigoroso, monitoramento intensivo (IDS/IPS);
• Variações: Triple-homed firewalls (3 interfaces)(2) ou arquitetura screened subnet dual-
firewall.
_________
(1) Email relay é um servidor intermediário que recebe mensagens de um remetente e as encaminha para outro 
servidor de destino, funcionando como ponte entre diferentes domínios ou zonas de segurança (ex: da DMZ 
para a Internet ou da Internet para a rede interna), filtrando spam, malware e anonimizando a topologia interna. 
da Internet para a rede interna), filtrando spam, malware e anonimizando a topologia interna. 
(2) Triple-homed firewalls são dispositivos de segurança equipados com três interfaces de rede distintas — 
tipicamente External (Internet), Internal (rede corporativa) e DMZ — permitindo a segmentação física das zonas 
de segurança com inspeção stateful de todo tráfego entre elas, eliminando a necessidade de dois firewalls 
separados em arquiteturas de menor criticidade.
(3) Arquitetura screened subnet dual-firewall é um modelo de segurança robusto onde a DMZ é isolada por dois 
firewalls distintos — um externo (fazendo filtragem básica de Internet para DMZ) e outro interno (fazendo 
filtragem rigorosa de DMZ para rede corporativa) — criando uma "sub-rede triangulada" onde comprometimento 
do firewall externo não garante acesso à rede interna, pois o segundo firewall permanece como barreira 
adicional. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Arquitetura de zonas de segurança
IDA (sólido): Internet → External → FW-EXT → DMZ → FW-INT → Internal (acesso externo aos serviços DMZ)
RETORNO (tracejado): Internal → FW-INT → DMZ → FW-EXT → External → Internet (navegação, downloads, consultas DNS) 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
  Subnetting para Segurança
• O subnetting IP, tradicionalmente utilizado para otimização de endereçamento, 
adquire dimensão estratégica em arquiteturas seguras através da 
microssegmentação;
• Dividir blocos CIDR em subnets menores permite isolar funcionalidades críticas 
– como bancos de dados, sistemas ICS ou management interfaces – em 
broadcast domains distintos, dificultando reconhecimento de rede por atacantes. 
Subnets menores (ex: /30, /29 para links point-to-point(1 ou /28 para pequenos 
grupos de servidores) reduzem o escopo de varreduras e limitam o impacto de 
ARP spoofing(2) em segmentos críticos. 
______
(1) Links point-to-point são conexões de rede dedicadas que interconectam exatamente dois 
dispositivos — como roteadores, switches ou firewalls — sem dispositivos intermediários, utilizando 
sub-redes /30 ou /31 (apenas 2 endereços IP utilizáveis) para maximizar a eficiência do 
endereçamento e isolar o tráfego entre aqueles dois pontos específicos da topologia. 
(2) ARP spoofing é um ataque de envenenamento de tabela ARP onde o atacante envia respostas ARP 
falsas associando seu próprio endereço MAC ao IP de outro host (gateway ou vítima), interceptando 
tráfego de camada 3 destinado a esse IP em uma rede local compartilhada. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
  Subnetting – Aplicações Defensivas
• Segmentação Funcional: Cada subnet = função específica (web, app, db, 
mgmt);
• Máscaras Variáveis: VLSM (Variable Length Subnet Masking) para otimização 
hierárquica;
• Segurança: Subnets menores = menor número de hosts potencialmente 
comprometidos;
• Controle: ACLs e firewall rules mais específicas e gerenciáveis;
• Ocultação: Dificulta reconhecimento de topologia completa via scanning.
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Zonas de Segurança e Modelagem de Ameaças
• A definição de zonas de segurança classifica segmentos de rede baseando-se 
no nível de confiança e criticidade dos ativos;
• Tipicamente, identificam-se quatro zonas essenciais: External (Internet não 
controlada), DMZ (serviços expostos controlados), Internal (usuários e recursos 
corporativos) e Management (infraestrutura crítica de administração);
• Cada zona possui perfis de ameaça distintos e, consequentemente, controles 
diferenciados;
• A zona Management, por exemplo, deve ser inacessível diretamente da DMZ ou 
Internet, utilizando jump hosts(1) e autenticação multifator obrigatória.
_____
(1) Jump host (ou bastion host) é um servidor hardened e fortemente monitorado posicionado em uma 
zona de segurança intermediária (DMZ ou segmento dedicado), utilizado como ponto de entrada único 
e controlado para acesso administrativo à infraestrutura crítica, exigindo autenticação rigorosa e 
registrando todas as sessões, de modo que administradores nunca acessem diretamente sistemas 
sensíveis, mas sim "pulem" através deste gateway auditável.
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Zonas de Segurança – Hierarquia
• External (Nível 0): Zero confiança, todo tráfego considerado hostil;
• DMZ (Nível 1): Alta exposição, hardening máximo, mínimo privilégio de saída;
• Internal (Nível 2): Usuários autenticados, acesso controlado a recursos 
corporativos;
• Management (Nível 3): Acesso altamente restrito, monitoramento e logging 
intensivos;
• Princípio: Fluxo de dados deve ser explicitamente permitido; negação implícita 
entre zonas.
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Arquiteturas Modernas vs. Legadas
• A convergência de IT/OT(1), adoção de cloud híbrida(2) e trabalho remoto massivo 
demandam arquiteturas híbridas que transcendem o data center físico;
• Modelos modernos integram SASE (Secure Access Service Edge) e SSE (Security Service 
Edge), estendendo segmentação para endpoints dispersos geograficamente;
• Enquanto redes legadas dependem de backhauling de tráfego(3) para inspeção 
centralizada, arquiteturas contemporâneas distribuem políticas de segurança através de 
SD-WAN e zero trust network access (ZTNA)(4), mantendo princípios de segmentação 
independentemente da localização física ou lógica do recurso. 
_______
A convergência de IT/OT é a integração crescente entre as redes de Tecnologia da Informação (IT — sistemas 
corporativos, dados, cloud) e Tecnologia Operacional (OT — sistemas industriais, IoT, automação de fábricas).
Cloud híbrida é uma arquitetura de computação que combina infraestrutura on-premise (data centers corporativos 
privados) com serviços de nuvem pública (AWS, Azure, Google Cloud), permitindo que dados e aplicações se movam 
fluidamente entre ambos os ambientes — mantendo cargas sensíveis localmente por compliance ou latência, enquanto 
aproveita a elasticidade e custo-benefício da nuvem para demandas variáveis — exigindo segmentação de segurança 
consistente que transcenda o perímetro físico tradicional.
(3) Backhauling de tráfego é a prática de direcionar todo o tráfego de rede — incluindo acesso à Internet, nuvem ou 
comunicação entre filiais — através de um ponto centralizado (geralmente o data center corporativo principal ou HQ), 
onde ocorre inspeção de segurança por firewalls e proxies, antes de ser encaminhado ao destino final, criando latência e 
gargalos em arquiteturas modernas distribuídas.
(4) ZTNA (Zero Trust Network Access) é um modelo de acesso remoto que substitui as VPNs tradicionais, onde os 
usuários não obtêm acesso à rede corporativa, mas sim conectam-se diretamente a aplicações específicas validadas 
por identidade, contexto de dispositivo e políticas dinâmicas de segurança — eliminando a visibilidade lateral e 
aplicando o princípio de "nunca confie, sempre verifique" mesmo para usuários autenticados. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Arquiteturas Modernas vs. Legadas
• SASE (Secure Access Service Edge) é uma arquitetura de rede e segurança 
convergida que combina SD-WAN (conectividade inteligente) com serviços de 
segurança em nuvem, eliminando o backhauling centralizado ao aplicar políticas de 
segmentação e Zero Trust diretamente nos pontos de presença de borda (edge), 
próximos aos usuários dispersos geograficamente;
• SSE (Security Service Edge) é o componente puramente de segurança dentro do 
SASE — um conjunto de serviços cloud-native (ZTNA, Secure Web Gateway, Cloud 
Access Security Broker, sandboxing) que substitui appliances físicos de perímetro, 
permitindo inspeção de tráfego e acesso seguro a recursos independentemente da 
localização do usuário ou workload;
• Enquanto VLANs e firewalls físicos segmentam o data center, SASE/SSE estendem 
essa segmentação lógica para qualquer lugar — casa do funcionário, café, filial remota 
— mantendo as políticas de Zero Trust sem depender do perímetro físico da empresa. 
Arquitetura Legada SASE/SSE Moderno
Backhauling para HQ → depois para 
Internet/Cloud
Acesso direto local à edge security node
Segurança centralizada em appliances físicos Segurança distribuída como serviço (cloud)
VPN tradicional (túnel para rede corporativa) ZTNA (accesso a aplicação específica, não à rede)
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Considerações sobre Implementação
• A implementação de arquiteturas segmentadas exige balanceamento entre 
segurança, performance e operabilidade;
• Segmentação excessivamente granular pode introduzir complexidade 
administrativa insustentável, latência em roteamentos inter-subnet e dificuldades 
em troubleshooting;
• Recomenda-se adoção gradual: inicia-se com DMZ e VLANs de management, 
expandindo-se para microssegmentação conforme maturidade da equipe;
•  Documentação rigorosa de fluxos de dados (data flow diagrams) é pré-requisito 
indispensável para definição de políticas de firewall eficazes e evitar over-
permissiveness por desconhecimento das dependências de aplicações. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Boas Práticas de Implementação
• Faseamento: Priorizar segmentação de ativos críticos e expostos (crown jewels);
• Documentação: Mapeamento completo de fluxos de dados antes de implementar 
regras;
• Automação: Infraestrutura como Código (IaC)(1) para consistência em regras de 
segmentação;
• Monitoramento: NetFlow/sFlow entre zonas para detectar anomalias de 
comunicação;
• Revisão: Auditoria periódica de regras de firewall e validação de necessidade 
business.
_____
(1) Infraestrutura como Código (IaC) é a prática de gerenciar e provisionar recursos de infraestrutura — 
servidores, redes, firewalls, VLANs — através de arquivos de configuração versionáveis e automatizáveis 
(ex: Terraform, Ansible, CloudFormation), garantindo consistência, auditoria e reprodutibilidade das 
políticas de segurança em ambientes on-premise, cloud ou híbridos. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Caso de Uso: Arquitetura Multi-Camadas
• Um e-commerce típico ilustra a aplicação prática destes conceitos: a camada de 
apresentação (web servers) reside na DMZ, comunicando-se apenas via HTTPS 
com clientes e via APIs restritas com a camada de aplicação em VLAN interna 
distinta;
• A camada de dados (banco de dados) habita subnet adicional, acessível 
exclusivamente por ports específicos dos servidores de aplicação;
• A zona de management isola backups, logs e acesso administrativo;
• Comprometimento do web server não propaga lateralmente devido à ausência de 
rotas diretas para a subnet de banco de dados, exemplificando Defense in Depth 
através de segmentação estratégica. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Evolução Arquitetural
• Legado: Hub-and-spoke(1), backhauling centralizado, VPNs de acesso remoto 
tradicionais
• Moderno: Mesh(2) distribuído, inspeção local (edge computing), ZTNA
• Convergência: Integração de políticas on-premise e cloud-native (hybrid cloud)(3)
• Elasticidade: Segmentação dinâmica baseada em identidade, não endereço IP 
estático
• Desafio: Complexidade aumentada exige automação e orquestração (SDN)
______
(1) Hub-and-spoke é uma topologia de rede WAN tradicional onde todas as filiais (spokes) se conectam 
exclusivamente a um site centralizado (hub) — geralmente o data center corporativo ou matriz — para 
acessar a Internet, serviços de nuvem ou comunicar-se entre si, forçando o backhauling de tráfego e 
criando latência, gargalos e ponto único de falha, sendo substituída por arquiteturas mesh/SASE em 
redes modernas;
(2) Mesh é uma topologia de rede distribuída onde os nós (filiais, data centers, endpoints) interconectam-
se diretamente entre si formando múltiplos caminhos alternativos, permitindo comunicação ponto-a-ponto 
sem backhauling por um hub centralizado, oferecendo redundância automática e latência reduzida — 
característica fundamental das arquiteturas SD-WAN e SASE modernas.
(3) On-premise refere-se a infraestrutura de TI fisicamente instalada e operada nos data centers 
corporativos próprios, enquanto cloud-native descreve aplicações arquitetadas especificamente para 
operar em ambientes de nuvem pública ou privada, utilizando contêineres, microserviços e orquestração 
dinâmica, sem dependência de hardware local. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Análise de Caso
• Camada Web (DMZ): Apache/Nginx expostos, apenas portas 80/443 abertas 
externamente
• Camada Aplicação: VLAN interna, comunicação encriptada com web servers, sem 
acesso Internet
• Camada Dados: Subnet isolada, SQL ports restritos aos IPs dos app servers
• Management: VPN obrigatória, jump host, 2FA(1), logging de todas as sessões 
administrativas
• Resultado: Movimentação lateral impedida; atacante em DMZ não alcança dados 
sensíveis
_____
(2) 2FA (Two-Factor Authentication, ou Autenticação de Dois Fatores) é um mecanismo de segurança 
que exige duas categorias distintas de evidência para verificação de identidade — algo que o usuário 
sabe (senha), algo que possui (token, smartphone) ou algo que é (biometria) — impedindo acesso não 
autorizado mesmo que uma das credenciais seja comprometida, sendo obrigatório para acesso à zona 
de Management. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Síntese e Transição para Prática
• Os princípios teóricos aqui apresentados – transição de perímetro fixo para Zero 
Trust, segmentação lógica via VLANs e subnets, e contenção através de DMZs – 
constituem a base para a atividade prática subsequente. A implementação destas 
arquiteturas em ambientes virtualizados permite validação controlada de políticas 
de segurança sem risco à infraestrutura produtiva. A sessão prática demonstrará 
como estas abstrações teóricas materializam-se em regras de firewall, interfaces 
de rede e rotas estáticas em ambiente laboratorial. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica
Arquivos da disciplina
• Link para aGoogle Drive com os arquivos da disciplina:
– https://drive.google.com/drive/folders/
1KuGQgeDWl5RLBZntXmgqlx6NkJnvQx_i?usp=sharing
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-01 - Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica

---

## Módulo 02 — Roteamento Seguro e ACLs

Segurança em Sistemas Operacionais e Redes de
Computadores II
ISG012-02 - Roteamento Seguro e ACLs - Teoria

Objetivo
• Diferenciar roteamento estático de dinâmico sob a ótica da segurança, 
configurar um roteador Linux multi-homed utilizando os comandos ip route e ip 
rule, e implementar ACLs avançadas com nftables filtrando tráfego por interface 
de entrada e saída, bloqueando comunicação entre VLANs específicas de forma 
controlada. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Introdução ao Roteamento
• O roteamento é o processo fundamental que determina o caminho que os 
pacotes de dados percorrem entre redes distintas;
• Em ambientes corporativos, a forma como o tráfego é direcionado impacta 
diretamente a segurança da infraestrutura;
• Um roteador bem configurado não apenas conecta segmentos, mas também 
serve como ponto de controle para aplicar políticas de segurança, prevenindo 
que tráfego não autorizado atravesse fronteiras de rede;
• A compreensão dos mecanismos de encaminhamento é essencial para 
arquitetar defesas em camadas, onde o roteamento atua como a primeira 
barreira lógica contra acessos indevidos. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Introdução ao Roteamento
• Definição: Processo de seleção de caminhos em uma rede para encaminhar 
pacotes entre diferentes segmentos
• Função do roteador: Dispositivo de camada 3 que interconecta redes e toma 
decisões de encaminhamento baseadas em tabelas de roteamento
• Segurança no roteamento: O roteador é um ponto crítico de controle onde 
políticas de acesso podem ser aplicadas
• Tabela de roteamento: Estrutura de dados que armazena rotas conhecidas, 
métricas e interfaces de saída
• Next-hop: Endereço IP do próximo dispositivo no caminho até o destino final
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Roteamento Estático
• O roteamento estático consiste na configuração manual de rotas na tabela de 
roteamento pelo administrador da rede;
• Diferente do roteamento dinâmico, não há troca automática de informações 
entre roteadores;
• Cada entrada é inserida explicitamente, definindo-se a rede de destino, a 
máscara, o gateway de próximo salto e a interface de saída;
• Do ponto de vista da segurança, o roteamento estático oferece previsibilidade 
total: o administrador sabe exatamente por onde o tráfego flui, eliminando 
surpresas causadas por alterações automáticas de topologia;
• No entanto, exige manutenção manual em caso de falhas de links. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Roteamento Estático
• Configuração manual: O administrador insere cada rota individualmente no 
roteador
• Comando Linux: ip route add 192.168.2.0/24 via 192.168.1.1 dev eth0
• Vantagem de segurança: Previsibilidade total do caminho do tráfego
• Desvantagem: Não se adapta automaticamente a falhas de links ou mudanças 
de topologia
• Uso recomendado: Redes pequenas, rotas default, segmentos críticos onde o 
controle absoluto é necessário
• Persistência: Rotas adicionadas via CLI são voláteis; scripts de inicialização 
garantem persistência
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Roteamento Dinâmico — Conceitos de Segurança
• Os protocolos de roteamento dinâmico permitem que roteadores troquem 
informações de topologia automaticamente, adaptando-se a mudanças na rede;
• RIP (Routing Information Protocol) e OSPF (Open Shortest Path First) são os 
protocolos interior gateway mais conhecidos;
• Do ponto de vista da segurança, o risco principal reside na possibilidade de um 
roteador malicioso ou comprometido injetar rotas falsas na rede, desviando 
tráfego para interceptação (ataque Man-in-the-Middle);
• Por isso, em ambientes seguros, o roteamento dinâmico deve ser combinado 
com autenticação de vizinhos e filtragem de rotas. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Roteamento Dinâmico — Conceitos de Segurança
• RIP (Routing Information Protocol): Protocolo distance-vector com limite de 
15 hops; métrica baseada em contagem de saltos 
• RIPv2: Suporta autenticação por texto ou MD5, VLSM e endereçamento 
classless 
• OSPF (Open Shortest Path First): Protocolo link-state que utiliza o algoritmo 
de Dijkstra; divide a rede em áreas hierárquicas 
• Risco de segurança: Injeção de rotas falsas por roteadores não autorizados
• Mitigação: Autenticação de vizinhos, filtragem de prefixos, uso de áreas OSPF 
stub
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
RIP — Fundamentos e Segurança
• RIP é um dos protocolos de roteamento mais antigos, utilizando o algoritmo 
distance-vector onde cada roteador compartilha sua tabela completa com 
vizinhos a cada 30 segundos;
• A métrica é simplesmente a contagem de saltos (hops), com um limite máximo 
de 15, tornando-o inadequado para redes grandes;
• A versão 1 (RIPv1) não possui mecanismos de autenticação, transmitindo 
atualizações em broadcast, o que a torna insegura;
• A versão 2 (RIPv2) introduziu suporte a autenticação via senha em texto ou 
hash MD5, além de multicast direcionado (224.0.0.9), reduzindo a exposição de 
informações de roteamento. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
RIP — Fundamentos e Segurança
• Distance-vector: Cada roteador conhece apenas a distância (hops) e a direção 
para cada destino
• Broadcast vs Multicast: RIPv1 usa 255.255.255.255; RIPv2 usa 224.0.0.9
• Autenticação RIPv2: Suporta senha em texto simples ou MD5 hash 
• Split horizon e poison reverse: Mecanismos para prevenir loops de 
roteamento
• Limite de 15 hops: Rotas com 16 hops são consideradas inalcançáveis
• Insegurança inerente: Ausência de criptografia forte; vulnerável a spoofing de 
vizinhos
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
OSPF — Fundamentos e Segurança
• OSPF é um protocolo link-state que constrói um mapa completo da topologia da 
rede através do banco de dados de estado de links (LSDB);
• Cada roteador calcula independentemente a melhor rota usando o algoritmo 
SPF (Shortest Path First) de Dijkstra;
• A rede é dividida em áreas hierárquicas, com uma área backbone (Area 0) 
obrigatória;
• Do ponto de vista da segurança, OSPF suporta autenticação de área (texto 
simples, MD5 ou SHA) e pode utilizar áreas stub para limitar a propagação de 
rotas externas;
• A segmentação em áreas reduz o domínio de falhas e limita a exposição da 
topologia completa. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
OSPF — Fundamentos e Segurança
• Link-state: Cada roteador possui uma visão completa da topologia da rede
• Áreas: Segmentação hierárquica com Area 0 (backbone) como centro 
• ABR (Area Border Router): Conecta áreas não-backbone ao backbone
• Autenticação: Suporta null, simple password e MD5/HMAC-SHA
• Áreas stub: Limitam rotas externas (LSAs tipo 5), reduzindo tamanho da LSDB
• Convergência rápida: Atualizações triggered (não periódicas) quando há 
mudanças
• Métrica de custo: Baseada na largura de banda do link, não apenas hops
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Linux como Roteador Multi-Homed
• Um sistema Linux pode funcionar como roteador quando possui múltiplas 
interfaces de rede conectadas a segmentos diferentes, configuração conhecida 
como multi-homed;
• Para que o encaminhamento de pacotes entre interfaces funcione, é necessário 
habilitar o IP forwarding no kernel (net.ipv4.ip_forward=1);
• O comando ip route gerencia a tabela de roteamento principal, enquanto ip rule 
implementa Policy-Based Routing (PBR), permitindo que decisões de 
roteamento considerem não apenas o destino, mas também a origem, a 
interface de entrada ou marcas de pacotes;
• Essa flexibilidade é crucial para segurança, pois permite isolar tráfego entre 
segmentos. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Linux como Roteador Multi-Homed
• Multi-homed: Sistema com múltiplas NICs em redes distintas
• IP forwarding: Habilitado via sysctl -w net.ipv4.ip_forward=1 ou /etc/sysctl.conf
• ip route: Gerencia rotas na tabela principal ou em tabelas customizadas 
• ip rule: Define políticas que selecionam qual tabela de roteamento consultar 
• Tabelas customizadas: Definidas em /etc/iproute2/rt_tables (ex: 200 labnet)
• Persistência: Requer scripts em /etc/network/interfaces ou NetworkManager 
dispatcher 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Policy-Based Routing (PBR) no Linux
• O Policy-Based Routing estende o roteamento tradicional ao permitir que o 
administrador defina múltiplas tabelas de roteamento e regras que selecionam 
qual tabela usar com base em critérios além do endereço de destino;
• O kernel avalia as regras em ordem de prioridade (menor número = maior 
prioridade). Por padrão, existem três regras: local (prioridade 0), main (32766) e 
default (32767);
• Com PBR, é possível criar regras como "todo tráfego proveniente da interface 
eth1 deve usar a tabela 200", ou "pacotes da subnet 192.168.10.0/24 devem 
sair pelo gateway 10.0.0.1";
• Isso permite segmentar o fluxo de dados de forma granular. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Policy-Based Routing (PBR) no Linux
• ip rule show: Lista as regras atuais de roteamento por política
• Seletores comuns: from (origem), to (destino), iif (interface entrada), fwmark 
(marca do firewall)
• Criação de tabela: echo "200 labnet" >> /etc/iproute2/rt_tables
• Adicionar rota à tabela: ip route add default via 10.0.0.1 dev eth1 table labnet
• Adicionar regra: ip rule add from 192.168.10.0/24 table labnet priority 100
• Verificação: ip route get 8.8.8.8 from 192.168.10.50 simula a decisão de 
roteamento
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Access Control Lists (ACLs)
• As Listas de Controle de Acesso são regras que permitem ou negam o tráfego 
de rede baseando-se em critérios como endereços IP de origem/destino, 
protocolos, portas ou interfaces;
• No contexto de roteamento, as ACLs são aplicadas nas interfaces do roteador 
para filtrar pacotes que tentam atravessar entre segmentos;
• Diferente de um firewall de host que protege apenas o próprio sistema, ACLs 
em roteadores controlam o fluxo entre redes inteiras;
• O nftables é o framework moderno no Linux para implementar ACLs, 
substituindo o antigo iptables com uma sintaxe mais coesa e melhor 
desempenho. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Access Control Lists (ACLs)
• Função: Filtrar tráfego baseado em endereços, protocolos, portas e interfaces
• Aplicação: Interfaces de roteador controlam fluxo entre segmentos de rede
• nftables: Framework moderno de filtragem de pacotes no Linux 
• Família inet: Suporta IPv4 e IPv6 simultaneamente na mesma tabela
• Hooks: input (para o roteador), forward (através do roteador), output (do 
roteador)
• Estado da conexão: ct state established,related permite tráfego de retorno sem 
regras explícitas
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
nftables — Estrutura e Conceitos
• O nftables organiza as regras em uma hierarquia de tabelas, chains e regras;
• Uma tabela é um container que agrupa chains de um mesmo tipo de 
endereçamento (ip, ip6, inet, arp, bridge, netdev);
• As chains são ancoradas em hooks do kernel — pontos específicos no fluxo de 
processamento de pacotes como prerouting, input, forward, output e 
postrouting;
• A chain do tipo filter com hook forward é particularmente importante para 
roteadores, pois processa pacotes que atravessam o sistema;
• A política padrão (policy drop) define a ação quando nenhuma regra 
corresponde, sendo a postura de segurança recomendada. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
nftables — Estrutura e Conceitos
• Tabela: Container para chains; família inet recomendada para dual-stack 
• Chain: Container para regras; requer type, hook e priority
• Hook forward: Processa pacotes que atravessam o roteador entre interfaces
• Prioridade: Ordem de processamento; filter tem valor padrão 0
• Política padrão: policy drop nega tudo não explicitamente permitido
• Match iifname/oifname: Filtra por nome da interface de entrada/saída 
• Persistência: Configuração salva em /etc/nftables.conf e carregada via 
systemctl
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Filtragem por Interface com nftables
• A capacidade de filtrar pacotes com base na interface de entrada (iifname) e 
saída (oifname) é fundamental para roteadores multi-homed;
• Essa abordagem permite criar zonas de segurança onde o tráfego entre 
segmentos é explicitamente controlado;
• Por exemplo, pode-se permitir que a interface eth1 (rede interna) acesse a eth0 
(internet), mas bloquear o caminho inverso para novas conexões;
• O uso de variáveis no nftables simplifica a manutenção, permitindo definir 
nomes simbólicos para interfaces e conjuntos de endereços IP, tornando o 
ruleset mais legível e menos propenso a erros de configuração. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Filtragem por Interface com nftables
• ifname: Match pelo nome da interface de entrada (string comparison) 
• oifname: Match pelo nome da interface de saída
• Vantagem sobre iif: Aceita wildcards (ex: iifname "eth*") e interfaces 
inexistentes
• Regra exemplo: iifname "eth1" oifname "eth0" tcp dport 443 accept
• Bloqueio entre VLANs: iifname "eth1.10" oifname "eth1.20" drop
• Variáveis: define LAN_DEV = eth1 permite referenciar $LAN_DEV nas regras 
• Sets: Coleções de endereços ou interfaces para regras concisas
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Bloqueio de Tráfego Entre VLANs
• A segmentação de rede em VLANs é uma prática essencial de segurança, 
isolando broadcast domains e limitando a propagação de ameaças laterais;
• No entanto, para que diferentes VLANs se comuniquem, é necessário um 
roteador ou switch Layer 3;
• Esse ponto de interconexão é onde as ACLs devem ser aplicadas para controlar 
quais fluxos são permitidos;
• Com nftables em um roteador Linux, é possível criar regras específicas que 
bloqueiam completamente a comunicação entre VLANs sensíveis (ex: VLAN de 
finanças e VLAN de visitantes), ou permitem apenas protocolos específicos (ex: 
HTTP da VLAN de visitantes para a VLAN de servidores web, mas nada mais). 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Bloqueio de Tráfego Entre VLANs
• VLAN tagging: Identificação lógica de segmentos na mesma infraestrutura 
física
• Roteamento entre VLANs: Ocorre no roteador (router-on-a-stick) ou switch 
Layer 3
• Ponto de controle: O roteador é onde as ACLs devem ser aplicadas
• Regra de isolamento: iifname "eth0.10" oifname "eth0.20" drop
• Regra seletiva: iifname "eth0.20" oifname "eth0.10" tcp dport 80 accept
• Logging: log prefix "VLAN-BLOCK: " para auditoria de tentativas de acesso
• Princípio do menor privilégio: Negar tudo, permitir apenas o necessário
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Path Isolation e Segurança de Roteamento
• O isolamento de caminhos (path isolation) é uma estratégia de segurança que 
garante que tráfego de diferentes classes de serviço ou níveis de sensibilidade 
não compartilhem os mesmos caminhos físicos ou lógicos;
• Em ambientes virtualizados, isso pode ser implementado através de redes 
separadas no hypervisor (como diferentes adaptadores de rede no VirtualBox), 
cada uma mapeada para uma interface distinta no roteador Linux;
• Combinado com PBR e nftables, o administrador pode garantir que tráfego de 
gerenciamento nunca transite pela mesma interface que tráfego de visitantes, 
mesmo que ambos cheguem ao mesmo host físico. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Path Isolation e Segurança de Roteamento
• Definição: Garantia de caminhos de rede separados para diferentes tipos de 
tráfego
• Implementação: Interfaces físicas ou virtuais dedicadas por segmento de 
segurança
• VirtualBox: Adaptadores de rede separados para cada segmento (Internal 
Network 1, 2, 3)
• PBR para isolamento: Regras que forçam tráfego de gerenciamento por 
interface exclusiva
• nftables para reforço: Drop de pacotes que tentam "saltar" entre caminhos não 
autorizados
• Vantagem: Comprometimento de um segmento não afeta diretamente os outros
• Conformidade: Alinhado com frameworks como ISO 27001 e NIST SP 800-53
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Roteamento Estático vs Dinâmico
• A escolha entre roteamento estático e dinâmico envolve trade-offs entre 
administrabilidade e segurança;
• O roteamento estático oferece controle absoluto e superfície de ataque reduzida 
(não há protocolos de roteamento escutando em portas UDP), mas não se 
recupera automaticamente de falhas;
• O roteamento dinâmico oferece resiliência e escalabilidade, mas introduz uma 
superfície de ataque adicional: protocolos como RIP (UDP 520) e OSPF podem 
ser explorados se não autenticados;
• Em ambientes de alta segurança, a recomendação é utilizar roteamento estático 
para segmentos críticos e dinâmico apenas onde a resiliência é mandatória, 
sempre com autenticação habilitada. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
 Roteamento Estático vs Dinâmico — Comparativo de Segurança
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Critério Roteamento Estático Roteamento Dinâmico
**Controle** Total (administrador define tudo) Parcial (protocolo decide)
**Resiliência** Manual (requer intervenção) Automática (convergência)
**Superfície de ataque** Mínima (sem portas de protocolo) Maior (RIP/BGP/OSPF expostos)
**Autenticação** N/A (não há troca de informações) Obrigatória (MD5/SHA em OSPF)
**Escalabilidade** Baixa (trabalho manual cresce) Alta (automatizado)
**Previsibilidade** Alta (caminhos fixos) Baixa (caminhos podem mudar)
Boas Práticas de Roteamento Seguro
• A implementação de roteamento seguro requer uma abordagem em camadas 
que combine configuração correta do roteador, filtragem de pacotes e 
monitoramento contínuo;
• Primeiro, desative serviços desnecessários no roteador Linux;
• Segundo, utilize roteamento estático para segmentos críticos onde a 
previsibilidade é mais importante que a resiliência automática;
• Terceiro, quando usar roteamento dinâmico, habilite autenticação de vizinhos e 
filtre quais prefixos podem ser anunciados.
• Quarto, aplique ACLs com nftables em todas as interfaces, seguindo o princípio 
de negação padrão;
• Quinto, mantenha logs de tráfego negado para análise forense. Sexto, 
documente todas as rotas e regras para auditoria e recuperação de desastres. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Boas Práticas de Roteamento Seguro
• Desativar serviços: Remover daemons de roteamento não utilizados
• Estático para críticos: Segmentos DMZ, gerenciamento, servidores sensíveis
• Autenticação dinâmica: Sempre habilitar em RIPv2, OSPF, EIGRP, BGP
• Filtragem de prefixos: Route-maps para limitar quem pode anunciar rotas
• ACLs default-deny: policy drop em todas as chains de forward
• Logging: Registrar tentativas de acesso negadas para detecção de 
reconhecimento
• Documentação: Diagramas de rede e tabelas de roteamento atualizadas
• Auditoria: Revisões periódicas de rotas e regras de firewall
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs
Arquivos da disciplina
• Link para aGoogle Drive com os arquivos da disciplina:
– https://drive.google.com/drive/folders/
1KuGQgeDWl5RLBZntXmgqlx6NkJnvQx_i?usp=sharing
• Link encurtado:
– https://ziply.pk/QbJHLB
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-02 - Roteamento Seguro e ACLs

---

## Módulo 03 — Firewalls de Perímetro e Filtragem Avançada

Segurança em Sistemas Operacionais e Redes de
Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria

Objetivo
• O objetivo desta aula é capacitar os estudantes a compreenderem e 
implementarem arquiteturas de segurança de perímetro utilizando firewalls 
modernos. Ao final desta sessão, o aluno será capaz de diferenciar os tipos de 
firewalls (packet filtering, stateful inspection e application layer), projetar uma 
zona desmilitarizada (DMZ) segura, configurar regras avançadas de NAT (SNAT 
e DNAT) utilizando nftables, e aplicar conceitos de segmentação de rede para 
proteger ativos corporativos críticos contra acessos não autorizados 
provenientes da Internet. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Objetivo
• Diferenciar arquiteturas de firewalls (packet filter, stateful, application layer)
• Projetar e implementar uma DMZ segura
• Configurar NAT avançado (SNAT/DNAT) com nftables
• Aplicar segmentação de rede para proteção de perímetro
• Compreender logging e monitoramento de firewalls
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Introdução aos Firewalls de Perímetro
• Firewalls de perímetro constituem a primeira linha de defesa entre uma rede 
organizacional e a Internet. Diferentemente dos firewalls de host, que protegem 
máquinas individuais, os firewalls de perímetro controlam o tráfego entre redes 
distintas, tipicamente posicionados na borda da infraestrutura. Sua função 
principal é implementar a política de segurança de acesso, determinando quais 
conexões podem entrar, sair ou atravessar os limites da rede organizacional. A 
eficácia de um firewall de perímetro depende de sua correta colocação 
topológica, da precisão de suas regras de filtragem e da capacidade de 
inspeção de tráfego em múltiplas camadas do modelo OSI. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Introdução aos Firewalls de Perímetro
• Posicionamento na borda da rede (edge/border)
• Controle de tráfego entre redes de diferentes níveis de confiança
• Implementação da política de segurança de acesso
• Ponto único de entrada/saída monitorado
• Base para arquiteturas Defense in Depth
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Arquiteturas de Firewall
• As arquiteturas de firewall evoluíram significativamente desde os simples filtros 
de pacotes da primeira geração até os Next-Generation Firewalls (NGFW) 
atuais. O packet filtering firewall opera na camada 3 do modelo OSI, analisando 
apenas cabeçalhos IP e portas TCP/UDP, sendo rápido mas limitado. O stateful 
inspection firewall adiciona o conceito de tabela de estados, rastreando 
conexões ativas e permitindo decisões contextuais. O application layer firewall 
(proxy) inspeciona o conteúdo dos pacotes na camada 7, oferecendo segurança 
superior ao custo de maior latência. Cada arquitetura apresenta trade-offs entre 
performance e nível de segurança. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Arquiteturas de Firewall
• Packet Filter (1ª geração): Camada 3, análise de IP/porta, stateless
• Stateful Inspection (2ª geração): Camadas 3-4, tabela de estados, tracking de 
sessões
• Application Layer (3ª geração): Camada 7, proxy, inspeção profunda de 
conteúdo
• NGFW: Integração de múltiplas funções (IPS, VPN, identificação de aplicações)
• Trade-off: Performance vs. profundidade de inspeção
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Evolução das Arquiteturas de Firewall
• A evolução das arquiteturas de firewall reflete a crescente sofisticação das 
ameaças cibernéticas. Os primeiros filtros de pacotes (packet filtering) eram 
stateless, analisando cada pacote isoladamente sem contexto de conexão, o 
que os tornava vulneráveis a ataques de spoofing. A segunda geração 
introduziu o stateful inspection, mantendo uma tabela de estado que registra 
todas as conexões ativas (5-tuple: IP origem, IP destino, protocolo, porta 
origem, porta destino), permitindo que o firewall entenda se um pacote pertence 
a uma sessão estabelecida. A terceira geração expandiu a inspeção para a 
camada de aplicação, analisando payloads HTTP, FTP e outros protocolos, 
possibilitando bloquear malware e conteúdo malicioso que poderia passar 
despercebido em firewalls tradicionais. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Evolução das Arquiteturas de Firewall
• 1ª Geração: Packet Filter - Rápido, sem estado, vulnerável a spoofing
• 2ª Geração: Stateful Inspection - Contexto de conexão, tabela de estados, 
bloqueia spoofing
• 3ª Geração: Application Layer/Proxy - Inspeção profunda, controle de conteúdo, 
alta latência
• NGFW: Deep Packet Inspection (DPI), identificação de usuários, integração com 
AD
• Tendência: Convergência de funções de segurança em appliances unificados
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria

Conceito de DMZ (Zona Desmilitarizada)
• A Zona Desmilitarizada (DMZ - Demilitarized Zone) é uma sub-rede física ou 
lógica que expõe serviços externos de uma organização à Internet, isolando-os 
da rede interna corporativa. A DMZ funciona como uma área intermediária de 
segurança, onde residem servidores que precisam ser acessíveis externamente 
(web, DNS, email), mas que não devem ter acesso direto aos ativos internos 
sensíveis. A arquitetura típica utiliza dois firewalls: um externo (perímetro) que 
protege a DMZ da Internet, e um interno que protege a rede corporativa da 
DMZ. Se um servidor na DMZ for comprometido, o atacante ainda enfrenta uma 
barreira adicional para alcançar a rede interna. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Conceito de DMZ (Zona Desmilitarizada)
• Rede intermediária entre Internet e rede interna
• Hospeda serviços públicos (web, DNS, email, FTP)
• Isolamento de ativos críticos internos
• Arquitetura de duplo firewall ou tri-homed firewall
• Princípio: comprometimento da DMZ ≠ acesso à rede interna
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria

Arquitetura de Firewall de Perímetro com DMZ
• A arquitetura de perímetro com DMZ estabelece três zonas de segurança 
distintas: a zona não confiável (Internet), a zona controlada (DMZ) e a zona 
confiável (rede interna). O firewall de perímetro (externo) filtra tráfego entre 
Internet e DMZ, tipicamente permitindo apenas portas específicas (80, 443, 25, 
53) para servidores públicos. O firewall interno controla o tráfego entre DMZ e 
rede interna, sendo mais restritivo e permitindo apenas conexões iniciadas 
internamente ou respostas a solicitações legítimas. Uma zona adicional de 
gerenciamento (management) pode ser implementada para acesso 
administrativo seguro via jump hosts (bastion hosts), isolando o acesso 
administrativo do tráfego operacional. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Arquitetura de Firewall de Perímetro com DMZ
• Zona Não Confiável (Internet): Acesso irrestrito, maior risco
• Zona Controlada (DMZ): Serviços públicos, acesso limitado
• Zona Confiável (Internal): Ativos críticos, acesso restrito
• Firewall Perímetro: Entre Internet e DMZ, regras permissivas controladas
• Firewall Interno: Entre DMZ e Internal, regras restritivas
• Zona de Gerenciamento: Acesso administrativo isolado (jump host)
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Design de DMZ e Posicionamento de Serviços
• O design efetivo de uma DMZ requer planejamento cuidadoso do 
posicionamento de serviços baseado em sua exposição necessária e 
criticidade. Servidores web públicos são colocados na DMZ frontal, acessíveis 
diretamente da Internet. Servidores de aplicação que processam dados 
sensíveis podem residir em uma DMZ de backend ou em uma zona semi-
confiável. Bancos de dados e sistemas de arquivos críticos permanecem 
exclusivamente na rede interna, sem acesso direto da DMZ. O princípio do 
menor privilégio determina que servidores na DMZ devem ter apenas as portas 
necessárias abertas e comunicação restrita com a rede interna, tipicamente 
através de protocolos específicos em portas predefinidas. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Design de DMZ e Posicionamento de Serviços
• DMZ Frontal: Web servers, proxies reversos, DNS externos
• DMZ de Backend: Application servers, middleware, serviços de integração
• Rede Interna: Bancos de dados, file servers, AD, sistemas críticos
• Princípio do menor privilégio: Apenas portas necessárias, comunicação mínima
• Segmentação vertical: Múltiplas DMZs para diferentes níveis de sensibilidade
• Jump Hosts: Pontos de acesso administrativo únicos e monitorados
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Stateful vs Stateless Inspection
• A distinção entre inspeção stateful e stateless é fundamental para compreender 
as capacidades de um firewall. Firewalls stateless (packet filters tradicionais) 
analisam cada pacote individualmente, baseando decisões apenas em 
informações estáticas do cabeçalho (IP origem/destino, porta, protocolo), sem 
memória de conexões anteriores. Firewalls stateful mantêm uma tabela de 
estado (state table) que registra todas as conexões ativas, permitindo identificar 
se um pacote pertence a uma sessão estabelecida, é uma nova conexão ou um 
pacote inválido. Essa capacidade permite que firewalls stateful bloqueiem 
ataques de spoofing e session hijacking, além de simplificar as regras (não é 
necessário permitir explicitamente o tráfego de retorno). 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Stateful vs Stateless Inspection
• Stateless: Sem memória de estado, cada pacote analisado isoladamente
• Stateful: Mantém tabela de conexões ativas (state table)
• 5-tuple matching: IP src/dst, protocol, port src/dst para identificar sessões
• Vantagens stateful: Bloqueia spoofing, simplifica regras, permite tráfego de 
retorno automático
• Timeout de sessão: Estados expiram após período de inatividade
• Uso moderno: Stateful é padrão; stateless usado em data centers de alta 
performance
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
 Tabela de Estados (State Table)
• A tabela de estados é a estrutura de dados central de um firewall stateful, 
mantendo registros de todas as conexões de rede ativas que passaram pelo 
dispositivo. Cada entrada na tabela típicamente contém o 5-tuple (endereço IP 
de origem e destino, portas de origem e destino, protocolo), o estado atual da 
conexão TCP (SYN_SENT, ESTABLISHED, TIME_WAIT), timestamps de última 
atividade, e flags de controle. Quando um pacote chega, o firewall primeiro 
consulta a tabela de estados; se houver correspondência, o pacote é permitido 
sem nova avaliação de regras, otimizando performance. Se não houver 
correspondência, o pacote é avaliado contra as regras de firewall, e se 
permitido, uma nova entrada é criada na tabela. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
 Tabela de Estados (State Table)
• Estrutura: Hash table ou árvore balanceada para busca rápida
• Campos: 5-tuple, estado TCP, contadores de pacotes/bytes, timestamp
• Estados TCP: NONE, SYN_SENT, SYN_RECV, ESTABLISHED, FIN_WAIT, 
CLOSE_WAIT, LAST_ACK, TIME_WAIT, CLOSE
• Estados UDP/ICMP: Simulados (UDP tem estado "virtual" baseado em timeout)
• Timeout dinâmico: TCP estabelecido (horas), TCP SYN (minutos), UDP 
(segundos)
• Limitações: Consumo de memória RAM proporcional ao número de conexões
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
  Network Address Translation (NAT)
• Network Address Translation (NAT) é uma técnica essencial em firewalls de 
perímetro que permite múltiplos hosts em redes privadas (RFC 1918: 10.0.0.0/8, 
172.16.0.0/12, 192.168.0.0/16) compartilharem endereços IP públicos para 
comunicação com a Internet. O NAT opera modificando os cabeçalhos IP de 
pacotes em trânsito, substituindo endereços privados por públicos (ou vice-
versa). Além da conservação de endereços IPv4, o NAT proporciona uma 
camada adicional de segurança através da ocultação da topologia interna da 
rede, dificultando que atacantes externos mapeiem diretamente a infraestrutura 
interna. O NAT é tipicamente implementado no firewall de perímetro, no ponto 
de saída da rede para a Internet. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
  Network Address Translation (NAT)
• Conservação de IPs: Múltiplos hosts privados compartilham IP público
• Ocultação de topologia: Rede interna invisível da Internet
• RFC 1918: Endereços privados não roteáveis na Internet pública
• Stateful NAT: Rastreia conexões NAT na tabela de estados
• Segurança adicional: Barreira contra scanning direto de hosts internos
• Limitações: Quebra conexões end-to-end, complica troubleshooting
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
  Tipos de NAT: SNAT (Source NAT)
• Source NAT (SNAT), também conhecido como mascaramento (masquerading) 
quando o IP de origem é dinâmico, é o tipo de NAT utilizado quando hosts 
internos iniciam conexões para a Internet. O SNAT altera o endereço IP de 
origem dos pacotes que saem da rede privada, substituindo-o pelo endereço IP 
público do firewall. No nftables, o SNAT é implementado na chain 
POSTROUTING (após a decisão de roteamento), pois a alteração do endereço 
de origem deve ocorrer depois que o pacote já foi roteado para a interface 
externa. O SNAT pode ser estático (mapeamento fixo 1:1) ou dinâmico 
(masquerade, usando o IP atual da interface), sendo o masquerade preferido 
quando o IP público é atribuído via DHCP. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
  Tipos de NAT: SNAT (Source NAT)
• Função: Altera IP de origem de pacotes saindo da rede
• Chain: POSTROUTING (após roteamento, antes de sair pela interface)
• Sintaxe nftables: snat to IP ou masquerade (para IP dinâmico)
• Uso principal: Acesso à Internet a partir de rede privada
• SNAT Estático: Um IP interno → Um IP externo fixo
• Masquerade: Múltiplos IPs internos → IP dinâmico da interface externa
• Port Address Translation (PAT): Múltiplos hosts usam mesmo IP com portas 
diferentes
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Tipos de NAT: DNAT (Destination NAT)
• Destination NAT (DNAT) é utilizado quando tráfego da Internet precisa acessar 
servidores localizados na rede interna ou DMZ. O DNAT altera o endereço IP de 
destino dos pacotes que chegam do exterior, redirecionando-os para endereços 
privados internos. Esta técnica é fundamental para publicar serviços internos 
(web, email, SSH) na Internet sem expor diretamente os servidores. No nftables, 
o DNAT é implementado na chain PREROUTING (antes da decisão de 
roteamento), pois a alteração do destino deve ocorrer para que o pacote seja 
corretamente roteado para a rede interna. O DNAT pode redirecionar para 
diferentes portas (port forwarding), permitindo, por exemplo, que a porta 2222 
externa acesse a porta 22 (SSH) interna. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Tipos de NAT: DNAT (Destination NAT)
• Função: Altera IP de destino de pacotes entrando da Internet
• Chain: PREROUTING (antes do roteamento, logo após entrada na interface)
• Sintaxe nftables: dnat to IP:porta
• Uso principal: Publicação de servidores internos (port forwarding)
• Port Forwarding: Redirecionamento de portas (ex: 2222 externo → 22 interno)
• Load Balancing: DNAT para múltiplos backends (round-robin)
• Segurança: Permite ocultar servidores reais atrás de IPs públicos
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Comparação SNAT vs DNAT
• SNAT e DNAT são operações complementares que atuam em direções opostas 
do fluxo de tráfego. O SNAT modifica o endereço de origem e é aplicado na 
chain POSTROUTING, sendo utilizado para tráfego de saída (outbound), 
permitindo que múltiplos hosts internos acessem a Internet usando um único IP 
público. O DNAT modifica o endereço de destino e é aplicado na chain 
PREROUTING, sendo utilizado para tráfego de entrada (inbound), permitindo 
que servidores internos sejam acessíveis externamente. Ambos requerem que o 
firewall tenha habilitado o IP forwarding (roteamento entre interfaces) e que as 
regras de filtragem (filter table) permitam o tráfego encaminhado (chain 
FORWARD). 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria

Comparação SNAT vs DNAT
• SNAT: POSTROUTING, altera origem, tráfego outbound (interno → externo)
• DNAT: PREROUTING, altera destino, tráfego inbound (externo → interno)
• SNAT: Mascaramento de múltiplos hosts, acesso à Internet
• DNAT: Publicação de serviços, port forwarding
• Requisito comum: IP forwarding habilitado (net.ipv4.ip_forward=1)
• Chain FORWARD: Deve permitir tráfego entre interfaces (filter table)
• Combinação: DMZ tipicamente usa ambos (DNAT para entrada, SNAT para 
saída)
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Fluxo de Processamento no Netfilter/nftables
• O framework netfilter no kernel Linux processa pacotes através de uma série de 
hooks (pontos de interceptação) onde firewalls podem inspecionar e modificar o 
tráfego. Quando um pacote entra pela interface de rede, passa primeiro pelo 
hook PREROUTING (onde DNAT é aplicado), depois pela decisão de 
roteamento (o pacote é para mim ou para outro host?). Se for para outro host, 
passa pela chain FORWARD e depois POSTROUTING (onde SNAT é aplicado) 
antes de sair. Se for para o próprio host, passa pela chain INPUT e entrega ao 
processo local. Pacotes gerados localmente saem pela chain OUTPUT e depois 
POSTROUTING. Cada hook pode conter múltiplas tabelas (filter, nat, mangle, 
raw) com chains específicas. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Fluxo de Processamento no Netfilter/nftables
• PREROUTING: Primeiro hook, antes do roteamento (DNAT aqui)
• Decisão de roteamento: Pacote é local ou para encaminhar?
• INPUT: Pacotes destinados ao próprio host
• FORWARD: Pacotes passando pelo host (router/firewall)
• OUTPUT: Pacotes gerados pelo próprio host
• POSTROUTING: Último hook, após roteamento (SNAT aqui)
• Ordem de tabelas: raw → mangle → nat → filter
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria

Tabelas e Chains no nftables
• O nftables organiza as regras de firewall em tabelas (tables), que são coleções 
de chains (cadeias de regras) associadas a uma família de protocolos (ip, ip6, 
inet, arp, bridge). A tabela filter é usada para filtragem de pacotes (accept, drop, 
reject), sendo a mais comum para políticas de segurança básicas. A tabela nat é 
usada para tradução de endereços (snat, dnat, masquerade, redirect). A tabela 
mangle permite modificação de cabeçalhos IP (TOS, TTL). A tabela raw é usada 
para exceções de connection tracking. Cada tabela contém chains que se ligam 
aos hooks do netfilter (input, output, forward, prerouting, postrouting), permitindo 
processamento em diferentes pontos do fluxo do pacote. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Tabelas e Chains no nftables
• Famílias: inet (IPv4+IPv6), ip (IPv4), ip6 (IPv6), arp, bridge
• Tabela filter: Filtragem básica (accept, drop, reject, log)
• Tabela nat: Tradução de endereços (snat, dnat, masquerade, redirect)
• Tabela mangle: Modificação de cabeçalhos, marcação de pacotes
• Tabela raw: Exceções de connection tracking (notrack)
• Chains base: input, output, forward, prerouting, postrouting
• Chains definidas pelo usuário: Nomes arbitrários, ligados a hooks específicos
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Sintaxe Básica do nftables
• O nftables utiliza uma sintaxe declarativa e unificada que substitui as 
ferramentas legadas (iptables, ip6tables, arptables, ebtables). A estrutura 
hierárquica é: tabela → chain → regra. Para criar uma configuração básica, 
primeiro define-se a tabela (nft add table inet filter), depois a chain (nft add chain 
inet filter input { type filter hook input priority 0 \; }), e então as regras (nft add 
rule inet filter input tcp dport 22 accept). A sintaxe suporta expressões 
complexas, conjuntos (sets) para múltiplos endereços/portas, e mapas para 
configurações dinâmicas. As regras podem ser persistentes quando salvas 
em /etc/nftables.conf e carregadas com nft -f /etc/nftables.conf. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Sintaxe Básica do nftables
• Estrutura: Table → Chain → Rule
• Criação de tabela: nft add table <família> <nome>
• Criação de chain: nft add chain <table> <chain> { type <tipo> hook <hook> 
priority <n> \; }
• Adição de regra: nft add rule <table> <chain> <expressão> <ação>
• Sets: { 22, 80, 443 } para múltiplos valores
• Persistência: Arquivo /etc/nftables.conf carregado via systemd
• Visualização: nft list ruleset mostra todas as regras ativas
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Regras de Filtragem Stateful
• A configuração de regras stateful no nftables aproveita o connection tracking 
(conntrack) do kernel para identificar o estado das conexões. A expressão ct 
state permite verificar se um pacote pertence a uma conexão estabelecida 
(established), relacionada (related), nova (new) ou inválida (invalid). A política 
recomendada é permitir tráfego established e related (retorno de conexões 
iniciadas internamente), permitir new para serviços específicos desejados, e 
dropar invalid. Esta abordagem simplifica drasticamente as regras, pois não é 
necessário criar regras explícitas para o tráfego de retorno. A ordem das regras 
é importante: established/related devem vir primeiro para otimização de 
performance. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Regras de Filtragem Stateful
• Estados conntrack: new, established, related, invalid, untracked
• Regra established: ct state established,related accept (tipicamente primeira 
regra)
• Regra new: ct state new tcp dport 22 accept (para novas conexões permitidas)
• Regra invalid: ct state invalid drop (bloqueia pacotes malformados)
• Vantagem: Não precisa de regras explícitas para tráfego de retorno
• Performance: Established é processado rapidamente sem avaliação de regras 
adicionais
• Protocolos sem estado: UDP e ICMP têm estados "virtuais" baseados em 
timeouts
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Logging e Monitoramento de Firewalls
• O logging é essencial para auditoria, troubleshooting e detecção de tentativas 
de intrusão em firewalls. No nftables, o logging pode ser implementado via ação 
log (mensagens no kernel log, acessíveis via dmesg ou journalctl) ou counter 
(contagem de pacotes sem log). É recomendado logar drops de tráfego 
suspeito, especialmente na chain INPUT, para identificar tentativas de scanning 
e ataques. O prefixo de log permite identificar a origem da mensagem (log prefix 
\"DROP-INPUT: \"). Para análise centralizada, os logs podem ser encaminhados 
via rsyslog para um servidor SIEM. O monitoramento contínuo inclui análise de 
padrões de tráfego, detecção de anomalias e alertas automatizados para 
eventos de segurança. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Logging e Monitoramento de Firewalls
• Ação log: log prefix \"descricao: \" envia para kernel log
• Visualização: dmesg, journalctl -k, ou /var/log/kern.log
• Counter: Contagem sem log para estatísticas (counter packets 0 bytes 0)
• Rate limiting: limit rate 10/second evita flood de logs
• Log de drops: Essencial para detectar tentativas de ataque
• SIEM: Integração com sistemas de gerenciamento de eventos de segurança
• Análise: Ferramentas como fwlogwatch ou scripts customizados para parse de 
logs
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Práticas de Hardening de Firewalls
• O hardening de firewalls de perímetro envolve configurações que minimizam a 
superfície de ataque e garantem a integridade das políticas de segurança. A 
política padrão (default policy) deve ser DROP para todas as chains (input, 
forward, output), permitindo explicitamente apenas o tráfego necessário. O 
acesso administrativo deve ser restrito a interfaces específicas (nunca acessível 
via Internet diretamente) e utilizar autenticação forte (chaves SSH, não senhas). 
As regras devem ser documentadas extensivamente com comentários. O 
firewall deve sincronizar seu relógio via NTP para correlação precisa de logs. 
Revisões periódicas das regras devem remover regras obsoletas e verificar a 
conformidade com as políticas de segurança atualizadas. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Práticas de Hardening de Firewalls
• Política padrão: DROP all, ALLOW explicitamente o necessário (whitelist)
• Acesso administrativo: Apenas via interface interna ou VPN, nunca via WAN
• Autenticação: Chaves SSH, 2FA, sem login root direto
• Documentação: Comentários em todas as regras explicando propósito
• Sincronização de tempo: NTP essencial para correlação de logs
• Revisões periódicas: Auditoria trimestral de regras e políticas
• Backup: Configurações versionadas e backup antes de alterações
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Considerações de Performance
• A performance de firewalls de perímetro é crítica, pois representam um ponto de 
estrangulamento potencial para todo o tráfego da organização. Firewalls stateful 
consomem memória RAM proporcional ao número de conexões simultâneas 
(state table), enquanto firewalls com Deep Packet Inspection (DPI) consomem 
CPU intensivamente. Para otimização, regras mais frequentemente 
correspondidas devem ser colocadas no início das chains. O uso de sets 
(conjuntos) para múltiplos endereços ou portas é mais eficiente que regras 
individuais. O connection tracking pode ser desabilitado para tráfego específico 
onde não é necessário (notrack). Em ambientes de alta performance, considere 
hardware dedicado ou smartNICs com offloading de processamento de pacotes. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Considerações de Performance
• Consumo de RAM: State table cresce com conexões simultâneas (bytes por 
estado: ~300 bytes)
• Consumo de CPU: DPI e inspeção SSL/TLS são intensivos
• Otimização de regras: Regras comuns primeiro, sets ao invés de múltiplas 
regras similares
• Notrack: Desabilitar conntrack para tráfego que não precisa (ex: balanceadores 
internos)
• Offloading: Hardware dedicado para firewalls de alta performance (10Gbps+)
• Benchmarking: Testes de carga regulares para validar capacidade
• Escalabilidade: Clustering de firewalls para redundância e performance
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria
Arquivos da disciplina
• Link para o Google Drive com os arquivos da disciplina:
– https://drive.google.com/drive/folders/
1KuGQgeDWl5RLBZntXmgqlx6NkJnvQx_i?usp=sharing
• Link encurtado:
– https://ziply.pk/QbJHLB
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Teoria

---

## Módulo 04 — Redes Privadas Virtuais (VPN)

Segurança em Sistemas Operacionais e Redes de
Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria

Objetivo
• Compreender os fundamentos teóricos e práticos das Redes Privadas Virtuais (VPN), 
incluindo tipos de implementação, protocolos criptográficos (IPsec, SSL/TLS, WireGuard), 
arquiteturas de túnel versus transporte, criptografia assimétrica aplicada a VPNs e o 
conceito de Perfect Forward Secrecy;
• Ao final, o aluno será capaz de implementar uma VPN site-to-site simples utilizando 
WireGuard entre duas máquinas virtuais Linux Mint, configurar chaves públicas/privadas, 
testar conectividade segura entre segmentos de rede e comparar o desempenho e 
complexidade com OpenVPN. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Conceitos Fundamentais de VPN
• Uma Rede Privada Virtual (VPN) é uma tecnologia que cria um túnel criptografado sobre 
uma rede pública não confiável, tipicamente a Internet, permitindo que dispositivos se 
comuniquem como se estivessem conectados diretamente a uma rede privada;
• A VPN garante confidencialidade, integridade e autenticidade dos dados transmitidos 
através de algoritmos criptográficos robustos. Historicamente, surgiram como resposta à 
necessidade de interconectar filiais de empresas de forma segura sem o custo de links 
dedicados privados;
• Hoje, são essenciais para trabalho remoto, proteção de dados em redes públicas e 
conformidade regulatória;
• A arquitetura VPN substitui a camada física de rede por uma camada lógica abstrata, onde 
a segurança é implementada através de protocolos específicos que encapsulam e 
criptografam o tráfego original. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Conceitos Fundamentais de VPN
• Definição: Túnel lógico criptografado sobre rede pública não confiável
• Objetivos principais: Confidencialidade, integridade, autenticidade e não-repúdio
• Contexto histórico: Substituíram links dedicados caros para interligação de filiais
• Aplicações modernas: Trabalho remoto, BYOD, proteção em Wi-Fi público, compliance
• Princípio de funcionamento: Encapsulamento de pacotes + criptografia + autenticação
• Diferença de rede privada física: Usa infraestrutura compartilhada logicamente isolada
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Conceitos Fundamentais de VPN
Tipos de VPN – Site-to-Site vs Remote Access
• As VPNs são classificadas principalmente pelo seu modelo de deployment e uso;
• O tipo site-to-site interconecta duas ou mais redes fixas, como filiais de uma empresa, 
através de gateways VPN que criptografam todo o tráfego entre as redes 
automaticamente, sem necessidade de configuração individual nos dispositivos dos 
usuários;
• O tipo remote access (acesso remoto) conecta um dispositivo individual, como o laptop de 
um funcionário, à rede corporativa central, exigindo instalação de software cliente e 
autenticação do usuário;
• Existe ainda a variação host-to-host, rara em ambientes corporativos, onde dois 
dispositivos individuais se comunicam diretamente;
• A escolha do tipo depende do cenário: site-to-site é ideal para infraestrutura permanente 
entre filiais, enquanto remote access é essencial para mobilidade e home office. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Tipos de VPN – Site-to-Site vs Remote Access
• Site-to-Site: Conecta redes completas (filial ↔ matriz); gateways cuidam da criptografia
• Intranet-based: Mesma organização, múltiplas localidades
• Extranet-based: Conexão segura com parceiros de negócio
• Remote Access: Dispositivo individual ↔ rede corporativa; requer cliente VPN
• SSL VPN: Acesso via browser, granularidade por aplicação
• Client-based: Software dedicado, acesso completo à rede
• Host-to-Host: Comunicação direta entre dois endpoints específicos
• Critérios de escolha: Escalabilidade, custo, requisitos de segurança, experiência do 
usuário
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Tipos de VPN – Site-to-Site vs Remote Access
 IPsec – Arquitetura e Modos de Operação
• IPsec (Internet Protocol Security) é um conjunto de protocolos padronizado pela IETF que 
opera na camada de rede (camada 3 do modelo OSI), oferecendo segurança transparente 
para todas as aplicações sem necessidade de modificação;
• É composto por três protocolos principais: AH (Authentication Header) que garante 
autenticidade e integridade mas não criptografa; ESP (Encapsulating Security Payload) 
que oferece confidencialidade, integridade e autenticidade; e IKE (Internet Key Exchange) 
que gerencia o estabelecimento de chaves e negociação de parâmetros de segurança;
• IPsec opera em dois modos: modo transporte, que protege apenas o payload do pacote IP 
mantendo o cabeçalho original visível, ideal para host-to-host; e modo túnel, que 
encapsula o pacote IP inteiro dentro de um novo pacote IP, sendo o padrão para VPNs 
site-to-site;
• A complexidade de configuração e o overhead de processamento são suas principais 
desvantagens comparadas a soluções modernas. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
 IPsec
• Camada de operação: Rede (OSI L3) – transparente para aplicações
• Componentes principais:
• AH (Authentication Header): Integridade e autenticação, sem criptografia
• ESP (Encapsulating Security Payload): Confidencialidade + integridade + 
autenticação
• IKE/IKEv2: Troca automática de chaves e negociação de SAs (Security Associations)
• Modos de operação:
• Transporte: Protege payload; mantém cabeçalho IP original visível
• Túnel: Encapsula pacote IP inteiro; usado em VPNs site-to-site
• Vantagens: Padronização IETF, interoperabilidade entre vendors, suporte nativo em SOs
• Desvantagens: Complexidade de configuração, overhead de processamento, dificuldade 
com NAT
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
SSL/TLS VPN – Acesso Baseado em Aplicação
• As VPNs baseadas em SSL/TLS operam na camada de aplicação (camada 7 do modelo 
OSI), utilizando o protocolo HTTPS (porta 443) já permitido na maioria dos firewalls 
corporativos, o que elimina problemas de travessia de NAT e firewall;
• Diferentemente do IPsec que concede acesso completo à rede, as VPNs SSL/TLS podem 
oferecer granularidade por aplicação (web, e-mail, arquivo), reduzindo a superfície de 
ataque;
• Funcionam através de navegadores web com plugins ou clientes leves, simplificando a 
distribuição e manutenção. OpenVPN é a implementação open-source mais conhecida, 
utilizando bibliotecas OpenSSL para criptografia;
• A principal limitação é o desempenho inferior em altas taxas de transferência comparado a 
soluções de camada inferior e a dependência de certificados digitais bem gerenciados. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
SSL/TLS VPN
• Camada de operação: Aplicação (OSI L7) – usa porta HTTPS/443
• Vantagens de traversabilidade: Funciona através de NATs e firewalls restritivos
• Granularidade: Acesso por aplicação vs acesso completo à rede (full tunnel)
• Implementação típica: Cliente leve ou browser-based; fácil deploy
• OpenVPN: Implementação open-source madura, usa OpenSSL, suporta múltiplas 
plataformas
• Desafios: Overhead de TLS, gerenciamento de certificados, dependência de infraestrutura 
PKI
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
WireGuard – A Nova Geração de VPN
• WireGuard é um protocolo VPN moderno desenvolvido por Jason Donenfeld, projetado 
para ser extremamente simples, rápido e seguro, com uma base de código de 
aproximadamente 4.000 linhas (vs 400.000+ do OpenVPN/Ipsec);
• Opera no kernel Linux como módulo, oferecendo desempenho próximo ao de IPsec nativo 
com configuração drasticamente simplificada;
• Utiliza criptografia de curvas elípticas Curve25519 para troca de chaves, ChaCha20 para 
criptografia simétrica e Poly1305 para autenticação de mensagens – um conjunto 
criptográfico moderno e eficiente;
• A configuração baseia-se em troca de chaves públicas entre pares (peers), eliminando a 
necessidade de infraestrutura de certificados complexa;
• Sua simplicidade reduz a superfície de ataque e facilita auditorias de segurança formais. É 
ideal para cenários site-to-site e remote access, sendo adotado rapidamente por 
provedores de VPN comerciais e administradores de sistemas. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
WireGuard
• Filosofia: Código mínimo (~4.000 linhas), alta performance, configuração simples
• Integração: Módulo do kernel Linux; também disponível para Windows, macOS, BSD, 
mobile
• Criptografia moderna:
• Curve25519: Troca de chaves de curva elíptica
• ChaCha20: Cifra de fluxo, mais rápida que AES em software sem aceleração 
hardware
• Poly1305: MAC (Message Authentication Code) para integridade
• Blake2s: Hashing para derivação de chaves
• Modelo de configuração: Chaves públicas/privadas por peer; sem certificados X.509 
complexos
• Vantagens: Velocidade, simplicidade de configuração, menor superfície de ataque, 
auditável
• Limitações: Relativamente novo (2015+), ecossistema de ferramentas ainda em evolução
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria

Túnel vs Transporte – Arquiteturas de Encapsulamento
• A distinção entre modos túnel e transporte define como os pacotes originais são 
processados pela VPN;
• No modo túnel, todo o pacote IP original (cabeçalho + payload) é encapsulado dentro de 
um novo pacote, criando uma nova camada de roteamento;
• Isso permite que redes com esquemas de endereçamento diferentes ou sobrepostos se 
comuniquem, pois os endereços internos ficam ocultos;
• É o padrão para VPNs site-to-site. No modo transporte, apenas o payload (dados da 
camada superior) é protegido, mantendo o cabeçalho IP original intacto e visível;
• Isso requer que os endpoints tenham endereços IP roteáveis e visíveis um para o outro, 
sendo adequado para comunicação host-to-host em redes já interconectadas;
• A escolha impacta diretamente a visibilidade do tráfego, a capacidade de traversar NAT e 
a complexidade de roteamento. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Túnel vs Transporte
• Modo Túnel:
• Encapsula pacote IP inteiro em novo pacote IP
• Endereços internos ficam ocultos (privados) atrás do gateway VPN
• Permite sobreposição de endereçamento entre redes
• Padrão para site-to-site; essencial para conectar filiais
• Modo Transporte:
• Protege apenas payload; cabeçalho IP original permanece visível
• Requer conectividade IP direta entre endpoints
• Menor overhead de encapsulamento
• Ideal para host-to-host ou proteção de tráfego já roteável
• Decisão de design: Depende de requisitos de privacidade de endereçamento, NAT e 
topologia
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
IPsec – Modos Túnel vs Transporte
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria

Criptografia Assimétrica na VPN
• A criptografia assimétrica (de chave pública) é fundamental para o estabelecimento inicial 
de VPNs, resolvendo o problema da distribuição segura de chaves em canais inseguros;
• Cada participante possui um par de chaves: uma chave privada mantida em segredo 
absoluto e uma chave pública distribuída livremente;
• Na prática VPN, as chaves públicas são trocadas entre pares (peers) ou através de 
certificados digitais assinados por uma Autoridade Certificadora (CA);
• O processo de handshake utiliza estas chaves para autenticar as identidades e negociar 
uma chave de sessão simétrica que será usada para criptografar o volume real de dados;
• Algoritmos como RSA (tradicional) e ECC/Elliptic Curve Cryptography (moderno, usado 
pelo WireGuard) são empregados;
• A segurança baseia-se em problemas matemáticos computacionalmente difíceis: fatoração 
de grandes números primos (RSA) ou logaritmo discreto em curvas elípticas (ECC). 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Criptografia Assimétrica
• Par de chaves: Privada (secreta) + Pública (distribuída)
• Função na VPN: Autenticação de identidade + estabelecimento de canal seguro para 
troca de chaves simétricas
• Algoritmos tradicionais: RSA (baseado em fatoração de primos)
• Algoritmos modernos: ECC – Curve25519, P-256 (menores chaves, mesmo nível de 
segurança)
• Processo prático:
• Troca de chaves públicas entre peers
• Autenticação mútua via assinaturas digitais
• Geração de chave de sessão simétrica via Diffie-Hellman (estabelecimento de segredo 
compartilhado via Diffie-Hellman (ECDH), seguido de derivação de chaves simétricas 
de sessão via KDF(1));
• Criptografia simétrica assume o tráfego de dados
• Vantagem sobre distribuição de chaves simétricas: Elimina necessidade de canal 
seguro prévio
• __________
(1) 1. Troca de chaves públicas (ou certificados); 2. Autenticação mútua (assinaturas digitais / 
certificados / PSK); 3. ECDH → gera segredo compartilhado; 4. KDF → deriva chaves simétricas de 
sessão; 5. Criptografia simétrica assume o tráfego
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Perfect Forward Secrecy (PFS)
• Perfect Forward Secrecy (PFS), também chamada de forward secrecy, é uma propriedade 
criptográfica essencial que garante que a comprometimento de uma chave privada de 
longo prazo não permita a decifração de comunicações passadas registradas por um 
atacante;
• Sem PFS, um atacante que grave tráfego criptografado hoje poderia armazená-lo 
indefinidamente e decifrá-lo futuramente caso obtenha a chave privada do servidor através 
de um breach;
• Com PFS, cada sessão de comunicação gera chaves de sessão efêmeras (temporárias) 
através de troca Diffie-Hellman (DH) ou Elliptic Curve Diffie-Hellman (ECDH), que são 
descartadas após o término da sessão;
• Mesmo que a chave privada permanente seja comprometida posteriormente, as sessões 
anteriores permanecem seguras porque as chaves efêmeras não podem ser 
reconstruídas;
• O TLS 1.3 tornou PFS obrigatório, e protocolos VPN modernos como WireGuard e 
OpenVPN bem configurados a implementam por padrão. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Perfect Forward Secrecy
• Definição: Comprometimento de chave de longo prazo não expõe sessões passadas
• Mecanismo: Troca efêmera Diffie-Hellman (DHE) ou Elliptic Curve Diffie-Hellman 
(ECDHE) por sessão
• Ciclo de vida da chave: Gerada no handshake → usada na sessão → descartada 
permanentemente
• Proteção contra: Ataques de gravação passiva (store now, decrypt later) e breaches 
futuros
• Impacto do Heartbleed: PFS mitigou danos do vazamento OpenSSL ao proteger sessões 
históricas
• TLS 1.3: Torna PFS obrigatório; todas as cipher suites usam troca de chaves efêmera
• WireGuard: Implementa PFS nativamente através de Curve25519 com rekeying periódico
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria

WireGuard na Prática – Conceitos de Configuração
• A configuração do WireGuard é notavelmente simples comparada a alternativas 
tradicionais;
• Cada peer (par) é definido por uma interface virtual (tipicamente wg0) associada a uma 
chave privada e um endereço IP virtual dentro do túnel;
• A conectividade é estabelecida definindo peers através de suas chaves públicas, 
endereços IP permitidos (AllowedIPs) e, para peers iniciadores, o endpoint remoto 
(IP:porta);
• O WireGuard é stateless na maioria dos aspectos – não há handshake complexo 
persistente; se um peer possui o endereço do outro e as chaves corretas, simplesmente 
envia pacotes criptografados;
• A opção PersistentKeepalive mantém NAT mappings abertos enviando pacotes periódicos;
• Para site-to-site, cada gateway precisa rotear o tráfego das redes locais através da 
interface wg0 e configurar NAT/masquerade se necessário para acesso à Internet através 
do túnel. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
 Configuração WireGuard
• Interface virtual: wg0 com endereço IP privado do túnel (ex: 10.0.0.1/24)
• Chaves: Par de chaves Curve25519 por interface; pública é compartilhada, privada 
protegida
• Peers: Definidos por [Peer] com PublicKey, AllowedIPs, Endpoint (opcional para 
responder)
• AllowedIPs: Define quais destinos são roteados através do túnel (0.0.0.0/0 para full 
tunnel)
• PersistentKeepalive: Intervalo em segundos para manter conexão através de NAT
• Roteamento: ip route ou PostUp scripts para configurar forwarding e NAT
• Ferramentas: wg (CLI) e wg-quick (script para simplificar up/down da interface)
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
OpenVPN – Configuração Básica e Comparação
• OpenVPN, embora mais antigo e complexo, permanece como referência de 
interoperabilidade e flexibilidade;
• Utiliza arquivos de configuração .ovpn que combinam parâmetros de conexão, certificados 
e chaves;
• Requer uma infraestrutura de Certificados (CA) para assinar certificados de servidor e 
clientes, ou pode usar chaves estáticas pré-compartilhadas (menos seguro);
• Suporta tanto modo túnel (TUN – camada 3) quanto modo bridge (TAP – camada 2), 
oferecendo versatilidade para cenários que exigem broadcast;
• A configuração envolve gerar uma CA com Easy-RSA, criar certificados, configurar 
parâmetros de criptografia (cipher, auth, TLS-version) e definir rotas;
• Comparado ao WireGuard, exige mais etapas de setup, maior consumo de recursos, mas 
oferece recursos avançados como autenticação multi-fator, failover e integração com 
LDAP/AD. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
OpenVPN vs WireGuard
• OpenVPN:
• Baseado em SSL/TLS com certificados X.509
• Suporta TUN (L3) e TAP (L2/bridge)
• Configuração complexa: CA, certificados, ciphers, HMAC
• Alta compatibilidade: Windows, Linux, macOS, iOS, Android
• Recursos avançados: 2FA, scripts de up/down, plugins
• WireGuard:
• Baseado em chaves públicas Curve25519 (sem certificados)
• Apenas modo TUN (L3), código mínimo
• Configuração declarativa simples
• Performance superior, menor latência
• Criptografia moderna fixa (ChaCha20, Poly1305)
• Decisão: WireGuard para novos deployments simples; OpenVPN para requisitos 
corporativos complexos
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Considerações de Segurança em VPNs
• A segurança de uma VPN depende não apenas do protocolo escolhido, mas de práticas 
operacionais rigorosas;
• A proteção das chaves privadas é absoluta – devem ser armazenadas com permissões 
restritas (0400 no Linux) e nunca transmitidas por canais inseguros;
• A atualização regular do software VPN é crítica para correção de vulnerabilidades 
criptográficas;
• O gerenciamento de acessos deve seguir o princípio do menor privilégio: AllowedIPs no 
WireGuard ou ACLs no OpenVPN devem restringir exatamente o necessário;
• Logs de conexão devem ser monitorados para detectar tentativas de autenticação falhas 
ou padrões anômalos;
• Em ambientes corporativos, a segmentação via VPN deve integrar-se a firewalls de 
perímetro e sistemas IDS/IPS;
• Finalmente, a dependência de uma única VPN como única camada de defesa viola o 
princípio de defesa em profundidade – a VPN deve ser uma camada entre várias. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Segurança Operacional
• Proteção de chaves: Permissões 0400, armazenamento seguro, nunca em repositórios 
git
• Atualizações: Manter wireguard-tools/kernel module ou openvpn atualizados
• Menor privilégio: Restringir AllowedIPs/rotas ao mínimo necessário
• Monitoramento: Logs de handshake, bytes transferidos, erros de autenticação
• Integração: VPN como camada de uma arquitetura defense-in-depth com firewall + IDS
• Split tunneling vs full tunnel: Avaliar riscos de vazamento de tráfego no split tunnel
• Auditoria: Verificar periodicamente chaves ativas, peers não utilizados, configurações 
órfãs
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Troubleshooting Comum em VPNs
• Os problemas mais frequentes em VPNs envolvem conectividade, roteamento e 
performance;
• Falhas de conectividade geralmente originam-se de firewalls bloqueando as portas 
necessárias (UDP 51820 para WireGuard, UDP 1194 para OpenVPN padrão), NAT mal 
configurado ou chaves públicas trocadas incorretamente;
• Problemas de roteamento ocorrem quando AllowedIPs está mal configurado, forwarding 
de IP não está habilitado no kernel, ou regras de iptables/nftables bloqueiam o tráfego 
encapsulado;
• Degradação de performance pode ser causada por MTU incompatível (túneis adicionam 
overhead; WireGuard adiciona ~60 bytes), algoritmos criptográficos incompatíveis com 
aceleração hardware, ou latência excessiva do link subjacente;
• Ferramentas como ping, traceroute, tcpdump, wg show e logs do kernel (dmesg) são 
essenciais para diagnóstico sistemático. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
 Troubleshooting
• Problemas de conectividade:
• Verificar firewall (UDP 51820 WireGuard, UDP 1194 OpenVPN)
• Confirmar chaves públicas corretas entre pares
• Testar endpoint com nc -vu IP porta
• Problemas de roteamento:
• sysctl net.ipv4.ip_forward=1 habilitado?
• AllowedIPs cobre as redes de destino?
• Regras de firewall permitem tráfego na interface wg0?
• Problemas de performance:
• MTU ajustado (túnel reduz MTU efetivo; testar com ping -M do -s 1420)
• CPU saturada em criptografia? Verificar aceleração hardware
• Latência do link subjacente com mtr ou iperf3
• Ferramentas de diagnóstico: wg show, ip route, ss -tulpn, tcpdump -i wg0
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Tendências e Futuro das VPNs
• O cenário de VPNs evolui rapidamente com a adoção de arquiteturas Zero Trust, onde a 
simples conectividade à rede interna não concede mais acesso implícito;
• Modelos como SDP (Software-Defined Perimeter) substituem VPNs tradicionais por 
acesso contextual baseado em identidade;
• A resistência quântica torna-se preocupação crescente: algoritmos de troca de chaves 
baseados em curvas elípticas (ECC) serão vulneráveis a computadores quânticos via 
algoritmo de Shor, demandando migração para criptografia pós-quântica (ex: lattice-based 
KEMs);
• O WireGuard já experimenta extensões híbridas combinando X25519 com algoritmos pós-
quânticos;
• Mesh VPNs (como Tailscale baseado em WireGuard) simplificam conectividade entre 
múltiplos pontos eliminando configuração manual de peers;
• A integração com SASE (Secure Access Service Edge) unifica VPN, firewall, CASB e Zero 
Trust em plataformas cloud-native. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Futuro das VPNs
• Zero Trust Network Access (ZTNA): Acesso por aplicação, não por rede; verificação 
contínua
• Software-Defined Perimeter (SDP): Ocultação da infraestrutura; acesso apenas após 
autenticação forte
• Pós-quântico: Migração para algoritmos resistentes a Shor's algorithm (NIST PQC 
standards)
• Mesh VPNs: Tailscale, Headscale – auto-descoberta de peers, NAT traversal automático
• SASE: Convergência de VPN, segurança de rede e SD-WAN em serviços cloud
• WireGuard como base: Protocolo subjacente para muitas soluções modernas devido à 
simplicidade
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Resumo e Checklist de Decisão
• A escolha de uma solução VPN requer análise multidimensional;
• Para interligação permanente de filiais com alto throughput e baixa latência, WireGuard 
site-to-site é atualmente a escolha mais eficiente;
• Para ambientes corporativos que exigem integração com Active Directory, autenticação 
multi-fator e políticas complexas de acesso, OpenVPN ou soluções comerciais baseadas 
em IPsec permanecem relevantes;
• Para acesso remoto ocasional de funcionários, soluções SSL VPN browser-based 
oferecem simplicidade de deploy;
• Independentemente da escolha, o checklist deve incluir: (1) criptografia forte com PFS 
obrigatório; (2) gerenciamento seguro de chaves/certificados; (3) monitoramento e logging; 
(4) integração com firewall e IDS; (5) testes regulares de vulnerabilidade; (6) plano de 
atualização e patching;
• A segurança da VPN é tão forte quanto seu elo mais fraco – geralmente a configuração 
humana. 
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Checklist de Decisão
• Cenário Site-to-Site (filiais): WireGuard – performance, simplicidade, custo zero
• Cenário Corporate Complexo: OpenVPN/IPsec – AD integration, MFA, políticas 
granulares
• Cenário Remote Access Leve: SSL VPN browser-based – sem instalação de cliente
• Checklist de segurança obrigatório:
• PFS habilitado e verificável
• Chaves privadas com permissões 0400, sem backup em locais inseguros
• AllowedIPs/rotas minimizadas (princípio do menor privilégio)
• Logs de conexão centralizados e monitorados
• Firewall de perímetro integrado
• Testes de penetração anuais no túnel VPN
• Lembrete: A VPN é uma camada, não a solução completa de segurança
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria
Segurança em 
Sistemas 
Operacionais e 
Redes de 
Computadores II
ISG012-04 - Redes 
Privadas Virtuais 
(VPN) - Teoria

Arquivos da disciplina
• Link para o Google Drive com os arquivos da disciplina:
– https://drive.google.com/drive/folders/
1KuGQgeDWl5RLBZntXmgqlx6NkJnvQx_i?usp=sharing
• Link encurtado:
– https://ziply.pk/QbJHLB
Segurança em Sistemas Operacionais e Redes de Computadores II
ISG012-04 - Redes Privadas Virtuais (VPN) - Teoria

---

## Módulo 05 — Firewalls de Host: Defesa do Endpoint em Sistemas Operacionais

Segurança em Sistemas Operacionais e Redes de
Computadores I
ISG012-05 - Firewalls de Host: Defesa do Endpointem 
Sistemas Operacionais 

Objetivo
• Compreender a arquitetura e funcionamento dos firewalls de host em ambientes 
Windows e Linux, identificando os diferentes perfis de segurança, regras de 
tráfego inbound e outbound, mecanismos de logging, comparando as 
abordagens de segurança entre plataformas proprietárias e livres. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 

Arquitetura de Firewalls de Host
• O firewall de host constitui a última linha de defesa na arquitetura de segurança 
em camadas, operando diretamente sobre o sistema operacional para filtrar 
tráfego de rede na camada de aplicação e transporte. Diferente dos firewalls de 
perímetro, protege endpoints individuais através da inspeção de pacotes que 
entram (inbound) e saem (outbound) da máquina, aplicando políticas baseadas 
em endereços IP, portas, protocolos e aplicações específicas, integrando-se ao 
kernel ou subsistema de rede do sistema operacional. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Arquitetura de Firewalls de Host
• Definição: Software de filtragem de tráfego instalado no endpoint
• Posicionamento: Camada de host no modelo Defense in Depth
• Escopo: Proteção individual vs. firewalls de rede (proteção de segmento)
• Funcionalidades: Stateful inspection, filtragem por aplicação, logging local
• Integração: Kernel-level (Linux) ou serviço do sistema (Windows)
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Inspeção Stateful vs Stateless
• A inspeção stateful (com estado) representa a capacidade do firewall de manter 
o contexto das conexões de rede em uma tabela de estados, diferenciando 
pacotes que iniciam novas conexões daqueles que respondem a comunicações 
já estabelecidas;
• Diferentemente da abordagem stateless (sem estado), que analisa cada pacote 
isoladamente baseado apenas em headers, o stateful inspection rastreia o ciclo 
completo da conexão TCP (SYN, SYN-ACK, ACK) e associações UDP, 
permitindo regras mais seguras que bloqueiam tráfego não solicitado enquanto 
permitem respostas válidas a requisições internas, reduzindo a superfície de 
ataque sem comprometer a funcionalidade. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Inspeção Stateful vs Stateless
• Stateful: Mantém tabela de conexões ativas (conntrack); permite 
established/related
• Stateless: Análise packet-by-packet; regras estáticas baseadas em portas/IP
• Vantagem Stateful: Bloqueia scans furtivos e pacotes fora de sequência TCP
• Implementação Windows: Windows Firewall é stateful por padrão (diferenciação 
de conexões)
• Implementação Linux: Netfilter com módulo conntrack; nftables usa ct state
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Windows Firewall: Perfis de Rede
• O Windows Firewall implementa três perfis de segurança adaptativos que se 
ativam automaticamente conforme a localização da conexão de rede detectada;
•  O perfil Domain aplica-se quando o computador se conecta a uma rede 
corporativa com controlador de domínio autenticado, oferecendo políticas mais 
permissivas para serviços empresariais;
•  O perfil Private destina-se a redes domésticas ou de pequenos escritórios 
confiáveis, enquanto o perfil Public protege computadores em redes não 
confiáveis como Wi-Fi públicos, aplicando as restrições mais rigorosas. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Windows Firewall: Perfis de Rede
• Domain Profile: Ativo quando autenticado no AD; políticas corporativas 
aplicadas; discovery habilitado
• Private Profile: Redes confiáveis identificadas pelo usuário; compartilhamento 
de arquivos permitido
• Public Profile: Redes não identificadas; descoberta de rede desativada; bloqueio 
estrito de entrada
• Características: Perfis mutualmente exclusivos por interface de rede; adaptação 
automática
• Configuração: Gerenciável via GUI (wf.msc), GPO ou PowerShell (Set-
NetFirewallProfile)
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Windows Firewall: Perfis de Rede
• Domain Profile: Ativo quando autenticado no AD; políticas corporativas 
aplicadas; discovery habilitado
• Private Profile: Redes confiáveis identificadas pelo usuário; compartilhamento 
de arquivos permitido
• Public Profile: Redes não identificadas; descoberta de rede desativada; bloqueio 
estrito de entrada
• Características: Perfis mutualmente exclusivos por interface de rede; adaptação 
automática
• Configuração: Gerenciável via GUI (wf.msc), GPO ou PowerShell (Set-
NetFirewallProfile)
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Windows Firewall: Perfis de Rede
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Regras Inbound e Outbound
• As regras de firewall definem o comportamento do tráfego baseado na direção 
da comunicação;
• Regras inbound controlam conexões iniciadas externamente que tentam 
alcançar o host, protegendo contra acessos não solicitados a serviços locais; 
• Regras outbound gerenciam conexões iniciadas pelo host para destinos 
externos, essenciais para impedir que malware se comunique com servidores 
de comando e controle (C2) ou exfiltre dados;
• Ambas permitem especificar portas TCP/UDP, protocolos ICMP, caminhos de 
executáveis e perfis de rede aplicáveis. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Regras Inbound e Outbound
• Inbound Rules: Bloqueiam/permitem tráfego externo entrante; críticas para 
servidores locais; proteção contra scans
• Outbound Rules: Controlam tráfego de saída; importante para prevenir 
exfiltração de dados e comunicação C2
• Default Action: Geralmente allow outbound, block inbound (postura padrão 
Windows); Linux frequentemente drop all
• Escopo: Aplicáveis por perfil (Domain/Private/Public) ou interface específica
• Ações: Allow (permitir), Block (bloquear), Allow if secure (refere-se a uma ação 
avançada do Windows Firewall qu  condiciona a permissão de tráfego à 
autenticação e criptografia via protocolo IPsec (Internet Protocol Security)
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Regras Inbound e Outbound
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Logging e Monitoramento
• O registro de eventos do firewall fornece auditoria essencial para análise 
forense e detecção de tentativas de intrusão;
• O Windows Firewall gera logs em arquivo texto localizado em %SystemRoot%
\System32\LogFiles\Firewall\pfirewall.log, registrando conexões dropadas e 
bem-sucedidas conforme configuração;
• A integração com o Event Viewer permite correlacionar eventos de segurança 
(IDs 5150-5159) com outras atividades do sistema, possibilitando a identificação 
de padrões de scanning, tentativas de conexão em portas fechadas e violações 
de políticas de segurança estabelecidas. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Logging e Monitoramento
• Localização do log: C:\Windows\System32\LogFiles\Firewall\pfirewall.log(1)
• Event IDs relevantes: 5150 (regra bloqueada), 5156 (conexão permitida), 5157 
(conexão bloqueada)
• Configuração: Tamanho máximo do log, dropped packets only vs. successful 
connections
• Análise: Visualização via Event Viewer ou PowerShell (Get-WinEvent, Get-
Content)
• Integração: Encaminhamento via syslog para SIEM corporativo; análise de 
padrões de ataque
________
• (1)
  Versão do Windows          Comportamento Padrão
 Windows XP/Vista/7/8        `pfirewall.log` existia e era populado por padrão                 
 Logging **desativado por padrão**; apenas Event Viewer (IDs 515x) 
 Windows Server 2022         Logging desativado; requer configuração manual ou GPO             
 Windows 10/11/Server 2016+ 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Netfilter: Arquitetura Linux
• O Netfilter representa o framework de filtragem de pacotes integrado ao kernel 
Linux desde a versão 2.4, constituindo a base para ferramentas como iptables, 
ip6tables e nftables;
• Sua arquitetura implementa hooks em pontos estratégicos da pilha de rede 
(PREROUTING, INPUT, FORWARD, OUTPUT, POSTROUTING), permitindo 
interceptar e manipular pacotes através de tabelas especializadas (filter, nat, 
mangle, raw);
• A transição para nftables oferece sintaxe unificada, melhor desempenho e 
atomicidade na atualização de regras, substituindo as cadeias separadas do 
legado iptables. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Netfilter: Arquitetura Linux
• Framework: Subsistema do kernel Linux para manipulação de pacotes; hook-
based architecture;
• Tabelas: filter (permitir/bloquear), nat (tradução de endereços), mangle 
(modificação QoS), raw (exceções de tracking);
• Chains: INPUT (para o host), OUTPUT (do host), FORWARD (pass-through), 
PREROUTING/POSTROUTING (NAT);
• Nftables: Sucessor moderno do iptables; sintaxe consolidada IPv4/IPv6; 
performance superior via bytecode;
• Estado: Stateful  - inspeção através do “connection tracking” (conntrack) 
integrado.
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Nftables vs Iptables
• A evolução do iptables para nftables representa uma modernização significativa 
no gerenciamento de firewalls Linux;
• Enquanto o iptables mantinha cadeias separadas para IPv4 e IPv6, exigindo 
duplicação de regras, o nftables unifica a configuração em uma única tabela 
inet;
• A nova arquitetura utiliza uma máquina virtual de bytecode no kernel, 
oferecendo melhor performance e menor consumo de memória;
• A atomicidade das operações permite atualizar conjuntos inteiros de regras 
instantaneamente, eliminando estados transitórios vulneráveis que ocorriam nas 
atualizações sequenciais do iptables. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Nftables vs Iptables
• Unificação: Tabela inet cobre IPv4 e IPv6 simultaneamente; elimina duplicação 
de regras
• Sintaxe: Nftables usa sintaxe declarativa mais legível; iptables usa múltiplos 
utilitários (iptables, ip6tables, ebtables)
• Sets e Maps: Estruturas de dados eficientes para listas de IPs/portas sem criar 
regras individuais
• Atomicidade: Aplicação instantânea de todas as regras via arquivo de 
configuração único
• Debugging: Melhor feedback de erros e tracing integrado (nft trace) 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Integração Windows com AD
• GPO Deployment: Distribuição automática de regras via Group Policy; aplicação 
em massa
• Autenticação de Perfil: Validação via DC e Kerberos para ativação do Domain 
Profile
• WMI Filters: Aplicação condicional de regras baseada em atributos do sistema
• SecPol: Security Policy snap-in para configurações hardcoded em máquinas 
domain-joined
• Monitoramento Centralizado: Event logs encaminhados para coletores via 
Subscription
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Comparação Windows vs Linux
• As soluções de firewall de host apresentam filosofias distintas: o Windows 
Firewall oferece integração nativa com o ecossistema Microsoft, gerenciamento 
simplificado através de interfaces gráficas e PowerShell, com foco em 
usabilidade para administradores de infraestrutura heterogênea;
• Em contraste, as soluções Linux baseadas em netfilter proporcionam 
granularidade extrema através de linha de comando, scriptabilidade avançada 
com bash, e modularidade para cenários especializados de segurança, embora 
exijam maior curva de aprendizado técnico e conhecimento profundo de 
protocolos de rede. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Melhores Práticas de Hardening
• A configuração segura de firewalls de host requer aplicação do princípio do 
menor privilégio, iniciando com políticas default-deny para tráfego inbound e 
monitoramento cuidadoso de outbound;
• Regras devem ser específicas quanto a portas e endereços, evitando ranges 
amplos, e devem incluir logging para auditoria. A separação de perfis 
(especialmente Public vs Private) deve ser rigorosamente mantida, e regras 
obsoletas removidas periodicamente;
• Em ambientes corporativos, automação via PowerShell ou ansible garante 
consistência, enquanto testes regulares de penetração validam a eficácia das 
políticas implementadas. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG011-09 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Melhores Práticas de Hardening
• Default Deny: Bloquear todo tráfego inbound não explicitamente necessário; 
principio do menor privilégio;
• Regras Específicas: Evitar wildcards (*); especificar portas, protocolos e origens 
exatas;
• Auditoria: Manter logging habilitado para conexões dropadas; revisão periódica 
de logs;
• Higiene: Remover regras temporárias e desativadas; documentar propósito de 
cada regra;
• Automação: Versionar configurações (Git); usar IaC (Infrastructure as Code) 
para consistência.
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais 
Comparação Windows vs Linux
• Interface: Windows (GUI + PowerShell orientado a objetos) vs Linux (CLI/bash declarativo)
• Política padrão: Windows (permissivo outbound) vs Linux (frequentemente restrictivo drop-
all)(1)
• Integração: Windows (Active Directory, GPOs nativos) vs Linux (scripts init, systemd, 
ferramentas de config management)
• Granularidade: Windows (aplicação/porta/perfil) vs Linux 
(pacote/protocolo/estado/interface)(2)
• Custo e Licenciamento: Windows (componente do SO licenciado) vs Linux (código aberto, 
ferramentas 100% livres)
_______
(1)
(2) A granularidade refere-se ao nível de detalhe com que o firewall pode inspecionar e filtrar o tráfego. Quanto mais 
granular, mais preciso é o controle — mas também maior a complexidade de configuração. O Windows Firewall pensa 
em "quem está tentando fazer o quê, de onde". Sua unidade básica de controle é o contexto da aplicação e do usuário. 
O Linux (via Netfilter/nftables) pensa em "o que este pacote específico contém e como se comporta". Sua unidade 
básica é o pacote individual e seus atributos técnicos. 
 Postura  Significado  Efeito Prático
 **Restrictivo drop-all** 
 **Permissivo outbound**   Tudo que sai é permitido, exceto o 
explicitamente bloqueado 
 O host confia em si mesmo; aplicações 
comunicam livremente                        
 Tudo é bloqueado, exceto o 
explicitamente permitido         
 O host não confia em ninguém, nem em si 
mesmo; cada pacote precisa de autorização 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-05 - Firewalls de Host: Defesa do Endpoint em Sistemas 
Operacionais

---

## Módulo 06 — Netfilter / Iptables / Nftables

Segurança em Sistemas Operacionais e Redes de
Computadores I
ISG012-06 - Netfilter - Iptables - Nftables - Teoria

Objetivo
• Compreender a arquitetura interna do framework Netfilter do Linux, dominando o 
funcionamento das tabelas, chains e regras de filtragem. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria

Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
Objetivo
• Compreender a arquitetura do Netfilter e seu posicionamento no kernel Linux
• Diferenciar as ferramentas iptables (legado) e nftables (moderna)
• Dominar o conceito de tabelas (filter, nat, mangle) e chains (INPUT, FORWARD, OUTPUT, 
PREROUTING, POSTROUTING)
• Aplicar regras de filtragem stateful versus stateless
• Configurar NAT básico (SNAT e DNAT) para compartilhamento de conexão
• Implementar logging efetivo de tentativas de intrusão
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
Introdução ao Netfilter
• O Netfilter representa o framework de filtragem de pacotes integrado ao kernel Linux 
desde a versão 2.4, funcionando como a infraestrutura fundamental para firewall, NAT e 
manipulação de pacotes;
• Diferente de soluções externas, o Netfilter opera diretamente no espaço do kernel, 
garantindo alta performance e baixa latência no processamento de regras;
• Sua arquitetura modular permite interceptar pacotes em pontos específicos do stack de 
rede, possibilitando decisões de segurança baseadas em endereços, portas, protocolos e 
estado da conexão, constituindo a base para ferramentas como iptables e nftables. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
Introdução ao Netfilter
• Framework oficial do kernel Linux para processamento de pacotes
• Opera no kernel space (nível de privilégio mais alto)
• Suporta filtragem stateful (connection tracking)
• Permite manipulação de pacotes via hooks em 5 pontos críticos
• Base para implementação de firewalls, NAT e QoS
• Substituído o ipchains (Linux 2.2) por ser mais flexível e escalável
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
Evolução: iptables vs nftables
• O iptables dominou a administração de firewalls Linux por mais de duas décadas, 
utilizando estruturas de regras separadas para IPv4 e IPv6, com sintaxe complexa e baixa 
performance em regras extensas;
• O nftables, introduzido no kernel 3.13 e consolidado nas distribuições modernas como o 
Linux Mint 21+, representa uma revolução arquitetural;
• Utilizando uma máquina virtual de bytecode no kernel, o nftables unifica o tratamento de 
IPv4/IPv6, oferece sintaxe mais legível, suporta estruturas de dados avançadas (sets e 
maps) e permite atualizações atômicas de regras sem interromper o tráfego existente. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
Evolução: iptables vs nftables
• iptables (Legado):
• Sintaxe complexa e verbosa
• Tabelas separadas para IPv4 (iptables) e IPv6 (ip6tables)
• Performance degradada com milhares de regras
• Dificuldade em debugar regras complexas
• nftables (Moderno/Recomendado):
• Sintaxe unificada e intuitiva (família inet cobre IPv4/IPv6)
• Compilação para bytecode eficiente
• Suporte nativo a sets, maps e concatenations
• Atualizações atômicas via nft command
• Default no Linux Mint 20+ e Ubuntu 20.04+
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
Arquitetura de Tabelas e Chains no nftables
• A No nftables, a estrutura de controle de pacotes é organizada de forma flexível e 
hierárquica, diferente do modelo rígido do iptables legado;
• O administrador cria tabelas com nomes arbitrários e define sua família de endereçamento 
— inet para IPv4 e IPv6 simultaneamente, ip para IPv4 exclusivo, ou ip6 para IPv6 
exclusivo;
• Dentro de cada tabela, são criadas chains que especificam o tipo de processamento (filter 
para segurança, nat para tradução de endereços, route para roteamento especializado), o 
hook (ponto de interceptação no fluxo do pacote como input, forward, output, prerouting ou 
postrouting), a prioridade de execução e a política padrão (accept ou drop);
• Essa arquitetura permite que uma única tabela contenha múltiplas chains com funções 
distintas — por exemplo, uma chain de filtragem e outra de NAT coexistindo na mesma 
tabela inet firewall;
• O processamento ocorre sequencialmente dentro de cada chain até que uma ação 
terminal (accept, drop, reject) seja executada, determinando o destino do pacote;
• Essa flexibilidade elimina a necessidade de tabelas pré-definidas como raw ou security 
existentes no iptables, simplificando a administração e reduzindo erros de configuração. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
Arquitetura de Tabelas e Chains no nftables
• Conceito geral do Netfilter (válido para ambos):
• filter: Decisão de aceitar ou descartar pacotes (segurança padrão)
• nat: Tradução de endereços (SNAT, DNAT, masquerade)
• mangle: Modificação de campos do cabeçalho IP (TTL, TOS, MARK) para QoS
• Como funciona no nftables (moderno):
• O nome da tabela é definido pelo administrador (ex: filter, nat ou qualquer outro nome)
• Dentro da tabela, cria-se chains que especificam:
• Tipo: filter, nat ou route
• Hook: ponto de interceptação (input, output, forward, prerouting, postrouting, 
ingress)
• Prioridade: ordem de processamento no hook
• Política padrão: accept ou drop
• Uma mesma tabela pode conter chains de tipos diferentes (ex: uma chain filter e outra 
nat dentro da mesma tabela inet firewall)
• Não existem tabelas raw ou security pré-definidas como no iptables legado
• Ações disponíveis nas chains:
• accept, drop, reject (com mensagem ICMP), log, counter, masquerade, dnat, snat
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
Chains e Fluxo de Pacotes
• As chains representam os pontos de interceptação no caminho do pacote através do 
kernel;
• Quando um pacote chega à interface de rede, atravessa primeiro a chain PREROUTING 
(onde ocorre o DNAT), seguindo para a decisão de roteamento;
• Se destinado ao próprio host, direciona-se à chain INPUT; se destinado a outra rede, 
percorre a chain FORWARD e posteriormente POSTROUTING (onde ocorre o SNAT). 
Pacotes gerados localmente iniciam pela chain OUTPUT e também passam por 
POSTROUTING;
• Essa arquitetura de ganchos permite visibilidade total do tráfego em múltiplos estágios. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
Chains e Fluxo de Pacotes
• PREROUTING: Primeiro ponto de contato (DNAT, redirecionamento de portas)
• INPUT: Pacotes destinados ao próprio host (serviços locais)
• FORWARD: Pacotes roteados entre interfaces (gateway/roteador)
• OUTPUT: Pacotes gerados por processos locais
• POSTROUTING: Último ponto antes da transmissão (SNAT, mascaramento)
• Decisão de roteamento: Determina se pacote é local ou encaminhado
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
Sintaxe do nftables
• O nftables utiliza uma sintaxe declarativa e hierárquica através do comando nft, 
organizando as regras em tabelas, chains e regras propriamente ditas;
• Uma tabela é definida com sua família (ip, ip6, inet para ambos) e nome. Dentro da tabela, 
as chains são criadas com tipo (filter, nat), gancho de interface (input, forward, output) e 
prioridade;
• As regras utilizam expressões concisas para matching (ip saddr, tcp dport, ct state) e 
ações (accept, drop, reject, log, counter), suportando operadores lógicos e agrupamentos 
complexos através de sets para múltiplos endereços ou portas simultaneamente. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
Sintaxe do nftables
• Estrutura básica:
• bash
nft add table inet filter
nft add chain inet filter input { type filter hook input priority 0 \; policy drop \; }
nft add rule inet filter input tcp dport 22 accept 
• Componentes:
• Família: inet (IPv4+IPv6), ip, ip6, arp, bridge
• Tipo: filter, nat, route
• Gancho (hook): input, output, forward, prerouting, postrouting, ingress
• Prioridade: Ordem de processamento no gancho (0 = padrão)
• Política padrão: accept (recomendado para evitar lockout) ou drop
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
 Stateful vs Stateless Inspection
• A inspeção stateful representa a capacidade do firewall de monitorar o estado das 
conexões através do módulo conntrack (connection tracking), diferenciando pacotes que 
iniciam novas conexões daqueles pertencentes a sessões estabelecidas;
• Essa distinção permite criar regras altamente seguras onde apenas respostas a 
solicitações legítimas são aceitas, bloqueando implicitamente pacotes malformados ou 
ataques de scanning;
• Em contraste, firewalls stateless analisam cada pacote isoladamente, sem contexto de 
conexão, exigindo regras explícitas bidirecionais e sendo vulneráveis a spoofing de 
sessões, embora ofereçam menor overhead computacional. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
 Stateful vs Stateless Inspection
• Stateful (Recomendado):
• Mantém tabela de conexões ativas (/proc/net/nf_conntrack)
• Estados: new, established, related, invalid, untracked
• Regra eficiente: ct state established,related accept
• Proteção contra pacotes fora de sequência (TCP sequence checking)
• Suporte a protocolos complexos (FTP, SIP) via helpers
• Stateless:
• Análise individual de cada pacote
• Necessita regras explícitas para tráfego de retorno
• Menor consumo de memória (ideal para dispositivos embarcados)
• Vulnerável a ataques de fragmentação e spoofing
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
  
Connection Tracking
• O connection tracking (conntrack) constitui o mecanismo central da inspeção stateful no 
Linux, armazenando informações sobre todas as conexões de rede em uma tabela hash 
no kernel. Para cada fluxo, mantém metadados incluindo protocolo, endereços de 
origem/destino, portas, estado atual (SENT, RECEIVED, ESTABLISHED) e timeout;
• O sistema utiliza protocol trackers específicos para inspecionar camadas de aplicação, 
permitindo que protocolos como FTP (modo passivo), SIP e H.323 funcionem atrás de 
NAT;
• A visualização da tabela de conexões é realizada via comando conntrack -L, sendo 
essencial para troubleshooting de regras de firewall. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
  Connection Tracking
• Tabela de conexões: Armazenada em /proc/net/nf_conntrack
• Estados principais:
• NEW: Primeiro pacote da conexão (SYN sem resposta)
• ESTABLISHED: Handshake TCP completo ou tráfego UDP bidirecional
• RELATED: Nova conexão relacionada a uma existente (ex: FTP data channel)
• INVALID: Pacote que não pertence a nenhuma conexão conhecida (descartar!)
• Timeouts: TCP estabelecido (5 dias), UDP (30 segundos), SYN-SENT (2 minutos)
• Limitações: Consumo de memória proporcional ao número de conexões
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
  
Configuração de Regras Básicas
• A configuração efetiva de um firewall inicia-se com a definição da política padrão restritiva, 
recomendando-se iniciar com policy accept durante a configuração remota para evitar 
bloqueio acidental (lockout), migrando para policy drop após validação;
• As regras essenciais incluem permitir tráfego de loopback (lo interface), aceitar conexões 
estabelecidas, liberar acesso SSH administrativo (tcp/22) e habilitar consultas DNS 
(udp/53);
• A sintaxe do nftables permite combinações complexas usando sets para múltiplas portas e 
endereços, além de suportar logging integrado para auditoria de tentativas de acesso 
bloqueadas. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
  
Configuração de Regras Básicas
• Regras essenciais de segurança:
1. Loopback: iif lo accept (interface interna sempre liberada)
2. Estado: ct state established,related accept (stateful)
3. SSH: tcp dport 22 ct state new accept (administração remota)
4. DNS: udp dport 53 accept (resolução de nomes)
5. ICMP: icmp type echo-request accept (ping para diagnóstico)
• Boas práticas:
• Utilizar counter para monitorar hit counts de regras
• Adicionar comentários (comment "Descrição") para documentação
• Testar com nft -f /etc/nftables.conf antes de aplicar permanentemente
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
  
 NAT - Network Address Translation
• O NAT resolve a escassez de endereços IPv4 permitindo que múltiplos dispositivos em 
rede privada compartilhem um único endereço IP público;
• O SNAT (Source NAT) modifica o endereço de origem quando pacotes saem da rede 
interna para a internet, tipicamente usando mascaramento dinâmico (masquerade) para 
interfaces com IP variável (DHCP);
• O DNAT (Destination NAT) redireciona conexões externas para servidores internos, como 
publicar um servidor web da LAN para a WAN através do redirecionamento de portas;
•  Essas traduções ocorrem nas chains POSTROUTING (SNAT) e PREROUTING (DNAT), 
respectivamente, sendo fundamentais para segurança de perímetro e conservação de 
endereços. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
  
 NAT - Network Address Translation
• SNAT (Source NAT / Masquerade):
• Uso: Rede interna → Internet
• Chain: POSTROUTING
• Sintaxe: oif eth0 masquerade (IP dinâmico) ou snat to 203.0.113.1 (IP fixo)
• Função: Oculta IPs internos, permite múltiplos hosts com um IP público
• DNAT (Destination NAT / Port Forwarding):
• Uso: Internet → Servidor interno
• Chain: PREROUTING
• Sintaxe: dnat to 192.168.1.100:80 (redireciona porta 80 para servidor web interno)
• Função: Publicação de serviços, balanceamento de carga básico
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
  
 Logging e Monitoramento
• O logging eficiente em firewalls Linux é fundamental para detecção de incidentes e análise 
forense;
• O nftables integra a ação log diretamente nas regras, permitindo registrar tentativas de 
conexão bloqueadas ou suspeitas no journal do sistema (systemd-journald) ou syslog;
• Configurações avançadas permitem especificar o nível de prioridade (warn, info), prefixos 
identificáveis para facilitar a filtragem de logs, e limitação de taxa (rate limit) para prevenir 
flooding do disco em caso de ataques distribuídos;
• A análise desses logs revela padrões de port scanning, tentativas de brute force e 
varreduras automatizadas de vulnerabilidades. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
  Logging e Monitoramento
• Logging e Monitoramento (Bullet Points)
• Configuração de logging:
bash 
nft add rule inet filter input tcp dport 22 ct state new limit rate 3/second log prefix 
"SSH_ATTEMPT: " accept
• Parâmetros importantes:
• prefix: Identificador para grep/filtragem (ex: "FIREWALL_DROP:")
• level: Prioridade do log (emerg, alert, crit, err, warn, notice, info, debug)
• limit rate: Previne log flooding (ex: limit rate 10/minute)
• group: Netlink group para logs em userspace (0 = kernel log)
• Análise de logs:
• journalctl -k | grep FIREWALL (visualização em tempo real)
• tail -f /var/log/kern.log (syslog tradicional)
• Scripts Python para análise estatística de origens bloqueadas
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
  
Boas Práticas de Segurança
• A implementação segura de firewalls exige adesão a princípios fundamentais: inicie 
sempre com política padrão permissiva durante a configuração inicial para evitar bloqueio 
remoto irreversível, migrando para política restritiva apenas após validação completa das 
regras;
• Mantenha regras específicas antes de regras genéricas, pois o nftables processa 
sequencialmente e para na primeira correspondência;
• Utilize whitelist (permitir apenas o necessário) em vez de blacklist (bloquear o malicioso). 
Implemente rate limiting em serviços expostos como SSH para mitigar brute force;
• Documente todas as regras com comentários descritivos e mantenha backups 
versionados das configurações em /etc/nftables.conf. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
  
Boas Práticas de Segurança
• Política default: Iniciar com policy accept, migrar para drop após testes
• Ordem das regras: Específicas primeiro, genéricas por último (primeiro match wins)
• Princípio do menor privilégio: Liberar apenas portas/protocolos estritamente necessários
• Rate limiting: limit rate over 3/second para prevenir DoS em serviços
• Backup: nft list ruleset > /backup/firewall-$(date +%Y%m%d).conf
• Testes: Sempre validar em ambiente controlado antes de produção
• IPv6: Não esquecer a família inet (IPv4+IPv6) ou configurar ip6tables separadamente
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
Checklist de Validação
• Antes de considerar a configuração do firewall como concluída, execute um checklist 
sistemático de validação:
• Verifique se o loopback (lo) está explicitamente permitido para evitar quebra de 
funcionalidades locais;
• Confirme que conexões estabelecidas são aceitas para garantir o retorno do tráfego 
legítimo;
• Teste cada regra individualmente usando o comando counter para verificar se está 
sendo atingida; valide o acesso aos serviços críticos (SSH, DNS) a partir de hosts 
autorizados;
• Verifique se o logging está capturando eventos relevantes sem gerar ruído excessivo;
• Simule cenários de failover (refere-se a mecanismos de contingência que impedem o 
bloqueio permanente do administrador (lockout) caso uma regra de firewall seja 
aplicada incorretamente) para garantir que a política default não bloqueie acesso 
administrativo de emergência. 
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria
Checklist de Validação
[  ] Loopback interface (lo) configurado para accept
[  ] Stateful inspection habilitado (established, related)
[  ] Regras de gerenciamento (SSH) testadas e funcionando
[  ] DNS (UDP/53) e NTP (UDP/123) liberados se necessário
[  ] ICMP básico permitido (echo-request para diagnóstico)
[  ] Counters verificados em regras críticas (hit counts)
[  ] Logs gerando output em /var/log/kern.log ou journal
[  ] Backup da configuração salvo em local seguro
[  ] Política default alterada para drop apenas após validação completa
Segurança em Sistemas Operacionais e Redes de Computadores I 
ISG012-06 - Netfilter - Iptables - Nftables - Teoria

---

