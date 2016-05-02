# Lecture 22 - Summary Statistics

import numpy as np
from pandas import Series,DataFrame
import pandas as pd

arr = np.array([[1,2,np.nan],[np.nan,3,4]])

dframe1 = DataFrame(arr, index = ['A','B'], columns = ['One', 'Two', 'Three'])
dframe1

# Sum method
dframe1.sum() # ignores null values (treats them as 0s)
dframe1.sum(axis = 1) # sum across rows

# Min method
dframe1.min() # finds the minimum value in each column
dframe1.min(axis = 1) # minimum value of each row

dframe1.idxmin() # Find the index of minimum value column

# Max method
dframe1.max()
dframe1.idxmax()

# Cumulative sum
dframe1.cumsum() # accumulates along each columns values

# Describe method
dframe1.describe() # summary statistics of dataframe (by columns)

# correlation and covariance
import pandas.io.data as pdweb
# import pandas_datareader.data as pdweb
import datetime

prices = pdweb.get_data_yahoo(['CVX','XOM','BP'], start = datetime.datetime(2010,1,1),
                              end = datetime.datetime(2013,1,1))['Adj Close']
prices.head()

volume = pdweb.get_data_yahoo(['CVX','XOM','BP'], start = datetime.datetime(2010,1,1),
                              end = datetime.datetime(2013,1,1))['Volume']
volume.head()

rets = prices.pct_change()

# Correction of the stocks
rcorr = rets.corr

prices.plot()
volume.plot()

import seaborn as sns
import matplotlib.pyplot as plt

# seaborn correlation plot between pct change in stock price
sns.corrplot(rets, annot=False, diag_names=False)

prices.cov # covariance method

# unique values of a series
ser1 = Series(['w', 'w', 'x', 'y', 'z', 'w', 'x', 'y', 'x', 'a'])
ser1.unique()

ser1.value_counts()


















