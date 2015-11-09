#!/usr/bin/python

'''
notes: only serves as a main program for lib_random_gsl
'''

import time
from lib_random_gsl import stats_gaussian as stats_gaussian

# parameters
nsteps = 10 ** 8
sigma = 1.5

# computation
time_start = time.clock()
av, var = stats_gaussian(nsteps, sigma)
time_end = time.clock()

# output
print 'nsteps:   %e' % nsteps
print 'sigma:    %f' % sigma
print 'average:  %f (exact: 0)' % av
print 'variance: %f (exact: %f)' % (var, sigma ** 2)
print '[elapsed time: %.2f s]' % (time_end - time_start)
