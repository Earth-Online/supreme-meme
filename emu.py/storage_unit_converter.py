# -*- coding: utf-8 -*-
# binary.storage_unit_converter

yields = ['b', 'B', 'KB', 'M', 'G']
field = {'b':8589934592, 'B':1073741824, 'KB':1048576, 'M':1024, 'G':1}

def helper(dictd):
	# {'b':u'比特','B':u'字节','KB':u'千','M':u'兆','G':u'吉'}
	for d in yields:
		if d == 'B':
			print("%s %s -> 0x%x"%(dictd[d], d, dictd[d]))
			continue
		print("%s %s"%(dictd[d], d))

def convert(param, unit):
	d = dict()
	for _ in yields:
		d[_] = (float(param)/field[unit]) * field[_]
	return d

def paser(string):
	'''
		only support decimal as param
		校验参数并解析
	'''
	raw_argv = str.split(string,' ')
	if len(raw_argv) != 2 or (raw_argv[1] not in yields):
		raise RuntimeError('unit: %s'%raw_argv)
	try:
		return int(raw_argv[0]), raw_argv[1]
	except ValueError:
		raise RuntimeError('param: %s'%raw_argv[0])

if __name__ == '__main__':
	param, unit = paser('1440 KB')
	ans = convert(param, unit)
	helper(ans)
