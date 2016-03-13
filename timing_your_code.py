# timeit

import timeit

# create this string:
'0-1-2-3-...-99'


# time using a for loop:  1.139
timeit.timeit('"-".join(str(num) for num in range(100))', number = 10000)

# time using list comprehension: 0.983
timeit.timeit('"-".join([str(num) for num in range(100)])', number = 10000)

# time using map function: 0.706
timeit.timeit('"-".join(map(str,range(100)))', number = 10000)


# using magic functions in iPython
%timeit "-".join(str(num) for num in range(100)) # 210 microseconds per loop
%timeit "-".join([str(num) for num in range(100)]) # 95 microseconds per loop
%timeit "-".join(map(str, range(100))) # 86.8 microseconds per loop
