import sys
import core

def printf(string,top,left):
	raw = string.split('\n')
	for num in range(len(raw)):
		core.gotoxy((left,num+top))
		sys.stdout.write(raw[num])


if __name__ == '__main__':
	top,left=5,5
	string = "1xxxxx)\n2sssssss)\n3eeeeeeeee)\n4eeeeeeeeeee)"
	printf(string,top,left)
	raw_input()
