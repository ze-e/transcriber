@echo off

IF NOT EXIST env (
    echo Creating virtual environment...
    python -m venv env
    call env\Scripts\activate
    echo Installing dependencies...
    pip install -r requirements.txt
) ELSE (
    echo Activating existing virtual environment...
    call env\Scripts\activate
)

echo Starting Flask app...
start cmd /k "python app.py"
timeout /t 10
start http://127.0.0.1:5000
