# reduce
import math

# summing a list
lst = [47,11,42,13]
reduce(lambda x,y: x+y, lst)

# find the maximum of a sequence
reduce(lambda x,y: x if x > y else y, lst)


# multiply
reduce(lambda x,y: x * y, lst)
