import math

def cos_sum_cython(double a, double b):
    return math.cos(a + b)


cdef extern from "function_cos_sum.h":
    double __cos_sum_c "cos_sum"(double, double)


def cos_sum_c(double a, double b):
    return __cos_sum_c(a, b)
