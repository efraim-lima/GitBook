# Flashcards — DATAPREV Perfil 5 (Segurança) + Legislação
# Formato Q:/A: — converter com scripts/flashcards_to_anki.py

Q: NIST CSF v1.1 — quais as 5 funções do núcleo, em ordem?
A: Identify, Protect, Detect, Respond, Recover. (Govern só entra na v2.0.)
TAGS: dataprev seguranca nist

Q: NIST SP 800-61 — quais as 4 fases do ciclo de resposta a incidentes?
A: 1) Preparação; 2) Detecção e Análise; 3) Contenção, Erradicação e Recuperação; 4) Atividade Pós-Incidente (lições aprendidas).
TAGS: dataprev seguranca incidentes

Q: ISO/IEC 27001 vs 27002 — qual a diferença?
A: 27001 = requisitos do SGSI (norma certificável). 27002 = código de práticas / controles (guia de implementação).
TAGS: dataprev seguranca iso

Q: ISO/IEC 27005 trata de quê?
A: Gestão de riscos de segurança da informação.
TAGS: dataprev seguranca iso

Q: ISO 31000:2018 trata de quê?
A: Gestão de riscos — diretrizes (genérica, qualquer risco organizacional).
TAGS: dataprev seguranca riscos

Q: ISO 22301:2020 trata de quê?
A: Sistema de gestão de continuidade de negócios (SGCN) — requisitos.
TAGS: dataprev seguranca continuidade

Q: Criptografia simétrica vs assimétrica — chaves e exemplos?
A: Simétrica: mesma chave cifra e decifra (DES, AES) — rápida. Assimétrica: par pública/privada (RSA) — resolve troca de chave e permite assinatura.
TAGS: dataprev seguranca cripto

Q: Para garantir CONFIDENCIALIDADE numa mensagem assimétrica, cifra-se com qual chave?
A: Com a chave PÚBLICA do destinatário (só a privada dele decifra).
TAGS: dataprev seguranca cripto

Q: Para garantir AUTENTICIDADE/NÃO REPÚDIO (assinatura), usa-se qual chave?
A: A chave PRIVADA do remetente (qualquer um verifica com a pública dele).
TAGS: dataprev seguranca cripto

Q: Diferença entre IDS e IPS?
A: IDS detecta e alerta (passivo). IPS detecta e bloqueia/previne em linha (ativo).
TAGS: dataprev seguranca soc

Q: O que faz um SIEM?
A: Coleta e correlaciona logs de várias fontes, gera alertas e centraliza investigação de eventos de segurança.
TAGS: dataprev seguranca soc

Q: O que é SOAR?
A: Security Orchestration, Automation and Response — orquestra e automatiza respostas (playbooks) integrando ferramentas de segurança.
TAGS: dataprev seguranca soc

Q: O que é XDR?
A: Extended Detection and Response — detecção/resposta estendida correlacionando endpoint, rede, e-mail e nuvem em uma plataforma.
TAGS: dataprev seguranca soc

Q: O que é DLP?
A: Data Loss Prevention — previne vazamento/exfiltração de dados sensíveis (monitora e bloqueia saída não autorizada).
TAGS: dataprev seguranca soc

Q: O que é CASB?
A: Cloud Access Security Broker — intermediário que aplica políticas de segurança entre usuários e serviços de nuvem.
TAGS: dataprev seguranca nuvem

Q: MITRE ATT&CK — o que é "Lateral Movement"?
A: Tática de mover-se de um host comprometido para outros hosts na rede interna.
TAGS: dataprev seguranca mitre

Q: STRIDE — o que significa cada letra?
A: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege. Modelagem de ameaças da Microsoft.
TAGS: dataprev seguranca ameacas

Q: LGPD — o que são dados pessoais sensíveis?
A: Origem racial/étnica, convicção religiosa, opinião política, filiação sindical, dado sobre saúde/vida sexual, dado genético ou biométrico.
TAGS: dataprev legislacao lgpd

Q: LGPD — o consentimento é a única base legal para tratar dados?
A: Não. Há 10 bases legais (art. 7º): consentimento, obrigação legal, execução de contrato, exercício de direitos, proteção da vida, tutela da saúde, legítimo interesse, etc.
TAGS: dataprev legislacao lgpd

Q: Lei 12.737/2012 (art. 2º) tipifica qual crime?
A: Invasão de dispositivo informático (Lei "Carolina Dieckmann").
TAGS: dataprev legislacao penal

Q: Lei 12.527/2011 é conhecida como?
A: LAI — Lei de Acesso à Informação (regulamentada pelos Dec. 7.724 e 7.845).
TAGS: dataprev legislacao lai

Q: Lei 12.965/2014 é conhecida como?
A: Marco Civil da Internet (princípios, garantias, direitos e deveres no uso da internet).
TAGS: dataprev legislacao marcocivil

Q: TCP/IP — cite protocolos da camada de aplicação cobrados no edital.
A: FTP, SSH, DNS, SMTP, POP, IMAP, HTTP, HTTPS, SSL, RDP, DHCP, SNMP.
TAGS: dataprev seguranca redes

Q: IPSec VPN opera em qual camada? E SSL VPN?
A: IPSec = camada de rede (túnel de todo o tráfego IP). SSL/TLS VPN = camada de aplicação/transporte, acesso a serviços via navegador.
TAGS: dataprev seguranca redes

Q: SAST vs DAST?
A: SAST analisa o código-fonte estático (sem executar). DAST testa a aplicação em execução (caixa-preta, runtime).
TAGS: dataprev seguranca devsec
