# ISG012 — Segurança em SO e Redes II
# Questões de Múltipla Escolha — Perguntas, Respostas e Gabarito Consolidado

> **Disciplina:** ISG012 — [[Segurança]] em [[CyberSecurity/Notas/PENTESTING/Windows/Sistemas Operacionais|Sistemas Operacionais]] e Redes II  
> **Turno:** Noturno  
> **Compilado em:** [[reports/2026/2026|2026]]-06-02  

---

## Módulo 01 — Arquitetura de Redes Seguras: Do Perímetro à Segmentação Lógica

### Questões de Múltipla Escolha

```
ISG012-01 - Arquitetura de Redes Seguras Do Perímetro à Segmentação Lógica – Questões 
de múltipla escolha - Gabarito
Como obter maior aproveitamento deste objeto de apredizagem:
1. Responder sem olhar o gabarito. Para isso, procurar pelas respostas nos slides da aula 
“ISO001-09 - Gerenciamento de memória” (teoria e prática);
1. Após responder TODAS as questões, comparar com o gabarito;
2. Refazer os passos 1 e 2 novamente com todas as questões até obter 100% de acertos de 
uma só vez.
Importante: Embora seja baseado nos slides teóricos e nas atividades práticas, este 
questionário pode conter informações que não constam nesses documentos pois pode 
incluir algum nível detalhamento em relação a eles. Assim, considere as informações 
aqui contidas como parte complementar do conteúdo a ser estudado para as provas. 
Todo o material distribuido pelo professor poderá ser utilizado para a confecção das 
questões das provas. 
Teoria (14 questões)
1. Segundo o material teórico, qual é a característica principal que define uma rede plana (flat 
network)?
a) Utilização de múltiplos firewalls de borda
b) Segmentação lógica via VLANs restritas
c) Compartilhamento do mesmo domínio de broadcast e ausência de segmentação lógica ou física
d) Aplicação do modelo Zero Trust em todas as camadas
2. Qual conceito central descreve o modelo de perímetro tradicional?
a) "Nunca confie, sempre verifique"
b) "Hard outside, soft inside"
c) Privilégio mínimo absoluto
d) Microssegmentação dinâmica
3. Qual é o princípio fundamental da estratégia Defense in Depth (Defesa em Profundidade)?
a) Nenhum controle é infalível; redundância estratégica é essencial
b) Confiar apenas no perímetro externo como sentinela absoluta
c) Eliminar todas as camadas intermediárias de proteção
d) Centralizar toda a segurança em um único ponto de inspeção
4. O paradigma Zero Trust foi desenvolvido inicialmente pelo Forrester Research e posteriormente 
adotado pelo NIST. Qual norma técnica do NIST define sua arquitetura?
a) NIST SP 800-53
b) NIST SP 800-171
c) ISO/IEC 27001
5. A microssegmentação, no contexto de Zero Trust, pode ser definida como:
a) A substituição completa de firewalls físicos por virtuais
b) A divisão granular da rede em segmentos pequenos com políticas "default-deny" baseadas em 
identidade e contexto
c) A utilização de uma única VLAN para todos os departamentos
d) A centralização de logs em um servidor único da DMZ
6. As VLANs (Virtual Local Area Networks) constituem tecnologia de qual camada do modelo OSI?
a) Camada 1 (Física)
b) Camada 3 (Rede)
c) Camada 2 (Enlace de Dados)
d) Camada 4 (Transporte)
7. Qual é a "Regra de Ouro" em relação à DMZ (Zona Desmilitarizada)?
a) Nunca permitir conexões originadas na DMZ destinadas à rede interna
b) Permitir que servidores da DMZ acessem diretamente a zona Management
c) Manter todos os serviços corporativos críticos exclusivamente na DMZ
d) Desativar todo o firewall entre a DMZ e a Internet
8. No contexto defensivo do subnetting, qual é um dos principais benefícios de utilizar sub-redes 
menores (ex: /28, /29, /30)?
a) Aumentar o domínio de broadcast para melhorar a descoberta de serviços
b) Eliminar a necessidade de firewalls entre segmentos
c) Permitir que todos os hosts compartilhem a mesma tabela ARP
d) Reduzir o escopo de varreduras e limitar o impacto de ARP spoofing
9. Na hierarquia de zonas de segurança apresentada, qual nível de confiança e criticidade é 
atribuído à zona Management?
a) Nível 0 — Zero confiança
b) Nível 1 — Alta exposição
c) Nível 3 — Acesso altamente restrito
d) Nível 2 — Usuários autenticados
10. O que caracteriza a arquitetura SASE (Secure Access Service Edge)?
a) Centralização de todo o tráfego em um data center corporativo único
b) Combinação de SD-WAN com serviços de segurança em nuvem, eliminando o backhauling 
centralizado
c) Utilização exclusiva de VPNs tradicionais para acesso remoto
d) Substituição de todas as políticas de segmentação por VLANs físicas
11. Um Jump Host (ou Bastion Host) é melhor definido como:
a) Um servidor hardened e fortemente monitorado em zona intermediária, usado como ponto de 
entrada único para acesso administrativo
b) Um firewall de três interfaces conectado diretamente à Internet
c) Um servidor DNS externo hospedado na DMZ
d) Um balanceador de carga para aplicações web na camada de apresentação
12. Qual medida faz parte da prevenção contra VLAN hopping?
a) Habilitar o trunking dinâmico (DTP) em todas as portas
b) Compartilhar a VLAN nativa entre todos os switches sem restrições
c) Permitir que qualquer porta negocie automaticamente modo trunk
d) Desativar o trunking dinâmico e configurar explicitamente portas como access ou trunk
13. O backhauling de tráfego é definido como:
a) A distribuição automática de políticas de segurança via SD-WAN
b) A criação de túneis criptografados diretos entre filiais (topologia mesh)
c) A prática de direcionar todo o tráfego por um ponto centralizado antes do destino final
d) A substituição de firewalls físicos por serviços cloud-native
14. Infraestrutura como Código (IaC) é a prática de:
a) Escrever software exclusivamente para automação de backups
b) Gerenciar e provisionar recursos de infraestrutura através de arquivos de configuração 
versionáveis e automatizáveis
c) Substituir completamente os administradores de rede por inteligência artificial
d) Criar diagramas de rede manualmente em papel para auditoria
Prática (6 questões)
15. No laboratório prático, qual é o endereço IP configurado na interface eth2 (DMZ) do Linux Mint 
Gateway?
a) 192.168.1.1/24
b) 192.168.3.1/24
c) 10.0.0.1/24
d) 172.16.0.1/24
16. Qual comando habilita o IP forwarding temporariamente no Linux Mint Gateway?
a) sudo sysctl -w net.ipv4.ip_forward=1
b) sudo echo 1 > /etc/sysctl.conf
c) sudo iptables --enable-forwarding
d) sudo route add default gw 172.16.0.1
17. Qual é o arquivo de configuração do Netplan utilizado para definir as interfaces do gateway?
a) /etc/network/interfaces
b) /etc/dhcp/dhcpd.conf
c) /etc/netplan/01-netcfg.yaml
d) /etc/resolv.conf
18. Qual é a regra nftables que implementa o bloqueio crítico do tráfego da DMZ para a 
Management?
a) sudo nft add rule inet filter forward ip saddr 192.168.1.0/24 ip daddr 172.16.0.0/24 drop
b) sudo nft add rule inet filter forward ip saddr 172.16.0.0/24 ip daddr 192.168.3.0/24 drop
c) sudo nft add rule inet filter input tcp dport 22 drop
d) sudo nft add rule inet filter output ip daddr 192.168.3.0/24 accept
19. Na configuração do VirtualBox, qual faixa de rede IP é utilizada pela VM External (Windows 
10) que simula um atacante?
a) 10.0.0.0/24
b) 192.168.1.0/24
c) 172.16.0.0/24
d) 192.168.3.0/24
20. Para adicionar uma rota persistente no Windows (VM Internal) apontando para a rede DMZ via 
gateway Linux, qual parâmetro é essencial no comando route add?
a) -f
b) -n
c) -g
d) -p
```

### Gabarito Comentado

