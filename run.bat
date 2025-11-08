@echo off
setlocal
set PORT=8000
set ROOT=%~dp0web

echo Serving "%ROOT%" on:
echo    - http://localhost:%PORT%/

rem Start the web server in a new window
pushd "%ROOT%"
start "Web Server" python -m http.server %PORT%
popd

rem Open the main page in the default browser
start "" http://localhost:%PORT%/index.html

echo Server starting... If the browser didn't open, visit http://localhost:%PORT%/
exit /b 0