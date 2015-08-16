'''
created: 2015-10-16 -- 15:30 CEST
author: tc
'''


from nose.tools import assert_equal
from nose.tools import assert_greater_equal
from nose.tools import assert_less_equal

import numpy
import sys
sys.path.append('../python/radial_distribution_function/')

from gr_2d import generate_one_conf
from gr_2d import compute_distances
from gr_2d import compute_gr_2d
from gr_2d import plot_gr


class test_gr_2d():

    def test_generate_one_conf(self):
        N = 25
        dim = 2
        L = 100.0
        x = generate_one_conf(L, N, dim)
        assert_equal(x.shape, (N, dim))
        assert_greater_equal(x.min(), 0.0)
        assert_less_equal(x.max(), L)

    def test_compute_distances(self):
        N = 25
        dim = 2
        L = 100.0
        x = generate_one_conf(L, N, dim)
        dist = compute_distances(x, L, N, dim)
        assert_equal(dist.shape[0], N * (N - 1) / 2)

    def test_compute_gr_2d(self):
        N = 25
        dim = 2
        L = 100.0
        x = generate_one_conf(L, N, dim)
        dist = compute_distances(x, L, N, dim)
        r, gr = compute_gr_2d(dist, N, nbins=100)
        assert_greater_equal(gr.min(), 0.0)
        assert_less_equal(gr.max(), L * numpy.sqrt(dim))

    def test_plot_gr(self):
        N = 25
        dim = 2
        L = 100.0
        x = generate_one_conf(L, N, dim)
        dist = compute_distances(x, L, N, dim)
        r, gr = compute_gr_2d(dist, N, nbins=100)
        plot_gr(r, gr, N / float(L ** dim))
