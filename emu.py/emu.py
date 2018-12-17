#coding:utf-8
'''
|0x0...<0x7c00>MBR<lens>...0x1000000(16MB)|!MAP
'''
from __future__ import print_function
import capstone # disassemble
import keystone # assemble
import unicorn # emulate

_4k = 4*1024

def (filename):
	with open('mbr', 'rb') as f:
		DATA = f.read()

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
		
    def readreg(self, reg):
        ur =  getattr(unicorn.x86_const, "UC_X86_REG_%s"%reg.upper())
        return self.vm.reg_read(ur)

    def writereg(self, reg, val):
        ur =  getattr(unicorn.x86_const, "UC_X86_REG_%s"%reg.upper())
        self.vm.reg_write(ur, val)

    def ascode(self, code_list):
        code = b" ; ".join(code_list)
        return bytes(bytearray(self.asb.asm(code)[0]))

    def discode(self, bytecode):
        output = self.disas.disasm(bytecode)
        return output

    def writemem(self, address, bytecode):
        # write machine code to be emulated to memory
        self.vm.mem_write(address, bytecode)

	def readmem(self, address, size):
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
        print("EAX: %s"%self.readreg('EAX'))


def main():
    emu = Emulator()
    code = [
        'mov eax, 0x1',
        'mov ebx, 0x2',
        'add eax, ebx',
    ]
    a = emu.ascode(code)
    emu.write(0, a, r4k)
    emu.writereg('ecx', 10)
    emu.start(0, len(a))
    print(emu.readreg('eax'))
    code = [
        'mov ecx, 0xff',
    ]
    a = emu.ascode(code)
    #emu.write(4*1024+1, a, r4k)
    print(emu.readreg('ecx'))


if __name__ == '__main__':
    main()
