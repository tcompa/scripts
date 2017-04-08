import time
import cython
from lib_class_1 cimport MyClass1


cdef class MyClass2:

    cdef MyClass1 C

    def __init__(self, MyClass1 C):

        self.C = C

        cdef int step, nsteps = 10000000

        t0 = time.clock()
        for step in xrange(nsteps):
            C.method_def(2.0, 3.0, 4.0)
        print 'method_def:   %e s/call' % ((time.clock() - t0) / float(nsteps))

        t0 = time.clock()
        for step in xrange(nsteps):
            C.method_cpdef(2.0, 3.0, 4.0)
        print 'method_cpdef: %e s/call' % ((time.clock() - t0) / float(nsteps))

        t0 = time.clock()
        for step in xrange(nsteps):
            C.method_cdef(2.0, 3.0, 4.0)
        print 'method_cdef:  %e s/call' % ((time.clock() - t0) / float(nsteps))

