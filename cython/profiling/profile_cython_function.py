#!/usr/bin/env python

# program: profile_cython_function.py
# author: tc
# created: 2016-05-12 -- 19 CEST
# notes: heavily inspired by the example in
#        http://nbviewer.jupyter.org/gist/tillahoffmann/296501acea231cbdf5e7


import line_profiler
from my_function import sum_cython


arguments = [1000, 1000]

profile = line_profiler.LineProfiler(sum_cython)
profile.runcall(sum_cython, *arguments)
profile.print_stats()
