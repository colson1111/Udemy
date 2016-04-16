# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:44:43 2016

@author: Craig
"""

# PRINT FORMATTING

# STRINGS
print 'This is a string'

s = 'STRING'
print 'Place another string with a mod and s: %s' %(s)


# FLOATING POINT NUMBERS
print 'FLoating point numbers: %1.2f' %(13.144)

print 'Floating point numbers: %1.0f' %(13.144)

print 'Floating point numbers: %1.5f' %(13.144)

print 'Floating point numbers: %10.2f' %(13.144)

print 'Floating point numbers: %25.2f' %(13.144)

# CONVERSION FORMAT METHODS

print 'Here is a number: %s. Here is a string: %s' %(123.1, 'hi')

print 'Here is a number: %r. Here is a string: %r' %(123.1, 'hi')

# MULTIPLE FORMATTING
print 'First: %s, Second: %1.2f, Third: %r' %('hi!', 3.14, 22)

# USING THE STRING .format() METHOD
print 'This is a string with an {p}'.format(p = 'insert')

# multiple times:
print 'One: {p}, Two: {p}, Three: {p}'.format(p = 'Hi!')

# several objects
print 'Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a=1, b='two', c=12.3)

