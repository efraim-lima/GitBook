# SNMP

Sinais vitais que devemos prestar atenção na maquina: -temperatura -espaço e disco -alimentação -velocidade de cooler -utilização cpu -trafego na rede -INTI

Podemos fazer o acompanhamento destes sinais em uma ferramenta chamada NAGIOS

propor um roteiro com 5 intens de uma manutenção fisica preventiva: -limpeza de pó, apertar parafusos, troca de pasta termica, alteração de pata para sata

propor um roteiro com 5 intens de uma manutenção lógica preventiva: -ponto de restauração, desinstalar aplicativos não utilizados, varredura de malwares, defragmentação, limpeza de cookies;

KPIs

trabalharemos com indices específicos para que possamos compreender o que ocorre e em quanto tempo ocorrem os processos

I) MTBF - Medium Time Between Failure --> quando o ráfico está em cima significa que o equipamento está funcionando naquele timestamp do gráfico, o que avaliamos é a quantidade média em que a linha do gráfico esteve na posição superior do gráfico. Para medir este comportamento plea média de períodos ativo por periodos ativos, ou seja, a somatória de períodos ativos dividia pela quantidade de períodos ativos. --> aumenta a quantidade de manutenções preventivas e diminui a quantidade de manutenções corretivas; --> o processo de manutenção é procurar de 2 a 3 desvios padrões (4 ou 6 sigma) da média de tempo ativo para trás para acertar no ponto mais proximo da facilidade de manutenção.

Existem equipamentos que possuem uma característica de perder totalmente sua capacidade de uso, para tal determinamos o tempo em que este equipamento como lifetime.

bbath curve -> a curva da banheira determina que os defeitos em função do tempo ocorrem mais nos seus primeiros momentos (morte infantil ou prematura) ou ocorrer depois de muito tempo de uso (desgaste ou obsolescencia).

bath curve serve tanto para harwares quanto para softwares, pois podem ocorrer erros nos primeiros instantes ou depois de muito uso, ambas as duas tecnologias possuem a mesma curva.

QUESTÃO DE PROVA: Se uma rede possui uma MTBF de 97% significa que possui uma relação ruim de qualidade, a AWS garante 99.999% e para adicionar mais um 9 a este numero seriam gastos milhões de dolares.

II) MTTR - Main Time to Repair

Consideramos o tempo medio de reparo e conserto o tempo em que paramos de produzir informação e o tempo em que falaremos para o usuário em que nosso serviço ficará indisponível.

Calculamos MTTR a partir da média de tempo de reparos pela quantidade de reparos ocorridos, ou seja, a somatória dos tempos de reparos dividida pela quantidade de reparos que ocorreram no passado.

No gráfico de funcional x tempo enquanto a linha está em cima consideramos MTBF e quando está embaixo consideramos MTTR; outro ponto é que podemos trabalhar com PWM, assim como no arduino, controlando a saida digital, ou seja, mantemos algum equipamento standby para inserir

III) Disponibilidade --> é a porcentagem do tempo que o equipamento ou sistem fica disponivel

Podemos calcular a disponibilidade através da relação entre MTBF e MTTR, ou seja, dividindo MTBF por MTTR. A saída desta conta estará em porcentagem.

relação: 0 <= Disponibilidade <= 1

IV) Indisponibilidade

a indisponibilidade pode ser medida pela imagem da disponibilidade, ou seja, 1 -Disponibilidade

QUESTÃO DE PROVA Analisando a formaula da disponibilidade, proponha 3 ações efetivas para melhorar este índice: R: para melhorar este indice é preciso aumentar a disponibilidade, e para isso é necessário aumentar MTBF e/ou diminuir MTTR. Para aumentar MTBF podemos implementar ou aumentar manutenção preventiva/preditiva; treinar usuários, para diminuir MTTR podemos implementar treinamento técnico, spare parts (peçaas sobressalentes), disco padrão (clone de disco, cópia do Sistema Operacional com o objetivo aumentar a velocidade de recuperação do dispositivo).

Caso a pergunta seja de analisar a INDISPONIBILIDADE invertem-se os vetores de MTTR e MTBF na equação, ou seja, MTTR precisa diminuir e MTBF precisa aumentar na equação, mas as ações para isso são as mesmas que no caso anterior.

QUESTÃO DE PROVA Rede tem ua projeção de fincionamento de 4000hs. A disponibilidade é de 98%. Isso é bom ou é ruim? Justifique. R: Disponibilidade é tratado como SLRA. O calculo a ser feito é de: quantidade de horas (4000) divididas pelo MTTR ()

Fazer uma folha de caderno a resposta de algumas perguntas como: o que é downtime, quais as caracteristicas devem ser levadas em conta para se calcular o downtime e como calcular
