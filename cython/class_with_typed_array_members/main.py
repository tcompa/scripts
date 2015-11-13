#!/usr/bin/python

from lib_class import MyClass

c = MyClass(Nval=5)
c.print_all()

c.reset_N(7)
c.print_all()

c.array[3] = 55.0
c.print_all()
print 'c.sum_array() = %f' % c.sum_array()
print 'sum(c.array)  = %f' % sum(c.array)
