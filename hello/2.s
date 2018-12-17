	.file	"2.c"
	.intel_syntax noprefix
	.comm	v,4,4
	.text
	.globl	add2
	.type	add2, @function
add2:
.LFB0:
	push	ebp
.LCFI0:
	mov	ebp, esp
.LCFI1:
	mov	DWORD PTR v, 1
	mov	eax, DWORD PTR [ebp+12]
	mov	edx, DWORD PTR [ebp+8]
	add	eax, edx
	pop	ebp
.LCFI2:
	ret
.LFE0:
	.size	add2, .-add2
	.globl	main
	.type	main, @function
main:
.LFB1:
	push	ebp
.LCFI3:
	mov	ebp, esp
.LCFI4:
	sub	esp, 24
.LCFI5:
	mov	DWORD PTR [ebp-4], 1
	mov	DWORD PTR [ebp-8], 2
	mov	eax, DWORD PTR [ebp-8]
	mov	DWORD PTR [esp+4], eax
	mov	eax, DWORD PTR [ebp-4]
	mov	DWORD PTR [esp], eax
	call	add2
	mov	DWORD PTR [ebp-12], eax
	mov	eax, DWORD PTR [ebp-12]
	leave
.LCFI6:
	ret
.LFE1:
	.size	main, .-main
	.section	.eh_frame,"aw",@progbits
.Lframe1:
	.long	.LECIE1-.LSCIE1
.LSCIE1:
	.long	0
	.byte	0x1
	.string	""
	.byte	0x1
	.byte	0x7c
	.byte	0x8
	.byte	0xc
	.byte	0x4
	.byte	0x4
	.byte	0x88
	.byte	0x1
	.align 4
.LECIE1:
.LSFDE1:
	.long	.LEFDE1-.LASFDE1
.LASFDE1:
	.long	.LASFDE1-.Lframe1
	.long	.LFB0
	.long	.LFE0-.LFB0
	.byte	0x4
	.long	.LCFI0-.LFB0
	.byte	0xe
	.byte	0x8
	.byte	0x85
	.byte	0x2
	.byte	0x4
	.long	.LCFI1-.LCFI0
	.byte	0xd
	.byte	0x5
	.byte	0x4
	.long	.LCFI2-.LCFI1
	.byte	0xc
	.byte	0x4
	.byte	0x4
	.byte	0xc5
	.align 4
.LEFDE1:
.LSFDE3:
	.long	.LEFDE3-.LASFDE3
.LASFDE3:
	.long	.LASFDE3-.Lframe1
	.long	.LFB1
	.long	.LFE1-.LFB1
	.byte	0x4
	.long	.LCFI3-.LFB1
	.byte	0xe
	.byte	0x8
	.byte	0x85
	.byte	0x2
	.byte	0x4
	.long	.LCFI4-.LCFI3
	.byte	0xd
	.byte	0x5
	.byte	0x4
	.long	.LCFI6-.LCFI4
	.byte	0xc5
	.byte	0xc
	.byte	0x4
	.byte	0x4
	.align 4
.LEFDE3:
	.ident	"GCC: (GNU) 4.6.1"
