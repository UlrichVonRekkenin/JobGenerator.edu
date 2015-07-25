#define Name "Task Generator"
#define Version "1.0.0"
#define Author "UlrichVonRekkenin"
#define Site "https://github.com/UlrichVonRekkenin"
#define Release "https://github.com/UlrichVonRekkenin/JobGenerator.edu/releases"
#define BuildPath ".\build\exe.win32-3.4\"
#define ExeName "Task Generator.exe"
#define Ico "{app}\tools\main.ico"


[Setup]
AppId={{BEC6990F-2789-4B72-B1ED-056817A74F7A}
AppName={#Name}
AppVersion={#Version}
AppPublisher={#Author}
AppPublisherURL={#Site}
AppUpdatesURL={#Release}
DefaultDirName={userdocs}\Task Generator
DefaultGroupName={#Name}
OutputDir=setup
OutputBaseFileName=Setup-{#Name}-{#Version}
Compression=lzma2/max
SolidCompression=yes


[Files]
Source: "{#BuildPath}{#ExeName}"; DestDir: "{app}"; Flags: ignoreversion touch
Source: "{#BuildPath}cacert.pem"; DestDir: "{app}"; Flags: ignoreversion touch
Source: "{#BuildPath}tools\*.ico"; DestDir: "{app}\tools"; Flags: ignoreversion
Source: "{#BuildPath}tools\*.ui"; DestDir: "{app}\tools"; Flags: ignoreversion
Source: "{#BuildPath}msvcp100.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}MSVCR100.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}python34.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}QtCore4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}QtGui4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}PyQt4.Qt.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}PyQt4.QtCore.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}PyQt4.QtGui.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}sip.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion


[Dirs]
Name: "{app}\tools"


[UninstallDelete]
Type: files; Name: "{app}\dialog.json"
Type: filesandordirs; Name: "{app}\tools"
Type: files; Name: "{app}\qt.conf"


[Icons]
Name: {commondesktop}\{#Name}; Filename: {app}\{#Name}.exe; WorkingDir: {app}; IconFilename: "{#Ico}";
Name: {group}\{#Name}; Filename: {app}\{#Name}.exe; WorkingDir: {app}; IconFilename: "{#Ico}";
