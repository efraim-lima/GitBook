# Eletrica

I) Qualsade de rede elétrica parte II II) Anomalias a serem mitigadas da rede eletrica -filtross de linha -estabilizadores -ups/no breaks -geradores

V0 Infliencia das anomalias da rede eletrica nos bits da area de TI. Para isso vamos entender, por meio de uma fonte senial, didádica de como ocorre a conversão da tensão alternada para a tensão contínua:

Primário N1 --------> secindário N2 ---------> Ponte de diodos ---------> capacitor eletronico ------> filtro 6800 mi

```
              N1
```

> \-----------------------------------<

```
        Transformador
```

Capacitor eletrolitico se carrega com carga (ou seja, no pico das senoides), e de acordo com o tempo vai se descarregando aos poucos, mas sempre recarrega novamente se mantendo nos picos, a este processo chamamos de Ripple (zona de indefinição) onde ocorre

Exemplo:

N1=100 ; N2=12 ; V2=(12/100)\*127 ; V2≃15 Vac

N=Número de espints

N1/N2=V1/V2 ; V2=(N2/N1)\*V1

O transformador ajusta a tensão de entrada (127/220V) abaixando essa tensão para algo em torno de 5V/12V. A ponte de diodo, conhecida como ponte retificadora, transforma os ciclos negativos (-) em positivos e finalmente o capacitor eletronico mantem a tensão estável até o próximo "pulso".

\-Podemos perceber:

1. entrada mais baixa -> RESET Como podemos notar, a tensão contínua (bits)
2. entrada mais alta -> QUEIMA é função kdireta da tensão de entrada
3. ruidos na entrada -> portando alterações na entrada
4. quedas na alimentação -> causam alterações na tensão da saída.

VI) Anomalias da rede elétrica

A) Ruídos/Espúrios/Spikes/Spark - são disturbios conduzidos pela rede eletrica; Para mitigar esse tipo de problema utilizamos filtro de linha, não confundir com barra de tomada (extensões). O filtro de linha elimina os ruidos, geralmente ade alta frequencia. O fusivel e o vanistor são dispositivos de proteção; Os indutores e capacitores filtram.

Em voltagens mais altas a corrente é menor, por exemplo: 127V = 2 Amperes; 220V = 1 Amper

O indutor é ótimo paa manter o fluxo de energia, trabalhando junto ao capacitor; os capacitores ainda filtram a entrada.

B) Subtensão/Subretenção - para este tipo de anomalia é recomendado a utilização de estabilizadores, também conhecidos como reguladores de tensão. Um cuidado especial para sua utilização com equipamentos profissionais (servidores), verificar as especificações do estabilizador e do equipamento, não se surpreenda se as especificações do equipamento for melhor do que a especificação do estabilizador. Em geral, os estabilizadores possuem filtro de linha e várias tomadas de saída. Sua função é manter a saída estável, controlada, mesmo com alterações na entrada, chamada de range de variação, por exemplo: 114Vac até 137Vac => ele pega tudo isso e transforma em 127Vac. Os barulhos que ouvimos do estabilizador são as bubinas do primario sendo chaveadas para os primarios para manter a tensão correta para a saída do mesmo.

Quando um sinal cai pela metade dizemos que cai 3dbs Se tivermos um servidor de range de 96V a 290V podemos compreender que ele ja possui um filtro de linha embutido

C) Quedas curtas/short-breaks ups (Uninterruptable Power-Supply), equipamento que mantém a saída alimentada/energizada, mesmo com ausência do sinal de entrada. Esse dispositivo mantém a saída por pequenos intervalos de tempo. O tempo depende da cappacidade da bateria e o consumo da cargaa (computador); não ligamos impressoras, ou outrros equipamentos semelhantes no no-break pois vai consumir toda a energia do mesmo em caso de queda de energia. Premissa semelhante ao uso de bluetooth, onde gasta-se mais energia para enviar um bit via bluetooth do que para zipar um arquivo.

Recomenda-se sair (shitdown) de forma segura. Smart ups-iot

