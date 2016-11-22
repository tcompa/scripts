#!/usr/bin/env python

import random

import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

N = 100

M = numpy.random.uniform(0.0, 1.0, (N, N))

for step in xrange(20):
    for _ in xrange(1000):
        i = random.randint(0, N - 1)
        j = random.randint(0, N - 1)
        M[i, j] = min(M[i, j] + random.uniform(0.0, 2.0), 4.0)

    fig, ax = plt.subplots(1, 1, figsize=(4, 4))
    im = ax.matshow(M, vmin=0, vmax=4)
    ax.set_aspect(1)
    ax.axis('off')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)

    plt.colorbar(im, cax=cax)
    plt.savefig('snap_%03i.png' % step, bbox_inches='tight', dpi=200)
    plt.close()

