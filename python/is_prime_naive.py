'''
program: is_prime_naive.py
author: tc
created: 2016-01-26

Note: pure python2, it can be executed with pypy for speedup.
'''


def is_prime(N):
    '''
    Verifies whether N is prime.
    Returns either [True] or [False, divisor].
    '''
    assert N >= 0
    if N < 3:
        return [True]
    elif N % 2 == 0 and N > 2:
        return [False, 2]
    elif N % 3 == 0 and N > 3:
        return [False, 3]
    p = 3
    while N % p:
        p += 2
        if p > N / 2:
            return [True]
    else:
        return [False, p]


if __name__ == '__main__':
    N = 1
    l = []
    while len(l) < 10000:
        if is_prime(N)[0]:
            l.append(N)
        N += 1
    print 'First %i prime numbers:' % len(l)
    print '%7i): %i' % (1, l[0])
    print '%7i): %i' % (2, l[1])
    print '      ... ...'
    print '%7i): %i' % (len(l), l[len(l) - 1])
