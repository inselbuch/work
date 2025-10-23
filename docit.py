#from art import *
import pyfiglet

import sys
import re

try:
    fn = sys.argv[1]
except:
    sys.exit()

try:
    f = open(fn,"r")
except Exception as ex:
    print(ex)
    sys.exit()



for line in f:
    rex = re.search(r'( *)def (.*)\(',line)
    if rex:
        print(f"{rex.group(1)}'''")
        fig = pyfiglet.figlet_format(rex.group(2),font='utopiab')
        print(fig,end='')
        print(f"{rex.group(1)}'''")
        print(line,end='')
    else:
        print(line,end='')

f.close()


