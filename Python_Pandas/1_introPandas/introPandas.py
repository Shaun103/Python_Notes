import pandas as pd 

# # df = DataFrame 


df = pd.read_csv('bitcoin_Ether.csv')
df2 = pd.read_csv('Top250.csv')

print(df)

# _________________________________________________
# Displays number of rows columns
print('Shape: ', df.shape) 

# _________________________________________________
# Displays datatype values (int, string, ect..)

print('Informaiton: ', df.info())

# _________________________________________________
# Shows complete data sets to the console

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
print(df)


# _________________________________________________
# displaying the end of a dataset 

print('End of the data: ',df.tail(20))

# _________________________________________________
# displaying the first couple of lines

print('Start of the data: ',df.head(20))

# _________________________________________________
# Indexing Dictionaries

people = {
    "first": ['Corety', 'Jane', 'John'],
    "last": ['Schafer', 'Doe', 'Doe'],
    "email": ['CoreyMSchafer@email.com', 'JaneDoe@gmail.com', 'JohnDoe@email.com']
}

print(people['email'])

print('\n')
df = pd.DataFrame(people)
print(df)

# _________________________________________________
# 

print(type(df['email']))    # series object, one dimentional array 
print(df.email)             # dot notation - still valid, but use cation 

# _________________________________________________
# Displaying more than one column 

print(df[['email', 'first', 'last']])

print(df.columns)

# _________________________________________________
# iloc = integer location

print('\n')
print(df.iloc[0])       # first row
print(df.iloc[[0, 1]])  # first two rows 

print('\n')
print(df.iloc[[0, 1], 2])   # Grabing the first two rows, email address

# _________________________________________________
# loc - selects columns with a 'name'

print(df.loc[0])
print(df.loc[[0, 1]])
print(df.loc[[0, 1], 'email'])  # grab columns with strings 
print(df.loc[[0, 1], ['email', 'last']])


# _________________________________________________
# Testing intro Pandas

print(df2.shape)
print(df2.columns)
print(df2['Restaurant'])
print(df2['Restaurant'].value_counts())             # value_count - number of unique values 
print(df2.loc[0])                                   # Displays only the first row                  
print('Sales of first row: ', df2.loc[0, 'Sales'])  # Displays sales for first row
print('Sales of first three rows:\n ', df2.loc[[0, 1, 2], 'Sales'])   # shows the first three rows of Sales
print('Sales of first three rows:\n ', df2.loc[0:2, 'Sales'])          # index slicing first 3 rows of sales data  
print('Sales of first three rows:\n ', df2.loc[0:2, 'Sales' : 'Units'])  # inclusive - Records everything in between 