from time import sleep
from config import _setting
import program,kernel

setting=_setting()

print setting['text']['welcome']
sleep(1)
while True:
    raw=raw_input('>')
    op=raw.split()
    if len(op)==0:
        pass
    elif op[0]=='_hello_':
        program.hello(op)
    elif op[0]=='_quit_':
        if len(op)==1:
            break
        else:
            print kernel.error('para')
    elif op[0] in ['?','help','??']:
        if len(op)==1:
            print setting['text']['help']
        else:
            print kernel.error('para')
    else:
        print kernel.error('pro',op)
print setting['text']['bye']
sleep(1)
exit(0)
