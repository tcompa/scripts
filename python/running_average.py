#!/usr/bin/env python

'''
program:       running_average.py
last-modified: 2015-06-08 -- 14:30
author:        tc
notes:         computes and plots the running average of a .npy dataset
'''

import argparse
import os
import sys
import numpy
import matplotlib.pyplot as plt


# Parsing and preliminary checks
P = argparse.ArgumentParser(description='Running average of a time series')
P.add_argument('filename', metavar='filename', type=str,
               help='data file (accepted: npy/dat/txt)')
P.add_argument('-s', '--skip', metavar='SKIP', type=int, default=0,
               dest='skip', help='number of steps to skip')
args = P.parse_args()
if not os.path.isfile(args.filename):
    sys.exit('ERROR: %s missing.' % args.filename)
filetype = args.filename[-3:]
if filetype not in ('npy', 'dat', 'txt'):
    sys.exit('ERROR: %s has wrong format (accepted: npy/dat/txt).' %
             args.filename)
print 'asd'

# Load data
if filetype == 'npy':
    data = numpy.load(args.filename)
else:
    data = numpy.loadtxt(args.filename)
if len(data.shape) != 1:
    sys.exit('ERROR: %s is not 1D.' % args.filename)
print '| Loaded %s (#points=%i)' % (args.filename, data.shape[0])

# Skip some data
if len(data) < args.skip:
    sys.exit('ERROR: skip=%i > #data=%i' % (args.skip, len(data)))
data = data[args.skip:]

# Compute running average
t = numpy.arange(1, data.shape[0] + 1)
running = numpy.cumsum(data) / t
print '| Final avg: %f' % running[-1]


plt.title(args.filename.split('/')[-1])
plt.grid()
plt.xlabel('Step')
plt.ylabel('Running average')
plt.plot(t, running, lw=1.5, alpha=0.9)
plt.show()
