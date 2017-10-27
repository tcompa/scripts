'''
program:       setup_cython.py
author:        tc
last-modified: Thu Aug 11 09:07:37 CEST 2016
description:   compiles a cython module
notes:         to be executed through
               $ python setup_cython.py build_ext --inplace
'''

import glob
import os
from distutils.extension import Extension
from distutils.core import setup
from Cython.Distutils import build_ext
from Cython.Compiler import Options


# Set general options
libraries = []
define_macros = []

# Loop over all pyx files
for lib in glob.glob('*.pyx'):
    basename = lib[:-4]
    ext_modules = [Extension(basename, [basename + '.pyx'],
                             libraries=libraries,
                             define_macros=define_macros)]
    setup(cmdclass={'build_ext': build_ext}, ext_modules=ext_modules)
