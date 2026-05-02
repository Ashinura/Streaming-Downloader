@echo off

:: UTF-8 
chcp 65001 >nul

:: Racine du .bat (projet)
cd /d "%~dp0"

:: Vérification .venv
if not exist ".venv\Scripts\activate.bat" (
    echo [ERROR] - Le .venv n'existe pas. Lancez utils\setup.txt d'abord.
    pause
    exit /b 1
)

echo [INFO] - Activation du .venv...
call .venv\Scripts\activate.bat

echo [INFO] - Lancement de Streaming-Downloader...
python StrDL.py