from ctypes import *

STD_OUTPUT_HANDLE = -11
h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

class COORD(Structure):
   _fields_ = [('X', c_short),
               ('Y', c_short),
              ]

class SMALL_RECT(Structure):
   _fields_ = [('Left', c_short),
               ('Top', c_short),
               ('Right', c_short),
               ('Bottom', c_short),
              ]

class CONSOLE_SCREEN_BUFFER_INFO(Structure):
   _fields_ = [('dwSize', COORD),
               ('dwCursorPosition', COORD),
               ('wAttributes', c_uint),
               ('srWindow', SMALL_RECT),
               ('dwMaximumWindowSize', COORD),
              ]

def gotoxy((x,y)):
    windll.kernel32.SetConsoleCursorPosition(h, COORD(x,y))

cmd_info = CONSOLE_SCREEN_BUFFER_INFO()
def getxy():
	windll.kernel32.GetConsoleScreenBufferInfo(h, byref(cmd_info))
	return (cmd_info.dwCursorPosition.X,cmd_info.dwCursorPosition.Y)

if __name__ == '__main__':
	gotoxy((1,5))
	print "helloworld",
	print getxy()
	raw_input()