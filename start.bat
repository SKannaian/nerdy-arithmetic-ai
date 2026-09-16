@echo off
title Nerdy Arithmetic AI — K-5 Socratic Math Platform
color 0B

echo ======================================================================
echo           NERDY ARITHMETIC AI — K-5 SOCRATIC MATH GAME
echo              IXL-Inspired Cognitive Math Platform
echo ======================================================================
echo.

cd /d "%~dp0"

echo [1/3] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python was not found in your PATH.
    echo Please install Python 3.10+ from https://www.python.org/
    pause
    exit /b 1
)

echo [2/3] Checking dependencies...
pip install -q fastapi uvicorn pydantic python-dotenv google-genai

echo [3/3] Launching Nerdy Arithmetic AI server...
echo.
echo Opening browser to http://localhost:8765 ...
start http://localhost:8765

python server.py

pause