```
ISG012-01 - Arquitetura de Redes Seguras Do Perímetro à Segmentação Lógica – Questões 
de múltipla escolha - Gabarito
Como obter maior aproveitamento deste objeto de apredizagem:
1. Responder sem olhar o gabarito. Para isso, procurar pelas respostas nos slides da aula 
“ISO001-09 - Gerenciamento de memória” (teoria e prática);
1. Após responder TODAS as questões, comparar com o gabarito;
2. Refazer os passos 1 e 2 novamente com todas as questões até obter 100% de acertos de 
uma só vez.
Importante: Embora seja baseado nos slides teóricos e nas atividades práticas, este 
questionário pode conter informações que não constam nesses documentos pois pode 
incluir algum nível detalhamento em relação a eles. Assim, considere as informações 
aqui contidas como parte complementar do conteúdo a ser estudado para as provas. 
Todo o material distribuido pelo professor poderá ser utilizado para a confecção das 
questões das provas. 
Teoria (14 questões)
1. Segundo o material teórico, qual é a característica principal que define uma rede plana (flat 
network)?
a) Utilização de múltiplos firewalls de borda
b) Segmentação lógica via VLANs restritas
c) Compartilhamento do mesmo domínio de broadcast e ausência de segmentação lógica ou física
d) Aplicação do modelo Zero Trust em todas as camadas
Resposta correta: C — O texto define redes planas como infraestruturas onde todos os 
dispositivos compartilham o mesmo domínio de broadcast, operando em uma única VLAN ou sub-
rede, sem qualquer segmentação. 
2. Qual conceito central descreve o modelo de perímetro tradicional?
a) "Nunca confie, sempre verifique"
b) "Hard outside, soft inside"
c) Privilégio mínimo absoluto
d) Microssegmentação dinâmica
Resposta correta: B — O modelo de perímetro tradicional opera sob a premissa de proteção 
concentrada na borda (fronteira fortificada), enquanto o interior da rede goza de confiança 
implícita, resumido como "Hard outside, soft inside". 
3. Qual é o princípio fundamental da estratégia Defense in Depth (Defesa em Profundidade)?
a) Nenhum controle é infalível; redundância estratégica é essencial
b) Confiar apenas no perímetro externo como sentinela absoluta
c) Eliminar todas as camadas intermediárias de proteção
d) Centralizar toda a segurança em um único ponto de inspeção
Resposta correta: A — Defense in Depth emprega múltiplas camadas de controles defensivos ao 
longo do caminho de dados, partindo do princípio de que a falha de um único mecanismo não 
deve resultar em comprometimento total. 
4. O paradigma Zero Trust foi desenvolvido inicialmente pelo Forrester Research e posteriormente 
adotado pelo NIST. Qual norma técnica do NIST define sua arquitetura?
a) NIST SP 800-53
b) NIST SP 800-171
c) ISO/IEC 27001
d) NIST SP 800-207
Resposta correta: D — O material cita especificamente a norma NIST SP 800-207 como a 
publicação que define a arquitetura Zero Trust. 
5. A microssegmentação, no contexto de Zero Trust, pode ser definida como:
a) A substituição completa de firewalls físicos por virtuais
b) A divisão granular da rede em segmentos pequenos com políticas "default-deny" baseadas em 
identidade e contexto
c) A utilização de uma única VLAN para todos os departamentos
d) A centralização de logs em um servidor único da DMZ
Resposta correta: B — A nota de rodapé da pág. 13 define microssegmentação como a divisão 
granular em segmentos extremamente pequenos, onde políticas de acesso "default-deny" são 
aplicadas dinamicamente baseadas em identidade e contexto, não em endereços IP estáticos. 
6. As VLANs (Virtual Local Area Networks) constituem tecnologia de qual camada do modelo OSI?
a) Camada 1 (Física)
b) Camada 3 (Rede)
c) Camada 2 (Enlace de Dados)
d) Camada 4 (Transporte)
Resposta correta: C — O texto afirma que VLANs constituem tecnologia de camada 2 do modelo 
OSI, permitindo a criação de domínios de broadcast lógicos independentes da topologia física. 
7. Qual é a "Regra de Ouro" em relação à DMZ (Zona Desmilitarizada)?
a) Nunca permitir conexões originadas na DMZ destinadas à rede interna
b) Permitir que servidores da DMZ acessem diretamente a zona Management
c) Manter todos os serviços corporativos críticos exclusivamente na DMZ
d) Desativar todo o firewall entre a DMZ e a Internet
Resposta correta: A — A Regra de Ouro da DMZ estabelece que servidores nela alojados não 
podem iniciar conexões para a rede interna, apenas responder a solicitações legitimadas. 
8. No contexto defensivo do subnetting, qual é um dos principais benefícios de utilizar sub-redes 
menores (ex: /28, /29, /30)?
a) Aumentar o domínio de broadcast para melhorar a descoberta de serviços
b) Eliminar a necessidade de firewalls entre segmentos
c) Permitir que todos os hosts compartilhem a mesma tabela ARP
d) Reduzir o escopo de varreduras e limitar o impacto de ARP spoofing
Resposta correta: D — O material destaca que subnets menores reduzem o escopo de 
varreduras de atacantes e limitam o impacto de ARP spoofing nos segmentos. 
9. Na hierarquia de zonas de segurança apresentada, qual nível de confiança e criticidade é 
atribuído à zona Management?
a) Nível 0 — Zero confiança
b) Nível 1 — Alta exposição
c) Nível 3 — Acesso altamente restrito
d) Nível 2 — Usuários autenticados
Resposta correta: C — A zona Management é classificada como Nível 3, com acesso altamente 
restrito, monitoramento e logging intensivos. 
10. O que caracteriza a arquitetura SASE (Secure Access Service Edge)?
a) Centralização de todo o tráfego em um data center corporativo único
b) Combinação de SD-WAN com serviços de segurança em nuvem, eliminando o backhauling 
centralizado
c) Utilização exclusiva de VPNs tradicionais para acesso remoto
d) Substituição de todas as políticas de segmentação por VLANs físicas
Resposta correta: B — SASE é definida como uma arquitetura convergida que combina SD-
WAN com serviços de segurança em nuvem, aplicando políticas de segmentação e Zero Trust nos 
pontos de presença de borda.
11. Um Jump Host (ou Bastion Host) é melhor definido como:
a) Um servidor hardened e fortemente monitorado em zona intermediária, usado como ponto de 
entrada único para acesso administrativo
b) Um firewall de três interfaces conectado diretamente à Internet
c) Um servidor DNS externo hospedado na DMZ
d) Um balanceador de carga para aplicações web na camada de apresentação
Resposta correta: A — A nota de rodapé da pág. 21 define jump host como servidor hardened 
em zona intermediária, exigindo autenticação rigorosa e registrando todas as sessões 
administrativas. 
12. Qual medida faz parte da prevenção contra VLAN hopping?
a) Habilitar o trunking dinâmico (DTP) em todas as portas
b) Compartilhar a VLAN nativa entre todos os switches sem restrições
c) Permitir que qualquer porta negocie automaticamente modo trunk
d) Desativar o trunking dinâmico e configurar explicitamente portas como access ou trunk
Resposta correta: D — O material cita como hardening a desativação do trunking dinâmico 
(DTP), configuração explícita de portas e isolamento da VLAN nativa.
13. O backhauling de tráfego é definido como:
a) A distribuição automática de políticas de segurança via SD-WAN
b) A criação de túneis criptografados diretos entre filiais (topologia mesh)
c) A prática de direcionar todo o tráfego por um ponto centralizado antes do destino final
d) A substituição de firewalls físicos por serviços cloud-native
Resposta correta: C — A nota de rodapé da pág. 23 define backhauling como a prática de 
direcionar todo o tráfego através de um ponto centralizado (geralmente o data center corporativo) 
para inspeção de segurança.
14. Infraestrutura como Código (IaC) é a prática de:
a) Escrever software exclusivamente para automação de backups
b) Gerenciar e provisionar recursos de infraestrutura através de arquivos de configuração 
versionáveis e automatizáveis
c) Substituir completamente os administradores de rede por inteligência artificial
d) Criar diagramas de rede manualmente em papel para auditoria
Resposta correta: B — A nota de rodapé da pág. 26 define IaC como a prática de gerenciar 
servidores, redes e firewalls através de arquivos de configuração versionáveis, garantindo 
consistência e auditoria.
Prática (6 questões)
15. No laboratório prático, qual é o endereço IP configurado na interface eth2 (DMZ) do Linux Mint 
Gateway?
a) 192.168.1.1/24
b) 192.168.3.1/24
c) 10.0.0.1/24
d) 172.16.0.1/24
Resposta correta: D — A topologia do laboratório e o arquivo netplan indicam que eth2 (DMZ) 
possui o endereço 172.16.0.1/24.
16. Qual comando habilita o IP forwarding temporariamente no Linux Mint Gateway?
a) sudo sysctl -w net.ipv4.ip_forward=1
b) sudo echo 1 > /etc/sysctl.conf
c) sudo iptables --enable-forwarding
d) sudo route add default gw 172.16.0.1
Resposta correta: A — O material apresenta o comando sudo sysctl -w net.ipv4.ip_forward=1 
para habilitação temporária do encaminhamento de pacotes. 
17. Qual é o arquivo de configuração do Netplan utilizado para definir as interfaces do gateway?
a) /etc/network/interfaces
b) /etc/dhcp/dhcpd.conf
c) /etc/netplan/01-netcfg.yaml
d) /etc/resolv.conf
Resposta correta: C — O laboratório utiliza o arquivo /etc/netplan/01-netcfg.yaml para declarar 
as 4 interfaces de rede e suas respectivas zonas. 
18. Qual é a regra nftables que implementa o bloqueio crítico do tráfego da DMZ para a 
Management?
a) sudo nft add rule inet filter forward ip saddr 192.168.1.0/24 ip daddr 172.16.0.0/24 drop
b) sudo nft add rule inet filter forward ip saddr 172.16.0.0/24 ip daddr 192.168.3.0/24 drop
c) sudo nft add rule inet filter input tcp dport 22 drop
d) sudo nft add rule inet filter output ip daddr 192.168.3.0/24 accept
Resposta correta: B — A regra crítica bloqueia pacotes com origem na DMZ (172.16.0.0/24) e 
destino à Management (192.168.3.0/24), conforme script de firewall. 
19. Na configuração do VirtualBox, qual faixa de rede IP é utilizada pela VM External (Windows 
10) que simula um atacante?
a) 10.0.0.0/24
b) 192.168.1.0/24
c) 172.16.0.0/24
d) 192.168.3.0/24
Resposta correta: A — A VM External utiliza adaptador NAT isolado e recebe IP na faixa 
10.0.0.x/24 via DHCP, não acessando as zonas internas.
20. Para adicionar uma rota persistente no Windows (VM Internal) apontando para a rede DMZ via 
gateway Linux, qual parâmetro é essencial no comando route add?
a) -f
b) -n
c) -g
d) -p
Resposta correta: D — O parâmetro -p torna a rota persistente, mantendo-a após o reboot do 
sistema Windows.
```

### Atividades Práticas

```
ISG012-Aulas0102
Atividade ISG012-01 - Arquitetura de Redes Seguras Do Perímetro à Segmentação Lógica - 
Teoria
1. Explique a diferença fundamental entre o modelo de segurança baseado em perímetro e a 
arquitetura Zero Trust, destacando como cada abordagem trata o tráfego interno à rede 
corporativa.
2. Descreva o conceito de Defense in Depth e explique como a segmentação de rede 
contribui especificamente para este framework estratégico.
3. Analise a função estratégica da DMZ (Demilitarized Zone) em uma arquitetura de rede 
segura, explicando por que serviços expostos à Internet não devem residir diretamente na 
rede interna corporativa.
4. Discorra sobre como o subnetting pode ser utilizado como ferramenta de segurança, indo 
além de sua função tradicional de otimização de endereçamento IP.
5. Explique a importância da zona de Management separada fisicamente ou logicamente da 
rede de produção, citando controles específicos recomendados para este segmento crítico.
6. Compare as abordagens de segmentação VLAN (camada 2) e microssegmentação 
baseada em identidade (camada 7), discutindo cenários onde cada uma é mais 
apropriada.
Atividade ISG012-01 - Arquitetura de Redes Seguras Do Perímetro à Segmentação Lógica – 
Prática
1. Na configuração da topologia virtualizada com quatro segmentos de rede (Management, 
Internal, DMZ, External), qual comando Linux você utilizaria para verificar se a interface de 
rede da VM Linux Mint (gateway) está corretamente configurada em modo promíscuo para 
escutar tráfego entre segmentos, e como você validaria que o roteamento estático entre 
VLANs está funcional?
2. Durante a configuração do Linux Mint como gateway entre zonas, você precisa implementar 
uma regra de firewall utilizando nftables que bloqueie todo tráfego originado na DMZ 
(192.168.2.0/24) com destino à rede Management (192.168.3.0/24), mantendo o acesso 
permitido da Internal para DMZ. Qual seria a sintaxe básica do comando nftables para inserir 
esta regra na cadeia forward?
3. Na configuração de roteamento estático entre os quatro segmentos utilizando o Linux Mint 
como router multi-homed, após configurar os endereços IP em cada interface (eth0-External, 
eth1-Internal, eth2-DMZ, eth3-Management), qual comando você utilizaria para habilitar o IP 
forwarding no kernel Linux e como você configuraria uma rota estática específica para que a 
rede Internal (192.168.1.0/24) alcance a rede External (10.0.0.0/24) através do gateway 
192.168.1.1?
Atividade  ISG012-02 - Teoria
Pergunta 1: Explique a diferença fundamental entre roteamento estático e roteamento dinâmico  
sob a ótica da segurança de redes.
Pergunta 2: Descreva o funcionamento do RIP como protocolo distance-vector e explique por que 
a versão 1 é considerada insegura em comparação com a versão 2.
Pergunta 3:  Explique o conceito de áreas no OSPF e como essa hierarquia contribui para a  
segurança da rede.
Pergunta 4: O que é Policy-Based Routing (PBR) e como ele pode ser utilizado para implementar  
path isolation em um roteador Linux multi-homed?
Pergunta 5: Explique a importância do hook forward no nftables para a segurança de um roteador 
Linux e diferencie-o dos hooks input e output.
Pergunta 6:  Descreva o princípio do "menor privilégio" aplicado à configuração de ACLs em  
roteadores  e  explique  por  que  a  política  padrão  drop é  considerada  uma  boa  prática  de  
segurança.
Atividade ISG012-02 – Prática
Pergunta 1: Qual comando habilita o encaminhamento de pacotes (IP forwarding) no kernel Linux 
e como tornar essa configuração persistente entre reinicializações?
Pergunta 2: Na prática, qual regra do nftables implementa o bloqueio completo de tráfego entre o 
segmento de visitantes (eth3) e o segmento de servidores (eth2), incluindo logging para auditoria?
Pergunta 3: Como verificar se as regras do nftables foram carregadas corretamente e qual 
comando lista a tabela de roteamento principal no Linux?
Orientações
Código da atividade:  ISG012-Aulas0102
Enviar a atividade anexada em um e-mail para rglabrada.jog@gmail.com No assunto
coloque o código da atividade (ISG012-Aulas0102) e o seu nome completo.
Exemplo, supondo que o aluno se chama Fulano de Tal, colocar no assunto do e-mail: 
ISG012-Aulas0102 Fulano de Tal
A atividade deve ter 6 itens devidamente identificados (toda a atividade deve estar em um 
único arquivo com extensão .pdf):
Objetivo: até 2,0;
Atividade ISG012-01 – Teoria: até 1,5;
Atividade ISG012-01 – Prática: até 1,5;
Atividade  ISG012-02 - Teoria até 1,5;
Atividade ISG012-02  – Prática: até 1,5;
Conclusão: até 2,0.
Prazo: 09/06/2026 23:59
Atenção! Não serão consideradas as atividades recebidas após esse prazo.
Caso tenha dúvidas, procure o professor.
```

---

## Módulo 02 — Roteamento Seguro e ACLs

### Questões de Múltipla Escolha

