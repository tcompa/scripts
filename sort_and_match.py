# last modified: 2014-09-25
# author:        Tommaso Comparin
# description:   It reads a tab-delimited datafile with columns
#                (x1, y1, x2, y2), where len(x1) != len(x2)
#                It tries to match pairs (x1, x2) up to a given tolerance,
#                otherwise it fills the line with only one of the two.

import csv
import numpy
import pylab

# import tab-separated data
# columns: (TA, XA, TB, XB)
with open('data.dat', 'rb') as f:
    reading = csv.reader(f, delimiter='\t')
    columns = reading.next()
    hold_files = []
    for row in reading:
        hold_files.append(row)
data = numpy.array(hold_files)
data = data.T
TA = numpy.array([float(x) for x in data[0] if not x == ''])
XA = numpy.array([float(x) for x in data[1] if not x == ''])
TB = numpy.array([float(x) for x in data[2] if not x == ''])
XB = numpy.array([float(x) for x in data[3] if not x == ''])

# sort (TA,XA) and (TB,XB), according to the first element
iA = numpy.argsort(TA)
TA, XA = TA[iA], XA[iA]
iB = numpy.argsort(TB)
TB, XB = TB[iB], XB[iB]
nA, nB = len(TA), len(TB)
TA, TB, XA, XB = TA.tolist(), TB.tolist(), XA.tolist(), XB.tolist()

# build lines (TA, XA, TB, XB) with TA matching TB
tol    = 1.0
big_dT = max(numpy.amax(TA), numpy.amax(TB)) * 2.0
tab = []
taken = numpy.zeros(shape=(nA), dtype=numpy.int)
for iB in xrange(nB):
    # look for closest TA, excluding columns which are already taken
    dist = [abs(TB[iB] - TA[iA_]) + taken[iA_] * big_dT for iA_ in xrange(nA)]
    iA = numpy.argmin(numpy.array(dist))
    dT_min = abs(TB[iB] - TA[iA])
    if dT_min < tol:
        tab.append([TA[iA], XA[iA], TB[iB], XB[iB]])
        taken[iA] = 1
    else:
        tab.append([0, 0, TB[iB], XB[iB]])
for iA in xrange(nA):
    if not taken[iA]:
        tab.append([TA[iA], XA[iA], 0, 0])
    
# prepare column 'T', needed to sort the list of lines
tab = numpy.array(tab)
T = numpy.zeros(shape=tab.shape[0])
T += (tab[:,0] * tab[:,2] > 0) * (tab[:,0] + tab[:,2]) * 0.5 +\
     numpy.logical_and(tab[:,0] > 0, tab[:,2] == 0) * tab[:,0] +\
     numpy.logical_and(tab[:,0] == 0, tab[:,2] > 0) * tab[:,2]

# sort table according to T
tab_sorted = tab[numpy.argsort(numpy.array(T))]

# print
f = open('data_v2.dat', 'w')
for line in tab_sorted:
    f.write('%f\t%f\t%f\t%f\n' % (line[0], line[1], line[2], line[3]))
f.close()

