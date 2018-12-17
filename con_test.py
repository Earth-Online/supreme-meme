import IPython
import win32console, win32file, win32process

hfile = win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
IPython.embed()
win32file.WriteFile(hfile, "Hello, World!")
win32process.ExitProcess(0)