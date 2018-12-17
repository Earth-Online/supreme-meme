#coding:utf-8
from __future__ import print_function
import core
import time

tl=b'\xc9'.decode('ibm437')
tr=b'\xbb'.decode('ibm437')
bl=b'\xc8'.decode('ibm437')
br=b'\xbc'.decode('ibm437')
iv=b'\xcd'.decode('ibm437')
ih=b'\xba'.decode('ibm437')

class Form:
	def __init__(self,(a,b),(x,y),border=True,title=None):
		self.a,self.b=a,b
		self.x,self.y=x,y
		self.border=border
		self.title=title

	def scrbuffer(self,what,data):
		if what:
			data=self.boundary_b(data,0)
			self.scrbuff=data
		else:
			data=self.boundary_b(data)
			self.strbuff=data

	def boundary_b(self,data,index=None):
		raw = data.decode('utf-8')
		i,out=0,''
		for a in raw:
			out+=a
			if(True if a >= u'\u4e00' and a<=u'\u9fa5' else False):
				i+=2
			elif a=='\n':
				i=0
			else:
				i+=1
			if i>2*(self.a-1):
				out+='\n'
				i=0
		if index==None:
			return out.split('\n')
		else:
			return out.split('\n')[index:index+self.b]

	def gotoxy(self,(x1,y1)):
		core.gotoxy((self.x+x1,self.y+y1))

	def boundary_f(self,bord):
		for i in range(len(bord)):
			self.gotoxy((0,i))
			print(bord[i],end='')

	def print(self,string):
		for i in range(len(string)):
			self.gotoxy((2,i+1))
			print(string[i],end='')

	def refresh(self):#buff(arg)->screen
		if self.border:
			a,b=self.a,self.b
			if (self.title != None) and (len(self.title)<a*2):
				l = len(self.title)
				add=(' ',(l+1)/2) if l%2 else ('',l/2)
				title=self.title+add[0]
				bord=tl+title+iv*(a-add[1])+tr+'\n'
			else:
				bord=tl+iv*a+tr+'\n'
			bord+=(ih+'  '*a+ih+'\n')*b+bl+iv*a+br
			self.boundary_f(bord.split('\n'))
		else:
			pass
		self.print(self.scrbuff)

	def test(self):
		self.scrbuffer(True,"hello world!hello world!hello world!\n"*5)
		self.refresh()

	def cout(self):
		for i in range(20):
			self.scrbuffer(True,str(i))
			self.refresh()
			#time.sleep(0.08)

if __name__ == '__main__':
	f1=Form((15,8),(4,4),title="<1>test form")
	f2=Form((15,8),(8,8),title="<2>cout form")
	# f3=Form((10,6),(16,16),title="3 form")
	# f4=Form((10,6),(24,24),title="4 form")
	f1.test()
	f2.cout()
	# f3.test()
	# f4.test()
	#raw_input()
