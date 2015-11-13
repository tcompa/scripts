#!/usr/bin/python

from lib_class import MyClass

c = MyClass()
c.print_all()
c.reset_N(7)
c.print_all()
print 'x^N = %f' % c.get_x_power_N()
