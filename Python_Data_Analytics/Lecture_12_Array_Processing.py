# Lecture 12 - Array Processing

import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline (for jupyter notebook)

# create axis
points = np.arange(-5,5,0.01)

# create grid 
dx,dy = np.meshgrid(points,points)
dx
dy 

# evaluating function
z = (np.sin(dx) + np.sin(dy))
z

# plot z
plt.imshow(z) # sin along both x and y axes
plt.colorbar()
plt.title("Plot for sin(x) + sin(y)")

# numpy where: 
A = np.array([1,2,3,4])
B = np.array([100,200,300,400])

condition = np.array([True,True,False,False])

# using list comprehension to combine arrays conditionally
# choose A value when condition is true, choose B value otherwise
answer = [(A_val if cond else B_val) for A_val,B_val,cond in zip(A,B,condition)]
answer

# numpy where is short form of previous list comprehension
answer2 = np.where(condition,A,B)
answer2

# more np.where
from numpy.random import randn

arr = randn(5,5)
arr

# when array value is less than 0, make it a 0
np.where(arr<0,0,arr) # useful for cleaning up data

# more array processing
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr

# Basic Stats
arr.sum() # sum of all values in matrix
arr.sum(1) # sum along rows
arr.sum(0) # sum along columns
arr.mean() # average of matrix
arr.std() # standard deviation
arr.var() # variance

# Boolean
bool_arr = np.array([True,False,True])
bool_arr.any() # return True if any values are true
bool_arr.all() # return True if all values are true

# Sorting
arr = randn(5)
arr

arr.sort() # sort smallest to largest
arr

# Unique Values
countries = np.array(['France', 'Germany', 'USA', 'Russia', 'USA', 'Mexico', 'Germany'])
countries

np.unique(countries)

# Check if values exist in given array (countries)
np.in1d(['France', 'USA', 'Sweden'],countries)





