'''
program:       setup_cython.py
author:        tc
last-modified: Thu Aug 11 09:07:37 CEST 2016
description:   compiles a cython module (including the directives for
               line profiling)
notes:         to be executed through
               $ python setup_cython.py build_ext --inplace
'''

import glob
import os
from distutils.extension import Extension
from distutils.core import setup
from Cython.Distutils import build_ext
from Cython.Compiler.Options import directive_defaults

# Set some general options.
Profiling = False
GSLLibraries = False
Doc = False

# Do not modify anything below this line

# Set general options
define_macros = []
if Profiling:
    directive_defaults['linetrace'] = True
    directive_defaults['binding'] = True
    directive_defaults['profile'] = True
    define_macros = [('CYTHON_TRACE', '1')]
libraries = []
if GSLLibraries:
    libraries = ['gsl', 'gslcblas']
# Loop over all pyx files
for lib in glob.glob('*.pyx'):
    print '[compiling %s] start' % lib
    basename = lib[:-4]
    ext_modules = [Extension(basename, [basename + '.pyx'],
                             libraries=libraries,
                             define_macros=define_macros)]
    if Doc:
        for e in ext_modules:
            e.pyrex_directives = {'embedsignature': True}
    # Actual compiling
    setup(cmdclass={'build_ext': build_ext}, ext_modules=ext_modules)
    # Change permissions of the so file
    os.system('chmod -x %s.so' % basename)
    print '[compiling %s] end' % lib
