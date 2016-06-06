'''
program: use_argparse.py
author: tc
created: 2016-06-06 -- 9 CEST
'''

import argparse

P = argparse.ArgumentParser()
P.add_argument('-i', '--int', dest='int_arg', type=int, default=0,
               help='this has to be a integer', required=True)
P.add_argument('-s', '--string', dest='str_arg', type=str, default='ABC',
               help='this can be any string')
args = P.parse_args()
print 'int_arg:', args.int_arg
print 'str_arg:', args.str_arg
