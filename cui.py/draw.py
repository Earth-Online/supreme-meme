#coding:utf-8
from __future__ import print_function
import core
import msvcrt

tl=b'\xc9'.decode('ibm437')
tr=b'\xbb'.decode('ibm437')
bl=b'\xc8'.decode('ibm437')
br=b'\xbc'.decode('ibm437')
iv=b'\xcd'.decode('ibm437')
ih=b'\xba'.decode('ibm437')

class Form:
	def __init__(self,(a,b),(x,y),title):
		self.a,self.b=a,b
		self.x,self.y=x,y
		self.title=title
		self.printform()
		
	def write(self,string):
		raw = string.split('\n')
		for num in range(len(raw)):
			core.gotoxy((self.x+1,num+self.y+1))
			print(raw[num],end='')

	def cls(self):
		self.write((" "*self.a+'\n')*self.b)

	def printform(self):
		a,b,title=self.a,self.b,self.title
		l = len(title)
		string = tl+' '.join(title)+' '+iv*(a-l)+tr+'\n' if l<a*2 else tl+iv*a+tr+'\n'
		self.write(string+(ih+'  '*a+ih+'\n')*b+bl+iv*a+br)

def main():
	f1=Form((14,5),(5,7),'Form1')
	inp=False
	while True:
		while not inp:
			inp = msvcrt.getch()
		if inp=='h':
			f1.write('hello world\nFrist big project!')
		elif inp=='q':
			break
		elif inp=='c':
			f1.cls()
		inp=False

if __name__ == '__main__':
	main()
