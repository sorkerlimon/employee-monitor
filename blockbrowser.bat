@echo off

set "prefs_file=%LOCALAPPDATA%\Google\Chrome\User Data\Default\Preferences"

echo Changing Chrome preferences...

:: Check if the preferences file exists
if exist "%prefs_file%" (
    :: Search and replace the values in the preferences file
    powershell -Command "(Get-Content '%prefs_file%') -replace '\"credentials_enable_autosignin\": true,', '\"credentials_enable_autosignin\": false,' -replace '\"credentials_enable_service\": true,', '\"credentials_enable_service\": false,' | Set-Content '%prefs_file%'"
    
    echo Preferences updated successfully.
) else (
    echo Chrome preferences file not found.
)

pause
