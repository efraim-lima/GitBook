## Boas práticas para os processos

# Guia de Análise de Alertas de Rede

Este guia estabelece um fluxo de trabalho estruturado para a análise de tráfego suspeito, visando a identificação de incidentes e a correta classificação de alertas.

## 1. Coleta e Reconhecimento de Dados
O primeiro passo consiste em coletar informações rápidas para contextualizar o tráfego detectado.

### A. Tráfego proveniente da Internet (Origem Externa)
* **Propriedade do IP:** Identificar o tipo de endereço (Estático ou Pool) e o responsável pelo registro (ex: provedores de hospedagem).
* **Reputação:** Consultar bases de inteligência de ameaças (VirusTotal, AbuseIPDB, Cisco Talos).

### B. Tráfego proveniente da Rede Interna
* **Identificação:** Mapear o *hostname* do dispositivo.
* **Usuário:** Identificar o proprietário do ativo e o horário do último *logon*.

## 2. Análise Técnica do Tráfego
Não se limite à URL; o tráfego pode conter cargas maliciosas (payloads) em diversos campos da requisição.

* **Conteúdo:** Investigar padrões de ataques web (SQL Injection, XSS, Command Injection, IDOR, LFI/RFI).
* **Estrutura HTTP:** Examinar exaustivamente todos os campos da requisição HTTP.
* **Referência:** Consultar o material *Web Attacks 101* para aprofundamento em métodos de detecção.

## 3. Verificação de Falsos Positivos (Testes Planejados)
Simulações de ataque podem gerar alarmes falsos se as regras não estiverem refinadas.

1.  **Busca em E-mails:** Verificar se há registros de janelas de manutenção ou testes agendados envolvendo o *hostname*, usuário ou IP em questão.
2.  **Ferramentas de Simulação:** Validar se o tráfego origina-se de soluções de simulação de ataque (ex: Verodin, AttackIQ, Picus). Caso o *hostname* contenha o nome destas ferramentas, o evento é classificado como atividade planejada.

## 4. Compreensão do Acionamento da Regra
Antes de iniciar a análise profunda, é fundamental compreender a lógica por trás da detecção:

* **Nome da Regra:** Identificar o objetivo da regra. O nome, geralmente, descreve o tipo de ataque que o sistema foi configurado para detectar.
* **Fluxo de Tráfego:** Determinar os dispositivos envolvidos, a direção do fluxo (origem/destino) e o protocolo utilizado.

## 5. Critérios de Escalonamento (Tier 2)

A decisão de escalar o incidente para o Nível 2 deve seguir os critérios abaixo:

| Situação | Escalonar? |
| :--- | :--- |
| O ataque foi bem-sucedido | **Sim** |
| O atacante comprometeu um dispositivo interno (fluxo interno → interno) | **Sim** |
| Ataque proveniente da Internet que não obteve sucesso | **Não** |

> **Nota:** Estas diretrizes são genéricas. É imprescindível alinhar este processo aos procedimentos específicos de escalonamento adotados pela sua instituição.

