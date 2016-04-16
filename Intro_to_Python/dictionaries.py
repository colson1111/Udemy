# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:27:44 2016

@author: Craig
"""

# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

# Call values by their keys
my_dict['key1']

# Dictionaries are very flexible in the data types they can hold
my_dict = {'key1':123, 'key2':[12,23,33], 'key3':['item0','item1','item2']}

# Let's call items from the dictionary
my_dict['key3']

# Can call an index on that value
my_dict['key3'][0]

# Can then even call methods on that value
my_dict['key3'][0].upper()

my_dict['key1']

# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123

# Check
my_dict['key1']

# set the object equal to itself minus 123
my_dict['key1'] -= 123
my_dict['key1']

# Create keys by assignment
# Create a new dictionary
d = {}

# Create a new key
d['animal'] = 'Dog'
d['answer'] = 42
d

# NESTING WITH DICTIONARIES
# Dictionary nested inside a dictionary nested inside a dictionary
d = {'key1': {'nestkey': {'subnestkey':'value' } } }

# keep calling the keys
d['key1']['nestkey']['subnestkey']

# A FEW DICTIONARY METHODS
# Create a typical dictionary
d = {'key1':1, 'key2':2, 'key3':3}

# method to return a list of all keys
d.keys()

# method to grab all values
d.values()

# method to return tuples of all items
d.items()
