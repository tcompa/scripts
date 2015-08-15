#!/usr/bin/python

'''
program: broadcasting.py
author:  tc
created: 2015-08-14 -- 14:30 CEST
notes:   numpy broadcasting rules are taken from 'Efficient Computing with
         NumPy' (tutorial by J. Vanderplas at PyData NYC 2013).
'''


import numpy


def try_sum(shape_a, shape_b):
    a = numpy.ones(shape=shape_a)
    b = numpy.ones(shape=shape_b)
    try:
        c = a + b
        print a.shape, '+', b.shape, '->', c.shape
    except ValueError:
        print a.shape, '+', b.shape, '->', 'ValueError'

print 80 * '*'
print '1. If array shapes differ, left-pad the smaller shape with 1s:'
try_sum((4), (6, 4))
try_sum((4), (4, 6))
print 40 * '-+'
print '2. If any dimension does not match, ' + \
       'broadcast the dimension with size=1:'
try_sum((1), (3))
try_sum((1, 2), (3, 2))
try_sum((1, 2, 1), (3, 1, 4))
print 40 * '+-'
print '3. If neither non-matching dimension is 1, raise an error:'
try_sum((2, 3), (2, 4))
print 40 * '-+'
print 'X. Add dummy dimensions:'
a = numpy.ones(shape=(3))
print 'a.shape =', a.shape
print 'a[None, :].shape =', a[None, :].shape
b = numpy.ones(shape=(3, 2))
print 'b.shape =', b.shape
print 'b[:, None, :].shape =', b[:, None, :].shape
print 80 * '*'
