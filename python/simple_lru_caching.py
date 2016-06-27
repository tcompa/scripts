import time
try:
    from functools import lru_cache      # Py3
except ImportError:
    from functools32 import lru_cache    # Py2, needs functools32


@lru_cache()
def sum_slow(a, b, c):
    time.sleep(1)
    return a + b + c


for i in xrange(3):
    for j in xrange(3):
        for k in xrange(3):
            a, b, c = sorted((i, j, k))
            t0 = time.time()
            s = sum_slow(a, b, c)
            t1 = time.time()
            print '%i + %i + %i = %i (%.3f s)' % (i, j, k, s, t1 - t0)
