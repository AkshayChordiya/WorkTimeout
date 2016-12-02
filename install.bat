@echo off
rem INSTALL.BAT - Easy installer for Python

echo "Checking for Python...."
rem 1) test if python.exe is in the path:

python.exe --version >NUL 2>&1
if errorlevel 1 goto error

echo "Python found"
echo "Installing dependencies"
pip install virtualenv
virtualenv workenv
workenv\Scripts\pip.exe install easygui
xcopy timeout.bat %userprofile%\Start Menu\Programs\Startup\
pause

:ERROR
echo.
echo You need to install python and pip
REM pause