```
ISG012-02 - Roteamento Seguro e ACLs – Questões de múltipla escolha 
Como obter maior aproveitamento deste objeto de apredizagem:
1. Responder sem olhar o gabarito. Para isso, procurar pelas respostas nos slides da aula 
“ISO001-09 - Gerenciamento de memória” (teoria e prática);
1. Após responder TODAS as questões, comparar com o gabarito;
2. Refazer os passos 1 e 2 novamente com todas as questões até obter 100% de acertos de 
uma só vez.
Importante: Embora seja baseado nos slides teóricos e nas atividades práticas, este 
questionário pode conter informações que não constam nesses documentos pois pode 
incluir algum nível detalhamento em relação a eles. Assim, considere as informações aqui 
contidas como parte complementar do conteúdo a ser estudado para as provas. Todo o 
material distribuido pelo professor poderá ser utilizado para a confecção das questões das 
provas. 
Teoria
1. Segundo o material teórico, qual é a função principal de um roteador?
a) Dispositivo de camada 3 que interconecta redes e toma decisões de encaminhamento 
baseadas em tabelas de roteamento
b) Dispositivo de camada 2 que interconecta switches
c) Firewall de aplicação que filtra conteúdo malicioso na camada 7
d) Servidor de DNS recursivo para resolução de nomes
2. Sobre o roteamento estático, qual característica o diferencia fundamentalmente do roteamento 
dinâmico?
a) Utiliza protocolos como RIP e OSPF para troca automática de informações
b) Adapta-se automaticamente a falhas de links e mudanças de topologia
c) Requer autenticação MD5 obrigatória entre roteadores vizinhos
d) Consiste na configuração manual de rotas pelo administrador, oferecendo previsibilidade total 
do caminho do tráfego
3. Qual é o principal risco de segurança associado aos protocolos de roteamento dinâmico?
a) Lentidão na convergência superior a 60 segundos
b) Possibilidade de um roteador malicioso ou comprometido injetar rotas falsas, desviando tráfego 
para interceptação
c) Exigência de endereçamento IPv6 exclusivo
d) Consumo excessivo de largura de banda em broadcasts contínuos
4. Em relação ao protocolo RIP, qual afirmação está correta?
a) RIPv1 transmite atualizações em multicast no endereço 224.0.0.9
b) A métrica do RIP é baseada na largura de banda do enlace
c) RIPv2 introduziu suporte a autenticação via senha em texto ou hash MD5, além de multicast 
direcionado
d) O limite máximo de hops no RIP é 255, tornando-o ideal para redes grandes
5. No protocolo OSPF, qual elemento é obrigatório na hierarquia de áreas?
a) Área stub em cada segmento de rede
b) Área backbone (Area 0) como centro da hierarquia
c) ABR (Area Border Router) em cada subnet
d) Autenticação HMAC-SHA obrigatória em todas as interfaces
6. Para que um sistema Linux funcione como roteador multi-homed, qual parâmetro do kernel 
deve ser habilitado?
a) net.ipv4.ip_forward = 1
b) net.ipv4.conf.all.accept_redirects = 1
c) net.ipv4.tcp_syncookies = 0
d) net.ipv4.conf.all.rp_filter = 2
7. No Policy-Based Routing (PBR) do Linux, qual é o valor de prioridade padrão da tabela main?
a) 0
b) 100
c) 32766
d) 32767
8. Qual a distinção fundamental entre ACLs aplicadas em roteadores e firewalls de host?
a) ACLs operam exclusivamente na camada de aplicação
b) Firewalls de host protegem apenas o próprio sistema, enquanto ACLs em roteadores controlam 
o fluxo entre redes inteiras
c) ACLs não permitem filtragem baseada em endereços IP de origem
d) Firewalls de host são obrigatoriamente implementados em hardware dedicado
9. Em nftables, qual hook é especificamente utilizado para processar pacotes que atravessam o 
roteador entre interfaces distintas?
a) input
b) output
c) forward
d) prerouting
10. Em nftables, o match que filtra pacotes pela interface de saída é representado por:
a) iifname
b) iif
c) fwmark
d) oifname
11. A segmentação de rede em VLANs é considerada uma prática essencial de segurança porque:
a) Aumenta a velocidade de transmissão em até 50%
b) Isola broadcast domains e limita a propagação de ameaças laterais
c) Elimina completamente a necessidade de roteamento entre segmentos
d) Fornece endereçamento IP automático via DHCP integrado
12. O que caracteriza o conceito de Path Isolation em segurança de redes?
a) Criptografia simétrica aplicada a todos os pacotes IP
b) Estratégia que garante caminhos de rede separados para diferentes tipos de tráfego
c) Protocolo de roteamento dinâmico com convergência em 1 segundo
d) Técnica de balanceamento de carga por round-robin DNS
13. Em ambientes de alta segurança, qual é a recomendação híbrida para o uso de roteamento 
estático e dinâmico?
a) Utilizar roteamento estático para segmentos críticos e dinâmico apenas onde a resiliência é 
mandatória, sempre com autenticação
b) Utilizar apenas roteamento dinâmico em todos os segmentos
c) Desabilitar todas as ACLs para garantir alta disponibilidade
d) Adotar RIPv1 sem autenticação por simplicidade administrativa
14. Qual das seguintes opções NÃO representa uma boa prática de roteamento seguro segundo o 
material?
a) Desativar serviços desnecessários no roteador Linux
b) Aplicar ACLs com política default-deny
c) Manter logs de tráfego negado para análise forense
d) Aplicar política de permissão padrão (default-allow) nas chains de forward
Prática
15. Na topologia do laboratório prático, qual modo de adaptador de rede do VirtualBox deve ser 
utilizado para interconectar as VMs aos segmentos?
a) Host-only
b) NAT
c) Internal Network
d) Bridged Adapter
16. No script de configuração do roteador, qual comando habilita o encaminhamento de pacotes 
IPv4 entre as interfaces?
a) sudo sysctl -w net.ipv4.ip_forward=1
b) sudo ip route add default via 192.168.10.254
c) sudo ip link set eth1 up
d) sudo nft -f /etc/nftables.conf
17. No script de Policy-Based Routing, qual comando cria a regra que direciona o tráfego 
originado do segmento 30 para a tabela customizada "visitantes"?
a) sudo ip route add 192.168.30.0/24 table visitantes
b) sudo ip addr add 192.168.30.1/24 dev eth3
c) echo "200 visitantes" | sudo tee -a /etc/iproute2/rt_tables
d) sudo ip rule add from 192.168.30.0/24 table visitantes priority 100
18. Na configuração base do nftables apresentada no laboratório, qual é a política padrão definida 
para a chain input?
a) accept
b) drop
c) reject
d) log
19. Qual regra do script nftables_forward.sh implementa o bloqueio explícito do tráfego entre o 
segmento de Visitantes e o segmento de Servidores?
a) iifname GUESTDEVoifname SERV_DEV drop
b) iifname MGMTDEVoifname SERV_DEV accept
c) iifname SERVDEVoifname MGMT_DEV accept
d) iifname MGMTDEVoifname GUEST_DEV accept
20. No script de testes de validação, qual comando é utilizado para verificar os logs de tentativas 
de acesso bloqueadas entre VLANs?
a) sudo nft list ruleset
b) ip route show table visitantes
c) sudo systemctl status nftables
d) sudo dmesg | grep "VLAN-ISOLATION" | tail -5
```

### Gabarito Comentado

```
ISG012-02 - Roteamento Seguro e ACLs – Questões de múltipla escolha - Gabarito
Como obter maior aproveitamento deste objeto de apredizagem:
1. Responder sem olhar o gabarito. Para isso, procurar pelas respostas nos slides da aula 
“ISO001-09 - Gerenciamento de memória” (teoria e prática);
1. Após responder TODAS as questões, comparar com o gabarito;
2. Refazer os passos 1 e 2 novamente com todas as questões até obter 100% de acertos de 
uma só vez.
Importante: Embora seja baseado nos slides teóricos e nas atividades práticas, este 
questionário pode conter informações que não constam nesses documentos pois pode 
incluir algum nível detalhamento em relação a eles. Assim, considere as informações aqui 
contidas como parte complementar do conteúdo a ser estudado para as provas. Todo o 
material distribuido pelo professor poderá ser utilizado para a confecção das questões das 
provas. 
Teoria
1. Segundo o material teórico, qual é a função principal de um roteador?
a) Dispositivo de camada 3 que interconecta redes e toma decisões de encaminhamento 
baseadas em tabelas de roteamento
b) Dispositivo de camada 2 que interconecta switches
c) Firewall de aplicação que filtra conteúdo malicioso na camada 7
d) Servidor de DNS recursivo para resolução de nomes
Resposta: a
Comentário: O roteador é definido como dispositivo de camada 3 cuja função é interconectar 
redes distintas e tomar decisões de encaminhamento com base na tabela de roteamento.
2. Sobre o roteamento estático, qual característica o diferencia fundamentalmente do roteamento 
dinâmico?
a) Utiliza protocolos como RIP e OSPF para troca automática de informações
b) Adapta-se automaticamente a falhas de links e mudanças de topologia
c) Requer autenticação MD5 obrigatória entre roteadores vizinhos
d) Consiste na configuração manual de rotas pelo administrador, oferecendo previsibilidade total 
do caminho do tráfego
Resposta: d
Comentário: O roteamento estático é inserido manualmente pelo administrador, não há troca 
automática de informações entre roteadores e sua principal vantagem de segurança é a 
previsibilidade total dos caminhos.
3. Qual é o principal risco de segurança associado aos protocolos de roteamento dinâmico?
a) Lentidão na convergência superior a 60 segundos
b) Possibilidade de um roteador malicioso ou comprometido injetar rotas falsas, desviando tráfego 
para interceptação
c) Exigência de endereçamento IPv6 exclusivo
d) Consumo excessivo de largura de banda em broadcasts contínuos
Resposta: b
Comentário: Em roteamento dinâmico, o risco principal é a injeção de rotas falsas por roteadores 
não autorizados, possibilitando ataques Man-in-the-Middle.
4. Em relação ao protocolo RIP, qual afirmação está correta?
a) RIPv1 transmite atualizações em multicast no endereço 224.0.0.9
b) A métrica do RIP é baseada na largura de banda do enlace
c) RIPv2 introduziu suporte a autenticação via senha em texto ou hash MD5, além de multicast 
direcionado
d) O limite máximo de hops no RIP é 255, tornando-o ideal para redes grandes
Resposta: c
Comentário: RIPv2 trouxe autenticação (texto simples ou MD5) e utiliza multicast 224.0.0.9, 
diferente de RIPv1 que usa broadcast e não possui autenticação.
5. No protocolo OSPF, qual elemento é obrigatório na hierarquia de áreas?
a) Área stub em cada segmento de rede
b) Área backbone (Area 0) como centro da hierarquia
c) ABR (Area Border Router) em cada subnet
d) Autenticação HMAC-SHA obrigatória em todas as interfaces
Resposta: b
Comentário: O OSPF organiza a rede em áreas hierárquicas e a Area 0 (backbone) é obrigatória 
como centro da topologia.
6. Para que um sistema Linux funcione como roteador multi-homed, qual parâmetro do kernel 
deve ser habilitado?
a) net.ipv4.ip_forward = 1
b) net.ipv4.conf.all.accept_redirects = 1
c) net.ipv4.tcp_syncookies = 0
d) net.ipv4.conf.all.rp_filter = 2
Resposta: a
Comentário: O encaminhamento de pacotes entre interfaces no Linux exige a habilitação do IP 
forwarding via sysctl net.ipv4.ip_forward=1.
7. No Policy-Based Routing (PBR) do Linux, qual é o valor de prioridade padrão da tabela main?
a) 0
b) 100
c) 32766
d) 32767
Resposta: c
Comentário: As regras padrão do kernel incluem local (0), main (32766) e default (32767); a tabela 
main possui prioridade 32766.
8. Qual a distinção fundamental entre ACLs aplicadas em roteadores e firewalls de host?
a) ACLs operam exclusivamente na camada de aplicação
b) Firewalls de host protegem apenas o próprio sistema, enquanto ACLs em roteadores controlam 
o fluxo entre redes inteiras
c) ACLs não permitem filtragem baseada em endereços IP de origem
d) Firewalls de host são obrigatoriamente implementados em hardware dedicado
Resposta: b
Comentário: Enquanto o firewall de host protege apenas a máquina local, as ACLs em roteadores 
atuam como ponto de controle entre segmentos de rede distintos.
9. Em nftables, qual hook é especificamente utilizado para processar pacotes que atravessam o 
roteador entre interfaces distintas?
a) input
b) output
c) forward
d) prerouting
Resposta: c
Comentário: O hook forward processa pacotes que atravessam o sistema (de uma interface para 
outra), sendo essencial para roteadores.
10. Em nftables, o match que filtra pacotes pela interface de saída é representado por:
a) iifname
b) iif
c) fwmark
d) oifname
Resposta: d
Comentário: O match oifname (output interface name) filtra com base no nome da interface de 
saída do pacote.
11. A segmentação de rede em VLANs é considerada uma prática essencial de segurança porque:
a) Aumenta a velocidade de transmissão em até 50%
b) Isola broadcast domains e limita a propagação de ameaças laterais
c) Elimina completamente a necessidade de roteamento entre segmentos
d) Fornece endereçamento IP automático via DHCP integrado
Resposta: b
Comentário: VLANs isolam domínios de broadcast e restringem a movimentação lateral de 
ameaças, sendo fundamental para a segurança da infraestrutura.
12. O que caracteriza o conceito de Path Isolation em segurança de redes?
a) Criptografia simétrica aplicada a todos os pacotes IP
b) Estratégia que garante caminhos de rede separados para diferentes tipos de tráfego
c) Protocolo de roteamento dinâmico com convergência em 1 segundo
d) Técnica de balanceamento de carga por round-robin DNS
Resposta: b
Comentário: Path Isolation garante que tráfegos de diferentes classes de serviço ou sensibilidade 
não compartilhem os mesmos caminhos físicos ou lógicos.
13. Em ambientes de alta segurança, qual é a recomendação híbrida para o uso de roteamento 
estático e dinâmico?
a) Utilizar roteamento estático para segmentos críticos e dinâmico apenas onde a resiliência é 
mandatória, sempre com autenticação
b) Utilizar apenas roteamento dinâmico em todos os segmentos
c) Desabilitar todas as ACLs para garantir alta disponibilidade
d) Adotar RIPv1 sem autenticação por simplicidade administrativa
Resposta: a
Comentário: A recomendação é combinar estático em segmentos críticos (previsibilidade) com 
dinâmico apenas onde necessário, sempre com autenticação de vizinhos.
14. Qual das seguintes opções NÃO representa uma boa prática de roteamento seguro segundo o 
material?
a) Desativar serviços desnecessários no roteador Linux
b) Aplicar ACLs com política default-deny
c) Manter logs de tráfego negado para análise forense
d) Aplicar política de permissão padrão (default-allow) nas chains de forward
Resposta: d
Comentário: A postura de segurança recomendada é default-deny (negar tudo não explicitamente 
permitido); default-allow aumenta a superfície de ataque.
Prática
15. Na topologia do laboratório prático, qual modo de adaptador de rede do VirtualBox deve ser 
utilizado para interconectar as VMs aos segmentos?
a) Host-only
b) NAT
c) Internal Network
d) Bridged Adapter
Resposta: c
Comentário: O laboratório especifica o uso de adaptadores em modo "Internal Network" (seg10, 
seg20, seg30), proibindo Host-only por indisponibilidade no laboratório.
16. No script de configuração do roteador, qual comando habilita o encaminhamento de pacotes 
IPv4 entre as interfaces?
a) sudo sysctl -w net.ipv4.ip_forward=1
b) sudo ip route add default via 192.168.10.254
c) sudo ip link set eth1 up
d) sudo nft -f /etc/nftables.conf
Resposta: a
Comentário: O script setup_router.sh utiliza sysctl para habilitar o IP forwarding no kernel, 
essencial para o roteamento entre segmentos.
17. No script de Policy-Based Routing, qual comando cria a regra que direciona o tráfego 
originado do segmento 30 para a tabela customizada "visitantes"?
a) sudo ip route add 192.168.30.0/24 table visitantes
b) sudo ip addr add 192.168.30.1/24 dev eth3
c) echo "200 visitantes" | sudo tee -a /etc/iproute2/rt_tables
d) sudo ip rule add from 192.168.30.0/24 table visitantes priority 100
Resposta: d
Comentário: O comando ip rule add com o seletor from define que pacotes originados de 
192.168.30.0/24 devem consultar a tabela customizada visitantes.
18. Na configuração base do nftables apresentada no laboratório, qual é a política padrão definida 
para a chain input?
a) accept
b) drop
c) reject
d) log
Resposta: b
Comentário: A chain input é configurada com policy drop, negando todo tráfego não explicitamente 
permitido (postura de segurança default-deny).
19. Qual regra do script nftables_forward.sh implementa o bloqueio explícito do tráfego entre o 
segmento de Visitantes e o segmento de Servidores?
a) iifname GUESTDEVoifname SERV_DEV drop
b) iifname MGMTDEVoifname SERV_DEV accept
c) iifname SERVDEVoifname MGMT_DEV accept
d) iifname MGMTDEVoifname GUEST_DEV accept
Resposta: a
Comentário: A REGRA 3 do script utiliza iifname/oifname para bloquear explicitamente o tráfego 
originado em GUEST_DEV com destino a SERV_DEV.
20. No script de testes de validação, qual comando é utilizado para verificar os logs de tentativas 
de acesso bloqueadas entre VLANs?
a) sudo nft list ruleset
b) ip route show table visitantes
c) sudo systemctl status nftables
d) sudo dmesg | grep "VLAN-ISOLATION" | tail -5
Resposta: d
Comentário: O script test_lab.sh utiliza dmesg filtrando pelo prefixo "VLAN-ISOLATION" 
configurado nas regras de log do nftables para auditoria.
```

