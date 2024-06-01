@echo off

:: Activate the virtual environment
call lorareader\Scripts\activate

:: Run the Flask application
python lorareader.py

:: Keep the window open
pause