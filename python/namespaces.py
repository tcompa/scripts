'''
Example of the LEGB rule (Local/Enclosed/Global/Built-in) for
namespaces and scope resolution.

References:
http://stackoverflow.com/questions/291978/short-description-of-python-scoping-rules
https://docs.python.org/2/tutorial/classes.html#python-scopes-and-namespaces
'''


def inner_function(a):
    '''
    This function is called from within outer_function(), but it is
    defined at the main level. Therefore it only shares the module
    namespace, and not the one of outer_function().
    '''
    print '[inner_function]'
    print 'Local namespace:', dir()
    print 'a=%i, id(a)=%i' % (a, id(a))
    print 'b=%i, id(b)=%i' % (b, id(b))
    print 'c=%i, id(c)=%i' % (c, id(c))
    print


def outer_function(a, b):
    print '[outer_function]'
    print 'Local namespace:', dir()
    print 'a=%i, id(a)=%i' % (a, id(a))
    print 'b=%i, id(b)=%i' % (b, id(b))
    print 'c=%i, id(c)=%i' % (c, id(c))
    print

    def real_inner_function(a):
        '''
        This function is called from within outer_function(), and it
        is also defined from there. Therefore, it also shares the
        module namespace.
        '''
        print '[real_inner_function]'
        print 'Local namespace:', dir()
        print 'a=%i, id(a)=%i' % (a, id(a))
        print 'b=%i, id(b)=%i' % (b, id(b))
        print 'c=%i, id(c)=%i' % (c, id(c))
        print

    inner_function(2)
    real_inner_function(2)


a = 0
b = 0
c = 0
print '[module level]'
print 'Local namespace:', dir()
print 'a=%i, id(a)=%i' % (a, id(a))
print 'b=%i, id(b)=%i' % (b, id(b))
print 'c=%i, id(c)=%i' % (c, id(c))
print

outer_function(1, 1)
