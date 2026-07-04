---
Created: 2026-04-26T10:35
Criado em: 2026-04-26T10:35
Criado em 1: 2026-04-26T10:35
Criado por: 2026-04-26T10:35
---
## Especificações de Máquina
Ubuntu Server 20.4
4Gb RAM
50.9GB Armazenamento
  
![[image 30.png|image 30.png]]
![[image 1 3.png|image 1 3.png]]
![[image 2 3.png|image 2 3.png]]
Foi seguido o processo de instalação do docker, kubectl e demais dependencias do Agentk normalmente, em seguida foram seguidos alguns passos antes de usar docker compose.  
  
Foram feitos [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] seguintes passos para limpar espaço em disco, algo necessário para que possamos baixar o modelo de LLM ollama e também qwen.  
  
Limpa imagens, contêineres e volumes não utilizados do Docker
sudo docker system prune -a --volumes -y
Limpa o cache de pacotes baixados do sistema (APT)
sudo apt clean && sudo apt autoremove -y
Limpa [[CyberSecurity/Course/forense/logs/logs|logs]] de sistema muito antigos (deixa apenas [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] últimos 3 dias)
sudo journalctl --vacuum-time=3d
_# Verifica se há espaço livre no Volume Group (VFree)_
sudo vgs
_# Se houver espaço livre, você pode expandir o disco para usar 100% dele:_
sudo lvextend -l +100%FREE /[[DEV]]/mapper/ubuntu--vg-ubuntu--lv
_# E então redimensionar o sistema de arquivos para reconhecer o novo espaço:_
sudo resize2fs /[[DEV]]/mapper/ubuntu--vg-ubuntu--lv