# filter

        
lst = range(20)

# using def: even numbers
def even_check(num):
    if num % 2 == 0:
        return True
    else:
        return False

filter(even_check, lst)


# using lambda expression: odd numbers
filter(lambda x: x % 2 <> 0, lst)
