@echo off
cd /d "%~dp0"
echo.
echo   Starting local preview server...
echo   Address: http://localhost:4173/
echo   Close this window to stop the server.
echo.
start "" powershell -NoProfile -WindowStyle Hidden -Command "Start-Sleep 4; Start-Process 'http://localhost:4173/'"
call npm run preview
