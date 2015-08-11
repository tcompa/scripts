#!/usr/bin/python

'''
program:       aps_article.py
author:        tc
last modified: 2015-08-10 -- 12:00 CEST
notes:         opens articles from APS journals (see link.aps.org)
'''

import sys
import subprocess


def get_input():
    options = '| PRL: \'l\' [default]'
    options += '| PRA: \'a\' | .. | PRX: \'x\' | RMP: \'r\''
    journal = raw_input('| Journal?\n' + options + '\n')
    if not journal:
        journal = 'l'
    volume = raw_input('| Volume? ')
    page = raw_input('| Page? ')
    if not volume or not page:
        sys.exit('ERROR: missing input. Exit.')
    return journal, volume, page


# General options
browser = 'firefox'
proxy = ''
# proxy = '.proxyname.someuniversity.fr'


# Journal names: key/long/short
list_keys = ['a', 'b', 'c', 'd', 'e', 'x', 'l', 'r']
longname = {i: 'PhysRev%s' % i.capitalize()
            for i in list_keys if i not in ['l', 'r']}
longname['r'] = 'RevModPhys'
longname['l'] = 'PhysRevLett'
shortname = {i: 'pr%s' % i for i in list_keys if not i == 'r'}
shortname['r'] = 'rmp'


# Get and check input
journal, volume, page = get_input()
if journal not in list_keys:
    sys.exit('ERROR: wrong journal key (\'%s\'). Exit.' % journal)
if not volume.isdigit():
    sys.exit('ERROR: wrong volume (\'%s\'). Exit.' % volume)
if not page.isdigit():
    sys.exit('ERROR: wrong page number (\'%s\'). Exit.' % page)
print '| Journal: %s' % longname[journal]
print '| Volume:  %s' % volume
print '| Page:    %s' % page


# Open link
link = 'http://journals.aps.org%s/' % proxy
link += '%s/abstract/10.1103/' % shortname[journal]
link += '%s.%s.%s' % (longname[journal], volume, page)
print '| Now opening %s' % link
subprocess.Popen([browser, link])


# Print doi
doi = '10.1103/%s.%s.%s' % (longname[journal], volume, page)
doi_link = 'http://dx.doi.org/' + doi
print '| doi: %s' % doi
print '| doi_link: %s' % doi_link
print
