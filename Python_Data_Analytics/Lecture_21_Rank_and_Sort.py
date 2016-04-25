# Lecture 21 - Rank and Sort

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ser1 = Series(range(3), index = ['C','A','B'])
ser1

# use sort index to sort by index
ser1.sort_index()

# use order to sort by values
ser1.order()

from numpy.random import randn
ser2 = Series(randn(10))
ser2

# ranking
ser2.sort_values()

ser2.rank()

ser2.sort_values(ascending = False)

ser3 = Series(randn(10))
ser3

ser3.rank()
ser3 = ser3.sort_values()
ser3.rank()

