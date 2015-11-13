'''
program: lib_class.pyx
created: 2015-11-13 -- 15 CEST
'''

import numpy
import cython


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.initializedcheck(False)
cdef class MyClass:

    # do not set N as public, since it will give the size of the array array
    cdef int N
    cdef public double [:]array

    def __init__(self, int Nval=8):
        print '[MyClass.__init__]'
        self.N = Nval
        self.array = numpy.zeros(self.N)

    def print_all(self):
        print '  self.N = %i' % self.N
        cdef int i_dummy
        for i_dummy in xrange(self.N):
            print '  self.array[%i] = %f' % (i_dummy, self.array[i_dummy])
        print

    def reset_N(self, int Nval):
        print '!! WARNING'
        print '!! I do not want to change N, because it gives the size of the'
        print '!! array self.array.'
        print '!! Exit (not doing anything).'
        print

    cpdef double sum_array(self):
        cdef double res = 0.0
        cdef int i_dummy
        for i_dummy in xrange(self.N):
            res += self.array[i_dummy]
        return res
