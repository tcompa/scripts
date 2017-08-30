#!/usr/bin/env python

import mpmath


# A function with no parameters
def f(x, y):
    return mpmath.exp(3.0 * x - y)


# A function with a parameter (alpha)
def g(x, y, alpha):
    return mpmath.exp(alpha * x - y)


# Point where derivatives are evaluated
point = (1.0, 1.0)

# Order of x and y derivatives
order = (2, 1)

print mpmath.diff(f, point, order)
print mpmath.diff(lambda x, y: g(x, y, 3.0), point, order)
