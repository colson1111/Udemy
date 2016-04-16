# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 23:31:47 2016

@author: Craig
"""

# functions

# Example 1:  a simple print 'hello' function
def say_hello():
    print 'hello'
    
say_hello()

# Example 2:  a simple greeting function
def greeting(name):
    print 'Hello %s' %name

greeting('Craig')

# Example 3:  addition function
def add_num(num1,num2):
    return num1 + num2

add_num(4,5)

result = add_num(4,5)
print result

print add_num('one','two')

# example 4:  check if a number is prime
import math

def is_prime(num):
    '''
    check to see if number is prime
    '''
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

is_prime(16)
is_prime(31)



