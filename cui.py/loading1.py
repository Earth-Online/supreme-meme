import sys,time

def around():
	sys.stdout.write('|\b')
	time.sleep(0.05)
	sys.stdout.write('/\b')
	time.sleep(0.05)
	sys.stdout.write('\\\r')
	time.sleep(0.05)

def wave(string,i):
	for _ in range(i):
		for index in range(len(string)):
			after=string[index].upper()
			mix=string[:index]+after+string[index+1:]
			sys.stdout.write(mix+' ')
			around()
	print(string+' '*10)

if __name__ == '__main__':
	string="os is loading ..."
	wave(string,3)
	print("done!")
	raw_input()
