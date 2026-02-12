@echo off
REM Run this AFTER creating the repo on GitHub (see PUSH_TO_GITHUB.md)
cd /d "%~dp0"

echo Checking git...
git status 2>nul
if errorlevel 1 (
    echo Initializing git...
    git init
    git add .
    git commit -m "E-Commerce Sales Funnel & Product Insights - full project"
    git branch -M main
    echo.
    echo Now add your remote and push:
    echo   git remote add origin https://github.com/svegesa2/ecommerce-sales-funnel.git
    echo   git push -u origin main
    echo.
    echo Create the repo first at: https://github.com/new
    echo Name it: ecommerce-sales-funnel
) else (
    git add .
    git status
    echo.
    echo To commit and push, run:
    echo   git commit -m "Your message"
    echo   git push
)
pause
