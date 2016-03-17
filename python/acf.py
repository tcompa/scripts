#!/usr/bin/python

'''
program: acf.py
author: tc
created: 2014-12-16
last-modified: 2016-03-17 -- 14 CEST

Compute autocorrelation function (acf) of a time series.
Two methods available:
  + Standard evaluation of C(dt)
  * FFT evaluation
'''

import sys
import math
import os
import argparse
import numpy
import matplotlib.pyplot as plt


def variance(x):
    return numpy.dot(x, x) / float(len(x))


def autocorr_std(x, dt_max=100):
    n = len(x)
    x -= x.mean()
    var = variance(x)
    C = [1.0]
    for dt in xrange(1, dt_max):
        C.append(numpy.dot(x[dt:], x[:-dt]) / float(n - dt) / var)
    return numpy.array(C)


def autocorr_fft(x, dt_max=100):
    n = len(x)
    x -= x.mean()
    fvi = numpy.fft.fft(x, n=2 * n)
    C = numpy.real(numpy.fft.ifft(fvi * numpy.conjugate(fvi))[:n])
    C /= C[0]
    # check against the definition:
    C1_check = numpy.dot(x[1:], x[:-1]) / numpy.dot(x[:-1], x[:-1])
    diff_rel = abs(C[1] - C1_check) / (C[1] + C1_check) * 2.0
    if diff_rel > 1e-3:
        print C1_check, C[1]
        print 'ERROR: fft-autocorr results != defintion. Exit'
        sys.exit()
    return C[:dt_max]


# functions
###############################################################################
# main

# parse args
parser = argparse.ArgumentParser(description='compute autocorrelation of a ' +
                                 'time series.')
parser.add_argument('filename', metavar='filename', type=str,
                    help='npy data file')
parser.add_argument('-d', '--dtmax', metavar='<D>', type=int,
                    default=100, dest='dtmax',
                    help='set max value of dt')
parser.add_argument('-m', '--method', metavar='<M>', type=str, default='std',
                    dest='method', help='choose between std (standard) or ' +
                    'fft (fast-Fourier transform')
parser.add_argument('-s', '--save', action='store_true', default=False,
                    dest='save_data', help='save acf data')
args = parser.parse_args()
assert os.path.isfile(args.filename), '[autocorr] missing file. Exit.'
assert args.filename.endswith('.npy'), '[autocorr] npy file required. Exit.'
if args.method in ['std', 'standard']:
    do_std = True
    do_fft = False
elif args.method == 'fft':
    do_std = False
    do_fft = True
else:
    sys.exit('[autocorr] wrong method (%s)' % args.method)

# read/check data
data = numpy.load(os.getcwd() + '/' + args.filename)
dimensions = len(data.shape)
assert dimensions == 1, '[autocorr] dimensions=%i. Exit.' % len(dimensions)
assert variance(data) > 0.0, '[autocorr] zero variance. Exit.'
print '[autocorr] loaded %s' % args.filename
print '[autocorr] #data = %i' % len(data)

# compute autocorrelation
if do_std:
    acf = autocorr_std(data, args.dtmax + 1)
elif do_fft:
    acf = autocorr_fft(data, args.dtmax + 1)
print '[autocorr] computed C(dt) up to dt=%i' % args.dtmax

# save
if args.save_data:
    name, ext = os.path.splitext(args.filename)
    outfile = name + '_acf.dat'
    tosave = numpy.array([numpy.arange(args.dtmax + 1), acf]).T
    numpy.savetxt(os.getcwd() + '/' + outfile, tosave)
    print '[autocorr] saved acf data in %s' % outfile

# show
FS = 18
fig, ax = plt.subplots(1, 1)
ax.plot(acf, ls='-', marker='.', lw=1.5, c='darkgreen', label=args.method)
ax.set_yscale('log')
ax.set_xlabel('$t-t_0$', fontsize=FS)
ax.set_ylabel('$C(t-t_0)/C(0)$', fontsize=FS)
ylim_low = ax.get_ylim()[0]
for i in range(8):
    y = math.exp(- i)
    if y > ylim_low:
        ax.axhline(y, c='k', ls='--', lw=1.5)
    else:
        break
ax.legend(loc='best', scatterpoints=1, numpoints=1, fontsize=FS)

plt.title(args.filename)
plt.grid()
plt.show()
plt.close()
