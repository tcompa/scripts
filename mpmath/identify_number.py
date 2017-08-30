#!/usr/bin/env python

import sys
import mpmath

x = float(sys.argv[1])
mpmath.dps = 40
basis = ['e', 'pi', 'sqrt(2)', '2', '3', 'sqrt(3)']
print mpmath.identify(x, basis)
print

for p in mpmath.identify(x, basis, tol=1e-6, full=True):
    print p
