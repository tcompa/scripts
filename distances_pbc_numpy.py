#!/usr/bin/python

'''
program:       distances_pbc_numpy.py
last-modified: 2015-07-19 -- 23 CEST
author:        tc
notes:         Computes pairwise distances in a periodic box (via closest-image
               convention) with numpy. Inspired from
               https://www.youtube.com/watch?v=EEUXKG97YRw (min 25).
'''


import numpy
import itertools
import matplotlib.pyplot as plt


N_part = 20   # number of particles
N_dim = 2     # number of dimensions
L = 1.0       # box-edge size

# randomly generate N_part N_dim-dimensional points
X = numpy.random.uniform(0.0, L, size=(N_part, N_dim))

# compute difference vectors, with PBC conventions
assert N_part < 2500, 'WARNING: the \'diff\' variable can lead to MemoryError.'
diff = X.reshape(N_part, 1, N_dim) - X
diff = numpy.remainder(diff, L)
diff[diff > L / 2.0] -= L

# compute distances, and look for nearest neighbours
dist = (diff ** 2).sum(axis=-1)
numpy.fill_diagonal(dist, numpy.inf)
i_nearest = numpy.argmin(dist, 1)

# plotting
assert N_dim == 2, 'ERROR: only plotting if N_dim = 2. Exit.'
fig, ax = plt.subplots(1, 1)

# plot main box and periodic images
for (ix, iy) in itertools.product(range(-1, 2), repeat=2):
    if ix == iy == 0:
        ax.scatter(X[:, 0] + ix * L, X[:, 1] + iy * L, s=70, c='r')
    else:
        ax.scatter(X[:, 0] + ix * L, X[:, 1] + iy * L, s=70, c='b')

# draw lines between boxes
for i in range(0, 2):
    ax.axvline(i * L, ls='--', c='k')
    ax.axhline(i * L, ls='--', c='k')

# draw arrows for nearest neighbours
for i in range(N_part):
    x1, y1 = X[i]
    dx, dy = diff[i_nearest][i][i]
    ax.arrow(x1, y1, dx, dy, head_width=0.025, head_length=0.02, fc='k',
             ec='k')

# finalize and show
ax.set_aspect(1)
ax.set_xlim(- 0.2 * L, 1.2 * L)
ax.set_ylim(- 0.2 * L, 1.2 * L)
plt.show()
