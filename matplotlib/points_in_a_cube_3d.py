#!/usr/bin/python

'''
program: points_in_a_cube_3d.py
author:  tc
created: 2015-10-13 -- 9 CEST
notes:   tested on matplotlib 1.4.3
'''

import numpy
import itertools
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d


def draw_cube(ax, L):
    '''
    Draws a [0, L] cube in the given axis (function inspired by
    http://stackoverflow.com/a/11156353).
    '''
    r = [0.0, L]
    vertices = numpy.array(list(itertools.product(r, r, r)))
    for s, e in itertools.combinations(vertices, 2):
        if numpy.sum(numpy.abs(s - e)) == r[1] - r[0]:
            ax.plot3D(*zip(s, e), color='k')


# init figure and axis
fig = plt.figure()
ax = mpl_toolkits.mplot3d.axes3d.Axes3D(fig)

# generate points in the box
L = 1.0
N = 20
x, y, z = numpy.random.uniform(0.0, L, size=(3, N))

# draw points and cube
ax.scatter(x, y, z, s=100)
draw_cube(ax, L)

# finalize and show
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.grid(False)
plt.show()
