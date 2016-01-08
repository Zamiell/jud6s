@echo off

rem Check to see if the user is using the default resources path
if not exist "C:\Program Files (x86)\Steam\SteamApps\common\The Binding of Isaac Rebirth\resources" (
	echo.
	echo ^+------------------------------------------------------------------------^+
	echo ^| ERROR: I could not find the Afterbirth resources folder at:            ^|
	echo ^|                                                                        ^|
	echo ^|        "C:\Program Files (x86)\Steam\SteamApps\common\                 |
	echo ^|         The Binding of Isaac Rebirth\resources\"                       |
	echo ^|                                                                        ^|
	echo ^|        You will have to install the mod manually by copying the        ^|
	echo ^|        contents of the directory with the ruleset that you want to     ^|
	echo ^|        play into the Afterbirth resources folder.                      ^|
	echo ^+------------------------------------------------------------------------^+
	echo.
	pause
	exit /B
)

rem Welcome message and prompt user for the kind of ruleset
echo.
echo ^+----------------------------------------------------------^+
echo ^| WARNING: This script will delete all current mods in     ^|
echo ^|          your Afterbirth resources folder. If this is    ^|
echo ^|          is not what you want, close this window now.    ^|
echo ^+----------------------------------------------------------^+
echo.
echo Choose a ruleset:
echo   1) Normal
echo   2) More Options
echo   3) Seeded
echo   4) Dark Room
echo   5) Seeded Dark Room
echo.
echo Or:
echo   6) Uninstall all mods
echo.
set /p id="Enter your choice: "
echo.

rem Validate user input (the brackets are needed to test for an empty input)
if [%id%] == [1] goto :start
if [%id%] == [1] goto :start
if [%id%] == [2] goto :start
if [%id%] == [3] goto :start
if [%id%] == [4] goto :start
if [%id%] == [5] goto :start
if [%id%] == [6] goto :start
echo You did not enter a valid choice. Exiting...
pause
exit /B

rem Start the installation
:start 

rem Delete all files
for %%i in ("C:\Program Files (x86)\Steam\SteamApps\common\The Binding of Isaac Rebirth\resources\*") do (
	del /Q "%%i"
)

rem Delete all directories except for the resources one
for /D %%i in ("C:\Program Files (x86)\Steam\SteamApps\common\The Binding of Isaac Rebirth\resources\*") do (
	if "%%~nxi" NEQ "packed" rd /S /Q "%%i"
)

rem Copy the files over (the /S flag is to include folders and the /Q flag is to make it be quiet)
if [%id%] == [1] xcopy /S /Q "%~dp0Ruleset 1 - Normal" "C:\Program Files (x86)\Steam\SteamApps\common\The Binding of Isaac Rebirth\resources"
if [%id%] == [2] xcopy /S /Q "%~dp0Ruleset 2 - More Options" "C:\Program Files (x86)\Steam\SteamApps\common\The Binding of Isaac Rebirth\resources"
if [%id%] == [3] xcopy /S /Q "%~dp0Ruleset 3 - Seeded" "C:\Program Files (x86)\Steam\SteamApps\common\The Binding of Isaac Rebirth\resources"
if [%id%] == [4] xcopy /S /Q "%~dp0Ruleset 4 - Dark Room" "C:\Program Files (x86)\Steam\SteamApps\common\The Binding of Isaac Rebirth\resources"
if [%id%] == [5] xcopy /S /Q "%~dp0Ruleset 5 - Seeded Dark Room" "C:\Program Files (x86)\Steam\SteamApps\common\The Binding of Isaac Rebirth\resources"
if [%id%] == [6] echo All mods have been uninstalled.

rem Done
echo.
pause