# Framework For Dummies | Processo de Análise de E-mails e detecção de Phishing

Você sabe como verificar se um e-mail pode ou não ser um phishing?\
Sabia que existem formas de inferir se um e-mail é phishing ou não? E ainda mais, não precisa de extrema expertise na detecção de incidentes e nem de ferramentas específicas de detecção e gestão  de ameaças, 'da pra fazer de casa'.\
\
Os atacantes e golpistas que se utilizam de e-mails para angariar vitimas pretendem, com este material, inserir uma porta de entrada no sistema ou coletar credenciais que possam ser utilizadas no futuro para tentar acessar sistemas e causar prejuízos à vítima ou à organizações.\
\
As formas mais comuns de detectar e evitar se tornar uma vítima de phishing são:

* buscar por erros ortográficos e gramaticais no conteúdo;
* verificar o remetente do e-mail, assim como seu endereço;
* ter muita atenção ao conteúdo deste e-mail;
  * conteúdos de caráter urgente ou extremamente atrativos como direito a brindes ou bônus;
  * anexos, não abra anexos de remetentes suspeitos;
  * links suspeitos (passe o mouse sobre o link e verifique o real link de redirecionamento);&#x20;

Agora, neste material gostaria de aprofundar a análise dos metadados dos emails, uma prática mais avançada de análise, mas eficiente e que proporciona mais ferramentas para evitar que caiamos em golpes ou phishings.\
\
Primeiro precisamos entender o conceito de metadados (BUSCAR REFERENCIAS).\
\
Com isso em mente teremos maior propriedade para fazer esta análise e precisamos primeiro acessar tais metadados, para isso verifique como acessá-los em seu cliente de e-mail preferido, neste caso vamos utilizar o Outlook como referência e nele o processo consiste em abrir o e-mail de forma individual (clicando duas vezes sobre o e-mail), acessando o ícone de Arquivo e procurando por Propriedades, localizado no elemento Informações que encontra-se na coluna à esquerda.\
\
Ao abrir os metadados devemos prestar atenção a alguns elementos para verificar a autenticidade deste email:

* **Headers do E-mail;**
* **Campos como**:
  * **Received**: mostra o caminho percorrido pelo e-mail desde o remetente até o destinatário;
  * **From**: Indica o endereço de e-mail do remetente, mas este campo pode ser facilmente alterado pelo remetente;
  * **To:** podem ocorrer discrepâncias neste campo, o que estiver fora disso pode ser um alerta de indício de phishing;
  * **Return-Path**: Especifica o endereço de e-mail para onde devem ser enviadas as mensagens de erro ou de devolução (bounces) e ajuda a apresentar o endereço de e-mail real do remetente;
  * **Message-ID**: Fornece um identificador único para cada e-mail, geralmente gerado pelo servidor de envio;
  * **DKIM-Signature**: DKIM (Domain Keys Identified Mail) é uma assinatura digital que verifica se o e-mail foi enviado e autorizado pelo domínio indicado. Inclui uma chave criptográfica que pode ser verificada pelo servidor de recebimento;

