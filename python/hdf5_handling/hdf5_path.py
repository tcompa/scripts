#!/usr/bin/env python

'''
program: hdf5_path.py
created: Thu Feb  2 21:59:41 CET 2017
author: tc
'''

import sys
import h5py


datafile = sys.argv[1]
path = sys.argv[2]
assert datafile.endswith('h5'), 'Error, this works with *.h5 files.'
f = h5py.File(datafile, 'r')
x = f[path]
if isinstance(x, h5py.highlevel.Group):
    print '%s is a group, with keys:' % path
    for j in x.keys():
        print '  ', j, type(j)
elif isinstance(x, h5py.highlevel.Dataset):
    print '%s is a dataset:' % path
    print x.shape
    print x[()]
else:
    print '%s is something else:' % path, type(x)
