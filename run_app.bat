@echo off
title Plant Disease Classifier - Streamlit App
echo ========================================================
echo   Starting Plant Disease Classifier (Streamlit Web App)
echo ========================================================
echo.

cd /d "%~dp0"

echo Checking Streamlit installation...
python -m streamlit --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Streamlit not found. Installing requirements...
    pip install -r requirements.txt
)

echo.
echo Launching Streamlit web application in your browser...
echo.
python -m streamlit run app.py

pause
