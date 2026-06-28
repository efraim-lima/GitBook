---
Created: 2026-03-10T21:27
Criado em: 2026-03-10T21:27
Criado em 1: 2026-03-10T21:27
Criado por: 2026-03-10T21:27
---
Utilize [[CyberSecurity/Notas/SOC/Introdução/Ferramentas|Ferramentas]] como whois, ping, host, dnsenum, dnsrecon, wafwoof, e técnicas de Google Hacking para responder às perguntas abaixo. Você pode usar o Kali [[CyberSecurity/Notas/DFIR/Unix Like/Linux|Linux]] ou sites como [who.is](http://who.is/), [crt.sh](http://crt.sh/), e [registro.br](http://registro.br/).  
Sites utilizados no experimento:
- [Example.com](http://example.com/)
- [www.bancocn.com](http://www.bancocn.com/)
  
1. **Como obter informações de um domínio através do terminal do Kali?**
R.: Podemos utilizar [[CyberSecurity/Notas/SOC/Introdução/Ferramentas|Ferramentas]] como ping, traceroute, dig, nmap, whois, dnsenum, dnsrecon, wafwoof, whatweb, entre outras.  
  
O ping pode ser utilizado para descobrir o IP de um website (ao menos o IP exposto a nós.  
Ex.:
![[image 31.png|image 31.png]]
O traceroute nos auxilia a compreender [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] saltos e nodes entre a origem do emissor e nosso alvo, podendo nos dar indícios de algum tipo de WAF, Firewalls, Proxyes ou CDNs no meio do caminho.  
Ex.: Com o traceroute no domínio chegamos a um IP que não apareceu anteriormente neste caso, podendo ser um resultado de Anycast referente ao BGP, redirecionamento do CDN ou até mesmo ser efeito de algum proxy no meio do caminho  
![[image 1 4.png|image 1 4.png]]
Seguindo, podemos determinar também dados dos proprietários e também do dns, com [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] demais [[comandos]] assim como [[portas]] abertas, serviços e tecnologias utilizadas
  
1. **Como buscar informações em domínio internacionais? Qual melhor forma de obter essas informações?**
R.: Para este caso aqui podemos utilizar o whois, este protocolo compila as informações presentes em registradores de todo o mundo (GoDaddy, registro.br, etcs), o whois consulta bancos de dados de registro e puxa informações inerentes aos registros e nos exibe de forma estruturada.  
Ex.:
![[image 2 4.png|image 2 4.png]]
1. **Como buscar informações em domínio .br? Qual melhor forma de obter essas informações?**
R.: Da mesma forma como mencionado acima, o whois compila informações de domínios .br também, sendo uma ferramenta muito eficiente para a coleta de informações de websites.
1. **verificar se um site possui um firewall WAF ativo?**
R.: Para este caso podemos utilizar o comando wafwoof, que basicamente faz a varredura para nós e determina a presença de algum WAF no ambiente até nosso alvo. Como podemos ver que nosso [bancocn.com](http://bancocn.com) está atrás da [[Cloudflare]] WAF, algo que pode exemplificar nossos IPs discrepantes entre ping e traceroute.  
Ex.:  
![[image 3 3.png|image 3 3.png]]
1. **Como descobrir subdomínios utilizando a técnica brute force em um processo de footpring?**
R.: Aqui podemos utilizar a ferramenta dnsrecon, para poder levantar dados de subdominios
Ex.:
![[image 4 3.png|image 4 3.png]]
1. **Explique qual é a função do arquivo robots.txt, qual a sua importância e utilidades.**
O arquivo Robots.txt se trata de um arquivo que determina as permissões de acesso a determinadas páginas a BOTs na web, tendo alguns bots que podem ser bem vindos como [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] spiders/crawlers de indexadores na web (Google, DuckDuckGo, Yahoo, etc). A critérios de seguraça o robots.txt pode indicar paginas e outras áreas de um site que o proprietário não quer que sejam acessadas podendo ser fonte de reconhecimento do alvo.  
Ex.:
![[image 5 2.png|image 5 2.png]]
No exemplo acima conseguimos observar que o website permite o rastreio por todos user-[[AGENTS]], mas não permite acesso à path /admin.
1. **Como buscar subdomínios usando certificados SSL públicos?**
R.: Para isso podemos acessar a página [crt.sh](http://crt.sh) e inserir o domínio alvo na página, assim podemos levantar algumas informações de domínios e subdomínios.
![[image 6 2.png|image 6 2.png]]
1. **Como buscar IPs associados ao domínio que está sendo investigado?**
R.: para a coleta de IPs de um alvo eu gosto de usar 2 [[comandos]]: dig e host, basicamente o resultado foram [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] abaixo.  
Ex.:
![[image 7 2.png|image 7 2.png]]
![[image 8 2.png|image 8 2.png]]
1. **Como utilizar o Google para encontrar páginas específicas de um site?**
Podemos utilizar Google Dorks para levantar as possíveis páginas de um site no modelo:  
site:google.com intitle::login | inurl:contact  
  
Para este exemplo utilizei o alvo como o próprio Google devido a ausencia de elementos semelhantes nos nossos sites alvo.  
![[image 9 2.png|image 9 2.png]]
1. **Qual ferramenta pode ser usada para buscar registros DNS em um determinado domínio e qual é a sua abrangência?**
R.: Podemos utilizar [[CyberSecurity/Notas/SOC/Introdução/Ferramentas|Ferramentas]] como o dnsrecon e dig.
![[image 10 2.png|image 10 2.png]]
![[image 11 2.png|image 11 2.png]]
![[image 12 2.png|image 12 2.png]]