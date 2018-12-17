import zipfile
import optparse

def extractfile(topath,zfile,passwd):
	try:
		zfile.extractall(path=topath,pwd=passwd)
		return passwd
	except:
		pass

def main():
	parser = optparse.OptionParser("usage: -f <zipfile> -d <dictFile>")
	parser.add_option('-f',dest='zname',type='string',help='specify zip file')
	parser.add_option('-d',dest='dname',type='string',help='specify dict file')
	(options,args)=parser.parse_args()
	if(options.zname==None)|(options.dname==None):
		print parser.usage;
		exit(0);
	else:
		zname=options.zname;
		dname=options.dname;

	tmp=zname.strip('.zip')

	zfile = zipfile.ZipFile(zname)
	pfile = open(dname)

	for line in pfile.readlines():
		passwd = line.strip('\n')
		guess = extractfile('./%s'%tmp,zfile,passwd)
		if guess:
			print('The Passwd Is: %s'%guess)
			exit(0)
		else:
			print(paswd)
if __name__ == '__main__':
	main()