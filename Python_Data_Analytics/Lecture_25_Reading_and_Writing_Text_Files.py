# Lecture 25 - Reading and Writing Text Files

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# read a csv
dframe = pd.read_csv('C:\\Users\\Craig\\Documents\\GitHub\\Udemy\\Python_Data_Analytics\\lec25.csv')

# specify that header row is not included
dframe = pd.read_csv('C:\\Users\\Craig\\Documents\\GitHub\\Udemy\\Python_Data_Analytics\\lec25.csv',
                     header = None)

dframe

# using read_table - need to specify delimiter
dframe = pd.read_table('C:\\Users\\Craig\\Documents\\GitHub\\Udemy\\Python_Data_Analytics\\lec25.csv',
                       sep = ',',
                       header = None)
dframe

# indicate number of rows to be read
pd.read_csv('C:\\Users\\Craig\\Documents\\GitHub\\Udemy\\Python_Data_Analytics\\lec25.csv',
                     header = None,
                     nrows = 2)

# export file
dframe.to_csv('C:\\Users\\Craig\\Documents\\GitHub\\Udemy\\Python_Data_Analytics\\lec25_data_out.csv')

import sys # use to see output without saving

dframe.to_csv(sys.stdout, sep = '_')

dframe.to_csv(sys.stdout, sep = '?')


# writing a subset of columns
dframe.to_csv(sys.stdout, columns=[0,1,2])



