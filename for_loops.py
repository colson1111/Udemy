# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:15:39 2016

@author: Craig
"""

# We'll learn how to automate this sort of ilst in the next lecture
l = [1,2,3,4,5,6,7,8,9,10]

for num in l:
    print num
    
# Modulo
17 % 5

# 3 Remainder 10 = 1
10 % 3

# Print even numbers from the list
for num in l:
    if num % 2 == 0:
        print num
    else:
        print 'Odd Number'


# For loop to sum list
list_sum = 0

for num in l:
    list_sum += num

print list_sum

# Loop through string
for letter in 'This is a string.':
    print letter
    

# for loops and tuples
tup = (1,2,3,4,5)

for t in tup:
    print t
    
# tuple unpacking
l = [(2,4), (6,8), (10,12)]
for tup in l:
    print tup
    
# now with unpacking
for (t1,t2) in l:
    print t1
    print t2
    
# for loops with dictionaries
d = {'k1':1, 'k2':2, 'k3':3}

for item in d:
    print item
    
# only prints keys, how do we get the values or both keys and values?

# print only values
for k,v in d.iteritems():
    print v
    
# print both
for k,v in d.iteritems():
    print k
    print v

# try with .items() (Python 3 method, but still works in Python 2 only differently)
for k,v in d.items():
    print k
    print v

    