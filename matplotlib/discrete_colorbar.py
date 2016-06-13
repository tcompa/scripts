'''
program: discrete_colorbar.py
author: tc
created: 2016-06-13 -- 18 CEST
'''

import numpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm

N = 5
colors = iter([cm.viridis(x) for x in numpy.linspace(0.0, 0.9, N)])
x = numpy.linspace(0, 10)
for i in range(N):
    plt.plot(x, x / 2.0 + i, lw=3, c=colors.next())
plt.show()
