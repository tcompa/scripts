#!/usr/bin/python

'''
program: importance_sampling.py
created: 2015-09-09 -- 18 CEST
author:  tc
notes:   takes samples from the probability distribution Q(x), and computes
         average observables for the probability distribution P(x)
'''

import numpy


def obs(a):
    '''
    An observable.
    '''
    return a ** 2


def P(a):
    '''
    Gaussian distribution with sigma=1
    '''
    s = 1.0
    return numpy.exp(- 0.5 * (a / s) ** 2) / numpy.sqrt(2.0 * numpy.pi) / s


def Q(a):
    '''
    Gaussian distribution with sigma=2
    '''
    s = 2.0
    return numpy.exp(- 0.5 * (a / s) ** 2) / numpy.sqrt(2.0 * numpy.pi) / s


N = 10000000                           # number of samples
xP = numpy.random.normal(0.0, 1.0, N)  # samples from P
xQ = numpy.random.normal(0.0, 2.0, N)  # samples from Q

print '< obs(x) >_P:               %f' % obs(xP).mean()
print '< obs(y) >_Q:               %f' % obs(xQ).mean()
print '< obs(y) * P(y) / Q(y) >_Q: %f' % (obs(xQ) * P(xQ) / Q(xQ)).mean()
