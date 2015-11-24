'''
program: decorator.py
created: 2015-11-24 -- 15 CEST
author: tc, dc
'''


def decorator(f):
    '''
    Decorator for the function f, which is a function of one parameter only.
    '''
    def decorated_f(alpha):
        if alpha > 0.0:
            return f(alpha)
        else:
            return 0.0
    return decorated_f


@decorator
def long_calculation(alpha):
    return alpha ** 2


for i in range(- 5, 5):
    print i, long_calculation(i)
