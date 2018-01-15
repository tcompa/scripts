import numpy
import scipy.optimize


def fun_fit(variables_xy, par_0, par_1x, par_1y):
    return par_0 + par_1x * variables_xy[0] + par_1y * variables_xy[1]


n_points = 30
xy = numpy.random.uniform(-1.0, 1.0, (2, n_points))
z = 1.0 + 2.0 * xy[0] + 3.0 * xy[1] + numpy.random.uniform(-0.1, 0.1, n_points)

popt, pcov = scipy.optimize.curve_fit(fun_fit, xy, z)
print 'par_0:  %f +/- %f' % (popt[0], pcov[0, 0] ** 0.5)
print 'par_1x: %f +/- %f' % (popt[1], pcov[1, 1] ** 0.5)
print 'par_1y: %f +/- %f' % (popt[2], pcov[2, 2] ** 0.5)
