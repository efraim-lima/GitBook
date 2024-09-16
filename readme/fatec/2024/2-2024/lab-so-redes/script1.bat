@echo off
cls

set /p nome= Insira um nome: 
echo %nome%
pause

find "%nome%" nomes.txt

if %errorlevel% == 0 (
	echo %nome% encontrado
) else (
	echo %nome% não encontrado
echo %nome% >> nomes.txt
)
pause
cls