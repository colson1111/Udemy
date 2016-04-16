# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:18:39 2016

@author: Craig
"""

# Errors and Exception Handling

try:
    f = open('testfile', 'w')
    f.write("test write this")
except IOError:
    # this will only check for an IOerror
    print "Error:  could not find file or read data"
else:
    print "content written successfully"
    f.close()
    
# what if we tried to write a read-onl file?
try:
    f = open('testfile', 'r')
    f.write('Test write this')
except IOError:
    print "Error: could not find file or read data"
else:
    print "Content written successfully"
    f.close()


# same thing without specifying the type of exception
try:
    f = open('testfile', 'r')
    f.write('test write this')
except:
    print "error:  could not find file or read data"
else:
    print "content written successfully"
    f.close()


# Finally:  always run code even if there is an exception
try:
    f = open("testfile", "w")
    f.write("Test write statement")
finally:
    print "Always execute finally code blocks"


# using finally with an except block
def askint():
    try:
        val = int(raw_input("Please enter an integer: "))
    except:
        print "Looks like you did not enter an integer!"
    finally:
        print "Finally, it executed!"
    print val
 
askint()
   
# getting a new entry in the except block
def askint():
    try:
        val = int(raw_input("Please enter an integer:  "))
    except:
        print "Looks like you did not enter an integer!"
        val = int(raw_input("Try again, please enter an integer:  "))
    finally:
        print "Finally, I executed!"
    print val

askint()


# using a while loop to do more checks
def askint():
    while True:
        try:
            val = int(raw_input("Please enter an integer:  "))
        except:
            print "Looks like you did not enter an integer!"
            continue
        else:
            print "Yep, that's an integer!"
            break
        finally:
            print "Finally, I executed!"
        print val
        
askint()    