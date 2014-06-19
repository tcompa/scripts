# Example of numpy functions

import numpy

print 80 * '-'

# generate some initial numpy array
a = numpy.random.uniform(size=(7,3))
print 'a:'
print a
print 50 * '-'

# simple function
b = a ** 2 + 2.6 * a
print 'b'
print b
print 50 * '-'

# complicated function
def function(x):
    p1 = numpy.exp(-x ** 2 / 3.0)
    p2 = numpy.sinh(1.0 - x)
    p3 = numpy.tan(x) * (1.0 - x)
    return (p1 * p2 - p3)
c = function(a)
print 'c'
print c
print 50 * '-'
