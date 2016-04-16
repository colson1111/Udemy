# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 21:41:19 2016

@author: Craig
"""

l = [0,1,2,3,4,5]
l2 = [6,7,8,9,10]

# append new item to end of the list
l.append(3)

# count occurrences of a value in the list
l.count(3)

# append elements from iterable
l.extend(l2)

# returns the lowest index of the value from the list
l.index(3)

# insert object before the index (l.insert(index, object))
l.insert(0,-1)

# remove and return item at index
l.pop()
three = l.pop(7)

# remove first occurrence of a value
l.remove(-1)

# reverse list
l.reverse()

# sort the list
l.sort

