# coding:utf-8
import threading
import os
import dpkt # 待加强

class ping_class(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		
	def run(self):
		#os.system("psping64 -n 100 -w 0 172.16.24.182:80 -nobanner")
		os.system("psping64 -n 100 172.31.8.1")

for i in range(400):
	ping_class().start()