import numpy


N = 20
x = numpy.linspace(0.0, 1.0, N)
y = 2.0 + 3.0 * x + numpy.random.normal(0.0, 0.5, size=N)
yerr = numpy.random.uniform(0.2, 0.5, size=N)

numpy.savetxt('data.dat', numpy.array((x, y, yerr)).T)
