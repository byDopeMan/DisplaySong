@echo off
echo 🔨 Erstelle version.txt...
python write_version_txt.py

echo 🔨 Baue Projekt...

REM Alte Builds entfernen
rmdir /s /q build
rmdir /s /q dist

REM Build mit PyInstaller
pyinstaller install.spec

REM Signiere die EXE
echo 🔏 Signiere EXE...
pause
