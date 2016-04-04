'''
program: histo_2d.py
author: tc
created: 2016-04-04 -- 14:30 CEST

Notes:
I use histogram2d+matshow instead of hexbin, since I find it easier for
having a different resolution on the two axis.
'''

import numpy
import matplotlib.pyplot as plt


x = numpy.random.normal(0.0, 1.0, 10000)
y = numpy.random.normal(0.0, 3.0, 10000)

H, x_edges, y_edges = numpy.histogram2d(x, y, bins=(10, 30))
extent = [x_edges[0], x_edges[-1], y_edges[0], y_edges[-1]]

fig, ax = plt.subplots(1, 1)
ax.matshow(H,                           # the matrix to plot
           origin='lower',              # sets the origin on the bottom
           extent=extent                # (left, right, bottom, up) limits
           )
ax.xaxis.set_ticks_position('bottom')   # moves the x-axis ticks below the plot
ax.set_aspect(0.3)                      # change the aspect ratio
plt.show()
