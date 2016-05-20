import warnings

def get_seven():
    warnings.warn('get_seven is deprecated use the integer 7 instead.')
    return 7

seven = get_seven()
print 'seven =', seven
