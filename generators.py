# Generators

# generator function for the cube of numbers
def gencubes(n):
    for num in range(n):
        yield num**3
  
for x in gencubes(10):
    print x
    

# generates fibonacci numbers
def genfibon(n):
    a = 1
    b = 1
    
    for i in range(n):
        yield a
        a,b = b, a + b
        
for num in genfibon(10):
    print num
    
# generates factorial numbers
def gen_fact(n):
    b = 1

    for i in range(n):
        if i == 0:
            b = 1
        else:
            b = b * i
            
        yield b
        
for num in gen_fact(10):
    print num
    
    
    
# next() and iter() functions
def simple_gen():
    for x in range(3):
        yield x
        
# assign simple_gen
g = simple_gen()
        
print next(g)
print next(g)
print next(g)
print next(g)  # error, no more values


# iter
s = 'hello'

# strings are iterable, but they are not iterators
for let in s:
    print let

# string object supports iteration, but we cannot directly iterate over it as
# we could with a generator function.  The iter() function allows us to do that.

s_iter = iter(s)

next(s_iter)