---

## Módulo 03 — Firewalls de Perímetro e Filtragem Avançada

### Questões de Múltipla Escolha

```
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Q de múlt escolha
Como obter maior aproveitamento deste objeto de apredizagem:
1. Responder sem olhar o gabarito. Para isso, procurar pelas respostas nos slides da aula 
“ISG012-03 - Firewalls de Perímetro e Filtragem Avançada” (teoria e prática);
1. Após responder TODAS as questões, comparar com o gabarito;
2. Refazer os passos 1 e 2 novamente com todas as questões até obter 100% de acertos de 
uma só vez.
Importante: Embora seja baseado nos slides teóricos e nas atividades práticas, este 
questionário pode conter informações que não constam nesses documentos pois pode 
incluir algum nível detalhamento em relação a eles. Assim, considere as informações aqui 
contidas como parte complementar do conteúdo a ser estudado para as provas. Todo o 
material distribuido pelo professor poderá ser utilizado para a confecção das questões das 
provas. 
Teoria (14 questões)
1. Qual é o objetivo principal desta aula sobre Firewalls de Perímetro e Filtragem Avançada?
a) Ensinar configuração de switches Cisco apenas
b) Desenvolver aplicações web seguras em Java
c) Capacitar estudantes a compreender e implementar arquiteturas de segurança de perímetro 
com firewalls modernos
d) Configurar exclusivamente antivírus de endpoint
2. Em qual posição topológica típica se localiza um firewall de perímetro?
a) No centro da rede interna, entre departamentos
b) Na borda da infraestrutura, entre a rede organizacional e a Internet
c) Apenas dentro da DMZ de backend
d) Somente em servidores de arquivos internos
3. O packet filtering firewall (1ª geração) opera em qual camada do modelo OSI?
a) Camada 2 (Enlace)
b) Camada 5 (Sessão)
c) Camada 3 (Rede)
d) Camada 7 (Aplicação)
4. Qual característica define corretamente a 1ª geração de firewalls (Packet Filter)?
a) Realiza inspeção profunda de conteúdo na camada 7
b) É stateful e mantém tabela de conexões ativas
c) Identifica usuários através de integração com Active Directory
d) É rápido, stateless, analisa cada pacote isoladamente e é vulnerável a spoofing
5. A DMZ (Zona Desmilitarizada) é definida como:
a) Uma sub-rede intermediária que expõe serviços externos à Internet, isolando-os da rede interna 
corporativa
b) A rede interna completa onde residem os ativos críticos
c) Um tipo de firewall de aplicação específico para e-mail
d) A zona de maior confiança da arquitetura de rede
6. Na arquitetura de firewall de perímetro com DMZ, qual é a função do firewall externo 
(perímetro)?
a) Proteger a rede interna da DMZ com regras restritivas
b) Filtrar tráfego entre Internet e DMZ, permitindo apenas portas específicas para servidores 
públicos
c) Permitir acesso irrestrito da Internet para a rede interna
d) Gerenciar apenas o tráfego de e-mail corporativo
7. Segundo o princípio do menor privilégio no design de DMZ, servidores nessa zona devem:
a) Ter acesso total à rede interna para facilitar a administração
b) Ter todas as portas abertas para garantir disponibilidade
c) Ter apenas as portas necessárias abertas e comunicação restrita com a rede interna
d) Ser posicionados diretamente na rede interna sem isolamento
8. Qual é a principal vantagem de um firewall stateful em relação a um stateless?
a) É mais rápido e consome menos recursos de hardware
b) Não analisa cabeçalhos IP para filtragem
c) Opera exclusivamente com protocolos UDP
d) Bloqueia ataques de spoofing e permite tráfego de retorno automático sem regras explícitas
9. A tabela de estados (state table) de um firewall stateful tipicamente contém:
a) O 5-tuple (IP origem/destino, portas origem/destino, protocolo), estado TCP e timestamps
b) Apenas o endereço MAC dos dispositivos
c) Somente o nome de usuário de quem iniciou a conexão
d) Apenas o tamanho total dos pacotes transmitidos
10. Qual é a principal função do NAT (Network Address Translation) em firewalls de perímetro?
a) Criptografar todo o tráfego entre rede interna e Internet
b) Permitir que múltiplos hosts em redes privadas compartilhem endereços IP públicos e ocultem a 
topologia interna
c) Aumentar a velocidade de conexão com a Internet
d) Substituir a necessidade de firewalls na rede
11. O Source NAT (SNAT) com masquerade é implementado em qual chain do nftables?
a) PREROUTING
b) INPUT
c) POSTROUTING
d) FORWARD
12. O Destination NAT (DNAT) é implementado em qual chain do nftables?
a) POSTROUTING
b) OUTPUT
c) FORWARD
d) PREROUTING
13. No fluxo de processamento do netfilter, qual é a ordem correta dos hooks para um pacote 
encaminhado entre interfaces?
a) PREROUTING → Decisão de roteamento → FORWARD → POSTROUTING
b) INPUT → FORWARD → OUTPUT → POSTROUTING
c) PREROUTING → INPUT → FORWARD → OUTPUT
d) POSTROUTING → FORWARD → PREROUTING → INPUT
14. Qual é a prática recomendada de hardening para a política padrão (default policy) de um 
firewall?
a) ACCEPT all, DROP explicitamente o que não é necessário
b) DROP all, ALLOW explicitamente apenas o tráfego necessário (whitelist)
c) REJECT all sem nenhuma exceção
d) ACCEPT all e logar apenas tráfego HTTP
Prática (6 questões)
15. Quantas VMs são necessárias para montar o ambiente da prática de firewall de perímetro no 
VirtualBox?
a) 1 VM
b) 2 VMs
c) 3 VMs
d) 4 VMs
16. Qual é o endereço IP atribuído à interface WAN (eth0/NAT) do firewall no ambiente 
VirtualBox?
a) 192.168.56.1/24
b) 192.168.56.10/24
c) 172.16.0.1/24
d) 10.0.2.15 (DHCP)
17. Qual é o endereço IP configurado no Servidor DMZ na rede interna?
a) 192.168.56.10/24
b) 192.168.56.20/24
c) 10.0.2.15/24
d) 192.168.56.1/24
18. Qual comando habilita temporariamente o IP forwarding no firewall Linux?
a) sudo sysctl -w net.ipv4.ip_forward=0
b) sudo sysctl -w net.ipv4.ip_forward=1
c) sudo nft enable forwarding
d) sudo echo 1 > /etc/ip_forward
19. Na chain INPUT do script prático, qual serviço é permitido apenas pela interface interna 
(enp0s8)?
a) HTTP na porta 80
b) DNS na porta 53
c) SSH na porta 22
d) HTTPS na porta 443
20. Na regra de DNAT da prática, qual redirecionamento é configurado?
a) Porta 80 da WAN para porta 8080 do servidor interno
b) Porta 22 da WAN para porta 2222 do servidor interno
c) Porta 443 da WAN para porta 80 do servidor interno
d) Porta 8080 da WAN para porta 80 do servidor interno (192.168.56.10)
```

### Gabarito Comentado

