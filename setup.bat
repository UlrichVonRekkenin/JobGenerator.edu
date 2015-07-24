@echo off

REM Build *.exe file and all requirements libraries by cx_Freeze
py -3 setup.py build_exe

REM Build an installation file by Inno Setup
compil32 /cc setup.iss

REM Run builded file
cd setup
"Setup-Task Generator-1.0.0.exe"
cd ..
