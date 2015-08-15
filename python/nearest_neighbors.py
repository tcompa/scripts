#!/usr/bin/python

'''
last-modified: 2015-08-08 -- 16:30 CEST
author:        tc
notes:         MemoryError for large npts
'''


import numpy


def nearest(x, npts, ndimi, L):
    '''
    Computes nearest neighbours for a set of npts ndim-dimensional points in a
    [0, L] periodic box, with nearest-image convention. Based on 'Efficient
    Computing with NumPy', tutorial by J. Vanderplas at PyData NYC 2013.
    '''
    # preliminary checks
    assert len(x.shape) == 2, 'ERROR: len(x.shape) != 2'
    assert x.shape[0] == npts, 'ERROR: x.shape[0] != npts.'
    assert x.shape[1] == ndim, 'ERROR: x.shape[1] != ndim.'
    # compute relative positions, with nearest-image convention
    diff = x.reshape(npts, 1, ndim) - x
    diff = numpy.remainder(diff, L)
    diff[diff > L / 2.0] -= L
    dist = (diff ** 2).sum(axis=2) ** 0.5
    # find nearest neighbours
    i = numpy.arange(npts)
    dist[i, i] = numpy.inf
    i_nearest = numpy.argmin(dist, 1)
    return i_nearest


if __name__ == '__main__':
    npts = 100   # number of points
    ndim = 3     # number of dimensions
    L = 1.0      # box edge
    x = numpy.random.uniform(0.0, L, (npts, ndim))
    i_nearest = nearest(x, npts, ndim, L)

    for p in range(10):
        print 'nearest neighbor of %4i: %4i' % (p, i_nearest[p])
