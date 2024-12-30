# IDs de Eventos

O processo de análise de LOGs infere que precisamos reconstruir uma cadeia de eventos com o objetivo de se compreender a linha de tempo do que ocorreu e ter uma melhor visibilidade de como pode ter ocorrido um incidente, levantando cada etapa do incidente seja antes ou depois do mesmo ocorrer. Portanto é importante saber correlacionar os eventos detectados com etapas de um incidente, isso trará clareza e consciência de cada etapa e também a possiblidade de inferir qual foi a intenção da ação do atacante no ambiente.&#x20;

A partir disso é interessante correlacionar o framework Cyber Kill Chain, que descreve as etapas de um ataque cibernético e IDs de eventos específicos do Windows que levantarão eventos que podem ser associados a cada etapa do incidente.

Abaixo está uma lista detalhada dos IDs de eventos relevantes para o Windows, categorizados por cada etapa da Cyber Kill Chain.

#### 1. Reconhecimento

* ID de Evento 4688: Um novo processo foi criado (pode indicar ferramentas de reconhecimento).
* ID de Evento 4624: Logon bem-sucedido (pode mostrar tentativas de acesso para coletar informações).

#### 2. Armazenamento

* ID de Evento 4688: Criação de executáveis ou scripts maliciosos.
* ID de Evento 4697: Um serviço foi instalado no sistema (pode indicar armazenamento).

#### 3. Entrega

* ID de Evento 4625: Tentativas de logon falhadas (pode indicar tentativas de phishing).
* ID de Evento 1102: Log de auditoria limpo (pode ser usado para encobrir rastros após a entrega).

#### 4. Exploração

* ID de Evento 4688: Execução de código malicioso.
* ID de Evento 7045: Um serviço foi instalado (frequentemente usado por malware durante a exploração).

#### 5. Instalação

* ID de Evento 4698: Tarefa agendada criada (frequentemente usada para persistência).
* ID de Evento 4700: Tarefa agendada habilitada.
* ID de Evento 4701: Tarefa agendada desabilitada.

#### 6. Comando e Controle

* ID de Evento 5156: A Plataforma de Filtragem do Windows permitiu uma conexão (pode indicar tráfego C2).
* ID de Evento 5158: A Plataforma de Filtragem do Windows bloqueou uma conexão.

#### 7. Ações

* ID de Evento 4663: Uma tentativa foi feita para acessar um objeto (pode indicar exfiltração de dados).
* ID de Evento 4660\*\*: Um objeto foi deletado (possivelmente indicando destruição de dados).
