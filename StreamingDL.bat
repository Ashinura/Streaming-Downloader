@echo off

call .\.venv\Str-DL\Scripts\activate.bat
if %ERRORLEVEL% neq 0 (
    echo Error while trying to activate virtual environnement.
    pause
    exit /b 1
)

start /max .\.venv\Str-DL\Scripts\python.exe ./StreamingDL.py