```
ISG012-03 - Firewalls de Perímetro e Filtragem Avançada - Q de múlt escolha – Gabarito
Como obter maior aproveitamento deste objeto de apredizagem:
1. Responder sem olhar o gabarito. Para isso, procurar pelas respostas nos slides da aula 
“ISG012-03 - Firewalls de Perímetro e Filtragem Avançada” (teoria e prática);
1. Após responder TODAS as questões, comparar com o gabarito;
2. Refazer os passos 1 e 2 novamente com todas as questões até obter 100% de acertos de 
uma só vez.
Importante: Embora seja baseado nos slides teóricos e nas atividades práticas, este 
questionário pode conter informações que não constam nesses documentos pois pode 
incluir algum nível detalhamento em relação a eles. Assim, considere as informações aqui 
contidas como parte complementar do conteúdo a ser estudado para as provas. Todo o 
material distribuido pelo professor poderá ser utilizado para a confecção das questões das 
provas. 
Teoria (14 questões)
1. Qual é o objetivo principal desta aula sobre Firewalls de Perímetro e Filtragem Avançada?
a) Ensinar configuração de switches Cisco apenas
b) Desenvolver aplicações web seguras em Java
c) Capacitar estudantes a compreender e implementar arquiteturas de segurança de perímetro 
com firewalls modernos
d) Configurar exclusivamente antivírus de endpoint
Resposta correta: c
Comentário: O conteúdo programático visa capacitar os estudantes a compreenderem e 
implementarem arquiteturas de segurança de perímetro, diferenciando tipos de firewalls, 
projetando DMZ e configurando NAT com nftables.
2. Em qual posição topológica típica se localiza um firewall de perímetro?
a) No centro da rede interna, entre departamentos
b) Na borda da infraestrutura, entre a rede organizacional e a Internet
c) Apenas dentro da DMZ de backend
d) Somente em servidores de arquivos internos
Resposta correta: b
Comentário: Firewalls de perímetro são posicionados na borda (edge/border) da infraestrutura, 
constituindo a primeira linha de defesa entre a rede organizacional e a Internet. 
3. O packet filtering firewall (1ª geração) opera em qual camada do modelo OSI?
a) Camada 2 (Enlace)
b) Camada 5 (Sessão)
c) Camada 3 (Rede)
d) Camada 7 (Aplicação)
Resposta correta: c
Comentário: O packet filtering firewall opera na camada 3 do modelo OSI, analisando cabeçalhos 
IP e portas TCP/UDP, sendo rápido mas limitado por não inspectionar o conteúdo. 
4. Qual característica define corretamente a 1ª geração de firewalls (Packet Filter)?
a) Realiza inspeção profunda de conteúdo na camada 7
b) É stateful e mantém tabela de conexões ativas
c) Identifica usuários através de integração com Active Directory
d) É rápido, stateless, analisa cada pacote isoladamente e é vulnerável a spoofing
Resposta correta: d
Comentário: A 1ª geração é stateless, analisa pacotes individualmente sem contexto de conexão 
e é vulnerável a ataques de spoofing, diferentemente das gerações posteriores. 
5. A DMZ (Zona Desmilitarizada) é definida como:
a) Uma sub-rede intermediária que expõe serviços externos à Internet, isolando-os da rede interna 
corporativa
b) A rede interna completa onde residem os ativos críticos
c) Um tipo de firewall de aplicação específico para e-mail
d) A zona de maior confiança da arquitetura de rede
Resposta correta: a
Comentário: A DMZ é uma sub-rede física ou lógica que hospeda serviços públicos (web, DNS, 
e-mail) e funciona como área intermediária de segurança entre a Internet e a rede interna.
6. Na arquitetura de firewall de perímetro com DMZ, qual é a função do firewall externo 
(perímetro)?
a) Proteger a rede interna da DMZ com regras restritivas
b) Filtrar tráfego entre Internet e DMZ, permitindo apenas portas específicas para servidores 
públicos
c) Permitir acesso irrestrito da Internet para a rede interna
d) Gerenciar apenas o tráfego de e-mail corporativo
Resposta correta: b
Comentário: O firewall de perímetro (externo) controla o tráfego entre a zona não confiável 
(Internet) e a zona controlada (DMZ), tipicamente permitindo apenas portas específicas como 80, 
443, 25 e 53. 
7. Segundo o princípio do menor privilégio no design de DMZ, servidores nessa zona devem:
a) Ter acesso total à rede interna para facilitar a administração
b) Ter todas as portas abertas para garantir disponibilidade
c) Ter apenas as portas necessárias abertas e comunicação restrita com a rede interna
d) Ser posicionados diretamente na rede interna sem isolamento
Resposta correta: c
Comentário: O design efetivo de DMZ exige que servidores públicos tenham apenas as portas 
estritamente necessárias abertas e comunicação mínima com a rede interna, protegendo ativos 
críticos.
8. Qual é a principal vantagem de um firewall stateful em relação a um stateless?
a) É mais rápido e consome menos recursos de hardware
b) Não analisa cabeçalhos IP para filtragem
c) Opera exclusivamente com protocolos UDP
d) Bloqueia ataques de spoofing e permite tráfego de retorno automático sem regras explícitas
Resposta correta: d
Comentário: O firewall stateful mantém uma tabela de estados (state table) que registra conexões 
ativas, permitindo identificar pacotes de sessões estabelecidas e bloquear spoofing, além de 
simplificar as regras.
9. A tabela de estados (state table) de um firewall stateful tipicamente contém:
a) O 5-tuple (IP origem/destino, portas origem/destino, protocolo), estado TCP e timestamps
b) Apenas o endereço MAC dos dispositivos
c) Somente o nome de usuário de quem iniciou a conexão
d) Apenas o tamanho total dos pacotes transmitidos
Resposta correta: a
Comentário: Cada entrada na state table contém o 5-tuple, o estado atual da conexão TCP 
(SYN_SENT, ESTABLISHED, TIME_WAIT), timestamps de última atividade e flags de controle. 
10. Qual é a principal função do NAT (Network Address Translation) em firewalls de perímetro?
a) Criptografar todo o tráfego entre rede interna e Internet
b) Permitir que múltiplos hosts em redes privadas compartilhem endereços IP públicos e ocultem a 
topologia interna
c) Aumentar a velocidade de conexão com a Internet
d) Substituir a necessidade de firewalls na rede
Resposta correta: b
Comentário: O NAT permite que hosts em redes privadas (RFC 1918) compartilhem IPs públicos 
e proporciona segurança adicional ao ocultar a topologia interna da rede. 
11. O Source NAT (SNAT) com masquerade é implementado em qual chain do nftables?
a) PREROUTING
b) INPUT
c) POSTROUTING
d) FORWARD
Resposta correta: c
Comentário: O SNAT é implementado na chain POSTROUTING, pois a alteração do endereço de 
origem deve ocorrer após a decisão de roteamento, antes do pacote sair pela interface externa. 
12. O Destination NAT (DNAT) é implementado em qual chain do nftables?
a) POSTROUTING
b) OUTPUT
c) FORWARD
d) PREROUTING
Resposta correta: d
Comentário: O DNAT é aplicado na chain PREROUTING, antes da decisão de roteamento, para 
que o pacote seja corretamente redirecionado para a rede interna ou DMZ.
13. No fluxo de processamento do netfilter, qual é a ordem correta dos hooks para um pacote 
encaminhado entre interfaces?
a) PREROUTING → Decisão de roteamento → FORWARD → POSTROUTING
b) INPUT → FORWARD → OUTPUT → POSTROUTING
c) PREROUTING → INPUT → FORWARD → OUTPUT
d) POSTROUTING → FORWARD → PREROUTING → INPUT
Resposta correta: a
Comentário: Pacotes encaminhados passam por PREROUTING (onde DNAT é aplicado), 
decisão de roteamento, chain FORWARD e finalmente POSTROUTING (onde SNAT é aplicado) 
antes de sair.
14. Qual é a prática recomendada de hardening para a política padrão (default policy) de um 
firewall?
a) ACCEPT all, DROP explicitamente o que não é necessário
b) DROP all, ALLOW explicitamente apenas o tráfego necessário (whitelist)
c) REJECT all sem nenhuma exceção
d) ACCEPT all e logar apenas tráfego HTTP
Resposta correta: b
Comentário: A política padrão deve ser DROP para todas as chains, permitindo explicitamente 
apenas o tráfego necessário, minimizando a superfície de ataque.
Prática (6 questões)
15. Quantas VMs são necessárias para montar o ambiente da prática de firewall de perímetro no 
VirtualBox?
a) 1 VM
b) 2 VMs
c) 3 VMs
d) 4 VMs
Resposta correta: c
Comentário: O ambiente final utiliza 3 VMs: Firewall (2 interfaces), Servidor DMZ (1 interface) e 
Estação de Trabalho (1 interface). 
16. Qual é o endereço IP atribuído à interface WAN (eth0/NAT) do firewall no ambiente 
VirtualBox?
a) 192.168.56.1/24
b) 192.168.56.10/24
c) 172.16.0.1/24
d) 10.0.2.15 (DHCP)
Resposta correta: d
Comentário: A interface eth0 (NAT VirtualBox) do firewall recebe IP via DHCP na rede 
10.0.2.0/24, tipicamente 10.0.2.15, simulando o acesso à Internet.
17. Qual é o endereço IP configurado no Servidor DMZ na rede interna?
a) 192.168.56.10/24
b) 192.168.56.20/24
c) 10.0.2.15/24
d) 192.168.56.1/24
Resposta correta: a
Comentário: O Servidor DMZ é configurado com IP estático 192.168.56.10/24 na rede interna 
VirtualBox, com gateway 192.168.56.1.
18. Qual comando habilita temporariamente o IP forwarding no firewall Linux?
a) sudo sysctl -w net.ipv4.ip_forward=0
b) sudo sysctl -w net.ipv4.ip_forward=1
c) sudo nft enable forwarding
d) sudo echo 1 > /etc/ip_forward
Resposta correta: b
Comentário: O comando sudo sysctl -w net.ipv4.ip_forward=1 ativa o encaminhamento de 
pacotes entre interfaces temporariamente; para persistir, edita-se /etc/sysctl.conf.
19. Na chain INPUT do script prático, qual serviço é permitido apenas pela interface interna 
(enp0s8)?
a) HTTP na porta 80
b) DNS na porta 53
c) SSH na porta 22
d) HTTPS na porta 443
Resposta correta: c
Comentário: A regra nft add rule inet filter input iifname "enp0s8" tcp dport 22 ct state new 
accept permite SSH apenas pela interface LAN, bloqueando acesso administrativo pela WAN. 
20. Na regra de DNAT da prática, qual redirecionamento é configurado?
a) Porta 80 da WAN para porta 8080 do servidor interno
b) Porta 22 da WAN para porta 2222 do servidor interno
c) Porta 443 da WAN para porta 80 do servidor interno
d) Porta 8080 da WAN para porta 80 do servidor interno (192.168.56.10)
Resposta correta: d
Comentário: A regra nft add rule ip nat prerouting iifname "enp0s3" tcp dport 8080 dnat to 
192.168.56.10:80 redireciona a porta 8080 externa para a porta 80 do servidor web na DMZ.
```

### Atividades Práticas

```
ISG012-Aulas0304
Atividade ISG012-03 – Firewalls de Perímetro e Filtragem Avançada - Teoria
Questão 1
Enunciado: Explique a diferença fundamental entre firewalls stateless (packet filtering) e firewalls 
stateful inspection, destacando as vantagens de segurança proporcionadas pela abordagem 
stateful.
Questão 2
Enunciado: Descreva o propósito e a arquitetura típica de uma Zona Desmilitarizada (DMZ) em 
uma rede corporativa, explicando por que servidores públicos devem ser isolados tanto da Internet 
quanto da rede interna.
Questão 3
Enunciado: Explique o funcionamento do Source NAT (SNAT) e do Destination NAT (DNAT), 
diferenciando suas aplicações práticas em um firewall de perímetro.
Questão 4
Enunciado: Descreva como o connection tracking (conntrack) funciona em firewalls stateful e por 
que a regra "established,related accept" é tipicamente a primeira regra em uma chain de firewall.
Questão 5
Enunciado: Explique a importância da ordem das regras em um firewall e como a política padrão 
(default policy) afeta a segurança geral da configuração.
Questão 6
Enunciado: Descreva as melhores práticas para logging em firewalls de perímetro e como os logs 
contribuem para a detecção de tentativas de intrusão.
Atividade ISG012-03 – Firewalls de Perímetro e Filtragem Avançada -  Prática
Questão Prática 1
Enunciado: Qual comando nftables é utilizado para criar uma tabela que suporte tanto IPv4 
quanto IPv6, e qual a diferença em relação a uma tabela IP específica?
Questão Prática 2
Enunciado: Na experiência prática, como configurar o mascaramento (SNAT dinâmico) para 
permitir que a rede interna 192.168.56.0/24 acesse a Internet através do firewall, e por que usar 
masquerade em vez de snat to IP?
Questão Prática 3
Enunciado: Durante a experiência, após configurar o DNAT para redirecionar a porta 8080 do 
firewall para o servidor web interno (192.168.56.10:80), por que é necessário adicionar também 
uma regra na chain FORWARD da tabela filter, e qual seria o comando correto?
Atividade ISG012-04 – Teoria
1. Quais são os principais objetivos de aprendizagem propostos para o módulo de Redes Privadas 
Virtuais (VPN) e quais competências o aluno deve desenvolver ao final do curso?
2. De que forma as VPNs site-to-site e remote access diferenciam-se quanto ao modelo de 
deployment, à arquitetura de rede e aos cenários de uso mais adequados para cada uma?
3. Explique a arquitetura do IPsec, seus principais protocolos constituintes e como os modos de 
operação transporte e túnel atendem a diferentes cenários de comunicação segura.
4. Qual é o papel da criptografia assimétrica no estabelecimento de uma VPN e como os 
algoritmos modernos de curvas elípticas, como o Curve25519, apresentam vantagens em relação 
ao RSA tradicional?
5. Descreva o processo completo de estabelecimento de um canal seguro em uma VPN, desde a 
troca inicial de chaves públicas até a criptografia simétrica do tráfego de dados.
6. Por que o modo túnel do IPsec é considerado o padrão para VPNs site-to-site e quais são as 
principais desvantagens que tornam o IPsec menos competitivo frente a soluções modernas como 
WireGuard?
Atividade ISG012-04 – Prática
1. Qual é a topologia de laboratório proposta para simular uma VPN site-to-site entre duas filiais e  
como o VirtualBox deve ser configurado para viabilizar essa prática?
2. Quais são os procedimentos técnicos para gerar os pares de chaves Curve25519 e configurar 
as interfaces WireGuard (wg0) no modo site-to-site nas duas máquinas virtuais?
3. Como devemos proceder para ativar o túnel WireGuard, validar a conectividade entre as redes 
privadas simuladas e verificar, por meio de captura de pacotes, que a criptografia está 
efetivamente protegendo os dados?
Orientações
Código da atividade: ISG012-Aulas0304
Enviar a atividade anexada em um e-mail para rglabrada.jog@gmail.com No assunto
coloque o código da atividade (ISG012-Aulas0304) e o seu nome completo.
Exemplo, supondo que o aluno se chama Fulano de Tal, colocar no assunto do e-mail: 
ISG012-Aulas0304 Fulano de Tal
Envie somente um anexo por e-mail (envie um e-mail exclusivo para esta atividade).
A atividade deve ter 6 itens devidamente identificados (toda a atividade deve estar em um 
único arquivo com extensão .pdf):
Objetivo: até 2,0;
Atividade ISG012-03 – Teoria: até 1,5;
Atividade ISG012-03 – Prática: até 1,5;
Atividade ISG012-04 – Teoria até 1,5;
Atividade ISG012-04 – Prática: até 1,5;
Conclusão: até 2,0.
Prazo: 09/06/2026 23:59
Atenção! Não serão consideradas as atividades recebidas após esse prazo.
Caso tenha dúvidas, procure o professor.
```

---

## Módulo 04 — Redes Privadas Virtuais (VPN)

### Questões de Múltipla Escolha

