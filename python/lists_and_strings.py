'''
program: lists_and_strings.py
created: 2015-11-24 -- 14 CEST
last modified: 2015-11-24 -- 14 CEST
authors: tc qf
'''

# create and manipulate a list A
A = [1, 2, 3, 7, 3]
print 'A:', A
A.append(19)
print 'A:', A, ', after A.append(19)'
print 'A.index(7): %i' % A.index(7)
print 'A.count(3): %i' % A.count(3)
print 'A[1]:', A[1]
print 'A[-3:]:', A[-3:]
print 'sorted(A):',sorted(A)
# NOTE: reversed returns an *iterator*, not a list
print 'revesed(A):', reversed(A)
print 'reversed list:',
for i in reversed(A):
    print i,
print

# create a list B such that B[i] = str(A[i])
B = map(str, A)
print 'B:', B

# verify that the type changed
print 'type(A[0]): %s' % type(A[0])
print 'type(B[0]): %s' % type(B[0])

# create a string C by joining all elements of B, with a dot as a separator
C = '.'.join(B)
print 'C: %s' % C

# create a string D by joining all elements of B, with no separator
D = ''.join(B)
print 'D: %s' % D

# do something with the string D
print 'D[0]:', D[0]
print 'D[-1]:', D[-1]
print 'D.split(3):', D.split('3')
E = D + '-abc'
print 'E:', E
print 'E.split(\'-\')[-1]: %s' % E.split('-')[-1]
