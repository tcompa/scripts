d = {1: 'a', 2: 'b', 'c': 3, 7: 9}
for k in range(10):
    try:
        val = d[k]
        print 'OK: d[%i]=%s' % (k, val)
    except KeyError:
        print 'KeyError: the key %i is missing' % k
