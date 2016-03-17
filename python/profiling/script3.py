'''
Fake program, to be profiled via kernprof. Note: naively running in python
fails, due to the @profile decorators.
'''

import math


@profile
def useful_function_1():
    for i in xrange(100):
        b = math.sqrt(1.0)
        for j in xrange(10):
            b = math.exp(1.0)


@profile
def useful_function_2():
    for i in xrange(100):
        if i % 2 == 0:
            b = math.cos(1.0)
        elif i % 3 == 0:
            continue
        else:
            b = sum(math.factorial(n) for n in xrange(100))


def useless_function():
    print 'This function is pointless.'


# Main program

useless_function()
useful_function_1()
useless_function()
useful_function_2()
useless_function()
