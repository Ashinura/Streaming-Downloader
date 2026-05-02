WScript.Sleep 3000

Set fso = CreateObject("Scripting.FileSystemObject")
updateDir = fso.GetParentFolderName(WScript.ScriptFullName)
utilsDir = fso.GetParentFolderName(updateDir)
projectRoot = fso.GetParentFolderName(utilsDir)

launcherBat = projectRoot & "\launcher.bat"

Set shell = CreateObject("WScript.Shell")
shell.Run """" & launcherBat & """", 1, False