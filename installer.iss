[Setup]
AppName=EasyCmd
AppVersion=1.0
DefaultDirName={autopf}\EasyCmd
DefaultGroupName=EasyCmd
OutputDir=output
OutputBaseFilename=EasyCmdInstaller
AllowNoIcons=yes
PrivilegesRequired=admin

[Files]
Source: "dist\easycmd.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\EasyCmd"; Filename: "{app}\easycmd.exe"

[Tasks]
Name: "AddToPath"; Description: "Add EasyCmd to the system PATH"; GroupDescription: "Additional icons:"; Flags: unchecked

[Run]
Filename: "{app}\easycmd.exe"; Description: "Launch EasyCmd"; Flags: nowait postinstall skipifsilent
Filename: "cmd"; Parameters: "/C SETX PATH ""%PATH%;{app}"""; Flags: runhidden shellexec skipifsilent unchecked; Tasks: AddToPath
