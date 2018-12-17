"""
import socket

HOST = 'www.sina.com.cn'
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('A'*64)
data = s.recv(1024)
s.close()
print 'Received', repr(data)
"""

from multiprocessing.dummy import Pool,RLock
from socket import socket,AF_INET,SOCK_STREAM
from socketserver import BaseRequestHandler,ThreadingMixIn,UDPServer
from ssl import CERT_REQUIRED,PROTOCOL_TLS,SSLContext,SSLError
from struct import pack,unpack
from sys import stdout
from threading import activeCount
from traceback import print_exc

ENV={}

ENV['TLS']=None

ENV['SERVER_IP']='127.0.0.1'
ENV['SERVER_PORT']=6666

ENV['REMOTE_SERVERS']=[] # (hostname,ipaddr,port)

ENV['TIMEOUT']=5

def bytetodomain(b):
	l=[]
	s,e=0,1
	while True:
		n=unpack('!B',b[s:e])[0]
		if n==0:
			break
		s,e=e,e+n
		l.append(b[s:e])
		s,e=e,e+1
		return b'.'.join(l).decode('utf8')

def QueryDNS(remote_server,server,data,addr,lock,stat):
	hostname,ipaddr,port=remote_server
	if not ENV['TLS']:
		return
	bufl=pack('!h',len(data))
	data=bufl+data
	resp=b''
	try:
		with socket(AF_INET,SOCK_STREAM) as s:
			ss=ENV['TLS'].wrap_socket(s,server_hostname=hostname)
			ss.settimeout(ENV['TIMEOUT'])
			ss.connect((ipaddr,port))
			ss.send(data)
			size,_=unpack('!h',ss.recv(2))
			resp=ss.recv(size)
	except:
		print('{:=^60}'.format('Error'))
		print('d:{}:{}'.format(ipaddr,port))
		print('{:=^60}'.format('Info'))
		print(print_exc(file=stdout))
		print('{:=^60}'.format('End'))
	finally:
		return server,addr,resp,lock,stat,ipaddr

def SendDNS(argument):
	server,addr,data,lock,stat,dns=argument
	if not data:
		return
	if stat['size']:
		return
	with lock:
		server.sendto(data,addr)
		stat['size']+=1
		print('a:{},{}'.format(stat['domain'],dns))

def transfer(query,addr,server):
	if not query:
		return server.sendto(b'',addr)

	domain=bytetodomain(query[12:-4])

	qtype,_=unpack('!h',query[-4:-2])
	print('q:{},{:0>2}'.format(domain,qtype))
	stdout.flush()
	status=dict(size=0,domain=domain)
	lock=RLock()
	with Pool(ENV['REMOTE_SERVERS_LENGTH']) as pool:
		for dns in ENV['REMOTE_SERVERS']:
			pool.apply_async(QueryDNS,(dns,server,query,addr,lock,status),callback=SendDNS)
			pool.close()
			pool.join()
	if status['size']:
		return
	print('e:{},{:0>2}'.format(domain,qtype))
	return server.sendto(b'',addr)

class ThreadUDPServer(ThreadingMixIn,UDPServer):
	def __init__(self,s,t):
		UDPServer.__init__(self,s,t)

class ThreadUDPRequestHandler(BaseRequestHandler):
	# Ctrl-C will cleanly kill all spawned threads
	daemon_threads=True
	# much faster rebinding
	allow_reuse_address=True

def handle(self):
	data=self.request[0]
	serv=self.request[1]
	addr=self.client_address
	transfer(data,addr,serv)

if __name__ == "__main__":
	print('init')

	ENV['TLS']=SSLContext(PROTOCOL_TLS)
	ENV['TLS'].verify_mode=CERT_REQUIRED
	ENV['TLS'].check_hostname=True
	ENV['TLS'].load_default_certs()
	#tlsctx.load_verify_locations(cadata=cadata)

	# Cloudflare
	ENV['REMOTE_SERVERS'].append(('1.1.1.1','1.1.1.1',853))
	ENV['REMOTE_SERVERS'].append(('1.0.0.1','1.0.0.1',853))
	# Quad9 (Packet Clearing House and IBM)
	ENV['REMOTE_SERVERS'].append(('dns.quad9.net','9.9.9.9',853))
	ENV['REMOTE_SERVERS'].append(('dns.quad9.net','149.112.112.112',853))

	ENV['REMOTE_SERVERS_LENGTH']=len(ENV['REMOTE_SERVERS'])

	with ThreadUDPServer((ENV['SERVER_IP'],ENV['SERVER_PORT']),ThreadUDPRequestHandler) as server:
		print('finished')
		print('server on {}:{}'.format(ENV['SERVER_IP'],ENV['SERVER_PORT']))
		try:
			server.serve_forever()
		except KeyboardInterrupt:
			server.shutdown()
