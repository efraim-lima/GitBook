@echo off
CHCP 65001
cls

echo ╔════════════════════════════════════════════╗
echo ║  Script da Atividade de Laboratorio de OS  ║
echo ╚════════════════════════════════════════════╝
echo.
echo                    *****
echo.
echo   Olá, %username%.
echo   Você está utilizando:
echo   - Sistema operacional: %os%
echo   - Nome do seu servidor: %logonserver%
echo   - Arquitetura: %processor_architecture%
echo   - Numero de processadores: %number_of_processors%
echo   - Data e Hora: %date% ; %time%
echo.
echo                    *****
echo.
pause
cls

goto init

:init
rem fazer moldura para todos outputs e comunicação com o usuário
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  Este é seu menu principal, por favor escolha uma das opções. ║
echo ║  Digite:                                                      ║
echo ║  - [L] para listar arquivos temporarios                       ║
echo ║  - [A] para listar arquivos de aplicativos                    ║
echo ║  - [D] para listar arquivos locais de aplicativos             ║
echo ║  - [E] para sair                                              ║
echo ╚═══════════════════════════════════════════════════════════════╝
choice /C:LADE
echo.

if %errorlevel% == 1 (
echo.
goto lister
)
if %errorlevel% == 2 (
echo.
goto timer
)
if %errorlevel% == 3 (
echo.
goto dating
)
if %errorlevel% == 4 (
echo.
goto fim
)

:lister
echo ╔═════════════════════════════════════╗
echo ║  Listando o conteúdo do diretório   ║
echo ╚═════════════════════════════════════╝
echo.
echo                 *****
echo.
echo Você está no diretório: %tmp%
echo.
echo                 *****
echo.
echo **verificar a possibilidade de malware nestes arquivos
pause
dir %tmp%
pause
cls
goto init

:timer
echo ╔════════════════════════════════════╗
echo ║  Listando o conteúdo do diretório  ║
echo ╚════════════════════════════════════╝
echo.
echo                 *****
echo.
echo Você está no diretório: %appdata%
echo.
echo                 *****
echo.
dir %appdata%
pause
cls
goto init

:dating
echo ╔════════════════════════════════════╗
echo ║  Listando o conteúdo do diretório  ║
echo ╚════════════════════════════════════╝
echo.
echo                 *****
echo.
echo Você está no diretório: %localappdata%
echo.
echo                 *****
echo.
dir %localappdata%
pause
cls
goto init

:fim
echo ╔═══════════════════╗
echo ║  Chegamos ao fim  ║
echo ╚═══════════════════╝
pause
cls
exit
