#!/usr/bin/env python

'''
program: hdf5_tree.py
created: Thu Feb  2 21:59:41 CET 2017
author: tc
'''

import sys
import h5py


def print_tabbed_name(name):
    level = name.count('/')
    print(level * '.   ' + name.split('/')[-1])


datafile = sys.argv[1]
assert datafile.endswith('h5'), 'Error, this works with *.h5 files.'
with h5py.File(datafile, 'r') as f:
    print f.visit(print_tabbed_name)
