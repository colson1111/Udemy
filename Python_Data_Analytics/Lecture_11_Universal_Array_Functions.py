# Universal Array Functions

import numpy as np

arr = np.arange(11)

arr

# basic function applied to every value in array
np.sqrt(arr) # square root

np.exp(arr) # exponential

A = np.random.randn(10)
A

B = np.random.randn(10)
B

# Binary Functions
np.add(A,B) # add values in arrays

np.maximum(A,B) # Find the maximum b/w 2 array values

np.minimum(A,B) # find minimum of two values at each index

website = 'http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs'
import webbrowser

webbrowser.open(website)

