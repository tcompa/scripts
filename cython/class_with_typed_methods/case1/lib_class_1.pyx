import time


cdef class MyClass1:

    def __init__(self):
        pass

    def method_def(self, double x, double y, double z):
        return x + y + z

    cpdef double method_cpdef(self, double x, double y, double z):
        return x + y + z

    cdef double method_cdef(self, double x, double y, double z):
        return x + y + z


cdef class MyClass2:

    def __init__(self, MyClass1 C):

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
