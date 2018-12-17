import msvcrt,sys,time
inp=[]
maxl=15
cin=False
while True:
	while not cin:
		cin=msvcrt.getch()
	if cin=='d' and len(inp)>0:
			inp.pop()
	elif cin=='p':
		print inp
		time.sleep(2)
		break
	elif len(inp)<maxl:
		inp.append(cin)
	sys.stdout.write(' '*maxl+'\r')
	sys.stdout.write(''.join(inp)+'\r')
	cin=False