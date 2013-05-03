#!/u/shared/programs/x86_64/python/2.5.5/bin/python

# 2013-05-02, tc
# 
# Use:
#   ./integrate.py data.d
#
# The program computes (by the trapezoidal rule) the integral
# of one or more functions stored in the file 'data.d' as:
#   x0 f1(x0) f2(x0) ..
#   x1 f1(x1) f2(x1) ..
#   ..
#
# Note: recasting the data is not necessary, but makes the code
#       nicer.

import numpy 
import sys

#load data
filename = sys.argv[1]
#filename=raw_input()
data = numpy.loadtxt(filename)
rows=len(data)
cols=len(data[0])
nsets=cols-1

print 'WARNING: only works if each row has the same number of elements'
print nsets,'sets of data with',rows,'elements each.'

#recast data
x=[]
y=numpy.zeros((rows,nsets))
for i in range(rows):
  x.append(data[i][0])
  for j in range(1,cols):
    y[i][j-1]=data[i][j]

#compute the integrals
sum=numpy.zeros(nsets)
i
for j in range(nsets):
   for i in range(rows-1):
     sum[j]+=(x[i+1]-x[i])*(y[i][j]+y[i+1][j])
   sum[j]/=2.

print sum


