import msvcrt,sys
with open('fake.py','r') as fp:
    code = fp.read()
i = 0
l = len(code)
while True:
    if i != l:
        ch = msvcrt.getch()
        sys.stdout.write(code[i])
        if ch == '~':
            break
        i+=1
    else:
        break
print "\nsending..."
msvcrt.getch()
