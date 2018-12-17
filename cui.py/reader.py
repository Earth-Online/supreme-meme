#coding:utf-8
import sys,os,msvcrt
import core

def cut(s,b):
	def is_chinese(s):
		if s >= u'\u4e00' and s<=u'\u9fa5':
			return True
		else:
			return False
	raw=s.decode('utf-8')
	i,out=0,''
	for a in raw:
		out+=a
		if(is_chinese(a)):
			i+=2
		elif a=='\n':
			i=0
		else:
			i+=1
		if i>2*(b-1):
			out+='\n'
			i=0
	return out.encode('gbk')

def printf(raw,top,left):
	for num in range(len(raw)):
		core.gotoxy((left,num+top))
		sys.stdout.write(raw[num])

def main(string,(top,left),(a,b)):
	inp,i=False,0
	cls=["#"+"="*(a+1)*2+"#"]+["|"+" "*(a+1)*2+"|" for _ in range(b)]+["#"+"="*(a+1)*2+"#"]
	string = cut(string,a).split('\n')
	tmp = string[:b]
	while True:
		printf(cls,top-1,left-1)
		printf(tmp,top,left)
		while not inp :
			inp = msvcrt.getch()
		if inp=='s':
			tmp = string[i:i+b]
			if i!=len(string):
				i+=1
		elif inp=='w':
			tmp = string[i:i+b]
			if i!=0:
				i-=1
		elif inp=='q':
			break
		inp=False	

if __name__ == '__main__':
	top,left=4,8
	a,b=15,8
	string = '''Python的创始人为Guido van Rossum。1989年圣诞节期间，在阿姆斯特丹，Guido为了打发圣诞节的无趣，决心开发一个新的脚本解释程序，做为ABC 语言的一种继承。之所以选中Python（大蟒蛇的意思）作为该编程语言的名字，是因为他是一个叫Monty Python的喜剧团体的爱好者。\n
                Python在设计上坚持了清晰划一的风格，这使得Python成为一门易读、易维护，并且被大量用户所欢迎的、用途广泛的语言。\n
                设计者开发时总的指导思想是，对于一个特定的问题，只要有一种最好的方法来解决就好了。这在由Tim Peters写的Python格言（称为The Zen of Python）里面表述为：There should be one-- and preferably only one --obvious way to do it. 这正好和Perl语言（另一种功能类似的高级动态语言）的中心思想TMTOWTDI（There's More Than One Way To Do It）完全相反。'''
	main(string,(top,left),(a,b))