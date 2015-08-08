#!/usr/bin/python

'''
program:       aps_article.py
author:        tc
last modified: 2015-08-08 -- 17:30 CEST
notes:         opens articles from APS journals (see link.aps.org)
'''

import os


browser = 'firefox'
proxy = ''
# proxy = '.proxyname.someuniversity.fr'

print
print '*' * 80
print 'Open article link from APS journals (PRL, PR{A,B,C,D,E,X}, RMP)'
print

list_pr = ['a', 'b', 'c', 'd', 'e', 'x', 'l']
longnames = {i: 'PhysRev%s' % i.capitalize() for i in list_pr}
longnames['rmp'] = 'RevModPhys'
shortnames = {i: 'pr%s' % i for i in list_pr}
shortnames['rmp'] = 'rmp'

# input
OpenHome = False
journal = raw_input('Journal? [default: PRL, others: a, b, c, d, e, x, rmp] ')
if not journal:
    journal = 'l'
volume = raw_input('Volume? ')
page = raw_input('Page? ')
if not volume or not page or journal not in list_pr + ['rmp']:
    print 'Something went wrong, open '
    OpenHome = True

print 'Journal: %s' % longnames[journal]

# check volume
if volume.isdigit():
    print 'Volume:  %s' % volume
else:
    print 'Wrong volume number -> journal homepage'
    OpenHome = True

# check page
if page.isdigit():
    print 'Page:    %s' % page
else:
    print 'Wrong page number -> journal homepage'
    OpenHome = True

if OpenHome:
    link = 'http://%s.aps.org%s' % (shortnames[journal], proxy)
else:
    link = 'http://journals.aps.org%s/' % proxy
    link += '%s/abstract/10.1103/' % shortnames[journal]
    link += '%s.%s.%s' % (longnames[journal], volume, page)

print
print 'Trying to open %s' % link
print '**********************************************************************'
print

os.system('%s %s &' % (browser, link))
