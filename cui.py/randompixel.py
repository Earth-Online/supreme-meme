from ctypes import *
from msvcrt import getch
from os import system
import time,random
import core

system('mode con lines=37 cols=80')
hwnd = windll.kernel32.GetConsoleWindow()
hdc = windll.user32.GetDC(hwnd)

a,b=550,550
i=6666
size=5
color=0xffffff

start = time.clock()
for _ in range(i):
	x,y=random.randrange(0,a+1,size),random.randrange(0,b+1,size)
	for x_ in range(size):
		for y_ in range(size):
			windll.gdi32.SetPixel(hdc,c_int(x+x_),c_int(y+y_),c_ulong(color))
end = time.clock()
core.gotoxy((0,35))
print "%d random block cost: %fs"%(i,(end-start))
getch()