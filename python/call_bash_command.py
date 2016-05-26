'''
program: call_bash_command
created: 2016-05-26 -- 12 CEST
author: tc

'''

import subprocess


def call_bash_command(cmdlist, Verbose=False):
    '''
    Call a bash command and catch its returncode, stdout, and stderr.
    '''
    p = subprocess.Popen(cmdlist, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if Verbose:
        print '*' * 80
        print '[call_bash_command] start'
        print 'returncode:'
        print p.returncode
        print 'stdout:'
        print stdout
        print 'stderr:'
        print stderr
        print '[call_bash_command] end'
        print '*' * 80
    return p.returncode, stdout, stderr


if __name__ == '__main__':
    cmdlist = ['ls', 'missing_file']
    roe = call_bash_command(cmdlist, Verbose=True)
    cmdlist = ['ls', '.']
    roe = call_bash_command(cmdlist, Verbose=True)
