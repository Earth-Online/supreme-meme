# import os
# command = raw_input('/>')
# if not os.system(command):
# 	raw = os.popen(command).read()

# import subprocess,sys,time
# command = 'ping localhost'
# sp = subprocess.Popen(command , shell=True, stdout=subprocess.PIPE)
# for _ in range(6):
# 	sys.stdout.write('.')
# 	time.sleep(0.5)
# print
# print sp.stdout.read()

import subprocess
command = raw_input('/>')
sp =subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)
print sp.stderr.read()