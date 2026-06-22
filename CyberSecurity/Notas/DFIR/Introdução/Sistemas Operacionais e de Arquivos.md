---
Created: 2026-01-05T22:24
Criado em: 2026-01-05T22:24
Criado em 1: 2026-01-05T22:24
Criado por: 2026-01-05T22:24
Module Code: DFIR
---
# 📝 Sistemas Operacionais e de Arquivos
Sistema operacional é o software fundamental que atua como intermediário entre o usuário e o hardware do dispositivo, gerenciando recursos como memória, processador e dispositivos de entrada/saída, e criando uma plataforma para que outros programas funcionem, tornando o uso do computador, celular ou tablet possível e intuitivo, sem a necessidade de conhecer a complexidade do hardware. Exemplos comuns são Windows, macOS, Linux, Android e iOS, que permitem desde abrir aplicativos até acessar a internet. 
Sistemas de arquivos são formas em que os arquivos podem ser organizados para um bom desempenho e robustez do sistema como um todo.
Imagine que temos diversos documentos que precisamos organizar, mas não apenas organizar cada um em uma caixinha, porque alguns desses papéis são credenciais de acesso, crachás por exemplo, que permitem nosso acesso ao ambiente.  
Outros documentos são fotos, que terão sua caixa correta e identificada, outros documentos são certificados de compra de produtos, por exemplo.
Todos esses documentos serão organizados e ao organizar cada um devemos salvar também um indicador de onde estamos salvando os arquivos (a caixa e a posição do arquivo), isso para podermos encontrar novamente os documentos quando precisarmos procurar.  
  
Para compreendermos sistemas de arquivos precisamos compreender que eles se distinguem em sistemas operacionais.  
  
Para falar um pouco sobre os principais que eu adoto vou deixar um trecho informando a aplicabilidade deles em nosso tema:
## 🐧 Unix Like

> [!important] 🗣️ **Opinião**: Meus sistemas favoritos são provenientes do Unix
Sistemas Linux são frequentemente a escolha para a estaçao de trabalho do perito forense e essenciais para investigar servidores e infraestrutura de nuvem.
- **Segurança e Bloqueio de Escrita:** Distros como **CAINE** são configuradas para montar mídias apenas em modo de leitura (_read-only_) por padrão, protegendo a integridade da evidência.
- **Poder de Linha de Comando:** Ferramentas nativas como `dd` (aquisição), `grep` (busca), `find` e `awk` permitem analisar dados com uma rapidez que interfaces gráficas raramente alcançam.
- **Análise de Servidores:** Investigar um sistema Unix envolve analisar logs centralizados em `/var/log` (auth.log, syslog) e o histórico de comandos (`.bash_history`), cruciais em casos de intrusão.
- **Sistemas de Arquivos:** O suporte nativo a múltiplos sistemas (Ext4, XFS, Btrfs, ZFS) torna o Linux a plataforma superior para montar e explorar imagens de disco complexas.
## 🪟 WIndows

> [!important] ⚠️ **DIca**: Como é o mais usado também é o mais atacado 😁
O Windows é o alvo principal devido à sua onipresença. Sua utilidade forense reside na abundância de artefatos de persistência e atividade do usuário.
- **Registro do Windows (Registry):** O "santo graal" da forense Windows. Contém evidências de dispositivos USB conectados, softwares instalados, redes acessadas e configurações de sistema.
- **Artefatos de Execução:** Arquivos Prefetch, Shimcache e Amcache permitem provar que um programa foi executado, mesmo que tenha sido deletado.
- **Rastros de Atividade:** LNK files e Jump Lists mostram quais arquivos o usuário abriu recentemente e de onde (ex: rede, pen drive).
- **Shadow Copies (VSS):** Permite recuperar versões anteriores de arquivos e configurações, agindo como uma "máquina do tempo" nativa.
  
Aqui veremos um pouco de cada um desses pontos, pra deixar nosso conteúdo robusto e eficiente.
  
---
## 💾 File Systems

> [!important] ⚠️ **DIca**: Pela parte do [[CyberSecurity/Notas/DFIR/Windows/Windows|Windows]] temos FATx e NTFS, sendo que existe toda uma jornada de evolução, passando por FAT16, FAT32 e por fim NTFS, sendo uma versão mais moderna e segura.
Nisso temos alguns padrões de organizações desses arquivos de forma lógica dentro de nossos [[CyberSecurity/Notas/PENTESTING/Windows/Sistemas Operacionais|Sistemas Operacionais]].