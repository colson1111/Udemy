# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:31:14 2016

@author: Craig
"""

# IF, ELIF, ELSE STATEMENTS

if True:
    print 'It was true!'

# add some logic
x = False

if x:
    print 'x was true!'
else:
    print 'I will be printed in any case where x is not true'

# MULTIPLE BRANCHES
loc = 'Bank'

if loc == 'Auto Shop':
    print 'Welcome to the Auto Shop!'
elif loc == 'Bank':
    print 'Welcome to the Bank!'
else:
    print 'Where are you?'


person = 'Sammy'

if person == 'Sammy':
    print 'Welcome Sammy!'
else:
    print "Welcome, what's your name?"


person = 'George'

if person == 'Sammy':
    print 'Welcome Sammy!'
elif person == 'George':
    print 'Welcome George!'
else:
    print "Welcome, what's your name?"
