# enumerate
def enumerate1(sequence, start = 0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
        
lst = ['a', 'b', 'c']

for i, item in enumerate(lst):
    print i
    print item

for i, item in enumerate1(lst):
    print i
    print item


# useful in cases where you need to track which element you are at
for i, item in enumerate(lst):
    if i >= 2:
        break
    else:
        print item
