# Art.: Segurança de Aplicações IoT

## Artigo: Segurança de Aplicações IoT

O objetivo de nosso trabalho é abordar a segurança de aplicações para ambiente IoT e, propor soluções para este tipo de ambiente para que seja mais seguro no contexto digital. Analisando o conteúdo disponibilizado pelo prof. Dr. Fabio H. Cabrini, nos deparamos com alguns elementos que, de acordo com sua arquitetura e dependências incorporadas em seu ambiente de produção, podem apresentar vulnerabilidades intrínsecas e inerentes a composição destes elementos o que expõe o FIWARE a vulnerabilidades que estão indiretamente relacionadas à ferramenta em si. Ter conhecimento dessas vulnerabilidades é um ponto inicial para que possamos adotar medidas de endurecimento da segurança nestes ambientes. Vamos pontuar alguns elementos e suas vulnerabilidades correlacionadas adiante, para boa granularidade dessas vulnerabilidades, precisamos consultar as principais fontes que já organizam e catalogam essas informações de vulnerabilidades, com isso chegamos às CVEs. Considerando a natureza da FIWARE (baseada no Docker) e de seu padrão de interface NGSI, que funciona através de APIS, podemos inferir que as vulnerabilidades encontradas nessas duas tecnologias (Docker e API) serão transferidas para a FIWARE. O processo de qualificar as principais CVEs correlacionadas às dependências da FIWARE parte de: listar as principais CVEs por ferramenta e verificar sua potencialidade destrutiva ao ambiente.

Listagem de vulnerabilidades correlacionadas ao FIWARE por ferramentas encontradas no site [https://cve.mitre.org/cve/search\_cve\_list.html](https://cve.mitre.org/cve/search_cve_list.html):

API: 5495 resultados&#x20;

Docker: 357 resultados