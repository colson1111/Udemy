# Indexing Arrays

import numpy as np

# Creating a sample array
arr = np.arange(0,11)

# Show
arr

# Get a value at an index
arr[8]

# Get values in a range
arr[1:5]
arr[0:5]

# Setting a value with index range (Broadcasting)
arr[0:5] = 100
arr

# Reset array
arr = np.arange(0,11)
arr

# Slicing
slice_of_arr = arr[0:6]
slice_of_arr

# Change slice
slice_of_arr[:] = 99
slice_of_arr

# The changes also occur in the original array
arr

# For arrays, the data is not copied, it is a reference to the original array

# to get a copy, need to be explicit
arr_copy = arr.copy()
arr_copy




# Indexing a 2D array
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
arr_2d

# Indexing row
arr_2d[1]

# Format is:  arr_2d[row][col] or arr_2d[row,col]
arr_2d[1][0]

arr_2d[1,0]

# 2D array slicing
arr_2d

# shape (2,2) from top right corner
arr_2d[:2,1:]

# Shape bottom row
arr_2d[2]
arr_2d[2,:]

# Fancy Indexing

# Set up matrix
arr2d = np.zeros((10,10))

# length of array
arr_length = arr2d.shape[1]

# Set up array
for i in range(arr_length):
    arr2d[i] = i
    
arr2d

# choose rows where all values are equal to given values
arr2d[[2,4,6,8]]

# allowed in any order
arr2d[[6,4,2,7]]
