
# importing modules
# https://stackoverflow.com/questions/3144089/expand-python-search-path-to-other-source
# project directory is automatically added as part of sys.path (temporarily)

import math                         # system module
from testfolder.mycalc import add   # this in a folder called testfolder and I created the module mycalc
from os import system,name          # required for clear command
import sys

sys.path.append(".")                # this adds all sub-folders so we can reference the modules inside them                

def clear(): 
   _ = system('clear') 
        
        

clear()

print()
print (sys.path)
print()
print(add(1,9))



