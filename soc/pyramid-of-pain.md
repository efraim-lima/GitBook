---
description: >-
  Determinando a dificuldade que um adversário enfrenta ao tentar adaptar suas
  táticas, técnicas e procedimentos (TTPs) após ser detectado por mecanismos de
  defesa em uma rede.
---

# Pyramid Of Pain

Um atacante precisa estar munido de informações e [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]] para conseguir passar as [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]] de segurança de um determinado sistema e, do lado da defesa, precisamos estar munidos de [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]] que possibilitam compreensão se o sistema está robusto e devidamente configurado e eficaz contra as ameaças destes atacantes assim como deixar o processo de ataque mais difícil para [[fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] atacantes adqurirem acesso aos recursos que desejam, causando "dor" para o atacante, daí Pyramid of Pain.

Pyramid of Pain classifica [[fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] indicadores de comprometimento (IoCs) de acordo com a dificuldade que eles causam ao atacante quando são detectados e neutralizados, tais indicadores são:

1. **Hash Values**:
   * O processo consiste em gerar hashes de arquivos que podem ser em [[md5]], SHA-1 e SHA-2 e verificar se batem com hashes de arquivos maliciosos, este processo gera um impacto mínimo para a complhexidade do ataque para o atacante, pois ele pode facilmente modificar [[fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] arquivos para alterar o hash.
     * Podemos usar [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]] para analisar o hash dos arquivos nas [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]]:
       *
2. **IP Addresses**:
   * Aqui endereços IP são analisados e verificados se estes estão associados a [[ATIVIDADES]] maliciosas. Nos pocessos de proteção e seguraça tem um baixo impacto para ação do atacante porque ele pode mudar seus servidores ou usar endereços IP diferentes.
3. **Domain Names**:
   * O processo é bem semelhante ao de análise de IP, mas avaliando [[fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] domínios e verificando se sãuo usados para [[comandos]] e controle (C2), [[phishing]], etc. gerando uma dificuldade moderada para o atacante, pois mudar de domínio exige mais esforço, mas ainda é uma tática relativamente fácil para o atacante.
4. **Network/Host Artifacts**:
   * Agora chegamos a uma área mais profunda no processo de detecção e dissuasão do atacante, o processo de análise de padrões específicos de tráfego, strings usadas em [[scripts]] maliciosos, etc. Constituindo em uma dificuldade alta para o atacante poder transpunir porque modificar artefatos de rede e host exige mais conhecimento e esforço, pois muitas vezes envolve mudanças significativas nas operações.
5. **[[tools]]**:
   * O processo de analsar as [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]] usadas pelo atacante, como exploits, backdoors, etc. possui uma dificuldade muito alta para o atacante, já que alterar ou substituir [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]] pode exigir [[fatec/Pesquisa/Pesquisa/ferramentas/desenvolvimento|desenvolvimento]] adicional ou encontrar alternativas adequadas.
6. **Tactics, Techniques, and Procedures (TTPs)**:
   * Por fim, pode-se fazer a análise de padrões de comportamento do atacante, como métodos específicos de infiltração, movimento lateral, exfiltração, etc. O que consiste em dificuldade extremamente alta para o atacante, uma vez que mudar TTPs requer um redesenho fundamental das operações e métodos, o que pode ser muito demorado e complexo.

Algumas [[fatec/Pesquisa/Pesquisa/ferramentas/ferramentas|ferramentas]] para anasarmos hash, IPs, URLs, Domínios, Arquivos ou até mesmo CVEs:

* [[soc/tools/malwares|malwares]] - [malwares.md](tools/malwares.md "mention")

####

\
