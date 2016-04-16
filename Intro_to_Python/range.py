# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 22:07:02 2016

@author: Craig
"""

# Range function

range(0, 10)

x = range(0,10)
type(x)

start = 0
stop = 20
x = range(start, stop)
x

# specify step size as an argument
start = 5
x = range(start, stop, 2)
x

# for super large ranges, we use xrange() in python 2.
# in python 3, we can just use range().  These functions
# create generators that provide the list of numbers
# for that instance, but do not store them in memory

for num in range(10):
    print num

for num in xrange(10):
    print num
    
# in python 2, if you do not need to save the results in a list,
# use xrange instead of range.

xrange(0,6,2)

x = xrange(1,6)
x2 = range(1,6)
type(x)

# can cast an xrange object into a list
list(x) == x2
