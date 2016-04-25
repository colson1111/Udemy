# lecture 14 - pandas Series

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = Series([3,6,9,12])
obj

obj.values # show series values

obj.index # show index values

ww2_cas = Series([8700000, 4300000, 3000000, 2100000, 400000], index = ['USSR','Germany','China','Japan','USA'])
ww2_cas

ww2_cas['USA']

# Check which countries had casualties greater than 4000000
ww2_cas[ww2_cas > 4000000]

# check if an index value exists in the series
'USSR' in ww2_cas

# convert Series into a dictionary
ww2_dict = ww2_cas.to_dict()
ww2_dict

# convert back into Series - feed into the Series() function
ww2_series = Series(ww2_dict)
ww2_series

# create new index
countries = ['China', 'Germany', 'USSR', 'Japan', 'USA', 'Argentina']
obj2 = Series(ww2_dict, index=countries)
obj2

# find null value in the series
pd.isnull(obj2)

# find non-null values
pd.notnull(obj2)

# add series to series, align data by index
obj2
ww2_series

ww2_series + obj2 # adds across the indexes

obj2.name = "World War 2 Casualties"
obj2

obj2.index.name = "Countries"
obj2



















