@echo off
echo.
echo  ======================================================
echo   Nerdy AI Hackathon Suite — Local Development Server
echo  ======================================================
echo.

:: Check python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not found in PATH. Please install Python 3.10+
    pause
    exit /b 1
)

:: Install dependencies if needed
pip show fastapi >nul 2>&1 || (
    echo  Installing dependencies from requirements.txt...
    pip install -r requirements.txt
)

echo  Starting server at http://127.0.0.1:8765
echo  Opening browser to test\index.html...
echo.

start http://127.0.0.1:8765
python server.py
