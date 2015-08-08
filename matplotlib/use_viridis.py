#!/usr/bin/python

'''
last-modified: 2015-08-08 -- 17 CEST
author:        tc
notes:         The viridis coloramp will be included in matplotlib >=1.5
               (see http://matplotlib.org/style_changes.html), this is just
               an example of how to use it before that version is released.
               The source of get_viridis_cmap is
               https://github.com/BIDS/colormap/blob/master/option_d.py
'''


import numpy
import matplotlib.pyplot as plt

from lib_viridis_cmap import get_viridis_cmap


def V(x, y):
    pot = -4.0 * x ** 2 - 2.0 * x ** 3 + 4.0 * x ** 4
    pot += -8.0 * y ** 2 - y ** 3 + 4.0 * y ** 4
    return pot


def show_V(cmap):
    x = numpy.linspace(-1.0, 1.0, 200)
    X, Y = numpy.meshgrid(x, x)
    Z = V(X, Y)
    plt.figure()
    C = plt.contour(X, Y, Z, 10, linewidths=0.5, linestyles='-', colors='k')
    CF = plt.contourf(X, Y, Z, 500, cmap=cmap)
    CL = plt.clabel(C, inline=1, fontsize=14, fmt='%.1f')
    CB = plt.colorbar(CF)
    plt.gca().set_aspect(1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('V(x, y)')
    plt.show()


viridis = get_viridis_cmap()
show_V(viridis)
