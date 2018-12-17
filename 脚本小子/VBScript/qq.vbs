Set WshShell= WScript.CreateObject("WScript.Shell")

WshShell.AppActivate"qqË¢ÆÁVBScript"

for i=1 to 200

WScript.Sleep 200

WshShell.Sendkeys "^v"

'WshShell.Sendkeys i

WshShell.Sendkeys "%s"

Next