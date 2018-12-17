import subprocess,os
path = os.path.abspath(__file__)
while True:
	raw_command = raw_input(path+'\>')
	tmp = raw_command.split()
	if tmp[0]=='cd':
		path = tmp[1]
		print 'path has been change into '+path
	elif tmp[0]=='exit':
		break
	else:
		if path==None:
			command = raw_command
		else:
			command = path +'&&'+ raw_command
		sp = subprocess.Popen(command,shell=True,stderr=subprocess.PIPE)
		print sp.stderr.read()