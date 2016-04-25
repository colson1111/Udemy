# Lecture 20 - Data Alignment

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

ser1 = Series([0,1,2],index=['A','B','C'])
ser1

ser2 = Series([3,4,5,6], index = ['A','B','C','D'])
ser2

# adding series
ser1 + ser2

dframe1 = DataFrame(np.arange(4).reshape((2,2)),
                    columns = list('AB'),
                    index = ['NYC','LA'])
dframe1


dframe2 = DataFrame(np.arange(9).reshape((3,3)),
                    columns = list('ADC'),
                    index = ['NYC','SF','LA'])
dframe2

# adding dataframes
dframe1 + dframe2 # only adds where both row and column match, everything else will be null

dframe1
dframe1.add(dframe2, fill_value = 0) # doesn't add if row/column combination doesn't exist in either table


# operations between Series and DataFrame
ser3 = dframe2.ix[0]
ser3

dframe2 - ser3


















