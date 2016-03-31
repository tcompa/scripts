'''
program: paths_2d.py
author: tc
created: 2016-03-31 -- 11 CEST
'''

import numpy


def construct_path_simple(x0, sigma, N):
    '''
    Construct a path starting at the 2D point x0, and return the array
    [x1, .., xN].
    '''
    d = numpy.random.normal(0.0, sigma, size=(N, 2))       # displacements
    x = x0 + d.cumsum(axis=0)                              # non-shifted path
    return x


def construct_path_shifted(x0, xN, sigma, N):
    '''
    Construct a path between the 2D points x0 and xN, and return the
    array [x1, .., xN].
    '''
    d = numpy.random.normal(0.0, sigma, size=(N, 2))       # displacements
    y = x0 + d.cumsum(axis=0)                              # non-shifted path
    s = (xN - y[-1]) / float(N)                            # last-point shift
    x = y + numpy.arange(1, N + 1)[:, None] * s[None, :]   # shifted path
    return x


def plot_path(x0, p, ax):
    '''Plot a path p=[x1, .., xN], starting at x0.'''
    x = [x0[0]] + p[:, 0].tolist()
    y = [x0[1]] + p[:, 1].tolist()
    ax.plot(x, y)


# this part is executed only if the program is run directly
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    # properties of paths
    start = numpy.array([0.0, 0.0])
    end = numpy.array([1.0, 5.0])
    n_steps = 50
    sigma = 0.05

    # some plotting options
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.set_title('simple paths', fontsize=18)
    ax2.set_title('shifted paths', fontsize=18)
    ax1.scatter(start[0], start[1], s=75, zorder=10)
    ax2.scatter(start[0], start[1], s=75, zorder=10)
    ax2.scatter(end[0], end[1], s=75, zorder=10)

    # construct/plot the paths
    n_paths = 6
    for i in xrange(n_paths):
        # non-shifted path
        path = construct_path_simple(start, sigma, n_steps)
        plot_path(start, path, ax1)
        # shifted path
        path = construct_path_shifted(start, end, sigma, n_steps)
        plot_path(start, path, ax2)

    plt.tight_layout()
    plt.show()
