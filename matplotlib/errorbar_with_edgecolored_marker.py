import numpy
import matplotlib.pyplot as plt


x = numpy.linspace(0.0, 1.0, 100)
y = numpy.random.normal(x ** 2, 0.02)
e = numpy.random.normal(0.1, 0.02, x.shape)

plt.errorbar(x, y, yerr=e, marker='o',
             markerfacecolor='r', markeredgecolor='k',
             markevery=4, errorevery=12,
             lw=0.5, elinewidth=2)
plt.show()
