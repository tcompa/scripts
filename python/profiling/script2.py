'''
Fake program, to be profiled via cProfile.
'''

import math
import random


def function1():
    x = 0
    N = 10000
    numbers = range(N)
    for i in range(N):
        x += random.random()
        x += math.cos(x)
        numbers.pop()


def function2():
    N = 10
    l = []
    for i in xrange(N):
        for j in xrange(N):
            for k in xrange(N):
                for h in xrange(N):
                    s = sorted([i, j, k, h])
                    l.append(s)


# Main program

for i in xrange(50):
    for j in xrange(10000):
        eta = random.random()
    if eta < 0.66:
        function1()
    else:
        function2()
