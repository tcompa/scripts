'''
program: lib_random_gsl.pyx
created: 2015-10-07 -- 12 CEST

#FIXME: add original reference
'''

# declaring external GSL functions to be used
cdef extern from "gsl/gsl_rng.h":
    ctypedef struct gsl_rng_type:
        pass
    ctypedef struct gsl_rng:
        pass
    gsl_rng_type * gsl_rng_mt19937
    gsl_rng * gsl_rng_alloc(gsl_rng_type * T)


cdef extern from "gsl/gsl_randist.h":
    double gamma "gsl_ran_gamma"(gsl_rng * r, double, double)
    double gaussian "gsl_ran_gaussian"(gsl_rng * r, double)


cdef gsl_rng * r = gsl_rng_alloc(gsl_rng_mt19937)


def stats_gaussian(int nsamples, double sigma):
    '''
    Generates gaussian random samples and computes average and variance.
    '''
    cdef double x
    cdef double tot = 0.0
    cdef double tot_sq = 0.0
    cdef int sample
    for sample in xrange(nsamples):
        x = gaussian(r, sigma)
        tot += x
        tot_sq += x ** 2
    av = tot / float(nsamples)
    av_sq = tot_sq / float(nsamples)
    var = av_sq - av ** 2
    return av, var
