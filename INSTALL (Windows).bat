@setlocal enableextensions enabledelayedexpansion
@echo off

rem If the script is failing, set the below line equal to where your Isaac "resources" folder is
set ResourcesFolder=

if not "%ResourcesFolder%"=="" goto ResourceFolderIsSet

set ResSubFolder=\SteamApps\common\The Binding of Isaac Rebirth\resources
set RegistrySteam="HKCU\Software\Valve\Steam"
set RegistrySteamPath="SteamPath"
set SteamPath=

rem Check to see if Steam is installed
reg query %RegistrySteam% /V %RegistrySteamPath% > nul || (
	echo ERROR: Steam does not appear to be installed, which means that I can't find the
	echo        path to your Isaac "resources" directory. Exiting...
	pause
	exit /B
)

rem Query Steam's install path
for /f "tokens=2,*" %%a in ('reg query %RegistrySteam% /V %RegistrySteamPath% ^| findstr %RegistrySteamPath%') do (
	set SteamPath=%%~fb
)

rem Search the resource directory from Steam's install and the library paths
if exist "%SteamPath%%ResSubFolder%" (
	set ResourcesFolder="%SteamPath%%ResSubFolder%"
) else (
	for /f "tokens=1,*" %%a in ('type "%SteamPath%\config\config.vdf" ^| findstr BaseInstallFolder_ ') do (
		if exist "%%~fb%ResSubFolder%" (
			set ResourcesFolder="%%~fb%ResSubFolder%"
		)
	)
)

set ResourcesFolder=!ResourcesFolder:~1,-1!

:ResourceFolderIsSet

rem Check to see if we can find the resources folder
if not exist "%ResourcesFolder%" (
	echo.
	echo ERROR: I could not find the Afterbirth resources folder at:
	echo "%ResourcesFolder%"
	echo.
	echo Edit this file with Notepad and put the path of the folder on line 5.
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
echo   1) Normal / Unseeded
echo.
echo Or:
echo   2) Uninstall all mods (except for config.ini)
echo   3) Do nothing and exit
echo.
set /p id="Enter your choice: "
echo.

rem Validate user input (the brackets are needed to test for an empty input)
if [%id%] == [1] goto :start
if [%id%] == [2] goto :start
if [%id%] == [3] exit /B
echo You did not enter a valid choice. Exiting...
pause
exit /B

rem Start the installation
:start

rem Delete all files except for config.ini
for %%i in ("%ResourcesFolder%\*") do (
	if "%%~nxi" NEQ "config.ini" del /Q "%%~fi"
)

rem Delete all directories except for the resources one
for /D %%i in ("%ResourcesFolder%\*") do (
	if "%%~nxi" NEQ "packed" rd /S /Q "%%~fi"
)

rem If we are not uninstalling all mods, copy over config.ini if it doesn't already exist
if not [%id%] == [6] (
	if not exist "%ResourcesFolder%\config.ini" (
		xcopy /Q "%~dp0miscellaneous\config.ini" "%ResourcesFolder%"
	)
)

rem Copy the files over (the /S flag is to include folders and the /Q flag is to make it be quiet)
if [%id%] == [1] xcopy /S /Q "%~dp0resources" "%ResourcesFolder%"
if [%id%] == [2] echo All mods have been uninstalled.

rem All done.
echo.
pause
