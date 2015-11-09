#!/usr/bin/python


'''
Example for set_xscale('symlog')
'''

import matplotlib.pyplot as plt
import numpy

x = numpy.linspace(- 100.0, 100., 10000)
y = numpy.sin(x / 3.0) * x ** 2

plt.plot(x, y, '.-')
plt.grid()
plt.xscale('symlog', basex=10.0, linthreshx=10.0, linscalex=0.25)
plt.yscale('symlog', basex=10.0, linthreshy=10.0, linscaley=2.0)
plt.show()
