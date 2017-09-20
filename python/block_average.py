import numpy


def block_average(_x, d):
    ''' Block-average the 1d vector _x, for block size d. '''
    return _x[:d * (_x.shape[0] // d)].reshape(-1, d).mean(axis=1)


y = numpy.arange(10.0)
print 'Original:    ', y
print 'Bloc-avg\'d 1:', block_average(y, 1)
print 'Bloc-avg\'d 2:', block_average(y, 2)
print 'Bloc-avg\'d 4:', block_average(y, 4)
print 'Bloc-avg\'d 6:', block_average(y, 6)
