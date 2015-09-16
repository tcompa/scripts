'''
program: bars_3d.py
author: tc
created: 2015-09-16 -- 23:30 CEST
useful links:
    + http://matplotlib.org/examples/mplot3d/hist3d_demo.html
    + http://stackoverflow.com/a/27080258
'''

import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D


def show_matrix_3d(M):

    # preliminary checks
    assert isinstance(M, numpy.ndarray), 'ERROR: M is not a numpy array'
    assert len(M.shape) == 2, 'ERROR: M should be 2D, not %iD' % len(M.shape)
    Nx, Ny = M.shape
    if Nx != Ny:
        print 'WARNING: not tested for rectangular matrix'
    if M.min():
        print 'WARNING: min(M)<0 can give strange visualization'

    # create x and y indices
    X = numpy.empty_like(M)
    Y = numpy.empty_like(M)
    # TODO: replace this for loop with a numpy function
    for ix in xrange(Nx):
        for iy in xrange(Ny):
            X[ix, iy] = ix
            Y[ix, iy] = iy
    X = X.flatten()
    Y = Y.flatten()

    # flatten Z and prepare colors
    Z = M.flatten()
    Z_zeros = numpy.zeros_like(Z)
    norm = matplotlib.colors.Normalize(-1, 1)
    colors = cm.RdBu(norm(Z))

    # plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(X, Y, Z_zeros, 1, 1, Z, color=colors)
    plt.show()


# create a 2D matrix to visualize
N = 25
X = numpy.arange(N)
Y = numpy.arange(N)
M = numpy.exp(- (X[:, None] / 2.0 - Y[None, :]) ** 2 -
              numpy.absolute((X[:, None] - 10.0) / 3.0))
M = numpy.random.normal(M + 0.5, 0.1)

# do it
show_matrix_3d(M)
