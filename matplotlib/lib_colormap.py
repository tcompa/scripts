#!/usr/bin/python

'''
program:     lib_colormap.py
author:      tc
created:     2015-09-23 -- 16 CEST
description: given three one-dimensional arrays x, y, and z, plots the colormap
             of z as a function of (x,y)
'''

import numpy
import scipy.interpolate
import matplotlib.pyplot as plt

# define colormap

_all_ = ['colormap_custom']


def choose_colors():
    '''
    Returns a matplotlib colormap (the custom lib_viridis, if available, or the
    coolwarm_r).
    In case of problems, replace this entire function with its last line:
        return plt.get_cmap('coolwarm_r')
    '''
    import imp
    try:
        imp.find_module('lib_viridis_cmap')
        from lib_viridis_cmap import get_viridis_cmap
        return get_viridis_cmap()
    except ImportError:
        return plt.get_cmap('coolwarm_r')


def colormap_custom(x, y, z, nlevels=10, nlines=10, ngrid=[20, 20]):
    '''
    notes
    '''

    # choose colors
    cm = choose_colors()

    # grid (x,y) data and interpolate z (methods: nearest, linear, or cubic)
    xmin, xmax = x.min() * 0.999, x.max() * 1.0001
    ymin, ymax = y.min() * 0.999, y.max() * 1.0001
    ngrid_x, ngrid_y = ngrid[:]
    xi = numpy.linspace(xmin, xmax, ngrid_x)
    yi = numpy.linspace(ymin, ymax, ngrid_y)
    zi = scipy.interpolate.griddata((x, y), z, (xi[None, :], yi[:, None]),
                                    method='linear')

    # plot measurement points
    plt.plot(x, y, 'k.')

    # plot colormap
    CC = plt.contourf(xi, yi, zi, nlevels, cmap=cm)
    cbar = plt.colorbar(CC)
    cbar.ax.tick_params(labelsize=16)

    # plot contour lines
    CS = plt.contour(xi, yi, zi, nlines, lw=0.5, colors='k')
    fmt = {l: '%.1f' % l for l in CS.levels}
    CL = plt.clabel(CS, inline=True, fmt=fmt, fontsize=14)

    # finalize and show
    plt.xlabel('x label', fontsize=16)
    plt.ylabel('y label', fontsize=16)
    plt.grid()
    plt.show()


if __name__ == '__main__':

    # create random points to plot
    N = 100
    x = numpy.random.uniform(0.0, 1.0, N)
    y = numpy.random.uniform(0.0, 1.0, N)
    z = x ** 2 + y ** 2 + numpy.random.uniform(0.0, 0.3, N)

    colormap_custom(x, y, z, nlevels=20, nlines=10, ngrid=[30, 30])
