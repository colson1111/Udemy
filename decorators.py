# Decorators

# Functions review
def func():
    return 1
    
func()

# Scope Review
s = 'Global Variable'

def func():
    print locals()
    
print globals()

print globals().keys()

print globals()['s']

def hello(name = 'Craig'):
    return 'Hello ' + name
    
hello()

greet = hello
greet
greet()
del hello
hello()
greet()



# Functions within Functions
def hello(name = 'Craig'):
    print 'The hello() function has been executed'
    
    def greet():
        return '\t This is inside the greet() function'
        
    def welcome():
        return '\t This is inside the welcome() function'
        
    print greet()
    print welcome()
    print "Now we are back inside the hello() function"

hello()

welcome() # not defined outside of hello function (due to scope)

# Returning Functions
def hello(name = 'Craig'):
    
    def greet():
        return '\t This is inside the greet() function'
        
    def welcome():
        return '\t This is inside the welcome() function'
        
    if name == 'Craig':
        return greet
    else:
        return welcome

x = hello()

x

print x()

# Functions as Arguments
def hello():
    return 'Hi Jose!'
    
def other(func):
    print 'Other code would go here'
    print func()
    
other(hello)



# Creating a Decorator
def new_decorator(func):
    
    def wrap_func():
        print "First piece of code"
        
        func()
        
        print "Second piece of code"
    
    return wrap_func
    
def func_needs_decorator():
    print "This function is in needs of a decorator"
    
# reassign func_needs_decorator()
func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()


# rewrite using @
@new_decorator
def func_needs_decorator():
    print "This function is in need of a decorator"
    
func_needs_decorator()


      

