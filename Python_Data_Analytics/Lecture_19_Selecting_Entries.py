# Lecture 19 - Selecting Entries

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

ser1 = Series(np.arange(3), index=['A','B','C'])
ser1

ser1 = 2*ser1 # double values to avoid confusion later on
ser1

ser1['B'] # select by index
ser1[1] # numerical value of index
ser1[0:3] # range of indices
ser1[['A','B']] # list of index value name

ser1
ser1[ser1 > 3] # entries greater than 3
ser1[ser1 > 3] = 10 # replace conditionally
ser1

# Selecting from a DataFrame
dframe = DataFrame(np.arange(25).reshape((5,5)),
                   index=['NYC','LA','SF','DC','CHI'],
                   columns=['A','B','C','D','E'])
dframe

dframe['B'] # columns name
dframe[['B','E']] # multiple columns
dframe[dframe['C'] > 8] # boolean

dframe > 10 # boolean data frame

dframe.ix['LA'] # returns the given row
dframe.ix[['LA', 'CHI']]

dframe.ix[1] # using the row index number







