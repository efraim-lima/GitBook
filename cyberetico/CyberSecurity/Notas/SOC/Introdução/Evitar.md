---
Created: 2026-01-14T22:04
Criado em: 2026-01-14T22:04
Criado em 1: 2026-01-14T22:04
Criado por: 2026-01-14T22:04
Module Code: SOC
---
# 🛠️ Evitar
## 📌Evitar no Processo de Analista de SOC
Alguns habitos e dependências devem ser evitados para quem depende atuar em um setor de [[CyberSecurity/Notas/SOC|SOC]]
  
EVITAR
- Fazer analises de Malware apressadas em [[CyberSecurity/Notas/SOC/Introdução/Ferramentas|Ferramentas]] de Sandbox
- Análise de [[CyberSecurity/Course/forense/logs/logs|logs]] inadequada
- Ignorar datas do VirusTotal
## ⚠️VirusTotal
Dependência excessiva de [[CyberSecurity/Notas/SOC/Introdução/Ferramentas|Ferramentas]] como VirusTotal

> [!important]
> 
> Maneiras de evitar falhas por conta disso
> 
> - Verificar de forma atenta as URLs dos arquivos presentes na análise (não confiar apenas na tag verde)
> 
> - Ter em mente que um arquivo malicioso pode não ter sido detectado por Antivirus previamente acompanhar
> 
> > [![[info]]] VirusTotal is not an Incident Responder  
> > This post reveals how VirusTotal is just a tool that aids in analysis and should not be a “one-stop-shop” in determining malicious content  
> > [https://medium.com/maverislabs/virustotal-is-not-an-incident-responder-80a6bb687eb9#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjdiZjU5NTQ4OWEwYmIxNThiMDg1ZTIzZTdiNTJiZjk4OTFlMDQ1MzgiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTc1NzU4OTI5MzA0MTg5MjA0NDgiLCJlbWFpbCI6ImVmcmFpbS5hbGltYUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibm9uY2UiOiJub3RfcHJvdmlkZWQiLCJuYmYiOjE3Njg0MzkzODQsIm5hbWUiOiJFZnJhaW0gTGltYSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NMYXJ5VE1jcXRhejdaalB2T2ZKQjBfWG10V0FoWE5WYTJVVThLN1lObE9jWlRib3NFYT1zOTYtYyIsImdpdmVuX25hbWUiOiJFZnJhaW0iLCJmYW1pbHlfbmFtZSI6IkxpbWEiLCJpYXQiOjE3Njg0Mzk2ODQsImV4cCI6MTc2ODQ0MzI4NCwianRpIjoiNjQ5YzlkMzU3MTE1NWUzMWY1MzkwOTFkMDc1MzkyYmQ5MzRiZGMwMCJ9.KQN4ukzOkmuib8ka_3iRJRGBGRZ1kLnJhfqGOnZUXTCWKE7o2Z5PCkDTQ5Tsrb9Rkp0nK0z-s8Qk_1a2AEqyvgwxG_ggoML2wyR_hiIV588us883rsfCWGMjN_vZxvT92OGMZjAb7-zIJJOAZZVgvZpuFpceFRVrXsV7usjRiKIH64P9JIR7rcYdf5Hn-Gutxit9gn--FvCISJPRAZlB8VA-0gXiq6g0J4StlYanrQ7Lj5LBlkaaXwdUpx-HeGvmiO_avo2juM3Y_GVH2pT1NbBNmx16MO93VbOVcRqlYMUOvu79AnD3bhXojIBUKMMnPKMKsSRUeCCtz3uxVp6dBQ](https://medium.com/maverislabs/virustotal-is-not-an-incident-responder-80a6bb687eb9#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjdiZjU5NTQ4OWEwYmIxNThiMDg1ZTIzZTdiNTJiZjk4OTFlMDQ1MzgiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTc1NzU4OTI5MzA0MTg5MjA0NDgiLCJlbWFpbCI6ImVmcmFpbS5hbGltYUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibm9uY2UiOiJub3RfcHJvdmlkZWQiLCJuYmYiOjE3Njg0MzkzODQsIm5hbWUiOiJFZnJhaW0gTGltYSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NMYXJ5VE1jcXRhejdaalB2T2ZKQjBfWG10V0FoWE5WYTJVVThLN1lObE9jWlRib3NFYT1zOTYtYyIsImdpdmVuX25hbWUiOiJFZnJhaW0iLCJmYW1pbHlfbmFtZSI6IkxpbWEiLCJpYXQiOjE3Njg0Mzk2ODQsImV4cCI6MTc2ODQ0MzI4NCwianRpIjoiNjQ5YzlkMzU3MTE1NWUzMWY1MzkwOTFkMDc1MzkyYmQ5MzRiZGMwMCJ9.KQN4ukzOkmuib8ka_3iRJRGBGRZ1kLnJhfqGOnZUXTCWKE7o2Z5PCkDTQ5Tsrb9Rkp0nK0z-s8Qk_1a2AEqyvgwxG_ggoML2wyR_hiIV588us883rsfCWGMjN_vZxvT92OGMZjAb7-zIJJOAZZVgvZpuFpceFRVrXsV7usjRiKIH64P9JIR7rcYdf5Hn-Gutxit9gn--FvCISJPRAZlB8VA-0gXiq6g0J4StlYanrQ7Lj5LBlkaaXwdUpx-HeGvmiO_avo2juM3Y_GVH2pT1NbBNmx16MO93VbOVcRqlYMUOvu79AnD3bhXojIBUKMMnPKMKsSRUeCCtz3uxVp6dBQ)  
> 
>   
## ⚠️Analise de Malware
Fazer analises de Malware apressadas em [[CyberSecurity/Notas/SOC/Introdução/Ferramentas|Ferramentas]] de Sandbox

> [!important]
> 
> Maneiras de evitar falhas por conta disso
> 
> - Analises curtas não podem conduzir toda a gama de informações necessárias para uma boa analise
> 
> - [[CyberSecurity/Course/tools/malwares|malwares]] ja conseguem detectar execução em sandboxes e não trigam funções maliciosas no ambiente
> 
> - Muitos [[CyberSecurity/Course/tools/malwares|malwares]] utilizam disparos programados (bomba relógio) para evitar fácil detecção
> 
> - Utilizar um ambiente real (como uma maquina virtual e, muitas vezes até mesmo uma maquina exclusiva)