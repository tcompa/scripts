#!/usr/bin/python

'''
created: 2015-08-31 -- 18 CEST
author:  tc
description: produces a scatter-plot with empty symbols
'''


import numpy
import matplotlib.pyplot as plt


N = 25
x = numpy.arange(N)
y = numpy.random.normal(x ** 0.5, 0.2)
plt.scatter(x, y, s=100, facecolor='none', edgecolor='k', linewidth=2)
plt.grid()
plt.show()
