@echo off

rem Set this equal to where your Afterbirth resources folder is
set ResourcesFolder=C:\Program Files (x86)\Steam\SteamApps\common\The Binding of Isaac Rebirth\resources

rem Check to see if we can find the resources folder
if not exist "%ResourcesFolder%" (
	echo.
	echo ERROR: I could not find the Afterbirth resources folder at:
	echo "%ResourcesFolder%"
	echo.
	echo Edit this file with Notepad and fix the path of the folder on line 4.
	echo Or, just install the mod manually by copying contents of the directory
	echo with the ruleset that you want to play into the Afterbirth resources folder.
	echo.
	pause
	exit /B
)

rem Prompt the user for the kind of ruleset to use
echo.
echo ^+-------------------------------------------------------------^+
echo ^| WARNING: This script will delete all of the current mods    ^|
echo ^|          in your Afterbirth resources folder. If this is    ^|
echo ^|          is not what you want, close this window now.       ^|
echo ^+-------------------------------------------------------------^+
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
for %%i in ("%ResourcesFolder%\*") do (
	del /Q "%%i"
)

rem Delete all directories except for the resources one
for /D %%i in ("%ResourcesFolder%\*") do (
	if "%%~nxi" NEQ "packed" rd /S /Q "%%i"
)

rem Copy the files over (the /S flag is to include folders and the /Q flag is to make it be quiet)
if [%id%] == [1] xcopy /S /Q "%~dp0Ruleset 1 - Normal" "%ResourcesFolder%"
if [%id%] == [2] xcopy /S /Q "%~dp0Ruleset 2 - More Options" "%ResourcesFolder%"
if [%id%] == [3] xcopy /S /Q "%~dp0Ruleset 3 - Seeded" "%ResourcesFolder%"
if [%id%] == [4] xcopy /S /Q "%~dp0Ruleset 4 - Dark Room" "%ResourcesFolder%"
if [%id%] == [5] xcopy /S /Q "%~dp0Ruleset 5 - Seeded Dark Room" "%ResourcesFolder%"
if [%id%] == [6] echo All mods have been uninstalled.

rem All done
echo.
pause
