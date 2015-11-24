'''
program: memoize_decorator.py
created: 2015-11-24 -- 15 CEST
author: tc
'''

import os
import numpy
import time


def memoize(f):
    '''
    Decorator for the function f, used for memoization.
    '''
    def decorated_f(N):
        datafile = 'data_N%i.dat' % N
        if os.path.isfile(datafile):
            print '%s already there, no need to compute' % datafile
            res = numpy.loadtxt(datafile)
            return res
        else:
            print '%s missing, need to compute' % datafile
            res = f(N)
            numpy.savetxt(datafile, numpy.array([res]))
            return res
    return decorated_f


def long_function(alpha):
    time.sleep(2)
    return alpha ** 2


memoized_function = memoize(long_function)

for i in range(3):
    square = memoized_function(i)
