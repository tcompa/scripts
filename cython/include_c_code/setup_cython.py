'''
program: setup_cython.py
author: tc
created: 2016-05-12 -- 19 CEST
notes: to be executed as
       $ python setup_cython.py build_ext --inplace
'''

from distutils.extension import Extension
from distutils.core import setup
from Cython.Distutils import build_ext


ext_modules = [Extension('wrapper', ['wrapper.pyx', 'function_cos_sum.c'])]
setup(cmdclass={'build_ext': build_ext}, ext_modules=ext_modules)
