# errors and exceptions homework

# Problem 1:  handle the exception thrown by the code below by using
#   try and except blocks
try:
    for i in ['a','b','c']:
        print i**2
except:
    print "An error has occurred"    
    
    
# Problem 2:  Handle the exception thrown by the code below by using
#    try and except blocks.  Then use a finally block to print 'all done'

x = 5
y = 0

try:
    z = x/y
except:
    print "an error has occurred"
finally:
    print "All Done"
    


# Problem 3:  Write a function that asks for an integer and prints the square
#   of it.  Use a while loop with a try, except, else block to account for incorrect
#   inputs.

def ask():
    while True:    
        try:
            integer = int(raw_input("Input an integer:  "))
        except:
            print "An error has occurred! Please try again!"
            continue
        else:
            break
    print "Thank you, your number squared is:  %d" %(integer**2)
    
ask()