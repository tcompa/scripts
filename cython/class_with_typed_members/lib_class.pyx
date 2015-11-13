'''
program: lib_class.pyx
created: 2015-11-13 -- 10 CEST
'''

import numpy


cdef class MyClass:

    cdef public int N
    cdef public double x, y

    def __init__(self, int Nval=10):
        print '[MyClass.__init__]'
        self.N = Nval
        self.x = 1.3

    def print_all(self):
        print '[MyClass.print_all]'
        print '  self.N = %i' % self.N
        print '  self.x = %f' % self.x

    def reset_N(self, int Nval):
        print '[MyClass.reset_N]'
        print '  resetting self.N to %i' % Nval
        self.N = Nval

    cpdef double get_x_power_N(self):
        print '[MyClass.get_x_power_N]'
        cdef double res = 1.0
        cdef int i_dummy
        for i_dummy in xrange(self.N):
            res *= self.x
        return res
