
# Flask Application Launcher Instructions

## Windows

### Create a Batch File
1. Write a batch file that starts your Flask app and then opens your default web browser to the Flask app's URL.
2. Create a file named `start_app.bat` with the following content:

   ```batch
   @echo off
   cd /d %~dp0
   echo Starting the Flask server...
   start /B python app.py
   echo Opening the browser...
   start http://127.0.0.1:5000
   ```

### Create a Desktop Shortcut
1. Right-click on your desktop, select "New", and then "Shortcut".
2. In the location field, enter the path to your batch file (e.g., `C:\path\to\your\start_app.bat`).
3. Name the shortcut appropriately, like "Start Flask App".

## macOS

### Create a Shell Script
1. Open a text editor and create a new file named `start_app.sh` with the following content:

   ```bash
   #!/bin/bash
   cd "$(dirname "$0")"
   echo "Starting the Flask server..."
   python app.py &
   echo "Opening the browser..."
   open http://127.0.0.1:5000
   ```

2. Save the script and make it executable by running `chmod +x start_app.sh` in the terminal.

### Create an Automator App
1. Open Automator and create a new "Application".
2. Drag "Run Shell Script" into the workflow.
3. Paste the path to your script (e.g., `/path/to/start_app.sh`) in the shell script area.
4. Save the Automator application to your Desktop or Applications folder.

## Linux

### Create a Shell Script
1. Create a file named `start_app.sh` with similar content as for macOS:

   ```bash
   #!/bin/bash
   cd "$(dirname "$0")"
   echo "Starting the Flask server..."
   python app.py &
   echo "Opening the browser..."
   xdg-open http://127.0.0.1:5000
   ```

2. Make it executable: `chmod +x start_app.sh`.

### Create a Desktop Entry
1. Create a file on your Desktop named `flask_app.desktop` with the following content:

   ```ini
   [Desktop Entry]
   Type=Application
   Terminal=false
   Name=Flask App
   Exec=/path/to/start_app.sh
   Icon=application-default-icon
   ```

2. Make sure the `Exec` path is correct and points to your shell script.
