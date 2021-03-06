# collatz conjecture
# Start with a number n > 1. Find the number of steps it takes to reach one 
# using the following process: If n is even, divide it by 2. If n is odd, 
# multiply it by 3 and add 1.

def collatz(num):
    
    steps = 0
    
    if num <= 0:
        return steps
    
    while num <> 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3) + 1
        steps += 1
    
    return steps
    
collatz(123)

import numpy as np
import matplotlib.pyplot as plt

dictionary = dict()

for i in range(1,1000000):
    dictionary[i] = collatz(i)

keys = np.array(dictionary.items())

inputs = keys[:,0]
outputs = keys[:,1]
plt.scatter(inputs,outputs)
plt.hist(outputs, 500)







    
# Sieve of Eratosthenes:  Find all prime numbers in range

def prime_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i * i, limit, i):
                a[n] = False


    
        