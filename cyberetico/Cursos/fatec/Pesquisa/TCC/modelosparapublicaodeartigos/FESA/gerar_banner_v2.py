# -*- coding: utf-8 -*-
"""Gera banner SIMAC v2 (versao densa) a partir do artigo submetido.
Fundo oficial VIII SIMAC + conteudo 2 colunas + tabelas nativas.
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

S = "/tmp/claude-1000/-home-efraim-Documents-Github-GitBook/32992106-ea5e-4dc4-9742-b1959e647a7e/scratchpad"
BG = os.path.join(S, "oldbanner_x/ppt/media/image1.jpg")      # fundo oficial VIII SIMAC
ARCH = os.path.join(S, "oldbanner_x/ppt/media/image2.png")    # diagrama arquitetura
OUT = os.path.join(S, "banner_v2.pptx")

# cores
AZUL = RGBColor(0x00, 0x3D, 0x7A)
AZUL2 = RGBColor(0x1F, 0x4E, 0x79)
PRETO = RGBColor(0x1A, 0x1A, 0x1A)
BRANCO = RGBColor(0xFF, 0xFF, 0xFF)
CINZA = RGBColor(0xEF, 0xF2, 0xF7)

W_IN, H_IN = 22.84, 47.24

prs = Presentation()
prs.slide_width = Inches(W_IN)
prs.slide_height = Inches(H_IN)
slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank

# fundo full-slide
slide.shapes.add_picture(BG, 0, 0, width=Inches(W_IN), height=Inches(H_IN))

# ---------- helpers ----------
def est_lines(text, width_in, size_pt):
    cpi = 128.0 / size_pt          # chars por polegada aprox (conservador)
    per_line = max(1, int(width_in * cpi))
    n = 0
    for para in text.split("\n"):
        if not para.strip():
            n += 1
            continue
        n += max(1, -(-len(para) // per_line))  # ceil
    return n

def line_h(size_pt):
    return size_pt * 1.24 / 72.0

def add_text(x, w, y, text, size, bold=False, color=PRETO, align=PP_ALIGN.LEFT,
             italic=False, space_after=6, line_spacing=1.05):
    lines = est_lines(text, w, size)
    h = lines * line_h(size) + 0.30
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    paras = text.split("\n")
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        p.space_after = Pt(space_after)
        r = p.add_run()
        r.text = para
        f = r.font
        f.size = Pt(size)
        f.bold = bold
        f.italic = italic
        f.name = "Calibri"
        f.color.rgb = color
    return y + h

def add_header(x, w, y, text):
    y2 = add_text(x, w, y, text, 30, bold=True, color=AZUL, space_after=2, line_spacing=1.0)
    # linha sob o header
    ln = slide.shapes.add_shape(1, Inches(x), Inches(y2 - 0.02), Inches(w), Pt(2.5))
    ln.fill.solid(); ln.fill.fore_color.rgb = AZUL
    ln.line.fill.background()
    return y2 + 0.12

def add_table(x, w, y, headers, rows, col_w=None, fsize=15, hsize=15,
              row_h=0.42, title=None, fonte=None):
    if title:
        y = add_text(x, w, y, title, 17, bold=True, color=AZUL2, space_after=2)
    nr = len(rows) + 1
    nc = len(headers)
    th = nr * row_h
    gx = slide.shapes.add_table(nr, nc, Inches(x), Inches(y), Inches(w), Inches(th))
    tbl = gx.table
    tbl.first_row = True
    if col_w:
        tot = sum(col_w)
        for i, cw in enumerate(col_w):
            tbl.columns[i].width = Inches(w * cw / tot)
    # header
    for j, htxt in enumerate(headers):
        c = tbl.cell(0, j)
        c.fill.solid(); c.fill.fore_color.rgb = AZUL
        c.vertical_anchor = MSO_ANCHOR.MIDDLE
        c.margin_top = Pt(2); c.margin_bottom = Pt(2)
        c.margin_left = Pt(5); c.margin_right = Pt(5)
        tf = c.text_frame; tf.word_wrap = True
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = htxt
        r.font.size = Pt(hsize); r.font.bold = True
        r.font.color.rgb = BRANCO; r.font.name = "Calibri"
    # body
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            c = tbl.cell(i + 1, j)
            c.fill.solid()
            c.fill.fore_color.rgb = CINZA if i % 2 == 0 else BRANCO
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            c.margin_top = Pt(2); c.margin_bottom = Pt(2)
            c.margin_left = Pt(5); c.margin_right = Pt(5)
            tf = c.text_frame; tf.word_wrap = True
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER if j > 0 else PP_ALIGN.LEFT
            r = p.add_run(); r.text = str(val)
            r.font.size = Pt(fsize); r.font.name = "Calibri"
            r.font.color.rgb = PRETO
    y = y + th
    if fonte:
        y = add_text(x, w, y + 0.02, fonte, 13, italic=True, color=AZUL2, space_after=4)
    return y + 0.1

# ---------- TITULO / AUTORES ----------
TITLE = ("Recomendacoes de seguranca para o uso do MCP AI integrado "
         "a plataforma de orquestracao de containers").replace("Recomendacoes","Recomendações").replace("seguranca","segurança").replace("integrado a","integrado à").replace("orquestracao","orquestração")
# usar texto correto direto:
TITLE = "Recomendações de segurança para o uso do MCP AI integrado à plataforma de orquestração de containers"
AUTORES = ("Arthur de Carvalho Batista  •  Efraim de Almeida Lima  •  "
           "Felipe Moya Figueiredo  •  Henrique Rodrigues Gonçalves")
ORIENT = "Orientador: Prof. Dr. Fábio Henrique Cabrini"
INST = "Fatec São Caetano do Sul – Antônio Russo (Centro Paula Souza)"

ytop = 10.4
ytop = add_text(1.2, 20.4, ytop, TITLE, 46, bold=True, color=AZUL,
                align=PP_ALIGN.CENTER, space_after=6, line_spacing=1.0)
ytop = add_text(1.2, 20.4, ytop, AUTORES, 23, bold=True, color=PRETO,
                align=PP_ALIGN.CENTER, space_after=2)
ytop = add_text(1.2, 20.4, ytop, ORIENT + "\n" + INST, 19, color=PRETO,
                align=PP_ALIGN.CENTER, space_after=2, line_spacing=1.0)

# ---------- COLUNAS ----------
LX, LW = 1.2, 9.9
RX, RW = 11.75, 9.9
yL = 14.9
yR = 14.9

# ===== LEFT =====
RESUMO = ("O uso de agentes de Inteligência Artificial (IA) conectados a ferramentas externas por "
    "meio do Model Context Protocol (MCP) amplia a interoperabilidade, mas introduz riscos de "
    "segurança relacionados à autenticação, autorização e execução de instruções maliciosas. "
    "Este trabalho tem por objetivo elaborar e validar boas práticas de segurança para "
    "implementações MCP integradas a uma plataforma de orquestração de containers. O marco "
    "teórico sustenta-se nos princípios de defesa em camadas, no gerenciamento de identidades "
    "digitais e nas recomendações da OWASP para aplicações baseadas em modelos de linguagem. A "
    "metodologia combina revisão bibliográfica, modelagem de ameaças pelo framework STRIDE e "
    "experimentação controlada com o servidor AgentK em três grupos comparáveis: baseline, "
    "hardening e hardening com guardrail semântico. Os resultados indicam redução média de 89% "
    "na pontuação de risco dos vetores avaliados, além de retenção de 95,65% dos prompts "
    "inadequados pelo filtro semântico. Conclui-se que a aplicação de múltiplas camadas de "
    "segurança contribui de forma relevante para a mitigação de riscos em ambientes baseados em "
    "agentes de IA, consolidada em um guia de recomendações aplicável a desenvolvedores e "
    "administradores de plataformas de orquestração.")
KW = ("Palavras-chave: Agentes de IA. Segurança. Controle de acesso. Prompt injection. MCP.")

yL = add_header(LX, LW, yL, "Resumo")
yL = add_text(LX, LW, yL, RESUMO, 18, color=PRETO, align=PP_ALIGN.JUSTIFY, space_after=4)
yL = add_text(LX, LW, yL, KW, 18, bold=True, color=AZUL2, align=PP_ALIGN.JUSTIFY, space_after=6)

INTRO1 = ("O uso de agentes de IA deixou de se restringir a interfaces de conversação e passou a "
    "executar ações sobre ferramentas, APIs e bancos de dados. O Model Context Protocol (MCP), "
    "divulgado pela Anthropic em 2024, padroniza a integração entre agentes, LLMs e recursos "
    "externos (ANTHROPIC, 2025), sendo comparado a um “USB-C para agentes de IA”. Um servidor "
    "MCP mal configurado permite exposição de portas, autenticação fraca, tráfego sem "
    "criptografia e ausência de rastreabilidade; SIMAN (s.d.) lista diversas CVEs associadas ao "
    "ecossistema, com a autenticação como falha recorrente (HASAN et al., 2025).")
INTRO2 = ("Como nenhum mecanismo isolado mitiga todos os riscos, a defesa em camadas combina "
    "controles independentes e complementares (NIST, 2017; OWASP, 2023). Três componentes a "
    "sustentam: o Keycloak (IdP com RBAC), o NGINX (proxy reverso e terminação TLS) e um "
    "Guardrail Gateway, apoiado na LLM local Qwen 2.5, que classifica semanticamente os prompts "
    "antes de alcançarem o orquestrador Kubernetes. O objetivo é elaborar e validar, em ambiente "
    "controlado, recomendações de segurança para o uso do MCP integrado a uma plataforma de "
    "orquestração de containers.")
yL = add_header(LX, LW, yL, "Introdução")
yL = add_text(LX, LW, yL, INTRO1 + "\n" + INTRO2, 18, align=PP_ALIGN.JUSTIFY, space_after=6)

yL = add_table(LX, LW, yL,
    ["CVE ID", "Produto", "Vetor de ataque", "Severidade"],
    [["CVE-2025-65720", "GPT Researcher", "UI injection / reverse shell", "Crítica"],
     ["CVE-2026-30623", "LiteLLM", "RCE autenticado via config JSON", "Crítica"],
     ["CVE-2026-30625", "Upsonic", "Allowlist bypass via npx/npm", "Alta"],
     ["CVE-2026-30615", "Windsurf", "Prompt injection zero-click p/ RCE", "Crítica"],
     ["CVE-2026-26015", "DocsGPT", "Substituição de transporte (MITM)", "Crítica"]],
    col_w=[1.5, 1.2, 2.6, 1.0], fsize=14, hsize=14, row_h=0.5,
    title="Tabela 1 – Exemplos de CVEs associadas ao ecossistema MCP",
    fonte="Fonte: SIMAN (s.d.)")

# Metodologia (coluna ESQUERDA)
METO1 = ("Pesquisa aplicada, de abordagem qualitativa, combinando revisão bibliográfica, modelagem "
    "de ameaças pelo framework STRIDE e experimentação controlada. O ambiente utilizou o servidor "
    "AgentK (MCP + Kubernetes/Minikube) sobre Ubuntu Server 24.04 LTS (4 GB RAM, 40 GB), "
    "orquestrado por Docker. Definiram-se três grupos comparáveis em clones da máquina virtual: "
    "(A) baseline — portas expostas, sem TLS e sem guardrail; (B) hardening — restrição de portas, "
    "proxy reverso, autenticação centralizada e RBAC; (C) guardrail — grupo B acrescido do gateway "
    "de classificação semântica, reautenticação para ações de risco e auditoria ampliada.")
METO2 = ("A mitigação do Controle de Acesso Quebrado (CWE-284) removeu o mapeamento de portas do "
    "agentk-client, restringindo-o à rede interna; o tráfego externo passou a ser intermediado pelo "
    "NGINX na porta 443 (certificados RSA 4096 bits, hash SHA-512). O Keycloak usou realm dedicado "
    "com grupos users e admins. O módulo PromptValidator (Java) encaminha cada instrução à Qwen 2.5, "
    "que a classifica em SAFE, SUSPECT, UNSAFE, RISKY e UNCERTAIN; prompts RISKY exigem "
    "reautenticação administrativa via Keycloak.")
yL = add_header(LX, LW, yL, "Metodologia")
yL = add_text(LX, LW, yL, METO1 + "\n" + METO2, 18, align=PP_ALIGN.JUSTIFY, space_after=6)

# ===== RIGHT =====
# figura arquitetura
fig_w = 9.9
fig_h = fig_w * (833.0/1442.0)  # proporção da imagem
pic = slide.shapes.add_picture(ARCH, Inches(RX), Inches(yR), width=Inches(fig_w))
pic.line.color.rgb = AZUL
pic.line.width = Pt(1.0)
yR = yR + Emu(pic.height).inches
yR = add_text(RX, RW, yR + 0.03,
    "Figura 1 – Diagrama da implementação das soluções propostas. Fonte: elaborado pelos autores (2026).",
    14, italic=True, color=AZUL2, space_after=6)

RES1 = ("A comparação entre os ambientes original e mitigado evidenciou redução consistente da "
    "superfície de ataque. Portas antes em 0.0.0.0 passaram a operar restritas ao loopback; o acesso "
    "ao AgentK passou a exigir login via Keycloak; e o tráfego, antes interceptável em texto claro, "
    "passou a fluir sob TLS 1.3. Aplicou-se uma métrica inspirada no CVSS (0–10): o score médio de "
    "risco caiu de 8,1 para 0,9 — redução de 89% (Tabela 2).")
RES2 = ("O filtro semântico, avaliado sobre 391 frases nas cinco categorias, reteve 95,65% dos "
    "prompts inadequados. Por ser um classificador de poucos parâmetros (0,5 bilhão), o valor não "
    "deve ser extrapolado como taxa universal; o objetivo foi demonstrar a utilidade prática da "
    "camada adicional. A validação em produção (AWS m7i-flex.large, Ubuntu 24.04) confirmou os cinco "
    "vereditos fora do laboratório, com OAuth Google no lugar do gerenciamento manual de usuários. "
    "Os resultados consolidaram um guia de recomendações (GP-01 a GP-11) em três níveis: "
    "obrigatórias, recomendadas e avançadas.")
yR = add_header(RX, RW, yR, "Resultados e discussão")
yR = add_text(RX, RW, yR, RES1 + "\n" + RES2, 18, align=PP_ALIGN.JUSTIFY, space_after=6)

yR = add_table(RX, RW, yR,
    ["Vulnerabilidade", "Antes", "Depois", "Redução"],
    [["Portas expostas na rede", "8.5", "1.0", "88%"],
     ["Acesso sem autenticação", "9.5", "1.0", "89%"],
     ["Tráfego em texto plano", "8.0", "0.5", "94%"],
     ["Ausência de controle de identidade", "9.0", "1.5", "83%"],
     ["Ausência de auditoria", "6.5", "1.0", "85%"],
     ["Média geral", "8.1", "0.9", "89%"]],
    col_w=[3.0, 0.8, 0.8, 1.0], fsize=15, hsize=15, row_h=0.46,
    title="Tabela 2 – Severidade antes e depois das mitigações (escala CVSS adaptada, 0–10)",
    fonte="Fonte: elaborado pelos autores (2026)")

CF1 = ("A prova de conceito no AgentK confirmou a hipótese: a aplicação incremental de controles "
    "reduziu a superfície de ataque de forma mensurável. Proxies reversos com TLS 1.3 neutralizaram "
    "a interceptação de tráfego; o Keycloak consolidou RBAC via fluxo OIDC; e o Guardrail Gateway "
    "com Qwen 2.5 bloqueou prompt injection e comandos destrutivos por análise semântica de "
    "intenções. A principal entrega é um guia de boas práticas aplicável a desenvolvedores e "
    "administradores de plataformas de orquestração de containers.")
CF2 = ("Como limitações, não houve experimento específico de tool poisoning nem medição de latência "
    "sob carga. Trabalhos futuros incluem Keycloak em produção com PostgreSQL, validação de tokens "
    "via JWK, certificados Let's Encrypt e avaliação de rate limiting e WAF integrados ao NGINX.")
yR = add_header(RX, RW, yR, "Considerações finais")
yR = add_text(RX, RW, yR, CF1 + "\n" + CF2, 18, align=PP_ALIGN.JUSTIFY, space_after=6)

REFS = ("ANTHROPIC. Model Context Protocol. 2025.  •  HASAN, M. M. et al. MCP at First Glance. arXiv, "
    "2025.  •  HOU, X. et al. MCP: landscape, security threats and future directions. arXiv, 2025.  •  "
    "NIST. Digital Identity Guidelines (SP 800-63B). 2017.  •  OWASP. Top 10 for LLM Applications. "
    "2023.  •  QWEN TEAM. Qwen2.5. 2024.  •  SIMAN, M. The Architectural Flaw at the Core of "
    "Anthropic's MCP. OX Security, s.d.  •  TIPTON, H.; KRAUSE, M. Information Security Management "
    "Handbook. 6. ed. CRC Press, 2012.")
yR = add_header(RX, RW, yR, "Referências")
yR = add_text(RX, RW, yR, REFS, 14, align=PP_ALIGN.JUSTIFY, space_after=4, line_spacing=1.0)

prs.save(OUT)
print("saved", OUT)
print("fim coluna ESQ y =", round(yL, 2), "| fim coluna DIR y =", round(yR, 2),
      "| limite ~42.5")
