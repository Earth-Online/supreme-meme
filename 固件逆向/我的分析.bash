型号:
TPLINK WR842N V3 CN

硬件:
MPIS32 SOC AR9341 / AP123 Board
Flash 2 Mb
DDRAM 16 Mb 0x1000000
Atheros AR7240

固件升级header:
0x00-0x03   00 18 B4 90                                      去除校验码后固件大小
0x04-0x13   D8 4C A7 7E E6 1B 24 FC E1 FB D6 C6 C6 BD 91 37  校验码（MD5值）

0x14-0x17   49 4D 47 30                                      IMG0 镜像起始标识（VxWorks）
0x18-0x1B   00 18 B4 90                                      去除头部 + 校验码（0x00-0x13）后固件大小
0x1C-0x1F   08 42 00 03                                      产品型号&版本
0x25-0x27	04 13 12										 固件版本号
0x37														 厂家标识，00是tplink，01是水星，02是迅捷
0x58-0x5B   00 18 B4 10                                      从0x94开始至结尾的大小

软件:
U-Boot 1.1.4 (Jan 22 2013 - 00:11:52)
VxWorks 5.5.1 / Tornado2.2

文件系统:
tftpboot 0x8022c090 uImage; bootm 0x8022c090
bootargs
	console=ttyS0,115200
	root=31:02
	rootfstype=jffs2
	init=/sbin/init
	mtdparts=ath-nor0:32k(u-boot1),32k(u-boot2),3008k(rootfs),896k(uImage),64k(mib0),64k(ART)
	bootcmd=bootm 0x9f300000
	bootdelay=1
	baudrate=115200
	ethaddr=0x00:0xaa:0xbb:0xcc:0xdd:0xee
	ipaddr=192.168.1.1
	serverip=192.168.1.10
	lu=tftp 0x80060000 tuboot.bin && erase 0x9f000000 + $filesize && cp.b $fileaddr 0x9f000000 $filesize
	lf=tftp 0x80060000 ${bc}-jffs2 && erase 0x9f010000 + $filesize && cp.b $fileaddr 0x9f010000 $filesize
	lk=tftp 0x80060000 vmlinux_${bc}.lzma.uImage && erase 0x9f300000 + $filesize && cp.b $fileaddr 0x9f300000 $filesize

0x14-0xE2FF Uboot 0x3C8D0
0x40094 kernel
0x141794 initfs

内存分布:
0x9f000000 bootloader
0x9f010000 filesys
0x9f040000 ?
0x9f300000 kernel

后门:
userRpm/NatDebugRpm26525557.htm

资源:
http://right.com.cn
http://www.anywlan.com