O no-break (ups) pdoe ser de dois tipo: on-line e of-line.

O no-break online é menor, em geral mais caro, ele isola o equipamento de TI da rede, precisa ser carregado para depois ser utilizado, a vida util da bateria é metade não tem chaveamento de relé. Os no-breaks offline possuem um processo de retificar o a energia conduzida (AC) para AD pela rede armazenando-a em uma bateria, quando ocorre a queda de energia ele faz o processo de inverter AD para AC e fornecer para o dispositivo conectado.

D) Quedas longas (blackout/brownout), são interrupções no fornecimento de energia da ordem de dezenas de minutos a´te horas ou dias. Nessas condições recomenda-se a utilização de geradores, dispositivos de motores autinomos (oleo dizel, gas, gasolina) que acionam os geradores (dínamos) que alimentam os circuitos de TI.

A ideia funciona de forma simples, um combustível alimenta um motor, que alimanta um gerador que é conectado a um banco de baterias e no-breaks; paralelamente a isso a entrada de energia está conectada ao mesmo motor através de um controle; caso caia a energia a rede fica conectada às baterias do banco e no-breaks até que o controle acione o motor (que deve estar com o combustível renovado) e volte a fornecer energia para a rede.

VI) Dimensionamento de equipamentos de proteção (estabilizadores, no-breaks e geradores)

Note que todos os equipamentos acima são especificados em vol x amperé (VA) e os equipamentos de TI (computador, roteador, impressora, monitor, etc) são especificados em watts. Infelizmente as duas gradezas não são iguais. Na escola, aprendemos que a potência é o produto entre tensão e corrente \[potencia = u (tensão) \* i (corrente)], isso é particularmente verdadeiro, pois só vale para cargas resistivas e na realidade as cargas são indutivas ou capacitivas A reação entre as potencias é:

PVA = (Pwatts/(M\*FP))

PVA = Potencia em Volt x Amperé Pwatts = Potência em watts M = (éta \[letra grega]) -> redimento FP = Fator de Potencia

M (éta) - rendimento-capacidade do dispsitivo de converter portencia de entrada em trabalho na saída.

As fontes de alimentação (ATX) têm rendimento acima de 80%. Motor a combustão (gasolina) tem baixo rendimento.

FP - Fator de Pottencia - é o coseno do angulo (omega) de defasagem entre a tensão e a corrente: Carga resistiva é uma relação entre defasagem de tensão e corrente par a par, de forma que ambas ocorrem ao mesmo tempo, Carga indutiva ocorre quando a defasagem da corrente ocorre em seguida, ela é induzida para o dispositivo Carga capacitiva é a que a defasagem da corrente antecede a tensão da rede, portanto geralmente possui rede própria para o dispositivo, assim como os elevadores dos prédios (estudar carga reativa).

Regra Prática: devemos dimensionar os equipamentos de proteão com o dobro da potencia em watts. Justificativa: adotando um rendimento de 70% e uma defasagem menor que 50º temos:

PVA = Pwatts/(0,7 x cos 50°) = Pwatts/(0,7 x 0,7) = Pwatts/0,49 ≃ Pwatts/0,5

Pwatts/(1/2)

O melhor equipamento para combater qualquer aanomalia é o gerador, porém ele é muito caro. O mais barato é o filtro de linha

Tomada vermelha em rede de TI é voltada para rede estabilizada, para ligar equipamentos estaveis.

no break nos EUA é UPS

REVISÃO: Ferramenta de Diagnósitico:

\-> Multimetro U=RI

Função - Medição de grandezas eletricas -tensão: alternada, entrada/rede continua - bateria/saida -resistencia: resistores -corrente: alternada e cotínua -diodo: led \[+] -->|- \[-] -capacitância (F) miF pF nF

Empresas especializadas em desenvolvimento de BIOS: Awards, AMI, Phoenix, Intel.

Devido às características intrínsecas do bios devemos ter cuidados especiais no processo de atualização/upgrade do BIOS.

