#!/u/shared/programs/x86_64/python/2.5.5/bin/python

# 2013-05-09, tc
# 
# Use:
#   ./pp.py data.d [lbin=1] [bin0=0]
#

import numpy 
from math import sqrt
import sys
import matplotlib.pyplot as pyplot

print
if len(sys.argv)<2:
  print '*****************************************'
  print 'usage: ./pp.py filename [lbin=1] [bin0=0]'
  print '*****************************************'
  quit()
elif len(sys.argv)<3:
  print '[default]: lbin=1, bin0=0'
  filename = sys.argv[1]
  lbin=1
  bin0=0
elif len(sys.argv)<4:
  print '[default]: bin0=0'
  filename = sys.argv[1]
  lbin=int(sys.argv[2])
else:
  filename = sys.argv[1]
  lbin=int(sys.argv[2])
  bin0=int(sys.argv[3])

#import data
y=numpy.loadtxt(filename)
rows=len(y)
if len(y.shape)>1:
  print 'ERROR: only works if each row has the same number of elements'
  quit()

#binning
j=0
bin=0
ybins=[]
if(rows%lbin==0): maxj=rows
else: maxj=rows-lbin
while j<maxj:
  sum=0
  while j<(bin+1)*lbin:
    sum+=y[j]
    j+=1
  ybins.append(sum/lbin*1.)
  bin+=1
nbinstot=bin
nbins=nbinstot-bin0


#analysis of the binned data
sum=0
sum2=0
count=0
for i in range(bin0,nbinstot,1):
  sum+=ybins[i]
  sum2+=ybins[i]**2
  count+=1
#check
if(count!=nbins):
  print 'ERROR: there are',count,'bins, not',nbins,"\n"
  quit()
av=sum/nbins
av2=sum2/nbins
var=av2-av**2
std=sqrt(var/nbins)

#output
print 'nrows:        ',nbinstot*lbin,'+',rows-nbinstot*lbin
print 'binning:      ',nbinstot,'bins, L =',lbin
print 'starting bin: ',bin0
print 'n bins:       ',nbins
print 'average:      ',av
print 'average2:     ',av2
print 'variance:     ',var
print 'std (av):     ',std


#plot
pyplot.figure()
pyplot.plot(ybins)
pyplot.axhline(av,linewidth=1.5,color='r')
pyplot.axhline(av+std,linewidth=1,color='r')
pyplot.axhline(av-std,linewidth=1,color='r')
x1,x2,y1,y2 = pyplot.axis()
pyplot.axis((x1,x2,0,y2))
pyplot.draw()
pyplot.show()

