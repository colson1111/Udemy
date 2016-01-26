# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 22:41:51 2016

@author: Craig
"""

# LIST COMPREHENSIONS

# Grab every letter in string
lst = [x for x in 'word']
lst

# square numbers in range and turn into list
lst = [x**2 for x in range(11)]
lst

# add in an if statement
# check for even numbers in range
lst = [x**2 for x in range(11) if x % 2 == 0]
lst

lst2 = [x**2 for x in range(0,11,2)]
lst == lst2

# convert celsius to fahrenheit
celsius = [0, 10, 20.1, 34.5]

fahrenheit = [((float(9)/5) * temp + 32) for temp in celsius]
fahrenheit

# nested list comprehensions
lst = [x**2 for x in [x**2 for x in range(11)]]
lst
