#!/usr/bin/python

'''
module:        example.py
author:        tc
created:       2015-08-11
notes:         example of how to use lib_gnuplot
'''

from lib_gnuplot import gnuplot_instance

p = gnuplot_instance()
p.add('set xlabel \'x\'')
p.add('set ylabel \'y\'')
p.add('set samples 1000')
p.add('set xrange [0:pi]')
p.add('plot \\')
for i in range(1, 3):
    p.add(' cos(%.2f * x),\\' % float(i)) 
p.add(' cos(%.2f * x)' % 3.0) 
p.run()
