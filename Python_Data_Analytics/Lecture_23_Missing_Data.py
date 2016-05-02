# Lecture 23 - Missing Data

import numpy as np
from pandas import Series,DataFrame
import pandas as pd

data = Series(['one', 'two', np.nan, 'four'])
data


data.isnull() # identify missing values

data.dropna() # drop all null values

dframe = DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])
dframe

clean_dframe = dframe.dropna() # returns rows without any nulls
clean_dframe

dframe.dropna(how = 'all') # drops rows with all values missing

dframe.dropna(axis = 1) # drops columns (will drop all of them)

npn = np.nan
dframe2 = DataFrame([[1,2,3,npn],[2,npn,5,6],[npn,7,npn,9],[1,npn,npn,npn]])
dframe2

# points without null
dframe2.dropna(thresh = 2) # rows with at least 2 data points

dframe2.dropna(thresh = 3) # rows with at least 3 data points

dframe2

# fill where null values exist
dframe.fillna(1) # replace null with 1

dframe2.fillna({0:0,1:1,2:2,3:3}) # replace using dictionary

dframe2.fillna(0)
dframe2

dframe2.fillna(0, inplace = True) # inplace replaces the object
dframe2




