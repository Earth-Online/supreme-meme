import re,os

def getsize():
    r = os.popen('chcp 437 & mode con /status & chcp 936')  
    text = r.read()  
    r.close()
    try:
        l=re.findall("Lines:(.*)",text)[0].strip()
        c=re.findall("Columns:(.*)",text)[0].strip()
        return l,c
    except:
        raise IOError
