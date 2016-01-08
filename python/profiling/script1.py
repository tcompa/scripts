'''
Fake program, to be profiled via cProfile.
'''

import time


def fast_function():
    time.sleep(0.0004)


def slow_function():
    time.sleep(0.005)


def very_slow_function():
    time.sleep(0.1)


# Main program

for i in xrange(5):
    very_slow_function()
for i in xrange(50):
    slow_function()
for i in xrange(100):
    fast_function()
