import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(0.0, 1.0, 10000)
y = numpy.random.normal(0.0, 3.0, 10000)

H, xe, ye = numpy.histogram2d(x, y, bins=(10, 30))

fig, ax = plt.subplots(1, 1)
ax.matshow(H, origin='lower', extent=[xe[0], xe[-1], ye[0], ye[-1]])
ax.xaxis.set_ticks_position('bottom')
ax.set_aspect(0.3)
plt.show()
