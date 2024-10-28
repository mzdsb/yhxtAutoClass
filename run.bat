@echo off

REM 检查虚拟环境是否存在，如果不存在则创建虚拟环境
if not exist "helloWorld\Scripts\activate" (
    echo Creating virtual environment...
    python -m venv helloWorld
    if errorlevel 1 (
        echo Failed to create virtual environment.
        pause
        exit /b
    )
)

REM 激活虚拟环境
call helloWorld\Scripts\activate
if errorlevel 1 (
    echo Failed to activate virtual environment.
    pause
    exit /b
)

REM 安装依赖项
echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install dependencies.
    pause
    exit /b
)

REM 设置 Flask 应用为开发者模式并启动应用
echo Setting up Flask developer environment...
set FLASK_APP=app.py
set FLASK_DEBUG=1
python -m flask run
if errorlevel 1 (
    echo Failed to start Flask application.
    pause
    exit /b
)

REM 暂停命令行窗口，等待用户按下任意键
pause
