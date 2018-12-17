
C:\Users\huaji0353\Desktop\ÄæÏò¹¤³Ì\hh3.golden.exe:     file format pei-i386


Disassembly of section .text:

00401000 <.text>:
  401000:	55                   	push   %ebp
  401001:	89 e5                	mov    %esp,%ebp
  401003:	83 ec 18             	sub    $0x18,%esp
  401006:	c7 04 24 f5 ff ff ff 	movl   $0xfffffff5,(%esp)
  40100d:	ff 15 3c 30 40 00    	call   *0x40303c
  401013:	52                   	push   %edx
  401014:	8d 55 fc             	lea    -0x4(%ebp),%edx
  401017:	c7 44 24 10 00 00 00 	movl   $0x0,0x10(%esp)
  40101e:	00 
  40101f:	89 54 24 0c          	mov    %edx,0xc(%esp)
  401023:	c7 44 24 08 0f 00 00 	movl   $0xf,0x8(%esp)
  40102a:	00 
  40102b:	c7 44 24 04 00 20 40 	movl   $0x402000,0x4(%esp)
  401032:	00 
  401033:	89 04 24             	mov    %eax,(%esp)
  401036:	ff 15 40 30 40 00    	call   *0x403040
  40103c:	83 ec 14             	sub    $0x14,%esp
  40103f:	c7 04 24 00 00 00 00 	movl   $0x0,(%esp)
  401046:	ff 15 38 30 40 00    	call   *0x403038
  40104c:	ff                   	(bad)  
  40104d:	ff                   	(bad)  
  40104e:	ff                   	(bad)  
  40104f:	ff 00                	incl   (%eax)
  401051:	00 00                	add    %al,(%eax)
  401053:	00 ff                	add    %bh,%bh
  401055:	ff                   	(bad)  
  401056:	ff                   	(bad)  
  401057:	ff 00                	incl   (%eax)
  401059:	00 00                	add    %al,(%eax)
	...

Disassembly of section .rdata:

00402000 <.rdata>:
  402000:	48                   	dec    %eax
  402001:	65                   	gs
  402002:	6c                   	insb   (%dx),%es:(%edi)
  402003:	6c                   	insb   (%dx),%es:(%edi)
  402004:	6f                   	outsl  %ds:(%esi),(%dx)
  402005:	2c 20                	sub    $0x20,%al
  402007:	57                   	push   %edi
  402008:	6f                   	outsl  %ds:(%esi),(%dx)
  402009:	72 6c                	jb     0x402077
  40200b:	64                   	fs
  40200c:	21                   	.byte 0x21
  40200d:	0d                   	.byte 0xd
  40200e:	0a 00                	or     (%eax),%al

Disassembly of section .idata:

00403000 <.idata>:
  403000:	28 30                	sub    %dh,(%eax)
	...
  40300a:	00 00                	add    %al,(%eax)
  40300c:	80 30 00             	xorb   $0x0,(%eax)
  40300f:	00 38                	add    %bh,(%eax)
  403011:	30 00                	xor    %al,(%eax)
	...
  403027:	00 48 30             	add    %cl,0x30(%eax)
  40302a:	00 00                	add    %al,(%eax)
  40302c:	56                   	push   %esi
  40302d:	30 00                	xor    %al,(%eax)
  40302f:	00 66 30             	add    %ah,0x30(%esi)
  403032:	00 00                	add    %al,(%eax)
  403034:	00 00                	add    %al,(%eax)
  403036:	00 00                	add    %al,(%eax)
  403038:	48                   	dec    %eax
  403039:	30 00                	xor    %al,(%eax)
  40303b:	00 56 30             	add    %dl,0x30(%esi)
  40303e:	00 00                	add    %al,(%eax)
  403040:	66                   	data16
  403041:	30 00                	xor    %al,(%eax)
  403043:	00 00                	add    %al,(%eax)
  403045:	00 00                	add    %al,(%eax)
  403047:	00 1a                	add    %bl,(%edx)
  403049:	01 45 78             	add    %eax,0x78(%ebp)
  40304c:	69 74 50 72 6f 63 65 	imul   $0x7365636f,0x72(%eax,%edx,2),%esi
  403053:	73 
  403054:	73 00                	jae    0x403056
  403056:	66                   	data16
  403057:	02 47 65             	add    0x65(%edi),%al
  40305a:	74 53                	je     0x4030af
  40305c:	74 64                	je     0x4030c2
  40305e:	48                   	dec    %eax
  40305f:	61                   	popa   
  403060:	6e                   	outsb  %ds:(%esi),(%dx)
  403061:	64                   	fs
  403062:	6c                   	insb   (%dx),%es:(%edi)
  403063:	65 00 00             	add    %al,%gs:(%eax)
  403066:	ee                   	out    %al,(%dx)
  403067:	04 57                	add    $0x57,%al
  403069:	72 69                	jb     0x4030d4
  40306b:	74 65                	je     0x4030d2
  40306d:	46                   	inc    %esi
  40306e:	69 6c 65 00 00 00 00 	imul   $0x30000000,0x0(%ebp,%eiz,2),%ebp
  403075:	30 
  403076:	00 00                	add    %al,(%eax)
  403078:	00 30                	add    %dh,(%eax)
  40307a:	00 00                	add    %al,(%eax)
  40307c:	00 30                	add    %dh,(%eax)
  40307e:	00 00                	add    %al,(%eax)
  403080:	4b                   	dec    %ebx
  403081:	45                   	inc    %ebp
  403082:	52                   	push   %edx
  403083:	4e                   	dec    %esi
  403084:	45                   	inc    %ebp
  403085:	4c                   	dec    %esp
  403086:	33 32                	xor    (%edx),%esi
  403088:	2e                   	cs
  403089:	64                   	fs
  40308a:	6c                   	insb   (%dx),%es:(%edi)
  40308b:	6c                   	insb   (%dx),%es:(%edi)
  40308c:	00 00                	add    %al,(%eax)
	...
