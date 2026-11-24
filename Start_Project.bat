@echo off
title Multimedia Forgery Detection System
cd /d "%~dp0"
taskkill /f /im python.exe >nul 2>&1
echo Starting Forensic Server...
timeout /t 1 >nul
start "" http://127.0.0.1:8080
python app.py
pause