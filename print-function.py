#!/u/shared/programs/x86_64/python/2.5.5/bin/python

# 2013-05-03, tc
# simple script to print the values of a function

from math import cos,pi

def f1(x):
  return cos(x*2*pi)


xmin=0
xmax=10
nx=100  # number of points is nx+1
dx=(xmax-xmin)/(nx+1.)

for i in range(nx+1):
   x=i*dx
   print x,f1(x)
