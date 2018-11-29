import numpy
import pandas
import time


datafile = '/tmp/big_pointless_file.dat'

for N in [10 ** 4, 10 ** 5, 10 ** 6]:
    numpy.savetxt(datafile, numpy.random.random((N, 2)))
    print 'Created big file (%s), with %i x 2 numbers' % (datafile, N)

    t0 = time.clock()
    x_numpy = numpy.loadtxt(datafile)
    t1 = time.clock()
    print 'Read file with numpy: %.3f s' % (t1 - t0)

    t0 = time.clock()
    x_pandas = pandas.read_csv(datafile, sep=' ', header=None).values
    t1 = time.clock()
    print 'Read file with pandas: %.3f s' % (t1 - t0)

    success = numpy.max(numpy.absolute(x_numpy - x_pandas)) < 1e-14
    print 'Are the two operations equivalent? ', success
    print
