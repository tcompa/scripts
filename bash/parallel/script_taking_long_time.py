#!/usr/bin/env python

import sys
import time

assert len(sys.argv) == 2
args = sys.argv[1].split(' ')
ID = '_'.join(args)

out = open('output_%s.dat' % ID, 'w')
out.write('Now starting on %s\n' % ID)
out.write('Now sleeping 10 seconds.\n')
out.flush()
time.sleep(10)
out.write('Done.\n')
