# Lecture 18: Drop Entry

import numpy as np
from pandas import Series,DataFrame
import pandas as pd

ser1 = Series(np.arange(3),index=['a','b','c'])
ser1

ser1.drop('b')

# data frame
dframe1 = DataFrame(np.arange(9).reshape(3,3),
                    index = ['SF','LA','NY'],
                    columns =['pop','size','year'])
dframe1

# drop a row
dframe1.drop('LA')

# drop a column
dframe1.drop('year', axis = 1) # axis = 0 is rows (default)




