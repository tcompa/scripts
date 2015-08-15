#!/usr/bin/python

'''
program:       gr_2d.py
author:        tc
created:       2015-10-16 -- 00:30 CEST
last-modified: 2015-10-16 -- 00:15 CEST
description:   Computes g(r) for a set of configurations of N two-dimensional
               points uniformly distributed in a square.
notes:         The computation of the full NxN distance matrix is not optimal,
               when N is large.
'''


import numpy
import matplotlib.pyplot as plt


def compute_gr_2d(samples, N, nbins=100):
    '''
    Returns g(r). The normalization is such that for a homogeneos system at
    density rho the large-r limit is g(r) = rho.
    '''
    prob_r, edges = numpy.histogram(samples, bins=nbins, normed=True)
    r = 0.5 * (edges[1:] + edges[:-1])
    gr = prob_r * N / (2.0 * numpy.pi * r)
    return r, gr


N = 300                    # number of points
L = 1000.0 ** (1.0 / 2.0)  # edge of the cube
rho = float(N) / L ** 2    # average density

indices_upper_triangle = numpy.triu_indices(N, k=1)
n_pairs = N * (N - 1) / 2

n_config = 1000
samples = numpy.empty(n_config * n_pairs)
for i_config in xrange(n_config):
    # generate N points in the cube
    x = numpy.random.uniform(0.0, L, size=(N, 2))
    # compute NxN distance matrix (with closest-image convention)
    diff = x.reshape(N, 1, 2) - x
    diff = numpy.remainder(diff, L)
    diff[diff > L / 2.0] -= L
    dist = (diff ** 2).sum(axis=2) ** 0.5
    # store distances (without double counting)
    dist = dist[indices_upper_triangle].flatten()
    samples[i_config * n_pairs:(i_config + 1) * n_pairs] = dist[:]

# compute g(r)
r, gr = compute_gr_2d(samples, N, 200)

# plot
plt.xlabel('$r$', fontsize=20)
plt.ylabel('$g(r)$', fontsize=20)
plt.plot(r, gr, 'k-')
plt.axhline(rho, c='r', ls='--', lw=2, label='$\\rho=%s$' % rho)
plt.legend(loc='best', frameon=False)
plt.savefig('fig_gr_2d.pdf', bbox_inches='tight')
plt.show()
