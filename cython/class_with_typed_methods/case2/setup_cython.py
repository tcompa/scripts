'''
program:       setup_cython.py
author:        tc
last-modified: 2015-04-16
notes:         to be executes through
               $ python setup_cython.py build_ext --inplace
'''

from distutils.extension import Extension
from Cython.Distutils import build_ext
from distutils.core import setup

if __name__ == '__main__':
    basename = 'lib_class_1'
    ext_modules = [Extension(basename, [basename + '.pyx'],
                             libraries=['gsl', 'gslcblas'])]
    # compiler directive which allows you to use pydoc
    for  e  in  ext_modules:
        e.pyrex_directives  =  {'embedsignature': True}
    # compiling
    setup(cmdclass={'build_ext': build_ext},
          ext_modules = ext_modules)

    basename = 'lib_class_2'
    ext_modules = [Extension(basename, [basename + '.pyx'],
                             libraries=['gsl', 'gslcblas'])]
    # compiler directive which allows you to use pydoc
    for  e  in  ext_modules:
        e.pyrex_directives  =  {'embedsignature': True}
    # compiling
    setup(cmdclass={'build_ext': build_ext},
          ext_modules = ext_modules)