```
ISG012-04 - Redes Privadas Virtuais (VPN) - Q de múlt escolha - Gabarito - INTERNO
Como obter maior aproveitamento deste objeto de apredizagem:
1. Responder sem olhar o gabarito. Para isso, procurar pelas respostas nos slides da aula 
“ISG012-04 - Redes Privadas Virtuais (VPN)” (teoria e prática);
1. Após responder TODAS as questões, comparar com o gabarito;
2. Refazer os passos 1 e 2 novamente com todas as questões até obter 100% de acertos de 
uma só vez.
Importante: Embora seja baseado nos slides teóricos e nas atividades práticas, este 
questionário pode conter informações que não constam nesses documentos pois pode 
incluir algum nível detalhamento em relação a eles. Assim, considere as informações aqui 
contidas como parte complementar do conteúdo a ser estudado para as provas. Todo o 
material distribuído pelo professor poderá ser utilizado para a confecção das questões das 
provas. 
PARTE TEÓRICA
1. Quais protocolos criptográficos são explicitamente mencionados como objetivo de estudo no 
módulo de VPN?
A) PPTP, L2TP, SSTP e OpenVPN
B) IPsec, SSL/TLS, WireGuard e SSH
C) IPsec, SSL/TLS, WireGuard e IKEv2
D) IPsec, SSL/TLS e WireGuard
2. Qual é a característica principal de uma VPN site-to-site?
A) Gateways VPN criptografam automaticamente o tráfego entre redes sem configuração 
individual nos dispositivos dos usuários
B) Exige instalação de software cliente em cada laptop de funcionário
C) Conecta um dispositivo individual à rede corporativa central
D) É utilizada exclusivamente para comunicação host-to-host entre dois Pcs
3. O que diferencia a VPN remote access da site-to-site?
A) Opera apenas na camada 2 do modelo OSI
B) Conecta um dispositivo individual à rede corporativa e exige autenticação do usuário
C) Utiliza apenas o protocolo AH do Ipsec
D) Não necessita de software cliente para funcionar Resposta correta: B. A remote access 
conecta um dispositivo individual à rede central, exigindo software cliente e autenticação do 
usuário, sendo essencial para mobilidade e home office.
4. Em qual camada do modelo OSI o IPsec opera?
A) Camada 2 (Enlace)
B) Camada 4 (Transporte)
C) Camada 3 (Rede)
D) Camada 7 (Aplicação)
5. Qual protocolo do IPsec garante autenticidade e integridade, mas NÃO oferece 
confidencialidade?
A) AH (Authentication Header)
B) ESP (Encapsulating Security Payload)
C) IKE (Internet Key Exchange)
D) GRE (Generic Routing Encapsulation)
6. No modo túnel do IPsec, o que ocorre com o pacote IP original?
A) Apenas o payload é criptografado, mantendo o cabeçalho original visível
B) O pacote IP inteiro é encapsulado dentro de um novo pacote IP
C) O cabeçalho é removido e substituído por um cabeçalho TCP
D) O pacote é fragmentado em múltiplos datagramas UDP
7. Quais são as principais desvantagens do IPsec em comparação com soluções modernas?
A) Baixa compatibilidade com firewalls e impossibilidade de NAT traversal
B) Falta de padronização pela IETF e ausência de modos de operação
C) Incompatibilidade com criptografia assimétrica e dependência de certificados digitais
D) Complexidade de configuração e overhead de processamento
8. Qual é a função da criptografia assimétrica no contexto de uma VPN?
A) Criptografar diretamente todo o tráfego de dados em alta velocidade
B) Substituir completamente a criptografia simétrica durante toda a sessão
C) Autenticação de identidade e estabelecimento de canal seguro para troca de chaves simétricas
D) Compactar pacotes antes do envio pelo túnel
9. Qual algoritmo de curvas elípticas é citado como moderno para uso em VPNs?
A) Curve25519
B) RSA-4096 C) AES-256
D) SHA-512
10. Qual é a primeira etapa do processo prático de estabelecimento de canal seguro?
A) Geração da chave de sessão simétrica via KDF
B) Troca de chaves públicas entre peers
C) Criptografia simétrica do tráfego de dados
D) Execução do protocolo ESP em modo túnel
11. O que o ECDH (Elliptic Curve Diffie-Hellman) gera durante o handshake?
A) Um certificado digital autoassinado
B) Uma chave pública de 4096 bits
C) Um hash de integridade do pacote
D) Um segredo compartilhado entre os peers
12. Após o segredo compartilhado gerado pelo ECDH, qual é a próxima etapa no processo?
A) Envio direto do segredo pela rede em texto claro
B) Assinatura digital do segredo com a chave privada
C) Derivação de chaves simétricas de sessão via KDF
D) Encerramento da conexão e reinício do handshake
13. Qual é a principal vantagem da criptografia assimétrica sobre a distribuição de chaves 
simétricas?
A) Elimina a necessidade de um canal seguro prévio para troca de chaves
B) Permite criptografar dados em velocidades superiores a 10 Gbps
C) Reduz o tamanho dos pacotes IP em 50%
D) Não requer o uso de algoritmos de hash
14. Qual conceito de segurança garante que a compromissão de uma chave de sessão não afete 
sessões anteriores?
A) NAT Traversal
B) Perfect Forward Secrecy
C) Split Tunneling
D) Dead Peer Detection
PARTE PRÁTICA
15. Na topologia do laboratório, qual é o modo de rede do adaptador eth0 em ambas as Vms?
A) Rede Interna (vpn-lab)
B) Bridge Adapter
C) Host-Only Adapter
D) NAT (padrão do VirtualBox)
16. Qual comando gera o par de chaves pública e privada Curve25519 no WireGuard?
A) sudo openssl genrsa -out privatekey 2048
B) sudo ssh-keygen -t ed25519
C) sudo wg genkey | sudo tee privatekey | sudo wg pubkey | sudo tee publickey
D) sudo ipsec genkey –curve25519
17. Qual permissão é recomendada para o diretório /etc/wireguard?
A) 700
B) 755
C) 644
D) 777
18. Qual comando cria o alias de loopback (lo:1) simulando a LAN da Filial A (172.16.1.0/24)?
A) sudo ip tunnel add lo:1 mode ipip local 172.16.1.1
B) sudo ip addr add 172.16.1.1/24 dev lo label lo:1
C) sudo ifconfig lo:1 172.16.1.1 netmask 255.255.0.0
D) sudo wg set lo:1 listen-port 51820 private-key /etc/wireguard/privatekey
19. Qual é a função do parâmetro PersistentKeepalive = 25 na configuração do WireGuard?
A) Renovar as chaves Curve25519 a cada 25 segundos
B) Limitar a banda do túnel a 25 KB/s
C) Manter sessões NAT/firewall abertas enviando pacotes a cada 25 segundos
D) Encerrar o túnel após 25 segundos de inatividade
20. Para comprovar visualmente que a criptografia está funcionando, onde o aluno deve capturar 
pacotes com tcpdump?
A) Na interface wg0, onde os pacotes aparecem criptografados
B) Na interface lo:1, onde o tráfego de LAN é encapsulado
C) Na interface NAT (eth0), filtrando pacotes ICMP
D) Na interface física (enp0s8), filtrando UDP porta 51820, onde os dados aparecem ilegíveis
```

### Gabarito Comentado

```
ISG012-04 - Redes Privadas Virtuais (VPN) - Q de múlt escolha - Gabarito - INTERNO
Como obter maior aproveitamento deste objeto de apredizagem:
1. Responder sem olhar o gabarito. Para isso, procurar pelas respostas nos slides da aula 
“ISG012-04 - Redes Privadas Virtuais (VPN)” (teoria e prática);
1. Após responder TODAS as questões, comparar com o gabarito;
2. Refazer os passos 1 e 2 novamente com todas as questões até obter 100% de acertos de 
uma só vez.
Importante: Embora seja baseado nos slides teóricos e nas atividades práticas, este 
questionário pode conter informações que não constam nesses documentos pois pode 
incluir algum nível detalhamento em relação a eles. Assim, considere as informações aqui 
contidas como parte complementar do conteúdo a ser estudado para as provas. Todo o 
material distribuído pelo professor poderá ser utilizado para a confecção das questões das 
provas. 
PARTE TEÓRICA
1. Quais protocolos criptográficos são explicitamente mencionados como objetivo de estudo no 
módulo de VPN?
A) PPTP, L2TP, SSTP e OpenVPN
B) IPsec, SSL/TLS, WireGuard e SSH
C) IPsec, SSL/TLS, WireGuard e IKEv2
D) IPsec, SSL/TLS e WireGuard
Resposta correta: D. O slide dos objetivos lista especificamente IPsec, SSL/TLS e WireGuard 
como protocolos criptográficos a serem estudados, sem mencionar SSH, PPTP, L2TP ou IKEv2 
como objetivos principais.
2. Qual é a característica principal de uma VPN site-to-site?
A) Gateways VPN criptografam automaticamente o tráfego entre redes sem configuração 
individual nos dispositivos dos usuários
B) Exige instalação de software cliente em cada laptop de funcionário
C) Conecta um dispositivo individual à rede corporativa central
D) É utilizada exclusivamente para comunicação host-to-host entre dois Pcs
Resposta correta: A. A VPN site-to-site interconecta redes fixas através de gateways que 
criptografam o tráfego automaticamente, sendo ideal para infraestrutura permanente entre filiais. 
3. O que diferencia a VPN remote access da site-to-site?
A) Opera apenas na camada 2 do modelo OSI
B) Conecta um dispositivo individual à rede corporativa e exige autenticação do usuário
C) Utiliza apenas o protocolo AH do Ipsec
D) Não necessita de software cliente para funcionar Resposta correta: B. A remote access 
conecta um dispositivo individual à rede central, exigindo software cliente e autenticação do 
usuário, sendo essencial para mobilidade e home office.
4. Em qual camada do modelo OSI o IPsec opera?
A) Camada 2 (Enlace)
B) Camada 4 (Transporte)
C) Camada 3 (Rede)
D) Camada 7 (Aplicação)
Resposta correta: C. O IPsec opera na camada de rede (camada 3 do modelo OSI), oferecendo 
segurança transparente para todas as aplicações.
5. Qual protocolo do IPsec garante autenticidade e integridade, mas NÃO oferece 
confidencialidade?
A) AH (Authentication Header)
B) ESP (Encapsulating Security Payload)
C) IKE (Internet Key Exchange)
D) GRE (Generic Routing Encapsulation)
Resposta correta: A. O AH garante autenticidade e integridade, mas não criptografa o conteúdo, 
ao contrário do ESP, que oferece confidencialidade, integridade e autenticidade. 
6. No modo túnel do IPsec, o que ocorre com o pacote IP original?
A) Apenas o payload é criptografado, mantendo o cabeçalho original visível
B) O pacote IP inteiro é encapsulado dentro de um novo pacote IP
C) O cabeçalho é removido e substituído por um cabeçalho TCP
D) O pacote é fragmentado em múltiplos datagramas UDP
Resposta correta: B. No modo túnel, o pacote IP inteiro é encapsulado dentro de um novo 
pacote IP, sendo o padrão para VPNs site-to-site.
7. Quais são as principais desvantagens do IPsec em comparação com soluções modernas?
A) Baixa compatibilidade com firewalls e impossibilidade de NAT traversal
B) Falta de padronização pela IETF e ausência de modos de operação
C) Incompatibilidade com criptografia assimétrica e dependência de certificados digitais
D) Complexidade de configuração e overhead de processamento
Resposta correta: D. A complexidade de configuração e o overhead de processamento são as 
principais desvantagens do IPsec comparadas a soluções mais modernas. 
8. Qual é a função da criptografia assimétrica no contexto de uma VPN?
A) Criptografar diretamente todo o tráfego de dados em alta velocidade
B) Substituir completamente a criptografia simétrica durante toda a sessão
C) Autenticação de identidade e estabelecimento de canal seguro para troca de chaves simétricas
D) Compactar pacotes antes do envio pelo túnel
Resposta correta: C. A criptografia assimétrica autentica identidades e estabelece um canal 
seguro para a troca das chaves simétricas que efetivamente criptografarão o tráfego.
9. Qual algoritmo de curvas elípticas é citado como moderno para uso em VPNs?
A) Curve25519
B) RSA-4096 C) AES-256
D) SHA-512
Resposta correta: A. Curve25519 é citado como algoritmo moderno de ECC, oferecendo 
menores chaves com o mesmo nível de segurança, ao lado do P-256.
10. Qual é a primeira etapa do processo prático de estabelecimento de canal seguro?
A) Geração da chave de sessão simétrica via KDF
B) Troca de chaves públicas entre peers
C) Criptografia simétrica do tráfego de dados
D) Execução do protocolo ESP em modo túnel
Resposta correta: B. O processo inicia com a troca de chaves públicas (ou certificados) entre os 
peers, seguido da autenticação mútua.
11. O que o ECDH (Elliptic Curve Diffie-Hellman) gera durante o handshake?
A) Um certificado digital autoassinado
B) Uma chave pública de 4096 bits
C) Um hash de integridade do pacote
D) Um segredo compartilhado entre os peers
Resposta correta: D. O ECDH gera um segredo compartilhado entre os peers, que servirá de 
base para a derivação das chaves simétricas de sessão via KDF.
12. Após o segredo compartilhado gerado pelo ECDH, qual é a próxima etapa no processo?
A) Envio direto do segredo pela rede em texto claro
B) Assinatura digital do segredo com a chave privada
C) Derivação de chaves simétricas de sessão via KDF
D) Encerramento da conexão e reinício do handshake
Resposta correta: C. O segredo compartilhado passa por uma função de derivação de chaves 
(KDF) para gerar as chaves simétricas de sessão que criptografarão o tráfego. 
13. Qual é a principal vantagem da criptografia assimétrica sobre a distribuição de chaves 
simétricas?
A) Elimina a necessidade de um canal seguro prévio para troca de chaves
B) Permite criptografar dados em velocidades superiores a 10 Gbps
C) Reduz o tamanho dos pacotes IP em 50%
D) Não requer o uso de algoritmos de hash
Resposta correta: A. A criptografia assimétrica elimina a necessidade de um canal seguro prévio, 
pois as chaves públicas podem ser distribuídas abertamente.
14. Qual conceito de segurança garante que a compromissão de uma chave de sessão não afete 
sessões anteriores?
A) NAT Traversal
B) Perfect Forward Secrecy
C) Split Tunneling
D) Dead Peer Detection
Resposta correta: B. O Perfect Forward Secrecy (PFS) garante que chaves de sessão 
comprometidas não permitam acessar sessões passadas, sendo um dos objetivos do módulo. 
PARTE PRÁTICA
15. Na topologia do laboratório, qual é o modo de rede do adaptador eth0 em ambas as Vms?
A) Rede Interna (vpn-lab)
B) Bridge Adapter
C) Host-Only Adapter
D) NAT (padrão do VirtualBox)
Resposta correta: D. O adaptador 1 (eth0) é configurado como NAT no VirtualBox para permitir 
acesso à Internet para instalação de pacotes.
16. Qual comando gera o par de chaves pública e privada Curve25519 no WireGuard?
A) sudo openssl genrsa -out privatekey 2048
B) sudo ssh-keygen -t ed25519
C) sudo wg genkey | sudo tee privatekey | sudo wg pubkey | sudo tee publickey
D) sudo ipsec genkey –curve25519
Resposta correta: C. O comando utiliza as ferramentas nativas do WireGuard (wg genkey e wg 
pubkey) para gerar o par de chaves no formato correto.
17. Qual permissão é recomendada para o diretório /etc/wireguard?
A) 700
B) 755
C) 644
D) 777
Resposta correta: A. O diretório deve ter permissão 700 (rwx------), garantindo que apenas o 
proprietário tenha acesso total às chaves.
18. Qual comando cria o alias de loopback (lo:1) simulando a LAN da Filial A (172.16.1.0/24)?
A) sudo ip tunnel add lo:1 mode ipip local 172.16.1.1
B) sudo ip addr add 172.16.1.1/24 dev lo label lo:1
C) sudo ifconfig lo:1 172.16.1.1 netmask 255.255.0.0
D) sudo wg set lo:1 listen-port 51820 private-key /etc/wireguard/privatekey
Resposta correta: B. O comando ip addr add com o parâmetro label lo:1 cria o alias de loopback 
que simula a rede LAN local.
19. Qual é a função do parâmetro PersistentKeepalive = 25 na configuração do WireGuard?
A) Renovar as chaves Curve25519 a cada 25 segundos
B) Limitar a banda do túnel a 25 KB/s
C) Manter sessões NAT/firewall abertas enviando pacotes a cada 25 segundos
D) Encerrar o túnel após 25 segundos de inatividade
Resposta correta: C. O PersistentKeepalive envia pacotes periódicos a cada 25 segundos para 
manter o mapeamento NAT ativo e evitar que firewalls fechem a conexão UDP.
20. Para comprovar visualmente que a criptografia está funcionando, onde o aluno deve capturar 
pacotes com tcpdump?
A) Na interface wg0, onde os pacotes aparecem criptografados
B) Na interface lo:1, onde o tráfego de LAN é encapsulado
C) Na interface NAT (eth0), filtrando pacotes ICMP
D) Na interface física (enp0s8), filtrando UDP porta 51820, onde os dados aparecem ilegíveis 
Resposta correta: D. Capturando na interface física (enp0s8) a porta UDP 51820, o aluno verá 
pacotes UDP criptografados e ilegíveis, provando que a criptografia protege o tráfego na rede 
pública.
```

