#!/usr/bin/python

'''
program:       gr_3d.py
author:        tc
created:       2015-10-15 -- 16 CEST
last-modified: 2015-10-15 -- 16 CEST
'''

import matplotlib.pyplot as plt
import numpy
import time
import math

def dist_sq(pos_A, pos_B, L):
    diff    = numpy.remainder(pos_A - pos_B, L)
    diff    = numpy.minimum(diff, L - diff)
    dist_sq = (diff ** 2).sum(axis=0)
    return dist_sq

N = 500
L = 1000.0 ** (1.0 / 3.0)
rho = float(N) / L ** 3

nsnaps = 1000
nruns = 1
t_start = time.clock()

upper_triangle = numpy.triu_indices(N, k=1)

all_dist = numpy.empty(nsnaps * N * (N - 1) / 2)
for snap in xrange(nsnaps):
    x = numpy.random.uniform(0.0, L, size=(N, 3))
    diff = x.reshape(N, 1, 3) - x
    diff = numpy.remainder(diff, L)
    diff[diff > L / 2.0] -= L
    dist = (diff ** 2).sum(axis=2) ** 0.5
    dist = dist[upper_triangle].flatten()
    assert dist.shape[0] == N * (N - 1) / 2
    all_dist[snap * N * (N - 1) / 2:(snap + 1) * N * (N - 1) / 2] = dist[:]
t_end = time.clock()
print '[elapsed time: %.1f sec]' % (t_end - t_start)

# raw histograms
h2, b2 = numpy.histogram(all_dist, normed=True, bins=100)
b2 = 0.5 * (b2[1:] + b2[:-1])
numpy.savetxt('data-uncorrelated-d2.dat', numpy.array([b2, h2]).T)

r = b2[:]
Pr_r2 = h2[:] * N * (N - 1) / 2

rho_gr = 2.0 * Pr_r2 / (N * 4.0 * math.pi * r ** 2)

rho_av = rho_gr[r < 2.0].mean()

plt.plot(r, rho_gr)
plt.axhline(rho, c='k', ls='--', lw=2)
plt.savefig('fig_gr.pdf', bbox_inches='tight')
plt.show()

