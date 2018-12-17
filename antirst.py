import sys
from scapy.all import * 
conf.verb=0

print "TCP Hijacking Delector by lake2"
print "[+] Sniffing ...."
ip_arr = {}
while 1:
	a=sniff( filter="tcp and src host not 192.168.1.10", count=50)
	for b in a:
		ip_src = b.sprintf(r"%IP.src%")
		ip_ttl = b.sprintf(r"%IP.ttl%")
		if ip_arr.has_key(ip_src):
			c = int(ip_ttl) - int(ip_arr[ip_src])
			if abs(c) > 4:
				print ip_src + " has been hijacking !!!   debug info : " + str(ip_ttl) + "  <-> " + str(ip_arr[ip_src])
		else:
			ip_arr[ip_src] = ip_ttl
	print "=>"