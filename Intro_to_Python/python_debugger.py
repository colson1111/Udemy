# python debugger


import pdb


x = [1,2,3]
y = 2
z = 3

result = y + z
print result

# set a trace using python debugger
pdb.set_trace()

result2 = y + x
print result2


