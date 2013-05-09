#!/u/shared/programs/x86_64/python/2.5.5/bin/python

# 2013-05-03, tc
# simple script to print the values of a function

#from random import uniform
import random
import sys
from math import exp

ntot=int(sys.argv[1])

for i in range(ntot):
   print (3*exp(-i*1./200)+0.5)+0.25*random.uniform(-1,1)
