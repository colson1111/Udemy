# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 17:52:30 2016

@author: Craig
"""

# CREATING A STRING
# Single word
'hello'

# Entire phrase
'This is also a string'

# We can also use double quotes
"String built with double quotes"

# Be careful with quotes:
# ' I'm using single quotes, but will create an error'

"Now I'm ready to use the single quotes insude a string!"


# PRINTING A STRING
print 'Hello World 1'
print 'Hello World 2'
print 'Use \n to print a new line'
print '\n'
print 'See what I mean?'

# Note:  Python 3 uses print('Hello World')...print is a function.
# To get this functionality in Python 2.7, use:
# from __future__ import print_function



# STRING BASICS
len('Hello World')

# STRING INDEXING
# Assign s as a string
s = 'Hello World'

# Check
s

# Show first element
s[0]
s[1]
s[2]

#  Grab everything past the first term all th way to the length of s which is len(s)
s[1:]

# Note that there is no change to the original s
s

# Grab everything up to the 3rc index
s[:3]

# Everything
s[:]

# Negative indexing
# Last letter (one index behind 0 so it loops back around)
s[-1]

# Grab everything but the last letter
s[:-1]

# Grab everything, but go in steps of size 1
s[::1]

# Grab everything, but go in step sizes of 2
s[::2]

# Use this to print a string backwards
s[::-1]

# STRING PROPERTIES
# Strings have immutability:  once created, the elements cannot be changed
s

# Causes an error:  s[0] = 'x'

# Concatenate strings
s + 'concatenate me!'

# reassign s completely
s = s + ' concatenate me!'

print s

# Use multiplication to create repetition
letter = 'z'
letter*10

# BASIC BUILT IN STRING METHODS

# upper case a string
s.upper()

#lower case
s.lower()

# split by blank spaces (default for split method)
s.split()

# split by a specific element (doesn't include the elemaent that was split on)
s.split('W')

# PRINT FORMATTING
'Insert another string with curly brackets: {}'.format('The inserted string')

# this is a random change for git testing