---

## Módulo 05 — Firewalls de Host: Defesa do Endpoint em Sistemas Operacionais

### Questões de Múltipla Escolha

```
ISG012-05 - Firewalls de Host Defesa do Endpoint em SOs - Teoria - Q de múlt escolha - 
Gabarito
Como obter maior aproveitamento deste objeto de apredizagem:
1. Responder sem olhar o gabarito. Para isso, procurar pelas respostas nos slides da aula 
“ISG012-05 - Firewalls de Host Defesa do Endpoint em Sistemas Operacionais - Teoria”;
2. Após responder TODAS as questões, comparar com o gabarito;
3. Refazer os passos 1 e 2 novamente com todas as questões até obter 100% de acertos de 
uma só vez.
Importante: Embora seja baseado nos slides teóricos e nas atividades práticas, este questionário 
pode conter informações que não constam nesses documentos pois pode incluir algum nível 
detalhamento em relação a eles. Assim, considere as informações aqui contidas como parte 
complementar do conteúdo a ser estudado para as provas. Todo o material distribuído pelo 
professor poderá ser utilizado para a confecção das questões das provas. 
1. No modelo Defense in Depth, qual é o posicionamento correto do firewall de host?
a) Camada de host
b) Camada de aplicação
c) Camada de rede
d) Camada de perímetro
2. A inspeção stateful difere da stateless porque mantém:
a) Apenas headers de pacotes individuais
b) Tabela de conexões ativas (conntrack)
c) Lista negra de endereços MAC
d) Cache ARP estático
3. O Windows Firewall implementa quantos perfis de segurança adaptativos? 
a) 2
b) 4
c) 3
d) 5
4. Qual dos seguintes NÃO é um hook da arquitetura Netfilter no Linux? 
a) PREROUTING
b) INPUT
c) POSTROUTING
d) ROUTING
5. Qual é a ação padrão (default action) para tráfego inbound no Windows Firewall? 
a) Block
b) Allow
c) Drop
d) Pass
6. Qual é o caminho completo padrão do arquivo de log pfirewall.log no Windows? 
a) C:\Windows\Logs
b) C:\Windows\System32\LogFiles\Firewall\pfirewall.log
c) C:\Program Files\Firewall\logs
d) C:\Temp\Firewall
7. Uma vantagem fundamental do nftables sobre o legado iptables é: a) Suportar apenas IPv4
b) Exigir duplicação de regras para IPv6
c) Unificar IPv4/IPv6 em uma única tabela inet
d) Não possuir atomicidade nas operações
8. No Event Viewer do Windows, qual Event ID corresponde a uma conexão bloqueada pelo 
firewall? a) 5156
b) 5150
c) 5155
d) 5157
9. No Netfilter, qual tabela tem como propósito principal permitir ou bloquear pacotes? 
a) filter
b) nat
c) mangle
d) raw
10. Qual perfil do Windows Firewall é ativado quando o computador se autentica em um 
controlador de domínio (AD)? 
a) Public
b) Private
c) Domain
d) Corporate
11. Qual é a política padrão de outbound no Windows Firewall? 
a) Drop all
b) Allow outbound
c) Block all
d) Restrictive
12. A ação avançada "Allow if secure" no Windows Firewall condiciona a permissão de tráfego 
a: a) Ser usuário administrador local
b) Ter o firewall de perímetro desativado
c) Permitir apenas tráfego HTTP criptografado
d) Autenticação e criptografia via IPsec
13. Qual é o nome do framework de filtragem de pacotes integrado ao kernel Linux desde a 
versão 2.4? 
a) Netfilter
b) WinFilter
c) IPChains
d) Windows Defender
14. Qual melhor prática de hardening deve ser aplicada inicialmente no firewall de host? 
a) Allow all inbound para evitar bloqueios acidentais
b) Usar wildcards (*) em portas e endereços para flexibilidade
c) Default deny inbound (bloquear tudo exceto o necessário)
d) Desativar logging para economizar disco
```

### Gabarito Comentado

```
ISG012-05 - Firewalls de Host Defesa do Endpoint em SOs - Teoria - Q de múlt escolha - 
Gabarito
Como obter maior aproveitamento deste objeto de apredizagem:
1. Responder sem olhar o gabarito. Para isso, procurar pelas respostas nos slides da aula 
“ISG012-05 - Firewalls de Host Defesa do Endpoint em Sistemas Operacionais - Teoria”;
2. Após responder TODAS as questões, comparar com o gabarito;
3. Refazer os passos 1 e 2 novamente com todas as questões até obter 100% de acertos de 
uma só vez.
Importante: Embora seja baseado nos slides teóricos e nas atividades práticas, este questionário 
pode conter informações que não constam nesses documentos pois pode incluir algum nível 
detalhamento em relação a eles. Assim, considere as informações aqui contidas como parte 
complementar do conteúdo a ser estudado para as provas. Todo o material distribuído pelo 
professor poderá ser utilizado para a confecção das questões das provas. 
Gabarito
1. No modelo Defense in Depth, qual é o posicionamento correto do firewall de host?
a) Camada de host
b) Camada de aplicação
c) Camada de rede
d) Camada de perímetro
Resposta correta: A — O firewall de host opera na camada de host do modelo Defense in Depth, 
constituindo a última linha de defesa do endpoint, diferente do firewall de perímetro que protege o 
segmento de rede.
2. A inspeção stateful difere da stateless porque mantém:
a) Apenas headers de pacotes individuais
b) Tabela de conexões ativas (conntrack)
c) Lista negra de endereços MAC
d) Cache ARP estático
Resposta correta: B — A inspeção stateful mantém o contexto das conexões em uma tabela de 
estados (conntrack), permitindo diferenciar pacotes de conexões estabelecidas de novas 
conexões ou pacotes inválidos.
3. O Windows Firewall implementa quantos perfis de segurança adaptativos? 
a) 2
b) 4
c) 3
d) 5
Resposta correta: C — São três perfis: Domain (rede corporativa), Private (rede confiável 
doméstica/escritório) e Public (redes não confiáveis como Wi-Fi público).
4. Qual dos seguintes NÃO é um hook da arquitetura Netfilter no Linux? 
a) PREROUTING
b) INPUT
c) POSTROUTING
d) ROUTING
Resposta correta: D — Os hooks do Netfilter são PREROUTING, INPUT, FORWARD, OUTPUT 
e POSTROUTING. "ROUTING" não é um hook oficial do framework.
5. Qual é a ação padrão (default action) para tráfego inbound no Windows Firewall? 
a) Block
b) Allow
c) Drop
d) Pass
Resposta correta: A — A postura padrão do Windows Firewall é bloquear todo tráfego inbound 
não explicitamente permitido, enquanto o outbound geralmente é permitido por padrão.
6. Qual é o caminho completo padrão do arquivo de log pfirewall.log no Windows? 
a) C:\Windows\Logs
b) C:\Windows\System32\LogFiles\Firewall\pfirewall.log
c) C:\Program Files\Firewall\logs
d) C:\Temp\Firewall
Resposta correta: B — O log textual do Windows Firewall está localizado em %SystemRoot%
\System32\LogFiles\Firewall\pfirewall.log, embora esteja desativado por padrão nas versões 
modernas.
7. Uma vantagem fundamental do nftables sobre o legado iptables é: a) Suportar apenas IPv4
b) Exigir duplicação de regras para IPv6
c) Unificar IPv4/IPv6 em uma única tabela inet
d) Não possuir atomicidade nas operações
Resposta correta: C — O nftables utiliza a tabela inet para tratar IPv4 e IPv6 simultaneamente, 
eliminando a necessidade de duplicar regras como no iptables/ip6tables.
8. No Event Viewer do Windows, qual Event ID corresponde a uma conexão bloqueada pelo 
firewall? a) 5156
b) 5150
c) 5155
d) 5157
Resposta correta: D — O Event ID 5157 registra conexões bloqueadas, enquanto 5156 registra 
conexões permitidas e 5150 registra regras bloqueadas.
9. No Netfilter, qual tabela tem como propósito principal permitir ou bloquear pacotes? 
a) filter
b) nat
c) mangle
d) raw
Resposta correta: A — A tabela filter é responsável pela filtragem básica de pacotes (permitir ou 
bloquear), enquanto nat traduz endereços, mangle modifica cabeçalhos e raw trata exceções de 
rastreamento.
10. Qual perfil do Windows Firewall é ativado quando o computador se autentica em um 
controlador de domínio (AD)? 
a) Public
b) Private
c) Domain
d) Corporate
Resposta correta: C — O Domain Profile é ativado automaticamente quando há autenticação no 
Active Directory via DC, aplicando políticas corporativas mais permissivas.
11. Qual é a política padrão de outbound no Windows Firewall? 
a) Drop all
b) Allow outbound
c) Block all
d) Restrictive
Resposta correta: B — O Windows adota por padrão a postura permissiva outbound, onde tudo 
que sai é permitido exceto o explicitamente bloqueado, diferente do Linux que frequentemente usa 
drop-all.
12. A ação avançada "Allow if secure" no Windows Firewall condiciona a permissão de tráfego 
a: a) Ser usuário administrador local
b) Ter o firewall de perímetro desativado
c) Permitir apenas tráfego HTTP criptografado
d) Autenticação e criptografia via IPsec
Resposta correta: D — "Allow if secure" é uma ação avançada que só permite o tráfego se ele 
estiver autenticado e criptografado através do protocolo IPsec (Internet Protocol Security).
13. Qual é o nome do framework de filtragem de pacotes integrado ao kernel Linux desde a 
versão 2.4? 
a) Netfilter
b) WinFilter
c) IPChains
d) Windows Defender
Resposta correta: A — O Netfilter é o framework hook-based integrado ao kernel Linux que serve 
de base para iptables, ip6tables e nftables.
14. Qual melhor prática de hardening deve ser aplicada inicialmente no firewall de host? 
a) Allow all inbound para evitar bloqueios acidentais
b) Usar wildcards (*) em portas e endereços para flexibilidade
c) Default deny inbound (bloquear tudo exceto o necessário)
d) Desativar logging para economizar disco
Resposta correta: C — O princípio do menor privilégio exige iniciar com política default-deny 
para inbound, bloqueando todo tráfego não explicitamente necessário.
```

