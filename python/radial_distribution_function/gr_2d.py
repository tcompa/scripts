#!/usr/bin/python

'''
program:       gr_2d.py
author:        tc
created:       2015-10-16 -- 00:30 CEST
last-modified: 2015-10-16 -- 15:30 CEST
description:   Computes g(r) for a set of configurations of N two-dimensional
               points uniformly distributed in a square.
notes:         The computation of the full NxN distance matrix is not optimal,
               when N is large.
'''


import numpy
import matplotlib.pyplot as plt


def generate_one_conf(L, N, dim):
    '''
    Generates a configuration for N dim-dimensional points in a dim-dimensional
    hypercube of edge L.
    '''
    return numpy.random.uniform(0.0, L, size=(N, dim))


def compute_distances(x, L, N, dim):
    '''
    Given a configuration of N points in [0, L] hypercube, computes all pair
    distances, with closest-image convention.
    '''
    assert x.shape[0] == N
    # compute NxN distance matrix (with closest-image convention)
    diff = x.reshape(N, 1, dim) - x
    diff = numpy.remainder(diff, L)
    diff[diff > L / 2.0] -= L
    dist = (diff ** 2).sum(axis=2) ** 0.5
    # store distances (without double counting)
    dist = dist[numpy.triu_indices(N, k=1)].flatten()
    return dist


def compute_gr_2d(samples, N, nbins=100):
    '''
    Returns g(r). The normalization is such that for a homogeneos system at
    density rho the large-r limit is g(r) = rho.
    '''
    prob_r, edges = numpy.histogram(samples, bins=nbins, normed=True)
    r = 0.5 * (edges[1:] + edges[:-1])
    gr = prob_r * N / (2.0 * numpy.pi * r)
    return r, gr


def plot_gr(r, gr, rho):
    plt.figure()
    plt.xlabel('$r$', fontsize=20)
    plt.ylabel('$g(r)$', fontsize=20)
    plt.plot(r, gr, 'k-')
    plt.axhline(rho, c='r', ls='--', lw=2, label='$\\rho=%s$' % rho)
    plt.legend()
    plt.savefig('fig_gr_2d.pdf', bbox_inches='tight')
    plt.close()


if __name__ == '__main__':

    dim = 2       # number of dimensions
    N = 300       # number of points
    L = 1000.0    # linear size of the box

    n_pairs = N * (N - 1) / 2

    # generate samples
    n_config = 100
    samples = numpy.empty(n_config * n_pairs)
    for i_config in xrange(n_config):
        x = generate_one_conf(L, N, dim)
        dist = compute_distances(x, L, N, dim)
        samples[i_config * n_pairs:(i_config + 1) * n_pairs] = dist[:]

    # compute and plot g(r)
    r, gr = compute_gr_2d(samples, N, 200)
    plot_gr(r, gr, float(N) / L ** dim)