Com essas informações em mãos poderemos verificar a autenticidade dos e-mails, para isso utilizaremos as ferramentas MXToolBox (disponível em [https://mxtoolbox.com/](https://mxtoolbox.com/)), VirusTotal (disponível em [https://www.virustotal.com/](https://www.virustotal.com/)) e IPVoid (disponível em [https://www.ipvoid.com/](https://www.ipvoid.com/)). Com isso poderemos dar sequência em nossa analise do e-mail.\
\
Tendo posse dos metadados e também das ferramentas listadas podemos seguir os passos a seguir:

1. **Verificando o Remetente e comparando com o Endereço de IP**:
   * Primeiro podemos utilizar a ferramenta de analise de headers da MXToolBox (disponível em: [https://mxtoolbox.com/EmailHeaders.aspx](https://mxtoolbox.com/EmailHeaders.aspx)) e coletar informações presentes no header, muito embora possamos fazer a analise direto do conteúdo bruto, os analisadores de headers categorizam com maior facilidade. Neste analisador de headers devemos coletar:
     * ARC-Authentication-Results
       * coletar o IP do campo "sender ip is \[IP]"
       * verificar os campos dkim e dmarc
     * Received-SPF
     * From
     * To
     * Date
     * Message-ID
     * Reply-To
     * Content-Type
     * Return-Path
   * Pode ocorrer de o IP encontrado no Receievd-SPF e no ARC-Authentication-Results não resolver em um domínio condizente com o do remetente caso utilizemos um WHOIS ou algo semelhante neste domínio, para isso precisaremos utilizar a ferramenta SPF Records (disponível em: [https://mxtoolbox.com/spf.aspx](https://mxtoolbox.com/spf.aspx)) e verificar se algum dos valores presentes cruza com o IP encontrado;
   * Utilizar a ferramenta IPVoid para identificar o IP do domínio que está escrito no remetente, no item Find Website IP (disponível em [https://www.ipvoid.com/find-website-ip/](https://www.ipvoid.com/find-website-ip/));
   * Pesquisar a reputação do domínio, do IP SPF e do IP do remetente no Vírus Total para verificar a reputação de ambos;&#x20;
     * caso tenhamos alertas provenientes do Virus Total precisamos estar alertados da alta probabilidade de ser um phishing;
   * Utilizar um WHOIS (disponível em [https://www.ipvoid.com/whois/](https://www.ipvoid.com/whois/)) para procurar indícios dos proprietários do domínio e IPs coletados;
     * No WHOIS é importante verificar alguns pontos, como indicadores de confiabilidade:
       * Registrador: Registradores conhecidos e confiáveis são um bom sinal de legitimidade.
       * Titular:  Verificar se o titular é uma entidade conhecida ou esperada pode ajudar a confirmar a autenticidade
       * Contato: Contatos válidos e detalhados são indicativos de um domínio legítimo. Informações incompletas ou genéricas podem ser suspeitas
       * DNS Server: Servidores desconhecidos ou mal configurados podem ser um péssimo sinal;
       * Data de Criação: Domínios recém criados são extremamente suspeitos
       * Data de Atualização: Domínios não renovados e/ou não atualizados indicam um problema sério;
2. **Analise os Links e URLs**:
   * Ao se deparar com links e URLs no e-mail, faremos um processo mais detalhado e seguro para analisar este conteúdo, pois não podemos acionar nenhum link presente neste email, pois isso pode disparar o processo de instalação de malwares e afins. Para isso podemos fazer de algumas formas, como:
     * A primeira forma de se verificar a URL é passando o mouse sobre os links no e-mail (sem clicar) para ver o URL real, caso a URL real seja diferente precisamos acender um alerta e seguir para o próximo passo apenas se quisermos garantir;
     * Abrir o e-mail na forma de "ver original" ou "ver codigo-fonte";
       * procurar por elementos como \<a href=\[URL]>;
       * copiar a URL ;
       * fazer o processo de verificação de URLs que mencionei acima (através do VirusTotal e do IPVoid, mas aqui pode-se fazer necessário verificar estes links através de sandboxing, para podemos utilizar as ferramentas AnyRun (disponível em [https://app.any.run/](https://app.any.run/)), URL Scanner da Cloudflare Radar (disponível em [https://radar.cloudflare.com/scan](https://radar.cloudflare.com/scan)), Hybrid Analysis (disponível em [https://www.hybrid-analysis.com/](https://www.hybrid-analysis.com/)) e URLScan (disponível em [https://urlscan.io/](https://urlscan.io/));&#x20;
3. **Examinando os Anexos**:
   * O ideal é não abrir os anexos presentes em emails, até mesmo baixar pode ser um risco, mas caso este documento tenha muita necessidade de ser aberto podemos baixá-lo e utilizar as ferramentas de análise presentes nas ferramentas como AnyRun, ClouldFlare, Hybrid Analysis locais também;&#x20;

Aqui podemos verificar um questionário desenvolvido com base no conteúdo apresentado acima e com propósito de facilitar a busca por pontos congruentes ou incongruentes em e-mails, sendo resultado do estudo deste conteúdo e proposta de criação de um possível "framework for dummies".\
Este questionário funciona da seguinte forma: quanto mais fundo o usuário precisar chegar, mais riscos pode estar correndo, porém, quanto mais elementos selecionar, mais seguro pode estar de que aquele e-mail não se trata de um phishing.\
\
Abaixo segue um exemplo do questionário ainda em formato de protótipo ou 'para beta-testers':

* [ ] Remetente: contato@exemplo.com.br
* [ ] Domínio: exemplo.com.br
* [ ] Find Website IP: 192.168.10.2 / 192.168.20.2
* [ ] WHOIS ⇒  IP
  * [ ] registrador parece ser confiável?
  * [ ] titular parece ser confiável?
  * [ ] data de criação é coerente?
  * [ ] data de modificação é coerente?
  * [ ] vencimento está próximo?
  * [ ] algo suspeito na parte de DNS?
* [ ] WHOIS ⇒ Domínio
  * [ ] registrador parece ser confiável?
  * [ ] titular parece ser confiável?
  * [ ] data de criação é coerente?
  * [ ] data de modificação é coerente?
  * [ ] vencimento está próximo?
  * [ ] algo suspeito na parte de DNS?
* [ ] Sender IP | SPF IP: 192.168.10.2
  * [ ] é o IP do domínio de origem?
  * [ ] SPF Records
    * [ ] IP encontrado no range dos valores?
  * [ ] Virus total
    * [ ] o IP é confiável?
  * [ ] scans de URL
    * [ ] o domínio é confiável?
* [ ] Content-Type:
  * [ ] text/plain
    * [ ] text/html
      * [ ] multipart/mixed
        * [ ] multipart/alternative
          * [ ] multipart/related
            * [ ] multipart/report
* [ ] Possui documento anexado
  * [ ] Preciso deste documento?
  * [ ] Preciso abrir este documento?
    * [ ] VirusTotal
      * [ ] o documento é confiável?
    * [ ] AnyRun
      * [ ] o documento é confiável?
    * [ ] HybridAnalysis
      * [ ] o documento é confiável?
* [ ] Estou disposto a correr este risco

Espero que este conteúdo tenha lhe auxiliado a ter melhor compreensão e a facilitar a tomada de decisão se um email é seguro ou não para se confiar. Preciso ressaltar que nada aqui é uma verdade absoluta, pois os atacantes são muito sofisticados e podem burlar diversos destes elementos



Fontes:\
[https://www.forensicsinsider.com/digital-forensics/email-header-analysis/](https://www.forensicsinsider.com/digital-forensics/email-header-analysis/)

[https://live.paloaltonetworks.com/t5/community-blogs/choosing-the-right-metadata-for-phishing-and-email-incidents/ba-p/532746](https://live.paloaltonetworks.com/t5/community-blogs/choosing-the-right-metadata-for-phishing-and-email-incidents/ba-p/532746)

[https://www.mailxaminer.com/blog/email-metadata-analysis/](https://www.mailxaminer.com/blog/email-metadata-analysis/)
