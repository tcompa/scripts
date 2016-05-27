#https://github.com/cython/cython/wiki/tutorials-NumpyPointerToC

import cython

# import both numpy and the Cython declarations for numpy
import numpy as np
cimport numpy as np

# declare the interface to the C code
cdef extern from "function_multiply_array_by_two.h":
    void c_multiply_array_by_two "multiply_array_by_two"(double *, int)


@cython.boundscheck(False)
@cython.wraparound(False)
def cython_multiply_array_by_two(np.ndarray[double, ndim=1, mode="c"] input not None):
    cdef int n
    n = input.shape[0]
    c_multiply_array_by_two(&input[0], n)
    return input[:]
