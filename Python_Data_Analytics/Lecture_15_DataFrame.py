# Lecture 15 - DataFrame

import numpy as np
import pandas as pd

from pandas import Series,DataFrame

import webbrowser

website = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'
webbrowser.open(website)

nfl_frame = pd.read_clipboard() # copy a table and read from clipboard
nfl_frame

nfl_frame.columns # column names

# select a column
nfl_frame.Team
nfl_frame['Team']
nfl_frame['First NFL Season']

# select multiple columns
DataFrame(nfl_frame, columns=['Team', 'First NFL Season', 'Total Games'])

# included column that doesn't exist: creates a null column
DataFrame(nfl_frame, columns=['Team', 'First NFL Season', 'Total Games', 'Stadium'])

# selecting rows
nfl_frame.head() # return first five rows
nfl_frame.head(3) # return first 3 rows
nfl_frame.tail(3) # return last 3 rows

nfl_frame.ix[3] # everything from row 3

nfl_frame['Stadium'] = "Levi's Stadium"
nfl_frame

nfl_frame['Stadium'] = np.arange(5)
nfl_frame

# add a series to a dataframe
stadiums = Series(["Levi's Stadium","AT&T Stadium"], index = [4,0])
stadiums

nfl_frame['Stadium'] = stadiums
nfl_frame

# delete a column
del nfl_frame['Stadium']
nfl_frame

# construct dataframe from a dictionary
data = {'City':['SF', 'LA', 'NYC'], 'Population':[837000,3880000,8400000]}
data

city_frame = DataFrame(data)
city_frame








