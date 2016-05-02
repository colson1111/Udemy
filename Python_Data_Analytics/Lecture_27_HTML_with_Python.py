# Lecture 27 - HTML with Python

import pandas as pd
from pandas import Series,DataFrame
from pandas import read_html

url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
# install beautiful-soup and html5lib

# read table as list of dataframes
dframe_list = pd.io.html.read_html(url)

# keep first data frame in hte list
dframe = dframe_list[0]
dframe

# view columns of the dataframe
dframe.columns.values
