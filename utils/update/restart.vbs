WScript.Sleep 3000

Set fso = CreateObject("Scripting.FileSystemObject")
projectRoot = fso.GetParentFolderName(fso.GetParentFolderName(WScript.ScriptFullName))

launcherBat = projectRoot & "\launcher.bat"

Set shell = CreateObject("WScript.Shell")
shell.Run """" & launcherBat & """", 0, False