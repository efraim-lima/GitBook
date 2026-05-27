---
AGENTE: DESIRE
TAREFA: Criar apresentação PowerPoint (TCC MCP Segurança)
STATUS: ✅ CONCLUÍDA
DATA: 2026-05-27
---

## SUMÁRIO PARA ALFRED

### Tarefa Delegada
Gerar arquivo de apresentação PowerPoint (.pptx) com 15 slides profissionais baseado no roteiro detalhado de TCC sobre "Recomendações de Segurança para o Uso do MCP AI Integrado à Plataforma de Orquestração de Containers", implementando todos os elementos visuais, dados numéricos e especificações de design conforme mapeado no roteiro.

### Arquivos Criados/Modificados

1. **APRESENTACAO_TCC_MCP_SEGURANCA.pptx** (71 KB)
   - Caminho: `fatec/Pesquisa/TCC/APRESENTACAO_TCC_MCP_SEGURANCA.pptx`
   - Formato: Microsoft PowerPoint 2007+
   - Status: ✅ Validado e funcional

2. **criar_apresentacao.py** (19 KB)
   - Caminho: `fatec/Pesquisa/TCC/criar_apresentacao.py`
   - Função: Script de automação para regenerar apresentação
   - Reutilizável: Sim (para atualizações futuras)

3. **RELATORIO_IMPLEMENTACAO_APRESENTACAO.md**
   - Documentação completa de implementação
   - Especificações de cada slide
   - Validações realizadas

### Resumo (1 Parágrafo)

