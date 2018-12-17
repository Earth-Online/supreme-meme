# coding: utf-8
'''
|0x0...<0x7c00>MBR<lens>...0x1000000(16MB)|!MAP
'''
from __future__ import print_function
import unicorn # emulate
 

with open('mbr', 'rb') as f:
	DATA = f.read()

#DATA = b'\x00\x00'
MBRADDRESS = 0x7c00

print("=" * 35)
# Initialize emulator in X86-16bit mode
vm = unicorn.Uc(unicorn.UC_ARCH_X86, unicorn.UC_MODE_16)

# map 16MB memory for this emulation
# 内存4KB 大小0x1000对齐
vm.mem_map(0, 16 * 1024 * 1024)

# write machine code to be emulated to memory
vm.mem_write(MBRADDRESS, DATA)

# emulate machine code in infinite time
#vm.emu_start(MBRADDRESS, MBRADDRESS+len(DATA))

# read from memory
tmp = vm.mem_read(MBRADDRESS, 4)
print(">>> Read 4 bytes from [0x%x] = 0x" %(MBRADDRESS), end="")
for i in reversed(tmp):
	print("%x" %(i), end="")
print("")

# now print out some registers
print(">>> Emulation done. Below is the CPU context")

