import cython


def compute_sum_of_array_py(x, n1, n2):
    tot = 0.0
    for i1 in xrange(n1):
        for i2 in xrange(n2):
            tot += x[i1, i2]
    return tot

def compute_sum_of_array_cy_v1(x, int n1, int n2):
    cdef int i1, i2
    cdef double tot = 0.0
    for i1 in xrange(n1):
        for i2 in xrange(n2):
            tot += x[i1, i2]
    return tot

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.initializedcheck(False)
def compute_sum_of_array_cy_v2(x, int n1, int n2):
    cdef int i1, i2
    cdef double tot = 0.0
    for i1 in xrange(n1):
        for i2 in xrange(n2):
            tot += x[i1, i2]
    return tot

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.initializedcheck(False)
def compute_sum_of_array_cy_v3(double [:, :] x, int n1, int n2):
    cdef int i1, i2
    cdef double tot = 0.0
    for i1 in xrange(n1):
        for i2 in xrange(n2):
            tot += x[i1, i2]
    return tot
