#!/usr/bin/env python

'''
program: hdf5_observable.py
created: Thu Feb  2 21:59:41 CET 2017
author: tc
'''

import sys
import h5py


datafile = sys.argv[1]
observable = sys.argv[2]
assert datafile.endswith('h5'), 'Error, this works with *.h5 files.'
assert observable in ['Density', 'Energy', 'Stiffness',
                      'D', 'E', 'S', 'd', 'e', 's']
observable = 'Density' if observable in ['D', 'd'] else observable
observable = 'Energy' if observable in ['E', 'e'] else observable
observable = 'Stiffness' if observable in ['S', 's'] else observable

f = h5py.File(datafile, 'r')
p = '/simulation/results/%s/' % observable


mean = f[p + 'mean/value'][()]
error = f[p + 'mean/error'][()]
error_convergence = f[p + 'mean/error_convergence'][()]
variance = f[p + 'variance/value'][()]
stddev = variance ** 0.5
count = f[p + 'count'][()]
tau = f[p + 'tau/value'][()]


print 'file:       %s' % datafile
print 'observable: %s' % observable
print 'mean:       %12f' % mean
print 'error:      %12f (convergence: %i)' % (error, error_convergence)
print 'naive_err:  %12f' % (stddev / (count / (2.0 * tau)) ** 0.5)

print ('count:         %.1e' % count).replace('e+0', ' x 10^')
print ('tau:           %.1e' % tau).replace('e+0', ' x 10^')
