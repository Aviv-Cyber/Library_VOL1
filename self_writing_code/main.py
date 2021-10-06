import os
import sys
import time

f = open("content.py", "w")
f.write("import re\n")
f.write("f = open('main.py', 'a')\n\n")
f.write("for i in range(5):\n\t")
f.write("i = f.write('f.write({})')\n".format("Hi"))
f.close()

os.system('content.py')
