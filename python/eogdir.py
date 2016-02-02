#!/usr/bin/python

'''
program: eogdir.py
author: tc
created: 2016-02-02 -- 16 CEST

notes: includes examples of printing on stderr and using the subprocess module
'''

from __future__ import print_function
import sys
import os
import glob
import subprocess


def print_stderr(*string):
    print(*string, file=sys.stderr)


def error(*message):
    print_stderr('')
    if message:
        print_stderr('ERROR:', *message)
        print_stderr('')
    usage = 'Correct usage:\n' +\
            '  eogdir.py [folder]   : show png files in <folder> ' +\
            '(default: current folder)\n' +\
            '  eogdir.py -h, --help : show this message'
    print_stderr(usage)
    print_stderr('')
    sys.exit()


if len(sys.argv) == 1:
    folder = os.getcwd()
elif len(sys.argv) == 2:
    if sys.argv[1] in ['-h', '--help']:
        error()
    folder = sys.argv[1]
    if not os.path.isdir(folder):
        error('missing folder %s.' % folder)
else:
    error('too many arguments.')

if not folder.endswith('/'):
    folder += '/'

png_files = glob.glob('%s*.png' % folder)
if len(png_files) == 0:
    error('no png files in %s.' % folder)
subprocess.call(['eog'] + png_files)
