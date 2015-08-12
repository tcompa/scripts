#!/usr/bin/python
 

'''
program: inset_zoom.py
author:  tc
created: 2015-10-12 -- 15 CEST
notes:   tested on matplotlib 1.4.3
'''


import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.ticker import MaxNLocator


x = numpy.linspace(0.0, 10.0, 1000)
y = numpy.exp(- x ** 2)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(x, y)
axins = inset_axes(ax, 2, 2,
                   bbox_to_anchor=(0.85, 0.9),
                   bbox_transform=ax.figure.transFigure)
axins.axis([0.0, 0.3, 0.9, 1.05])
axins.plot(x, y, 'k.-')
axins.xaxis.set_major_locator(MaxNLocator(nbins=4))
axins.yaxis.set_major_locator(MaxNLocator(nbins=5, prune='upper'))

plt.show()
