#coding:utf-8
'''
|0x0...<0x7c00>MBR<lens>...0x1000000(16MB)|!MAP
'''
from __future__ import print_function
import capstone # disassemble
import keystone # assemble
import unicorn # emulate

class Emulator:
	def __init__(self):
		'''初始化 instance 初始化模拟器参数 only x86'''
		# Initialize emulator in X86-32bit mode
		self.vm = unicorn.Uc(unicorn.UC_ARCH_X86, unicorn.UC_MODE_32 | unicorn.UC_MODE_LITTLE_ENDIAN)
		self.asb = keystone.Ks(keystone.KS_ARCH_X86, keystone.KS_MODE_32 | keystone.KS_MODE_LITTLE_ENDIAN)
		self.disas = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32 | capstone.CS_MODE_LITTLE_ENDIAN)
		self.__reinit__()

	def __reinit__(self):
		# map 16MB memory for this emulation
		# 内存4KB 大小0x1000对齐
		self.vm.mem_map(0, 16 * 1024 * 1024)
		self.__MBRADDRESS = 0x7c00
		self.__4k = 4*1024

	def write_reg(self, reg, val):
		ur =  getattr(unicorn.x86_const, "UC_X86_REG_%s"%reg.upper())
		self.vm.reg_write(ur, val)
				
	def read_reg(self, reg):
		ur =  getattr(unicorn.x86_const, "UC_X86_REG_%s"%reg.upper())
		return self.vm.reg_read(ur)

	def write_mem(self, address, bytecode):
		# write machine code to be emulated to memory
		self.vm.mem_write(address, bytecode)

	def read_mem(self, address, size):
		# read from memory
		val = self.vm.mem_read(address, size)
		return val

	def start(self, address, codelen):
		print("=" * 35)
		try:
		# emulate machine code in infinite time
			self.vm.emu_start(address, address+codelen)
		except unicorn.UcError as e:
			print("ERROR: %s" % e)
		self.stop()

	def stop(self):
		self.vm.emu_stop()
		print(">>> Emulation stop. Below is the CPU context")
		# now print out some registers
		print("EIP: 0x%x"%self.read_reg('EIP'))

###################待加强###TODOTODO###########################
	def write_file(self, fileA, seek):
		# TODO
		pass

	def read_file(self, fileA, seek=0):
		# TODO
		with open(fileA, 'rb') as f:
			binary = f.read()
		return binary

	def assemble(self, code_list):
		code = b" ; ".join(code_list)
		return bytes(bytearray(self.asb.asm(code)[0]))

	def disassemble(self, bytecode):
		# TODO
		output = self.disas.disasm(bytecode)
		return output



def test_ins1():
	emu = Emulator()
	code = [
		'mov eax, 0x1',
		'mov ebx, 0x2',
		'add eax, ebx',
	]
	binary = emu.assemble(code)
	emu.write_mem(0, binary)
	emu.start(0, len(binary))
	assert emu.read_reg('eax') == 0x3


if __name__ == '__main__':
	emu = Emulator()
	mbr = emu.read_file("mbr")
	print(emu.disassemble(mbr))
	emu.write_mem(0x7c00, mbr)
	emu.start(0x7c00, len(mbr))
