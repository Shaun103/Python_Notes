import pandas as pd
import os, glob
import datetime

# _______________Table Contents________________

# grabing the columns from the individual files
# Combining the columns together
# placing columns into list to be filtered through
# removing qoutes

# _______________Table Contents________________

# grabing the columns from the individual files
path = "/Users/User/Desktop/Python/Python_Pandas/xxxold_PANDAS_Resource/Pandas_Resource/data/Female_Names.csv"
df1 = pd.read_csv(path, usecols=['fname'])
print(df1) # checking data

path = "/Users/User/Desktop/Python/Python_Pandas/xxxold_PANDAS_Resource/Pandas_Resource/data/Male_Names.csv"
df2 = pd.read_csv(path, usecols = ['mname'])
# print(df2)

path = "/Users/User/Desktop/Python/Python_Pandas/xxxold_PANDAS_Resource/Pandas_Resource/data/Last_Name.csv"
df3 = pd.read_csv(path, usecols = ['lname'])
# print(df3)

path = "/Users/User/Desktop/Python/Python_Pandas/xxxold_PANDAS_Resource/Pandas_Resource/data/1_999.csv"
df4 = pd.read_csv( path, usecols = ['num'])
df4 = df4.applymap(str) # Converting into str 
# print(df4) 

# Combining the columns together
print('Columns Combinedxxx: ')
# x = df1['fname'].str.cat(df2['mname'], sep = ",").str.cat(df3['lname'], sep = ",")

# data = df1['fname'] + ", " + df2['mname'] + ", " + df3['lname']

data = df4['num'] + "," + df1['fname'] + "," + df2['mname'] + "," + df3['lname']
print(data)

# placing columns into list to be gone through
merged = []

for line in data:
    # print(line)
    merged.append(line)

df = pd.DataFrame(merged)
df.to_csv('list_With_Qoutes.csv', index=False)


# removing qoutes
pd.read_csv('list_With_Qoutes.csv').to_csv('list_With_Out_Qoutes.csv', sep=';', index=False)