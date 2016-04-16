# Creating Numpy Arrays

import numpy as np

# converting from a list
my_list1 = [1,2,3,4]
my_array1 = np.array(my_list1)
my_array1

# Make another list
my_list2 = [11,22,33,44]

# Make a list of lists
my_lists = [my_list1, my_list2]

# Make multi-dimensional array
my_array2 = np.array(my_lists)

# Show array
my_array2

# Get the size of the array
my_array2.shape # 2 rows, 4 columns

# Find the data type of the array
my_array2.dtype

# Making special case arrays

np.zeros(5) # zero array, 1x5

np.ones((5,5)) # ones array, 5x5

np.empty(5) # empty array, 1x5

np.empty((3,4)) # empty array, 3x4

np.eye(5) # Identity matrix array, 5x5

# Using a range
np.arange(5)

