# all() and any() functions

def all2(iterable):
    for element in iterable:
        if not element:
            return False
    return True
        
def any2(iterable):
    for element in iterable:
        if element:
            return True
    return False
    
lst = [True, True, False, True]

lst2 = [False, False, False, False]

lst3 = [1,1,1]


# are all elements of lst True?
all(lst)
# are any elements of lst True?
any(lst)


all(lst2)
any(lst2)

all(lst3)
any(lst3)




