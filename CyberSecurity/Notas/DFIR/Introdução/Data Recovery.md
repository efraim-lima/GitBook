---
Created: 2026-01-05T22:21
Criado em: 2026-01-05T22:21
Criado em 1: 2026-01-05T22:21
Criado por: 2026-01-05T22:21
Module Code: DFIR
---
# 📝 **Recuperação de dados** 
Quando alguma coisa é deletada de forma intencional ou não, podemos recorrer a algumas técnicas de recuperação de dados. Podemos utilizar [[CyberSecurity/Notas/SOC/Introdução/Ferramentas|Ferramentas]] de terceiros ou até mesmo tentar fazer da forma mais manual.
Se a deleção foi em um HDD temos uma grande chance de recuperar esses dados, agora, se foi em um SSD as chances são bem menores.
## 📌 SSD

> [!important] ⚠️ **Lembre-se**: Aqui o processo de recuperação é muito difícil
Como SSDs armazenam [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] dados de forma elétrica nas células da memória flash NAND a perda de dados pode ocorrer devido ao desgaste da memória, falhas eletrônicas e erros lógicos.
Em caso de deleção, o uso do comando TRIM pode inviabilizar de forma perpétua a recuperação, o comando TRIM informa o [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] quando [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] blocos de dados não estão mais disponíveis, limpando as marcas logo em seguida.
Para este tipo de recuperação podemos utiliza:
- Stellar Data Recovery
- Ontrack EasyRecovery
Para recuperação de hardware podemos recorrer a
- leitores NAND,
- removedores de chip de memória,
- kits de reparos eletronicos
## 📌 HDD

> [!important] ⚠️ **Dica**: Geralmente conseguimos recuperar dados apagados com certa facilidade
Como sabemos [[CyberSecurity/fatec/Pesquisa/Pesquisa/ferramentas/os/os|os]] dados podem estar presentes no disco fisico e apenas seus apontamentos podem ter sido marcados como disponíveis nas tabelas File Allocation Table (FAT) ou Master File Table (MFT), por conta disso podemos recuperar arquivos com maior chances de sucesso.
Para este tipo de recuperação podemos utilizar as seguintes [[CyberSecurity/Notas/SOC/Introdução/Ferramentas|Ferramentas]]:
- TestDisk
- Recuva
- R-Studio
- EaseUS
Para recuperação de hardware podemos recorrer a
- [[CyberSecurity/Notas/SOC/Introdução/Ferramentas|Ferramentas]] da DeepSpar Disk Imager,
- condições de salas limpas,
- [[CyberSecurity/Notas/SOC/Introdução/Ferramentas|Ferramentas]] de micro-cirurgia