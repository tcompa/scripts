cdef class MyClass1:

    def __init__(self):
        pass

    def method_def(self, double x, double y, double z):
        return x + y + z

    cpdef double method_cpdef(self, double x, double y, double z):
        return x + y + z

    cdef double method_cdef(self, double x, double y, double z):
        return x + y + z
