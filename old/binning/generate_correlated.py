import random

x = 0.0
delta = 0.1
for i in xrange(100000):
    x = (x + random.uniform(-delta, delta)) % 1.0
    print x
