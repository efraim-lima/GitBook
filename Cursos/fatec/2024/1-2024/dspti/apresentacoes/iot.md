# IoT

A conectividade proporcionada por IoT também trouxe varias brechas de [[Segurança]] e falhas correlacionadas a isso.

As principais ameaças a IoT são:

DDOS, [[CyberSecurity/Course/tools/malwares|malwares]], MitM

Vulnerabilidades mais comuns: Conectividade não segura, Credenciais fracas ou muito padronizadas, firmwares desatualizados, [[Criptografia]] fraca.

IoT é poica segira, pois [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] dispositivos est]ap conectados a uma rede e estão como slaves de um servidor considerado master, isso deixa o dispositivo vulneravel e vulnerabiliza o servidor ao mesmo tempo.

Alguns processos que podem auxiliar:

Autenticação Robusta, Critpgrafia avançada, atuaização de patches e monitoramento constante, Adotar um modelo de arquitetura segura e robusta (adotando políticas de gateway de gerenciamento - muito usada em ambientes comerciais em critérios de automação, Edge Computing - [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] dados ficam mais próximos ao limite da fronteira com o usuário - bem aderente no uso de carros autonomos, outra forma de manter essa [[Segurança]] é o uso de servidores cloud - onde pode-se implementar regras de autenticação e [[Governança]] dos dados a serem acessados).

Existem algumas normas e padrões para a [[Segurança]] de IoT, como por exemplo: -> ISO/IEC27001 -> Protocolo MQTT -> Certificação UL IoT -> IEC 62443

Casos de Estudo Ataque Mirai Botnet -> em 2016 | O ataque se deu basicamente por conta de firmware desatualizados e excesso de senhas padrão fracas. Invasão de câmeras de [[Segurança]] - em 2017 | Ataque também se deu por conta de firmwares desatualizadas e senhas padrão.

Implementações bem sucedidas

Monitoramento Industrial em Fábticas Alemãs Agricultura Inteligente Smart City em Barcelona -> usam [[Criptografia]] e autenticação para [[Segurança]] do sistema Saúde Conectada (dispositivos de leitura de diabetes, por exemplo)

Ameaças Emergentes: Novos ataques proporcionados pelo uso de IA estão aumentando Ransomwares Ataques sofisticados tirando proveito de falhas de seguranã nos dispositivos e sistemas Algumas ameaças traicionais como [[CyberSecurity/Course/tools/malwares|malwares]], invasão de sistemas e roubo de dados.

Desafios e soluções potenciais Alguns fabricantes possuem problemas de compatibilidade entre dispositivos
