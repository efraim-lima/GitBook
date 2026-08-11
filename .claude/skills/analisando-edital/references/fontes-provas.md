# Onde encontrar editais e provas anteriores (PDF)

Referência de fontes e estratégias de busca para localizar o edital vigente e
provas passadas de concursos públicos brasileiros. Sempre preferir o **PDF
oficial** e registrar a URL de origem no manifesto (`provas-anteriores/README.md`).

## Estratégia de busca

1. **Identificar a banca** no edital (Cebraspe/CESPE, FGV, FCC, Vunesp, IBFC,
   Quadrix, Instituto AOCP, IADES, Cesgranrio, Fundatec, IBADE...). A banca é o
   melhor filtro: o estilo de questão se repete por banca.
2. Buscar por: `"<órgão>" "<cargo>" prova <banca> <ano> filetype:pdf`.
3. Buscar também o **caderno de questões + gabarito** e, quando existir, o
   **caderno de respostas/padrão de resposta** (útil para discursivas).
4. Para provas muito recentes, o site da própria banca costuma ter os cadernos
   por alguns meses após a aplicação.

## Sites da banca (fonte primária — provas + gabaritos oficiais)

- Cebraspe (ex-CESPE): `cebraspe.org.br` → "Concursos encerrados"
- FGV: `fgv.br/concursos` (ou `conhecimento.fgv.br`)
- FCC: `concursosfcc.com.br`
- Vunesp: `vunesp.com.br`
- Cesgranrio: `cesgranrio.org.br`
- IBFC: `ibfc.org.br` · Quadrix: `quadrix.org.br` · AOCP: `institutoaocp.org.br`

## Agregadores (muitas provas em um lugar)

- **PCI Concursos** — `pciconcursos.com.br/provas` — grande acervo de PDFs por
  órgão/banca/ano, geralmente com gabarito.
- **QConcursos** — `qconcursos.com` — questões separadas por assunto/banca
  (bom para simulado por tópico; exige conta).
- **Portais oficiais do órgão** (Diário Oficial / seção "Concursos") para o
  edital vigente e retificações.

## Boas práticas ao salvar

- Nomear o arquivo de forma previsível:
  `AAAA_<banca>_<orgao>_<cargo>.pdf` (ex.: `2022_cebraspe_pf_agente.pdf`).
- Salvar em `Concursos/<slug>/provas-anteriores/`.
- Registrar cada arquivo na tabela do `provas-anteriores/README.md` com a URL
  de origem, para rastreabilidade.
- Preferir provas da **mesma banca e cargo**; em segundo lugar, mesma banca,
  cargos afins (o estilo de cobrança se mantém).

## Verificação de conteúdo

Antes de tratar um PDF como fonte confiável, confirmar que ele contém texto
real de prova (e não um resumo/anúncio). Checar rapidamente cabeçalho, banca,
ano e presença de gabarito.
