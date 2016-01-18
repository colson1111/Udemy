# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:19:36 2016

@author: Craig
"""

# Assign a list to a variable named my_list
my_list = [1,2,3]

# A list can hold different object types
my_list = ['A string', 23, 100.232, 'o']

len(my_list)

# INDEXING AND SLICING
my_list = ['one', 'two', 'three', 4, 5]

# grab element at index 0
my_list[0]

# grab index 1 and everything past it
my_list[1:]

# grab everything up to index 3
my_list[:3]

# we can use + to concatenate lists
my_list + ['new item']

# this doesn't change the actual list.
# reassign:
my_list = my_list + ['add new item permanently']
my_list

# we can use * for duplication
my_list * 2


# BASIC LIST METHODS
# create new list
l = [1,2,3]

# Append
l.append('append me!')
l

# Pop: used to 'pop off' an item from the list
l.pop()

# show
l

# Assign the popped element, remember default popped index is -1
popped_item = l.pop()

popped_item

# show the remaining list
l

# list indexing will return an error if there is no element at that index
l[100]

# using sort and reverse methods
new_list = ['a', 'e', 'x', 'b', 'c']

new_list

# use reverse to reverse the order (permanently)
new_list.reverse()
new_list

# use sort to sort the list: alphabetical or ascending
new_list.sort()
new_list


# NESTING LISTS
# Let's make three lists
lst_1 = [1,2,3]
lst_2 = [4,5,6]
lst_3 = [7,8,9]

# make a list of lists to form a matrix
matrix = [lst_1, lst_2, lst_3]
matrix

# Now we use two levels of indexing
# first item in matrix object
matrix[0]

# first item of the first item of matrix object
matrix[0][0]


# LIST COMPREHENSIONS
# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]
first_col

second_col = [r[1] for r in matrix]
second_col




