# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:09:20 2016

@author: Craig
"""

# SETS AND BOOLEANS

# SETS
x = set()

# we add to sets with the add() method
x.add(1)

x

# sets have unique values, what happens if we add a duplicate?
x.add(2)
x

# try to add the same element
x.add(1)

# it just doesn't add anything
x

# we can cast a list as a set to get the unique values from it
l = [1,1,2,2,3,4,5,6,1,1]
set(l)


# BOOLEANS

# set object to be a boolean
a = True
a

# Use comparison to create booleans
1 > 2

# use none as a boolean placeholder if we do not yet want an object to have a value
b = None
