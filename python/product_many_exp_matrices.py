#!/usr/bin/python

'''
program: product_many_exp_matrices.py
author: tc, lp
created: 2015-11-12
'''


import numpy
import math


def sum_log_naive(A, B):
    '''
    Computes the element-wise log of the product of the element-wise exp of
    to 2x2 matrices A and B.
    '''
    assert A.shape == (2, 2)
    assert B.shape == (2, 2)
    return numpy.log(numpy.dot(numpy.exp(A), numpy.exp(B)))


def sum_log_safe(A, B):
    '''
    Computes the element-wise log of the product of the element-wise exp of
    to 2x2 matrices A and B, in a way which tries to avoid includes products of
    large numbers.
    '''
    assert A.shape == (2, 2)
    assert B.shape == (2, 2)
    C = numpy.empty((2, 2))
    arg_min, arg_max = sorted([A[0, 0] + B[0, 0], A[0, 1] + B[1, 0]])
    C[0, 0] = arg_max + math.log(1.0 + math.exp(arg_min - arg_max))
    arg_min, arg_max = sorted([A[0, 0] + B[0, 1], A[0, 1] + B[1, 1]])
    C[0, 1] = arg_max + math.log(1.0 + math.exp(arg_min - arg_max))
    arg_min, arg_max = sorted([A[1, 0] + B[0, 0], A[1, 1] + B[1, 0]])
    C[1, 0] = arg_max + math.log(1.0 + math.exp(arg_min - arg_max))
    arg_min, arg_max = sorted([A[1, 1] + B[1, 1], A[1, 0] + B[0, 1]])
    C[1, 1] = arg_max + math.log(1.0 + math.exp(arg_min - arg_max))
    return C


# test that the two functions give the same result
A = numpy.random.uniform(0.0, 1.0, (2, 2))
B = numpy.random.uniform(0.0, 1.0, (2, 2))
if numpy.allclose(sum_log_safe(A, B), sum_log_naive(A, B)):
    print 'Ok. The two functions seem to do the same, on a simple example.'
else:
    sys.exit('ERROR: the two functions are different, on a simple example')

# use the two functions in a more realistic case, where the naive one fails
print 'Now moving to a more realistic example'
Nmat = 30000
M = numpy.random.uniform(0.0, 1.1, (Nmat, 2, 2))
Mlog = numpy.log(M)
prod_naive = reduce(sum_log_naive, Mlog)
prod_safe = reduce(sum_log_safe, Mlog)
print 'Element-wise log of the product, using *naive* version:'
print prod_naive
print 'Element-wise log of the product, using *safe* version:'
print prod_safe
