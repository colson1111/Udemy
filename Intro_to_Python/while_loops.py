# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:11:33 2016

@author: Craig
"""

# WHILE LOOPS
x = 0

while x < 10:
    print 'x is currently: ', x
    print ' x is still less than 10, adding 1 to x'
    x += 1

# using an else statement
x = 0
while x < 10:
    print 'x is currently: ',x
    print ' x is still less than 10, adding 1 to x'
    x += 1
else:
    print 'All Done!'
    
    
# break, continue, pass
x = 0

while x < 10:
    print 'x is currently: ',x
    print ' x is still less than 10, adding 1 to x'
    x += 1
    
    if x == 3:
        print 'x == 3'
    else:
        print 'continuing...'
        continue
else:
    print 'All Done!'


# break
x = 0

while x < 10:
    print 'x is currently: ',x
    print ' x is still less than 10, adding 1 to x'
    x += 1
    if x == 3:
        print 'Breaking because x == 3'
        break
    else:
        print 'continuing...'
        continue
else:
    print 'All Done!'
