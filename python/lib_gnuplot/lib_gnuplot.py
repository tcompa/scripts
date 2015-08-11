'''
module:        lib_gnuplot.py
author:        tc
created:       2015-04-15
last-modified: 2045-08-11 -- 22 CEST
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
