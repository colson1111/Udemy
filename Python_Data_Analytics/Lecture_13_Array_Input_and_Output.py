# Lecture 13 - Array Input and Output

import numpy as np

arr = np.arange(5)
arr

# save np array
np.save('myarray',arr)

# create new array with same name
arr = np.arange(10)
arr

# load original np array
np.load('myarray.npy')


# saving multiple arrays
arr1 = np.load('myarray.npy')
arr1

arr2 = arr

# save two arrays in a zip file
np.savez('ziparray.npz',x=arr1,y=arr2)

archive_array = np.load('ziparray.npz')
archive_array['x']

archive_array['y']

# save and load text files
arr = np.array([[1,2,3],[4,5,6]])
arr

np.savetxt('mytextarray.txt',arr,delimiter=',')

arr = np.loadtxt('mytextarray.txt',delimiter=',')
arr









