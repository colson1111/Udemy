# Lecture 29 - Merge

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

dframe1 = DataFrame({'key':['X','Z','Y','Z','X','X'],
                     'data_set_1':np.arange(6)})
dframe1

dframe2 = DataFrame({'key':['Q','Y','Z'],
                    'data_set_2':[1,2,3]})
dframe2                    

# merge: many-to-one method - merges on overlapping columns
pd.merge(dframe1, dframe2)

pd.merge(dframe2,dframe1)

# merge on a specific column
pd.merge(dframe1,dframe2, on = 'key')

# use how= to do left/right joins
pd.merge(dframe1, dframe2, on = 'key', how = 'left')
pd.merge(dframe2, dframe1, on = 'key', how = 'left')
pd.merge(dframe1, dframe2, on = 'key', how = 'right')

# union of both tables using how = 'outer'
pd.merge(dframe1, dframe2, on = 'key', how = 'outer')


# Many-to-Many Merges
dframe3 = DataFrame({'key': ['X','X','X','Y','Z','Z'],
                     'data_set_3' : range(6)})
                    
dframe4 = DataFrame({'key': ['Y','Y','X','X','Z'],
                     'data_set_4' : range(5)})

dframe3
dframe4

pd.merge(dframe3, dframe4)

# merging on multiple columns
df_left = DataFrame({'key1' : ['SF','SF','LA'],
                     'key2' : ['one','two','one'],
                     'left_data' : [10,20,30]})
df_left

df_right = DataFrame({'key1' : ['SF','SF','LA','LA'],
                      'key2' : ['one','one','one','two'],
                      'right_data' : [40,50,60,70]})
df_right

pd.merge(df_left, df_right, on = ['key1','key2'], how = 'outer')

# pandas will add a suffix if two dataframes have columns with the same name (and they are not joined on)
pd.merge(df_left, df_right, on = 'key1')

# specify suffix
pd.merge(df_left, df_right, on = 'key1', suffixes = ('_lefty','_righty'))

# more documentation of merge parameters
url = 'http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.merge.html'









