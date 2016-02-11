# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:59:27 2016

@author: Craig
"""

# Nested statements and scope
x = 25

def printer():
    x = 50
    return x
    
print x
printer()

# LEGB
# Local
# Enclosing function locals
# Global
# Built-in

# local
f = lambda x: x**2
f(20)

# enclosing function locals
name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'
    
    def hello():
        print 'Hello ' + name
    
    hello()
    
greet()

# global
print name

# built in
len




# Local Variables
x = 50

def func(x):
    print 'x is', x
    x = 2
    print 'Changed local x to',x
    
func(x)
print 'x is still',x

# The global statement
x = 50

def func():
    global x
    print 'This function is now using the global x!'
    print 'Because of global, x is: ',x
    x = 2
    print 'Ran function, changing global x to',x

print 'Before calling func(), x is: ',x
func()
print 'Value of x (outside of func()) is: ', x

