# Format specification mini-language:
#     https://docs.python.org/3/library/string.html#formatspec

# join strings together
a = ['word 1', 'word 2', 'word 3']
print ' SEPARATOR '.join(a)
print

# print formatted output
b = 0.2345243
print '%.3f' % b
print '{:.3f}'.format(b)
print
print '|', '{:<15.3f}'.format(b), '|'
print '|', '{:^15.3f}'.format(b), '|'
print '|', '{:>15.3f}'.format(b), '|'
print
print '|', '{:<015.3f}'.format(b), '|'
print '|', '{:^015.3f}'.format(b), '|'
print '|', '{:>015.3f}'.format(b), '|'
print

# print list with formatted item
c = [1, 5, 8, -1, -2]
print '|'.join('{}'.format(i) for i in c)
print ', '.join('{:.2f}'.format(i) for i in c)
print
