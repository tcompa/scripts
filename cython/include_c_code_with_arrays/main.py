import numpy
from wrapper import cython_multiply_array_by_two

a = numpy.arange(0.0, 3.0, 0.5)
print a
a = cython_multiply_array_by_two(a)
print a
