# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 22:56:00 2016

@author: Craig
"""

# lambda expressions

# start with a def
def square(num):
    result = num**2
    return result

square(2)

# break down
def square(num):
    return num**2

square(4)

# break down more
def square(num): return num**2
    
square(4)

# lambda function
square = lambda num: num**2
square(4)


# check if a number is even
even = lambda x: x % 2 == 0
even(3)
even(4)

# grab first character of string
first = lambda s: s[0]
first('hello')

# reverse a string
rev = lambda s: s[::-1]
rev('hello')

# add numbers
adder = lambda x,y: x + y
adder(2,3)