```
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| 		Afinal, quando devemos atalizar a BIOS?			   |
|    									   |
|  Sempre que o fabricante de placa (Asus, Gigabyte, etc) libera uma nova  |
|  versão?                                                                 |
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

A resposta é negativa, a atualização deve ser feita em situações que é necessaria para o correto funcionamento do sistema.

A) Em geral quando ocorrem mudanças no sistema que necessitam do suporte do BIOS para seu funcionamento.

```
windows 11 -> suporte TPM
```

B) Disponibilidadede novas funcionalidades como o USB 4.0, SATA III, pois devido ao time-to-market (tempo que leva-se para conseguirmos acessar uma funcionalidade no mercado, tipo configurações específicas para chipsets específicos), o hardware possui a funcionalidade, mas não é disponibilizada de imediato.

C) Avaliar o release p verificar se a atualização irá trazer algum benefício para o sistema. Em tempo, devido a sistemas frágeis, devemos nos certificar que oa Bios utilizada é livre de falhas, pois é comum a perda completa do sistema devido à falha de gravação de uma nova versão de BIOS (firmware), como por exemplo, a queda de energia durante o processo, especialmente para dispositivos de ti embedded como impressoras, routers, monitores, displays, etc...

O nível entre o hardwre e o software é o sistema de instruções do sistema, código de máquina. Tudo o que fazemos em software podemos criar um hardware que se comunique com isso, tudo que fazemos em hardware podemos emular em software.

Em mudanças bruscas de sitema (tipo uma BIOS nova) deve-se sempre fazer primeiro um projeto piloto antes de soltar em todo o sistema para evitar falhas e panes totais no sistema que podem ocorrer.

Para testar a memória do computador deve-se pegar a memória e preencher a memória com os seguintes padrões (para toda a memória):

000000000000000000000000000000000000000000000000000000000000000000000

```
		    -- DEPOIS --
```

111111111111111111111111111111111111111111111111111111111111111111111 FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

```
		    -- DEPOIS --
```

555555555555555555555555555555555555555555555555555555555555555555555 010101010101010101010101010101010101010101010101010101010101010101010

```
		    -- DEPOIS --
```

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA 101010101010101010101010101010101010101010101010101010101010101010101

```
		    -- DEPOIS --
```

QUando fechamos o computador e ele suspende suas configurações e aplicativos atuais ele salva o que estiver na RAM na memória swap

Atividade in class -> para entrega na próxima semana - individual Responda às seguintes questões:

1. Aonde fica armazenada o BIOS? R: Placa mae
2. Aonde ficam armazenados os parametros configurados pelo usuário? R: RAM CMOS, na flash ficam os parametros de babrica/default.
3. Aonde fica disponível a data e hora do sistema? R: Na bateria da placa mãe, no RTC (Real Time Clock)
4. Qual a função da bateria de lithium da placa-mãe? R: Manter o tempo do sistema just in time
5. Qual o sintoma de um computadore que tem o BIOS corrompido? (Exemplo: apagamento de todas as psoições da memória flash com 0xFFFF). R: No momento inicial não acontecerá nada, mas ao desligar o computador e religar a tela não ligará, sequer teremos sinal de que o dispositivo está energizado
6. Como você recomenta um roteiro seguro para a configuração do BIOS para um sistema instável? R: Uma das possibilidades de solução aqui é: entrar no BIOS e colocar valor default, se der certo é porque uma das configurações estavam conflitando com o sistema.

Homework

Escolha um computador qualquer:

1. Identifique-o: modelo/marca/CPU/memória/SO
2. Descreva como acessar o BIOS
3. Descreva pelo menos 10 características passiveis de configuração
4. Relacione pelo menos 5 características associada à segurança/disponibilidade da informação.
5. Pesquise os efeitos da perda/descarga da bateria.

\-a data hora é configurada direto no relógio -para resetar a bios basta desconectar da tomada, bateria e plugar uma chave de fenda no conector da bateria

Apresentação: não precisa de slides e nem de um trabalho à la ABNT, mas vale a pena mostrar um cronograma da apresentação e o que pode ser apresentado
