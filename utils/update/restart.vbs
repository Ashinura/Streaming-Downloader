WScript.Sleep 3000

Set fso = CreateObject("Scripting.FileSystemObject")
projectRoot = fso.GetParentFolderName(fso.GetParentFolderName(WScript.ScriptFullName))
scriptPath = projectRoot & "\StrDL.py"

venvPython = projectRoot & "\.venv\Scripts\pythonw.exe"
If Not fso.FileExists(venvPython) Then
    venvPython = "pythonw"
End If

CreateObject("WScript.Shell").Run """" & venvPython & """ """ & scriptPath & """", 0, False