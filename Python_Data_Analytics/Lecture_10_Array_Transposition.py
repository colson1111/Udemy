import numpy as np

arr = np.arange(50).reshape((10,5))

arr # 10x5 array

arr.T # 5x10 array

np.dot(arr.T,arr) # dot product of two arrays

# create 3d array
arr3d = np.arange(50).reshape((5,5,2))
arr3d # 5x5x2 array

arr3d.transpose((1,0,2)) # transpose 3d matrix
arr3d

# swap axes
arr = np.array([[1,2,3]])
arr

arr.swapaxes(0,1)

