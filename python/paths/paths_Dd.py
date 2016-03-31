'''
program: paths_Dd.py
author: tc
created: 2016-03-31 -- 13 CEST
'''

import numpy


def construct_path_simple(x0, sigma, N, D):
    '''
    Construct a path starting at the D-dimensional point x0, and
    return the array [x1, .., xN].
    '''
    assert x0.size == D, 'ERROR: wrong dimension'
    d = numpy.random.normal(0.0, sigma, size=(N, D))       # displacements
    x = x0 + d.cumsum(axis=0)                              # non-shifted path
    return x


def construct_path_shifted(x0, xN, sigma, N, D):
    '''
    Construct a path between the D-dimensional points x0 and xN, and
    return the array [x1, .., xN].
    '''
    assert x0.size == D, 'ERROR: wrong dimension'
    d = numpy.random.normal(0.0, sigma, size=(N, D))       # displacements
    y = x0 + d.cumsum(axis=0)                              # non-shifted path
    s = (xN - y[-1]) / float(N)                            # last-point shift
    x = y + numpy.arange(1, N + 1)[:, None] * s[None, :]   # shifted path
    return x


def print_path(x0, p):
    '''Print a path p=[x1, .., xN], starting at x0.'''
    print '--'
    print ', '.join('{:+.3f}'.format(i) for i in x0)
    for i in p:
        print ', '.join('{:+.3f}'.format(i) for i in i)
    print '--'


# this part is executed only if the program is run directly
if __name__ == '__main__':

    # properties of paths
    D = 6
    start = numpy.zeros(D)
    end = numpy.array([1.0, 5.0, 2.0, 1.0, 5.0, 2.0])
    n_steps = 10
    sigma = 0.1

    # simple path
    path = construct_path_simple(start, sigma, n_steps, D)
    print 'Print path (simple)'
    print_path(start, path)

    # shifted path
    path = construct_path_shifted(start, end, sigma, n_steps, D)
    print 'Print path (shifted)'
    print_path(start, path)
