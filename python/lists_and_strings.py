'''
program: lists_and_strings.py
created: 2015-11-24 -- 14 CEST
last modified: 2015-11-24 -- 16 CEST
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

# how to count the number of times each different element of a list occur
l = ['a','a','a','b','b','c','d','d']
n_occ = [[x, l.count(x)] for x in set(l)]
print 'inventory of elements contained in the list: %s' % n_occ

#how to remove a given element from a list
l2=l
l2.remove('c')
print 'list with the \'c\' element removed: %s' %l2

#how to remove all occurrences of a given element
l2=filter(lambda i: i!='b',l2)
print 'list without the \'b\'\'s: %s' %l2

#how to remove an element from a list when the element is identified by its index
l2.pop(-3)
print 'list with the antepenultimate element removed: %s' % l2

#how to remove a slice from the list
l3=l
del l3[3:6]
print 'list with the elements 3 to 5 removed: %s' % l3


