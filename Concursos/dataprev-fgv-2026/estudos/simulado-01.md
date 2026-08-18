# Simulado 01 — DATAPREV 2026 · Perfil 5 (Segurança Cibernética)

Estilo **FGV**: 5 alternativas, uma correta, caso concreto e distratores
plausíveis. 10 questões do Módulo Específico. Gabarito comentado no fim — não
espie antes. Tempo sugerido: ~15 min.

---

**1.** Um analista da DATAPREV precisa garantir **confidencialidade** e
**não repúdio** no envio de um relatório a um órgão externo. Qual combinação
atende aos dois requisitos simultaneamente?

- (A) Cifrar o relatório com a chave pública do destinatário apenas.
- (B) Cifrar com a chave pública do destinatário e assinar com a chave privada do remetente.
- (C) Aplicar função hash SHA-256 no relatório e enviar o digest.
- (D) Assinar com a chave pública do remetente.
- (E) Cifrar com a chave privada do remetente apenas.

**2.** Segundo o **NIST Cybersecurity Framework v1.1**, as funções do núcleo
(Framework Core) são, na ordem:

- (A) Governar, Identificar, Proteger, Detectar, Responder.
- (B) Identificar, Proteger, Detectar, Responder, Recuperar.
- (C) Prevenir, Detectar, Conter, Erradicar, Recuperar.
- (D) Identificar, Avaliar, Tratar, Monitorar, Comunicar.
- (E) Planejar, Fazer, Checar, Agir, Melhorar.

**3.** Durante um incidente, a equipe isola a máquina infectada da rede para
impedir a propagação do ransomware antes de remover o malware. Conforme o
**NIST SP 800-61**, essa ação pertence à fase de:

- (A) Preparação.
- (B) Detecção e Análise.
- (C) Contenção, Erradicação e Recuperação.
- (D) Atividade Pós-Incidente.
- (E) Lições Aprendidas.

**4.** A norma que estabelece o **código de práticas com os controles** de
segurança da informação (a ser implementados a partir dos requisitos do SGSI) é:

- (A) ABNT NBR ISO/IEC 27001:2022.
- (B) ABNT NBR ISO/IEC 27002:2022.
- (C) ABNT NBR ISO/IEC 27005:2019.
- (D) ABNT NBR ISO 31000:2018.
- (E) ABNT NBR ISO 22301:2020.

**5.** Uma solução de segurança correlaciona logs de firewall, EDR e servidores,
gera alertas e permite investigação centralizada de eventos. Trata-se de:

- (A) DLP.
- (B) CASB.
- (C) SIEM.
- (D) WAF.
- (E) IPS.

**6.** No **MITRE ATT&CK**, a movimentação de um atacante de um host já
comprometido para outros hosts da rede interna é classificada como a tática de:

- (A) Initial Access.
- (B) Persistence.
- (C) Privilege Escalation.
- (D) Lateral Movement.
- (E) Exfiltration.

**7.** Sobre a **LGPD** (Lei 13.709/2018), assinale a alternativa correta:

- (A) Aplica-se apenas a dados tratados por meios digitais.
- (B) O consentimento é a única base legal admitida para tratamento de dados pessoais.
- (C) Dado pessoal sensível inclui dado sobre origem racial, convicção religiosa e dado genético ou biométrico.
- (D) A anonimização torna o dado pessoal sensível, sujeitando-o a regras mais rígidas.
- (E) O encarregado (DPO) é obrigatoriamente um advogado inscrito na OAB.

**8.** Um protocolo da camada de aplicação do modelo TCP/IP, usado para
**gerência de redes** e coleta de métricas de dispositivos, é o:

- (A) RMON.
- (B) SNMP.
- (C) ICMP.
- (D) ARP.
- (E) RDP.

**9.** No contexto de VPN, a diferença central entre **IPSec VPN** e **SSL VPN**
é que, tipicamente:

- (A) IPSec opera na camada de aplicação e SSL na camada de rede.
- (B) IPSec exige apenas um navegador, enquanto SSL exige cliente dedicado.
- (C) IPSec atua na camada de rede (túnel de todo o tráfego IP) e SSL/TLS tipicamente na camada de aplicação/transporte (acesso a serviços via navegador).
- (D) Ambas operam exclusivamente na camada física.
- (E) SSL VPN não oferece criptografia, apenas autenticação.

**10.** A técnica de **modelagem de ameaças** que classifica ameaças em
Spoofing, Tampering, Repudiation, Information disclosure, Denial of service e
Elevation of privilege é o:

- (A) DREAD.
- (B) STRIDE.
- (C) PASTA.
- (D) OCTAVE.
- (E) Cyber Kill Chain.

---

## Gabarito comentado

1. **B.** Cifrar com a **pública do destinatário** garante confidencialidade
   (só ele decifra com a privada). Assinar com a **privada do remetente** dá
   autenticidade + não repúdio. (A) só confidencialidade; (C) só integridade;
   (E) qualquer um decifra com a pública → sem sigilo.
2. **B.** Identify, Protect, Detect, Respond, Recover. "Govern" é do CSF **2.0**;
   o edital pede a **v1.1** → não inclui Govern. (E) é PDCA. Pegadinha clássica.
3. **C.** Isolar/conter é **Contenção, Erradicação e Recuperação** no ciclo de 4
   fases do SP 800-61. (A) é preparo prévio; (B) é identificar/analisar.
4. **B.** **27002** = controles/código de práticas. **27001** = requisitos do
   SGSI (certificável). Não confundir: é o erro mais cobrado.
5. **C.** Correlação de logs + alertas + investigação central = **SIEM**. DLP
   previne vazamento; CASB media acesso à nuvem; WAF protege aplicação web.
6. **D.** **Lateral Movement**. Exfiltration seria roubo/saída de dados.
7. **C.** Dado sensível inclui origem racial/étnica, religião, biometria,
   genética etc. (A) errado: abrange também meio físico; (B) há 10 bases legais;
   (D) anonimizado sai do escopo; (E) DPO não precisa ser advogado.
8. **B.** **SNMP**. RMON complementa monitoração mas o protocolo de gerência é
   o SNMP; ICMP/ARP são de rede, RDP é acesso remoto.
9. **C.** IPSec = camada de rede (túnel IP completo); SSL/TLS VPN = acesso a
   aplicações via navegador (camada superior). (B) inverte os fatos.
10. **B.** **STRIDE** (Microsoft). DREAD é priorização de risco; PASTA e OCTAVE
    são metodologias; Kill Chain é fases de ataque.

**Placar:** ____/10 · Anote os erros no cronograma para revisão em 24h.
