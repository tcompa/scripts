#!/usr/bin/python

'''
program: integral_1d.py
authors: tc
created: 2015-10-07 -- 10 CEST
notes: computes a 1d integral with sympy
'''

import sympy

x = sympy.symbols('x', real=True)


def f(x):
    return sympy.exp(- x ** 2 / 2)

integral = sympy.integrate(f(x), (x, - sympy.oo, sympy.oo))
print '$int_{-\infty}^\infty \exp(-x^2 / 2)$:'
print integral