### Atividades Práticas

```
ISG012-Aulas0506
Atividade ISG012-05 - Firewalls de Host Defesa do Endpoint em Sistemas Operacionais - 
Teoria
1. Qual a diferença fundamental entre um firewall de host e um firewall de perímetro em termos de 
escopo de proteção, e por que ambos são necessários em uma arquitetura de defesa em 
camadas?
2. Explique como o Windows Firewall gerencia a aplicação de políticas diferentes através dos 
perfis Domain, Private e Public, e qual o critério técnico utilizado para determinar qual perfil está 
ativo em uma determinada interface de rede.
3. Por que as regras outbound (de saída) são tão importantes quanto as regras inbound (de 
entrada) na estratégia de segurança de um firewall de host, especialmente no contexto de 
prevenção de ameaças modernas?
4. Descreva a arquitetura do Netfilter no Linux, especificando o papel dos hooks (pontos de 
ancoragem) na pilha de rede e como as tabelas (filter, nat) se relacionam com as chains 
(INPUT , FORWARD, OUTPUT).
5. Quais as vantagens técnicas do nftables em relação ao legado iptables, e como a atomicidade 
na atualização de regras contribui para a segurança do sistema durante modificações de 
política?
6. Compare a abordagem de gerenciamento de firewalls entre Windows e Linux no contexto de 
automação e infraestrutura como código, considerando as ferramentas nativas (PowerShell vs 
bash/nftables) e a integração com sistemas de gerenciamento centralizado.
Atividade ISG012-05 – 06 - Teoria
Disponibilizada após a realização da aula.
Orientações
A atividade deve ter 6 itens devidamente identificados (toda a atividade deve estar em um único arquivo 
com extensão .pdf):
Objetivo: até 2,0;
Atividade ISG012-05 – Teoria: até 3,0;
Atividade ISG012-06 – Teoria até 3,0
Conclusão: até 2,0.
Prazo: 09/06/2026 23:59
Atenção! Não serão consideradas as atividades recebidas após esse prazo.
Caso tenha dúvidas, procure o professor.
```

---

## Módulo 06 — Netfilter / Iptables / Nftables

### Questões de Múltipla Escolha

```
ISG012-06 - Netfilter - Iptables - Nftables - Teoria - Q de múlt escolha 
Como obter maior aproveitamento deste objeto de apredizagem:
1. Responder sem olhar o gabarito. Para isso, procurar pelas respostas nos slides da aula 
“ISG012-06 - Netfilter - Iptables - Nftables - Teoria”;
2. Após responder TODAS as questões, comparar com o gabarito;
3. Refazer os passos 1 e 2 novamente com todas as questões até obter 100% de acertos de 
uma só vez.
Importante: Embora seja baseado nos slides teóricos e nas atividades práticas, este questionário 
pode conter informações que não constam nesses documentos pois pode incluir algum nível 
detalhamento em relação a eles. Assim, considere as informações aqui contidas como parte 
complementar do conteúdo a ser estudado para as provas. Todo o material distribuído pelo 
professor poderá ser utilizado para a confecção das questões das provas. 
1. O Netfilter foi introduzido no kernel Linux a partir de qual versão, substituindo o ipchains?
a) 2.2
b) 2.4
c) 3.13
d) 4.0
2. Qual das seguintes ferramentas é considerada legada (obsoleta) no framework Netfilter?
a) nftables
b) conntrack
c) iptables
d) ipset
3. No nftables, qual família de endereçamento permite tratar IPv4 e IPv6 simultaneamente?
a) ip
b) ip6
c) inet
d) bridge
4. Em qual chain ocorre tipicamente o DNAT (Destination NAT) no fluxo de pacotes?
a) INPUT
b) FORWARD
c) POSTROUTING
d) PREROUTING
5. Qual é a política padrão recomendada durante a configuração remota de um firewall para evitar 
lockout?
a) drop
b) reject
c) accept
d) log
6. O connection tracking (conntrack) armazena as informações de conexões ativas em qual local? 
a) /var/log/conntrack
b) /etc/netfilter/conntrack
c) /proc/net/nf_conntrack
d) /sys/kernel/netfilter
7. Qual ação do nftables descarta o pacote silenciosamente, sem enviar resposta ao originador? 
a) reject
b) drop
c) counter
d) log
8. No diagrama de fluxo de pacotes, qual é o caminho correto para um pacote destinado a um 
serviço local (ex: SSH no próprio host)?
a) PREROUTING → FORWARD → POSTROUTING → SAÍDA
b) INTERFACE → PREROUTING → INPUT → PROCESSO LOCAL → OUTPUT → 
POSTROUTING → SAÍDA
c) INTERFACE → INPUT → PREROUTING → PROCESSO LOCAL → OUTPUT
d) OUTPUT → POSTROUTING → PREROUTING → INPUT
9. Qual dos seguintes estados do connection tracking indica um pacote que não pertence a 
nenhuma conexão conhecida e deve ser descartado?
a) NEW
b) ESTABLISHED
c) RELATED
d) INVALID
10. A técnica de mascaramento dinâmico (masquerade) é utilizada principalmente em qual 
cenário?
a) Publicação de servidor web interno na Internet
b) Redirecionamento de porta 80 para IP interno fixo
c) Compartilhamento de conexão com IP público variável (DHCP)
d) Bloqueio de tráfego de saída em redes corporativas
11. Qual parâmetro no logging do nftables permite definir um identificador textual para facilitar a 
filtragem posterior dos logs?
a) level
b) limit rate
c) prefix
d) group
12. Em termos de arquitetura, qual vantagem o nftables possui sobre o iptables legado?
a) Exige tabelas pré-definidas obrigatórias como raw e security
b) Utiliza máquina virtual de bytecode e permite atualizações atômicas sem interromper o tráfego
c) Mantém sintaxe separada obrigatória para IPv4 e IPv6
d) Não suporta estruturas de dados como sets e maps
13. Qual regra essencial deve estar presente em praticamente todo firewall Linux para garantir 
funcionamento de serviços locais?
a) Bloquear todas as conexões na interface eth0
b) Permitir tráfego na interface de loopback (lo)
c) Habilitar NAT em todas as chains
d) Definir policy drop na chain FORWARD
14. O que caracteriza um firewall stateful em contraste com um stateless?
a) Analisa apenas o cabeçalho MAC dos pacotes
b) Monitora o estado das conexões e diferencia pacotes de sessões estabelecidas de novas 
conexões
c) Oferece maior performance e menor consumo de memória
d) Exige regras apenas na chain POSTROUTING
```

### Gabarito Comentado

```
ISG012-06 - Netfilter - Iptables - Nftables - Teoria - Q de múlt escolha - Gabarito
Como obter maior aproveitamento deste objeto de apredizagem:
1. Responder sem olhar o gabarito. Para isso, procurar pelas respostas nos slides da aula 
“ISG012-06 - Netfilter - Iptables - Nftables - Teoria”;
2. Após responder TODAS as questões, comparar com o gabarito;
3. Refazer os passos 1 e 2 novamente com todas as questões até obter 100% de acertos de 
uma só vez.
Importante: Embora seja baseado nos slides teóricos e nas atividades práticas, este questionário 
pode conter informações que não constam nesses documentos pois pode incluir algum nível 
detalhamento em relação a eles. Assim, considere as informações aqui contidas como parte 
complementar do conteúdo a ser estudado para as provas. Todo o material distribuído pelo 
professor poderá ser utilizado para a confecção das questões das provas. 
Gabarito
1. O Netfilter foi introduzido no kernel Linux a partir de qual versão, substituindo o ipchains?
a) 2.2
b) 2.4
c) 3.13
d) 4.0
Resposta correta: b) O Netfilter substituiu o ipchains a partir do kernel 2.4, oferecendo 
arquitetura mais flexível e escalável.
2. Qual das seguintes ferramentas é considerada legada (obsoleta) no framework Netfilter?
a) nftables
b) conntrack
c) iptables
d) ipset
Resposta correta: c) O iptables é classificado como legado/obsolete, enquanto o nftables é a 
ferramenta moderna e recomendada.
3. No nftables, qual família de endereçamento permite tratar IPv4 e IPv6 simultaneamente?
a) ip
b) ip6
c) inet
d) bridge
Resposta correta: c) A família inet unifica o tratamento de IPv4 e IPv6, eliminando a necessidade 
de regras duplicadas.
4. Em qual chain ocorre tipicamente o DNAT (Destination NAT) no fluxo de pacotes?
a) INPUT
b) FORWARD
c) POSTROUTING
d) PREROUTING
Resposta correta: d) O DNAT e o redirecionamento de portas ocorrem na chain PREROUTING, 
antes da decisão de roteamento.
5. Qual é a política padrão recomendada durante a configuração remota de um firewall para evitar 
lockout?
a) drop
b) reject
c) accept
d) log
Resposta correta: c) Recomenda-se iniciar com policy accept durante a configuração remota e 
migrar para drop apenas após validação completa.
6. O connection tracking (conntrack) armazena as informações de conexões ativas em qual local? 
a) /var/log/conntrack
b) /etc/netfilter/conntrack
c) /proc/net/nf_conntrack
d) /sys/kernel/netfilter
Resposta correta: c) A tabela de conexões é armazenada em /proc/net/nf_conntrack e pode ser 
visualizada com o comando conntrack -L.
7. Qual ação do nftables descarta o pacote silenciosamente, sem enviar resposta ao originador? 
a) reject
b) drop
c) counter
d) log
Resposta correta: b) A ação drop descarta o pacote sem notificação, enquanto reject envia uma 
mensagem ICMP de erro.
8. No diagrama de fluxo de pacotes, qual é o caminho correto para um pacote destinado a um 
serviço local (ex: SSH no próprio host)?
a) PREROUTING → FORWARD → POSTROUTING → SAÍDA
b) INTERFACE → PREROUTING → INPUT → PROCESSO LOCAL → OUTPUT → 
POSTROUTING → SAÍDA
c) INTERFACE → INPUT → PREROUTING → PROCESSO LOCAL → OUTPUT
d) OUTPUT → POSTROUTING → PREROUTING → INPUT
Resposta correta: b) O caminho local completo é: PREROUTING → decisão de roteamento → 
INPUT → Processo Local → OUTPUT → POSTROUTING → Saída. 
9. Qual dos seguintes estados do connection tracking indica um pacote que não pertence a 
nenhuma conexão conhecida e deve ser descartado?
a) NEW
b) ESTABLISHED
c) RELATED
d) INVALID
Resposta correta: d) O estado INVALID representa pacotes malformados ou fora de sequência 
que não correspondem a nenhuma conexão existente.
10. A técnica de mascaramento dinâmico (masquerade) é utilizada principalmente em qual 
cenário?
a) Publicação de servidor web interno na Internet
b) Redirecionamento de porta 80 para IP interno fixo
c) Compartilhamento de conexão com IP público variável (DHCP)
d) Bloqueio de tráfego de saída em redes corporativas
Resposta correta: c) O masquerade é uma forma de SNAT usada quando a interface externa 
possui IP dinâmico, típico de conexões DHCP.
11. Qual parâmetro no logging do nftables permite definir um identificador textual para facilitar a 
filtragem posterior dos logs?
a) level
b) limit rate
c) prefix
d) group
Resposta correta: c) O parâmetro prefix define um texto identificador (ex: "SSH_ATTEMPT:") que 
permite filtrar facilmente com grep ou journalctl.
12. Em termos de arquitetura, qual vantagem o nftables possui sobre o iptables legado?
a) Exige tabelas pré-definidas obrigatórias como raw e security
b) Utiliza máquina virtual de bytecode e permite atualizações atômicas sem interromper o tráfego
c) Mantém sintaxe separada obrigatória para IPv4 e IPv6
d) Não suporta estruturas de dados como sets e maps
Resposta correta: b) O nftables utiliza bytecode eficiente no kernel, suporta sets/maps e permite 
atualizações atômicas via comando nft. 
13. Qual regra essencial deve estar presente em praticamente todo firewall Linux para garantir 
funcionamento de serviços locais?
a) Bloquear todas as conexões na interface eth0
b) Permitir tráfego na interface de loopback (lo)
c) Habilitar NAT em todas as chains
d) Definir policy drop na chain FORWARD
Resposta correta: b) O tráfego de loopback (iif lo accept) deve ser sempre liberado, pois muitos 
serviços locais dependem dele.
14. O que caracteriza um firewall stateful em contraste com um stateless?
a) Analisa apenas o cabeçalho MAC dos pacotes
b) Monitora o estado das conexões e diferencia pacotes de sessões estabelecidas de novas 
conexões
c) Oferece maior performance e menor consumo de memória
d) Exige regras apenas na chain POSTROUTING
Resposta correta: b) O firewall stateful utiliza o módulo conntrack para acompanhar o estado das 
conexões, permitindo regras como ct state established,related accept.
```

---

