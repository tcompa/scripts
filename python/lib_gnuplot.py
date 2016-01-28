'''
module:        lib_gnuplot.py
author:        tc
created:       2015-04-15
last-modified: 2015-08-11 -- 22 CEST
notes:         allows a basic use of gnuplot in python
'''

import tempfile
import subprocess

__all__ = ['gnuplot_instance']


class gnuplot_instance:
    '''
    handles a gnuplot instance
    '''
    def __init__(self, options={}, Verbose=True):
        '''
        options:
          + 'persist' = True/False [default=True]
        '''
        # parse inputs
        try:
            persist = options['persist']
        except KeyError:
            persist = True
        # actual init
        self.Verbose = Verbose
        self.script = tempfile.NamedTemporaryFile(delete=False, suffix='.gpi')
        if self.Verbose:
            print '[gnuplot] script file: %s' % self.script.name
        shebang = '#!/usr/bin/gnuplot'
        if persist:
            shebang += ' --persist'
        self.script.write('%s\n' % shebang)
        return

    def add(self, command):
        '''
        adds one line to the gnuplot script
        '''
        self.script.write(command + '\n')
        self.script.flush()
        return

    def run(self):
        '''
        closes and runs the script
        '''
        if self.Verbose:
            print '[gnuplot] now running %s' % self.script.name
        self.script.close()
        subprocess.Popen(['chmod', '+x', self.script.name])
        subprocess.Popen([self.script.name])
        return

if __name__ == '__main__':
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
