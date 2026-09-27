@echo off
echo ========================================================
echo Starting GlaucoFusion-XAI Django Web Server
echo ========================================================
echo.
python manage.py migrate
echo.
echo Starting development server on http://127.0.0.1:8000/
python manage.py runserver
pause
