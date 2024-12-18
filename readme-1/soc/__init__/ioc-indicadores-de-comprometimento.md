# IOC - Indicadores de Comprometimento

Primeiro, quando tivermos algum primeiro Indicador de Comprometimento, precisamos fazer algumas avaliações sobre os Indicadores. O primeiro é averiguar alguns possíveis meios de indício. Estes são:

-Tráfego proveniente de regiões estranhas;

-Tráfego em redes e portas incomuns;

-Tráfego que esteja fora do padrão;

-Endereços de IP incomuns;

-Domínio/Subdomínio suspeito;

-Requisições de arquivos suspeitos;

-Hash Criptográfico;

-Tipo de Tráfego de Rede;

-Endereço URL;

-Domínios e Hosts;

-Criação/Remoção/Modificação em Chave de Registro no Sistema;

-Criação/Remoção/Modificação em Arquivos no Sistema;

Dados poderão chegar em forma de arquivo de tráfego ou binário.

PROCEDURE

Ao nos deparamos com domínios e IPs precisamos analisá-lo com o comando

-whois \<domain/IP>

aqui podemos confiar na data de criação, mas não na organização que criou e nem no estado e país

Próximo passo é analisar o User-Agent com o site WhatIsMyBrowser e entender o Navegador proveniente. Caso não encontremos um User-Agent ja temos um indicador de alerta, pois conexões web geralmente são feitas por navegadores e estes possuem User-Agent.

Depois, caso tenhamos algum host para avaliar, basta acessarmos o site Vírus Total, onde poderemos saber se este domínio está associado a atividades maliciosas
