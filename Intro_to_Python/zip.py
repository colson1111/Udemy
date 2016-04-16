# zip

# code in the zip function
def zip2(*iterables):
    # zip ('ABCD', 'xy') -- > Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)


# try it out:
x = [1,2,3]
y = [4,5,6]

zip(x,y)  # returns a list containing 3 tuples

# what if one list is longer?
x = [1,2,3]
y = [4,5,6,7,8]

zip(x,y)  # limited by the shorter list

# three lists
x = [1,2,3]
y = [4,5,6]
z = [7,8,9]
zip(x,y,z)

# zipping together dictionaries
d1 = {'a':1, 'b':2}
d2 = {'c':4, 'd':5}
zip(d1,d2)

# use dictionary methods to mix keys and values
zip(d2, d1.itervalues())

# define a function to switch the keys and values of two dictionaries
def switcharoo(d1,d2):
    dout = {}
    
    for d1key,d2value in zip(d1,d2.itervalues()):
        dout[d1key] = d2value
    
    return dout

switcharoo(d1,d2)

switcharoo(d2,d1)


