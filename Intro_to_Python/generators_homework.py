# Iterators and Generators homework


# problem 1

def gensquares(N):
    for x in range(N):
        yield x*x

for x in gensquares(10):
    print x
    
# problem 2
import random

random.randint(1,10)

def rand_num(low, high, n):
    for number in range(n):
        yield random.randint(low, high)

for num in rand_num(1,10,12):
    print num


# problem 3
s = 'hello'

s_iter = iter(s)
next(s_iter)



# EC

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print item
    
# same thing as a list comprehension:
listcomp = [item for item in my_list if item > 3]
print listcomp

