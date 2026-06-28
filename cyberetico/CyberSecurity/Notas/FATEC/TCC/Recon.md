---
Created: 2026-04-01T17:44
Criado em: 2026-04-01T17:44
Criado em 1: 2026-04-01T17:44
Criado por: 2026-04-01T17:44
---
## Identificando brechas externas
### Uso de nmap para verificar especificamente as portas mais sensíveis do servidor
Para validarmos as [[portas]] abertas e ativas no ambiente do servidor utilizamos o comando nmap aguerrido de alguns parametros e [[portas]] pré-estabelecidas para validarmos como está a saúde do ambiente.
![[image 28.png|image 28.png]]
Transcrição:  

> ──(root㉿1388d58b300a)-[/]  
> └─# nmap -sV -sC -p 8501,3333,22 192.168.15.24  
> Starting Nmap 7.98 ( [https://nmap.org](https://nmap.org/) ) at [[reports/2026/2026|2026]]-04-01 20:45 +0000  
> Nmap scan report for 192.168.15.24  
> Host is up (0.00059s latency).
> 
> PORT STATE SERVICE VERSION  
> 22/[[tcp]] open ssh OpenSSH 9.6p1 Ubuntu 3ubuntu13.15 (Ubuntu [[CyberSecurity/Notas/DFIR/Unix Like/Linux|Linux]]; protocol 2.0)  
> | ssh-hostkey:  
> | 256 c3:eb:be:38:f0:d5:a8:1e:1d:3f:52:74:95:70:15:80 (ECDSA)  
> |_ 256 f5:c7:44:a8:98:5f:0c:2c:04:26:25:eb:9c:2f:7a:71 (ED25519)  
> 3333/[[tcp]] open http Uvicorn  
> |_http-title: Site doesn't have a title (text/plain; charset=utf-8).  
> |_http-server-header: uvicorn  
> 8501/[[tcp]] open http Tornado httpd 6.5.5  
> |_http-title: Streamlit  
> |_http-server-header: TornadoServer/6.5.5  
> Service [[info]]: [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]]: [[CyberSecurity/Notas/DFIR/Unix Like/Linux|Linux]]; CPE: cpe:/o:[[CyberSecurity/Notas/DFIR/Unix Like/Linux|Linux]]:linux_kernel
> 
> Service detection performed. Please report any incorrect results at [https://nmap.org/submit/](https://nmap.org/submit/) .  
> Nmap done: 1 IP address (1 host up) scanned in 7.37 seconds