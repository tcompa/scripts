#!/usr/bin/env python

'''
program:       gr_2d.py
author:        tc
created:       2015-10-16 -- 00:30 CEST
last-modified: Tue Nov 22 14:42:10 CET 2016
description:   Compute g(r) for a set of configurations of N
               two-dimensional points uniformly distributed in a
               square.
notes:         The computation of the full NxN distance matrix is not
               optimal, when N is large.
'''


import math
import numpy
import matplotlib.pyplot as plt


def compute_distances(x, L, N, dim):
    '''
    Given a configuration of N points in [0, L] hypercube, computes all
    pair distances, with closest-image convention.
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


def compute_gr_2d(samples, area, nbins=100):
    '''
    Return g(r). The normalization is such that for a homogeneos
    system the large-r limit is g(r) = 1.
    '''
    prob_r, edges = numpy.histogram(samples, bins=nbins, normed=True)
    r = 0.5 * (edges[1:] + edges[:-1])
    gr = prob_r * area / (2.0 * math.pi * r)
    return r, gr


if __name__ == '__main__':

    dim = 2                  # number of dimensions
    N = 300                  # number of points
    L = 1000.0               # linear size of the box
    n_configurations = 100   # number of sampled configurations

    # generate distance samples
    n_pairs = N * (N - 1) / 2
    samples = numpy.empty(n_configurations * n_pairs)
    for i_config in xrange(n_configurations):
        # generate a configuration
        x = numpy.random.uniform(0.0, L, size=(N, dim))
        # compute all interparticle distances
        dist = compute_distances(x, L, N, dim)
        # update the list of distance samples
        samples[i_config * n_pairs:(i_config + 1) * n_pairs] = dist[:]

    # compute g(r)
    area = L ** dim
    r, gr = compute_gr_2d(samples, area, 200)

    # plot g(r)
    fig, ax = plt.subplots(1, 1)
    ax.plot(r, gr, c='k', ls='-', lw=2)
    ax.axhline(1.0, c='r', ls='--')
    ax.set_xlabel('$r$', fontsize=16)
    ax.set_ylabel('$g(r)$', fontsize=16)
    ax.set_xticks((0, L / 2.0, L / math.sqrt(2.0)))
    ax.set_xticklabels(('$0$', '$L/2$', '$L/\\sqrt{2}$'))
    ax.set_xlim(0, L / math.sqrt(2))
    ax.set_ylim(0, 1.25)
    plt.savefig('fig_gr_2d.pdf', bbox_inches='tight')
    plt.show()
