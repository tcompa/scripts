#!/usr/bin/python

'''
program:     hypergeometric_functions_with_mpmath.py
author:      tc
created:     2015-10-17 -- 11 CEST
description: computes some hypergeometric functions with mpmath, and checks
             with Mathematica values.
notes:       hyp0f1(a, z) fails at a=0, while the Mathematica version does not.
'''

import mpmath

a = [1, 1]
b = [3, 3, 3]
z = 2.0
res1 = float(mpmath.hyper(a, b, z))
res2 = float(mpmath.hyp0f1(1, 2))
print 'HypergeometricPFQ[{1, 1}, {3, 3, 3}, 2.0]: 1.07893'
print 'mpmath.hyper([1, 1], [3, 3, 3], 2.0):      %f' % res1
print 'Hypergeometric0F1Regularized[1, 2]: 4.25235'
print 'mpmath.hyp0f1(1, 2):                %f' % res2
