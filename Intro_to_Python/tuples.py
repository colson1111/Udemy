# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:52:55 2016

@author: Craig
"""

# tuples

# CONSTRUCTING A TUPLE

# create tuple using ()'s
t = (1,2,3)

# check length just like a list
len(t)

# can also mix object types
t = ('one', 2)

# show
t

# use indexing just like we did for lists
t[0]

# Slicing just like a list
t[-1]


# BASIC TUPLE METHODS
# use .index to enter a value and return the index
t.index('one')

# use .count to count the number of times a value appears
t = (0, 0, 0, 1, 1, 2)
t.count(0)


# IMMUTABILITY
t[0] = 'change'

t.append('nope')


# Tuples are used instead of lists when immutability is necessary.
# For example, days of the week or calendar dates

