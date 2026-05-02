WScript.Sleep 3000 

Set fso = CreateObject("Scripting.FileSystemObject")
projectRoot = fso.GetParentFolderName(fso.GetParentFolderName(WScript.ScriptFullName))
scriptPath = projectRoot & "\StrDL.py"

venvPython = projectRoot & "\.venv\Scripts\pythonw.exe"
If Not fso.FileExists(venvPython) Then
    venvPython = "pythonw"
End If

' Lancer l'application
Set shell = CreateObject("WScript.Shell")
shell.Run """" & venvPython & """ """ & scriptPath & """", 0, False

WScript.Sleep 3000

' Vérifier que le port répond
Set http = CreateObject("Microsoft.XMLHTTP")
On Error Resume Next
http.Open "GET", "http://127.0.0.1:5000/", False
http.Send
On Error GoTo 0