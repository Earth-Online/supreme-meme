Set WshShell= WScript.CreateObject("WScript.Shell")

WshShell.AppActivate"VBScript³Ë·¨±í"

for i=1 to 9
for j=1 to i
WScript.Sleep 800

WshShell.Sendkeys j&"x"&i&"="&(i*j)
WshShell.Sendkeys "%s"

next
next