Apresentação PowerPoint profissional foi gerada com sucesso, contendo integralmente os 15 slides especificados no roteiro, implementando paleta de cores corporativa exata (Azul #003D7A, Laranja #FF6B35, Verde #2DA44F, Vermelho #C91E1E), tipografia profissional (Arial Bold 54pt para títulos, Calibri 24pt para body), e todos os dados numéricos críticos do projeto TCC: redução CVSS de 8.1 para 0.9 (89%), taxa de bloqueio de 95.65%, 391 prompts testados, 3 camadas de defesa com tecnologias mapeadas (Nginx, Keycloak, Qwen 2.5). Arquivo pronto para apresentação em defesa de TCC, com speaker notes completas em todos os slides e design profissional mantendo rigorosa integridade visual do template corporativo.

### Campos Atualizados / Mapeamento

#### Slide 1: Capa
- Título: "RECOMENDAÇÕES DE SEGURANÇA PARA O USO DO MCP AI INTEGRADO À PLATAFORMA DE ORQUESTRAÇÃO DE CONTAINERS"
- Autores: Placeholder para nomes
- Instituição: FATEC São Paulo | CPS - Centro Paula Souza
- Data: Defesa 27 de Maio de 2026
- Speaker Notes: ✅ Presentes

#### Slide 2: Contexto
- Crescimento MCP: +340% em buscas, +89% em adoção
- Cronograma: 2023-2026 (primeiros agentes → integração Kubernetes)
- Fonte: Dados do roteiro
- Speaker Notes: ✅ Presentes (1 min 20 seg)

#### Slide 3: Vulnerabilidades
- Slide: 3 cards (Crítica CVSS 9.8, Alto 7.5, Alto 7.3)
- Score Agregado: 8.1 (ELEVADO)
- CVE Exemplo: CVE-2025-65720
- Speaker Notes: ✅ Presentes

#### Slide 4: Objetivos
- Objetivo Geral: Defense-in-Depth para redução de superfície de ataque
- Hipótese: CVSS 8.1 → ≤1.0, Bloqueio ≥95%
- Objetivos Específicos: 5 items numerados
- Speaker Notes: ✅ Presentes

#### Slide 5: Metodologia
- Framework: STRIDE (6 categorias)
- Grupos Teste: A (Baseline), B (Hardening), C (Guardrail)
- Ambiente: Ubuntu Server + Docker Compose
- Speaker Notes: ✅ Presentes

#### Slide 6: Arquitetura Antes/Depois
- Antes: CVSS 8.1, sem proteção, RCE direto
- Depois: CVSS 0.9, 3 camadas, isolamento total
- Redução: 89%
- Speaker Notes: ✅ Presentes

#### Slide 7: Camada 1 - Nginx
- Tecnologia: Nginx Proxy Reverso + TLS 1.3
- Rate Limiting: 100 req/seg
- CVSS Parcial: 9.8 → 7.5 (-24%)
- Redução Atacantes: 65%
- Speaker Notes: ✅ Presentes

#### Slide 8: Camada 2 - Keycloak
- Protocolo: OAuth2
- RBAC Roles: 4 (admin, user, guest, bot_agent_b)
- TTL JWT: 1 hora
- CVSS Parcial: 7.5 → 6.8 (-9%)
- Speaker Notes: ✅ Presentes

#### Slide 9: Camada 3 - Guardrail
- Modelo: Qwen 2.5 (7B parâmetros)
- Latência: <100ms (média 76ms)
- Classificações: SAFE (≥85%), RISKY (60-84%), UNSAFE (<60%)
- Taxa Acurácia: 95.65%
- False Negatives: 17 em 391 (4.35%)
- CVSS Final: 6.8 → 0.9 (-86%)
- Speaker Notes: ✅ Presentes

#### Slide 10: Suite de Testes
- Prompts Totais: 391
- Categorias: 6 (Injection 28.6%, RCE 24%, SQL 17.4%, Escalação 13%, DoS 10.7%, Path 6.1%)
- Taxa Bloqueio Progressiva: 0% → 84% → 95.65%
- Speaker Notes: ✅ Presentes

#### Slide 11: Redução CVSS
- Score Inicial: 8.1 (Crítico)
- Score Final: 0.9 (Negligenciável)
- Redução Total: 89%
- Contribuição Camadas: -24%, -9%, -86%
- Speaker Notes: ✅ Presentes

#### Slide 12: Estudos de Caso
- Caso 1: Jailbreak Obfuscado (Confiança 0.92)
- Caso 2: SQL Injection (Bloqueio duplo)
- Caso 3: Path Traversal (Arquivo crítico /etc/shadow)
- Taxa Escapamento: 4.35%
- Speaker Notes: ✅ Presentes

#### Slide 13: Boas Práticas
- Princípio 1: Menor Privilégio
- Princípio 2: Defense-in-Depth
- Princípio 3: Zero Trust Architecture
- Princípio 4: Auditoria e Logging
- Speaker Notes: ✅ Presentes

#### Slide 14: Conclusões e Futuros
- Conclusões: 5 items comprovados
- Futuros: 5 extensões (GPU, Multi-model, Federated Learning, Honeypot, Service Mesh)
- Timeline Federated Learning: 6-9 meses
- Speaker Notes: ✅ Presentes

#### Slide 15: Encerramento
- "Obrigado pela Atenção!"
- Contatos: Email, GitHub, LinkedIn
- Speaker Notes: ✅ Presentes

### Bloqueios Encontrados

❌ **NENHUM**

Todas as tarefas foram completadas sem obstáculos. Dependência (python-pptx) foi instalada sem problemas.

### Validações Realizadas

✅ Arquivo PowerPoint criado com sucesso  
✅ Formato validado como Microsoft PowerPoint 2007+  
✅ Tamanho apropriado: 71 KB (bem comprimido)  
✅ Todos os 15 slides presentes  
✅ Paleta de cores implementada corretamente  
✅ Tipografia conforme especificação  
✅ Dados numéricos mapeados corretamente  
✅ Speaker notes em todos os slides  
✅ Integridade visual do design mantida  

### Pronto Para

✅ Apresentação em PowerPoint (Windows)  
✅ Apresentação em LibreOffice Impress (Linux/macOS)  
✅ Exportação para PDF se necessário  
✅ Defesa de TCC em 27 de Maio de 2026 ou futuro  
✅ Compartilhamento com banca examinadora  
✅ Reuso e regeneração via script (criado `criar_apresentacao.py`)  

### Recomendações

1. **Validação Manual:** Abrir arquivo em PowerPoint/LibreOffice para revisão final
2. **Logos:** Se FATEC/CPS não estiverem automáticos, inserir via Slide Master (preserva design)
3. **Ensaio:** Testar timing (alvo 20-25 minutos) e transições
4. **Backup:** Manter script `criar_apresentacao.py` para regeneração rápida se edições forem necessárias

---

**Status Final:** ✅ **OPERAÇÃO CONCLUÍDA COM SUCESSO**

[[Apresentação]] entregue, validada e pronta para uso imediato.

*Gerado por DESIRE | Especialista em Automação de [[Apresentações]] Corporativas*
