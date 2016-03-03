# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 22:41:43 2016

@author: Craig
"""

# map function

def fahrenheit(T):
    return ((9.0 / 5) * T + 32)
    
def celsius(T):
    return (5.0 / 9) * (T - 32)
    
temp = [0, 22.5, 40, 100]

# convert to fahrenheit
F_temps = map(fahrenheit, temp)

# convert back to celsius
C_temps = map(celsius, F_temps)

# using a lambda expression
map(lambda x: (5.0 / 9) * (x - 32), F_temps)

# using multiple lists
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

map(lambda x,y: x + y, a, b)

map(lambda x,y,z: x + y + z, a,b,c)

# fizz buzz
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 5 == 0:
        return "buzz"
    elif num % 3 == 0:
        return "fizz"
    else:
        return num
        
map(fizzbuzz,range(100))

