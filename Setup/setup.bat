@echo off


echo [96mDownload package: 'virtualenv'   -   Step 1/7[0m
python -m pip install virtualenv
if %ERRORLEVEL% neq 0 (
    echo Error in installation of 'virtualenv'.
    pausez
    exit /b 1
)
cls
echo [92mSucess [Step 1/7][0m 



echo [96mCreate virtual environnement   -   Step 2/7 [0m
python -c "from setup import create_venv; create_venv()"
if %ERRORLEVEL% neq 0 (
    echo Error while create the virtual environnement.
    pause
    exit /b 1
)
cls
echo [92mSucess [Step 2/7][0m 


echo [96mActivate virtual environnement   -   Step 3/7[0m
call ..\.venv\Str-DL\Scripts\activate.bat
if %ERRORLEVEL% neq 0 (
    echo Error while trying to activate virtual environnement.
    pause
    exit /b 1
)
cls
echo [92mSucess [Step 3/7][0m 


echo [96mSearch for pip updates   -   Step 4/7[0m
..\.venv\Str-DL\Scripts\python.exe -m pip install --upgrade pip
if %ERRORLEVEL% neq 0 (
    echo Error while update 'pip'.
    pause
    exit /b 1
)
cls
echo [92mSucess [Step 4/7][0m 


echo [96mPackages installation   -   Step 5/7[0m
..\.venv\Str-DL\Scripts\python.exe -m pip install -r requirements.txt
if %ERRORLEVEL% neq 0 (
    echo Error while packages installation.
    pause
    exit /b 1
)
cls
echo [92mSucess [Step 5/7][0m 


echo [96mFFmpeg installation   -   Step 6/7[0m
spotdl --download-ffmpeg
if %ERRORLEVEL% neq 0 (
    echo Error in installation of FFmpeg.
    pause
    exit /b 1
)
cls
echo [92mSucess [Step 6/7][0m 


echo [96mAdding FFmpeg and Packages to PATH.   -   Step 7/7[0m
python -c "from setup import set_path; set_path()"
if %ERRORLEVEL% neq 0 (
    echo Error while added folder path to your USER PATH
    pause
    exit /b 1
)
echo [92mSucess [Step 7/7][0m 
pause
cls


echo [92mThe installation is now complete.[0m 
echo [93mYou need to restart your computer, restart now ? (y/n)[0m
set /p choix=
if /i "%choix%"=="y" (
    echo restart...
    shutdown /r /t 0
)