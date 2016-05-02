# Lecture 28 - Excel with Python

import pandas as pd

# install xlrd, openpyxl

xlsfile = pd.ExcelFile('C:\\Users\\Craig\\Documents\\GitHub\\Udemy\\Python_Data_Analytics\\lec28_excelfile.xlsx')

# specify sheet to import
dframe = xlsfile.parse('Sheet1')

dframe
