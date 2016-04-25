# Lecture 16 - Index Objects

import numpy as np
from pandas import Series, DataFrame
import pandas as pd

my_ser = Series([1,2,3,4], index = ['A','B','C','D'])
my_ser

# call index to get all indexes in series
my_index = my_ser.index
my_index

# specify individual or range of indices
my_index[2]
my_index[2:]

my_index[0]

# can't change an index: indexes are immutable
my_index[0] = 'Z'
