# _____________________________________________#
#___________Useful_Links______________________ #
# https://pbpython.com/excel-pandas-comp.html
# https://www.dataquest.io/blog/excel-and-pandas/
#           openpyxl
# https://realpython.com/openpyxl-excel-spreadsheets-python/
# _____________________________________________#

import pandas as pd
import numpy as np

path = '/Users/User/Desktop/Python/Data/Excel_Sample_Data.xlsx'
df = pd.read_excel(path)

print('\n')

# reads entire file
# data = pd.read_excel(path, nrows=20)
# print(data)

# displays overview of data columns 
x = df.dtypes
print(x)

# displays first five lines
x = df.head()
print(x)


# # ////////////////////////////////// 
# # creates a "total" category 
# # Sums all the data together 
df["total"] = df["Jan"] + df["Feb"] + df["Mar"]
x = df.head()
print(x)

sum_row = df[["Jan","Feb","Mar","total"]].sum()
print(sum_row)