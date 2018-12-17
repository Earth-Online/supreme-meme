# coding:utf-8
import threading
import os
import socket # 待加强底层能力tcpping
import fire # google牛逼的命令行

class ping_class(threading.Thread):
	def __init__(self, hostname, how_many):
		self.hostname = hostname
		self.how_many = how_many
		threading.Thread.__init__(self)
		
	def run(self):
		os.system("psping64 -n {how_many} -w 0 {hostname} -nobanner".format(how_many=self.how_many, hostname=self.hostname))


class start(object):
	def ack(self, hostname, how_many=64, thread_num=126):
		for i in range(thread_num):
			ping_class(hostname, how_many).start()

fire.Fire(start)