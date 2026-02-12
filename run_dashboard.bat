@echo off
REM Run the E-Commerce dashboard. Double-click this file or run from terminal.
cd /d "%~dp0"
echo Starting dashboard... Keep this window open.
echo.
streamlit run scripts/dashboard_app.py
if errorlevel 1 (
    echo.
    echo Something went wrong. Make sure you ran: pip install -r requirements.txt
    pause
)
