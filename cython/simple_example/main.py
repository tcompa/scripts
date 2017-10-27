import time
import numpy

from library_of_my_functions import compute_sum_of_array_py
from library_of_my_functions import compute_sum_of_array_cy_v1
from library_of_my_functions import compute_sum_of_array_cy_v2
from library_of_my_functions import compute_sum_of_array_cy_v3

# Define array of random numbers
n1 = 4000
n2 = 2000
x = numpy.random.rand(n1, n2)

time_start = time.clock()
for _ in xrange(5):
    tot = compute_sum_of_array_py(x, n1, n2)
print 'Pure python:        %.3e s [res=%f]' % (time.clock() - time_start, tot)

time_start = time.clock()
tot = compute_sum_of_array_cy_v1(x, n1, n2)
print 'Cython (version 1): %.3e s [res=%f]' % (time.clock() - time_start, tot)

time_start = time.clock()
tot = compute_sum_of_array_cy_v2(x, n1, n2)
print 'Cython (version 2): %.3e s [res=%f]' % (time.clock() - time_start, tot)

time_start = time.clock()
tot = compute_sum_of_array_cy_v3(x, n1, n2)
print 'Cython (version 3): %.3e s [res=%f]' % (time.clock() - time_start, tot)
