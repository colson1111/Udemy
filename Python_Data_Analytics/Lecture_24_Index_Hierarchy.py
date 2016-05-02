# Lecture 24 - Index Hierarchy

import numpy as np
from pandas import Series,DataFrame
import pandas as pd

from numpy.random import randn

ser = Series(randn(6), index = [[1,1,1,2,2,2],['a','b','c','a','b','c']])
ser

ser.index # get number of index levels and labels

# outer indexing
ser[2]

# internal indexing
ser[:,'a']


# creating dataframe from multi-index level Series
dframe = ser.unstack()
dframe

# construct dataframe with multiple index levels
dframe2 = DataFrame(np.arange(16).reshape(4,4),
                    index = [['a','a','b','b'],[1,2,1,2]],
                    columns = [['NY','NY','LA','SF'],['cold','hot','hot','cold']])

dframe2

# naming indexes and columns
dframe2.index.names = ['INDEX_1', 'INDEX_2']
dframe2.columns.names = ['Cities','Temp']
dframe2

# Interchange index level orders
dframe2.swaplevel('Cities','Temp',axis = 1)

# sorting levels
dframe2.sortlevel(level = 1, axis = 0)
dframe2.sortlevel(level = 0, axis = 0)
dframe2.sortlevel(level = 1, axis = 1)
dframe2.sortlevel(level = 0, axis = 1)

# summing on a specific level
dframe2.sum(level = 'Temp', axis = 1)












