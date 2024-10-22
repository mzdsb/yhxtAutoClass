
@echo off
call helloWorld\Scripts\activate
if errorlevel 1 (
    echo
    pause
    exit /b
)
python app.py
pause
