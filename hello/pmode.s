bits 16
org 0x7c00
 
Start:
xor ax,ax
mov ds,ax
 
cli
 
lgdt [GDTR]
 
mov eax,cr0
or al,1
mov cr0,eax
jmp dword 0x08:PEStart
 
GDTR:
.limit:
dw GDT.End-GDT-1
.base:
dd GDT
 
GDT:
dw 0,0,0,0
 
dw 0xffff
dw 0
dw 0x9a00
dw 0x00cf
 
dw 0xffff
dw 0
dw 0x9200
dw 0x00cf
.End:
 
PEStart:
bits 32
 
mov ax,0x10
mov es,ax
mov ss,ax
mov ds,ax
mov fs,ax
mov gs,ax
mov esp, 0xffff
 
.text:
mov dword[0xb8000],'P'|('r'<<16)|0x07000700
mov dword[0xb8004],'o'|('t'<<16)|0x07000700
mov dword[0xb8008],'e'|('c'<<16)|0x07000700
mov dword[0xb800c],'t'|('e'<<16)|0x07000700
mov dword[0xb8010],'d'|(' '<<16)|0x07000700
mov dword[0xb8014],'m'|('o'<<16)|0x07000700
mov dword[0xb8018],'d'|('e'<<16)|0x07000700
jmp .text
 
times 510-($-$$) db 0
dw 0xAA55