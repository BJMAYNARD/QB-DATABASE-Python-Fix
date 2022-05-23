::Resarting QuickBook Services
powershell -window hidden -command ""
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )
powershell -window hidden -command ""
@echo off
powershell -window hidden -command ""

@ECHO Off
::First the QB Monitor Service
net stop "QBCFMonitorService"
timeout 2 /nobreak
net start "QBCFMonitorService"

timeout 2 /nobreak

::Second the QBIDPService
net stop "QBIDPService"
timeout 2 /nobreak
net start "QBIDPService"
timeout 2 /nobreak

::Now the QB Database Manager
net stop "QuickBooksDB31"
timeout 2 /nobreak
net start "QuickBooksDB31"


::Creates a txt file that confirms stop and starting of services - must already have folder created

echo %date% %time% QBCFMonitorService service stopped >> C:/batch/QBServices.txt
echo %date% %time% QBCFMonitorService service started >> C:/batch/QBServices.txt
echo %date% %time% QBIDPService service stopped >> C:/batch/QBServices.txt
echo %date% %time% QBIDPService service started >> C:/batch/QBServices.txt
echo %date% %time% QuickBooksDB31 service stopped >> C:/batch/QBServices.txt
echo %date% %time% QuickBooksDB31 service started >> C:/batch/QBServices.txt

timeout 3 /nobreak
taskkill /IM cmd.exe

