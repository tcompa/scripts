import numpy
import matplotlib.pyplot as plt
import cmocean

x = numpy.linspace(0.0, 3.0, 100)
y = numpy.linspace(0.0, 3.0, 100)
z = numpy.sin(x[:, None] ** 2 + y[None, :] ** 2)
z += numpy.random.uniform(-0.1, 0.1, z.shape)

plt.contourf(x, y, z, 40, cmap=cmocean.cm.phase)
plt.show()
