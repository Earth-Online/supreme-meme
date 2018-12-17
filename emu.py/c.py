# -*- coding: utf-8 -*-
# binary.storage_unit_converter

import sys

"""_helper_memmap = {
	u'常规内存(Conventional Memory)'
	u'上位内存区(Upper Memory Area)'
	u'高端内存区(High Memory Area)' 
	u'扩展内存(Extended Memory)' 
}
"""
_convert_order = ['b', 'B', 'KB', 'M']#, 'G']
_convert_dict = {
	#'G' : 8589934592, 
	'M' : 8388608, 
	'KB' : 8192, 
	'B' : 8, 
	'b' : 1
}

def _inrange(v, l):
	if ( v>=x[0] and v<=x[1]):
		return True
	return False

def _sh2i(l):
	return eval("int(%s)"%l)

def _sh_2i(l):
	return eval("int(0x%s)"%l)

def helper(dictd):
	for d in _convert_order:
		if d == 'B':
			print("%s %s -> 0x%x"%(dictd[d], d, dictd[d]))
		else:
			print("%s %s"%(dictd[d], d))

def convert(param, unit):
	d = dict()
	for _ in _convert_order:
		d[_] = param*(_convert_dict[unit]*float(1)/_convert_dict[_])
	return d

def check(*argv):
	'''
		:param sys.argv
		:return val, unit
		only support decimal and hex as param
		校验参数并解析
	'''
	raw_argv = argv[0][1:]
	try:
		if len(raw_argv) == 1:
			try:
				return _sh2i(raw_argv[0]), 'B' # !!!!eval function warning!!!!
			except SyntaxError:
				# (0xf<<4)+0xc
				perfix = raw_argv[0].split(":")
				return (_sh_2i(perfix[0])<<4)+_sh_2i(perfix[1]), 'B'
		elif len(raw_argv) == 2 and (raw_argv[1] in _convert_order):
			return int(raw_argv[0]), raw_argv[1]
		else:
			raise RuntimeError('unit: %s'%raw_argv)
	except ValueError:
		raise RuntimeError('param: %s'%raw_argv[0])

if __name__ == '__main__':
	param, unit = check(sys.argv)
	ans = convert(param, unit)
	helper(ans)
