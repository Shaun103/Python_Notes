#____________________________________________________________________________________________________
#                                       Helpful resources:
#
# https://www.kite.com/python/answers/how-to-filter-a-pandas-dataframe-by-multiple-columns-in-python
# https://www.youtube.com/watch?v=r-uOLxNrNk8&t=8375s

#____________________________________________________________________________________________________

#_______________________________
#        Table contents
#_______________________________

# # lists all of the columns and their objects 
# # Selects the n rows
# # prints the value in the columns
# # prints what type of data
# # lists the order to individual choose
# # selectings particular data 
# # prints the data in the columns 
# # Mean of data 
# # Filtering through large data sets
# # Chain filtering
# # gives quick information about structure
# # Locate one row (horizontal)
# # Locate one row (Verticle)
# # Boolean selections
# # Operators
# # Rename Columns
# # Creating columns from other columns

# #________________
# # IMPORTANT # # 
# # Useful Methods  

import pandas as pd

path = '/Users/User/Desktop/Python/Python_Packages/Pandas_Resource/data/bestsellers_with_categories.csv'

# # Data to be read

data = pd.read_csv(path)

print('\n')

# #____________________________________________________________________________________________________
# # lists all of the columns and their objects 
# IMPORTANT # #
# print(data.dtypes)


# # #____________________________________________________________________________________________________
# # # quick information about structure
# # print(data.info)

# # #____________________________________________________________________________________________________
# # # shapes of data - ( number rows, number columns) 
# print(data.shape)

# # #____________________________________________________________________________________________________
# # # Selects the n rows
# data = pd.read_csv(path, nrows=20)
# print(data)


# # #____________________________________________________________________________________________________
# # prints the value in the columns 
# print(data.values)

# # #____________________________________________________________________________________________________
# # prints what type of data
# print(type(data.values))


# # #____________________________________________________________________________________________________
# # # lists the order to individual choose
# print(data.index)


# # #____________________________________________________________________________________________________
# # # selectings particular data 
# print("Data values: ")
# print(data.values[3])


# #____________________________________________________________________________________________________
# # prints the data in the columns 
# x = data['Author']
# print(x)

# x = data['Name']
# print(x)


# #____________________________________________________________________________________________________ 
# # Mean of data 
# x = data['User Rating'][1: 11].mean()
# print(x)

# #____________________________________________________________________________________________________
# # Filtering through large data sets
# x = data['User Rating'] # < 4.3  
# print(x)

# #____________________________________________________________________________________________________
# # Printing more than one column from a dataset 
# x = data[['Name', 'User Rating']] 
# print(x)

# #____________________________________________________________________________________________________
# x = data[['Name', 'Price']]
# print(x)

# y = x[(x['Price'] > 8)] 
# print(y)

# #____________________________________________________________________________________________________
# # Chain filtering
# x = data[['Name', 'Price']]

# y = x[(x['Price'] > 8) & (x['Name'] == 'Wonder')] 
# print(y)

# z = x[((x["Name"]=="Wonder") & (x["Price"]<=9)) | (x["Price"]<=4)]
# print(z)

# #____________________________________________________________________________________________________
# # Locate one row (horizontal)
# print(data.loc[1])
# print(data.loc[1:2])

# #____________________________________________________________________________________________________
# # Locate one row (Verticle)
# print(data.iloc[1])
# print(data.iloc[[0, 1, -1]])
# print(data.iloc[1:11])

# #____________________________________________________________________________________________________
# # Boolean selections
# x = data.loc[data['User Rating'] > 4.7]
# y = data.loc[data['User Rating'] > 4.7, 'Name']
# z = data.drop(columns=['Name', 'User Rating'])
# z = data.drop([1, 2], axis='rows')

# print(x)
# print(y)
# print(z)

# #____________________________________________________________________________________________________
# Operators
# z = data[['User Rating', 'Year']]

# y = pd.Series([-1, 1000], index=['User Rating', 'Year'])

# x = data[['User Rating', 'Year']] + y    # other operaters can be used + - * / 

# print(z)
# print(y)
# print(x)

# #____________________________________________________________________________________________________
# # Rename Columns
    # All changes are immutable  
# x = data.rename(
#     columns={
#         'Name': 'Book_Name',
#         'Author' : 'Writer',
#         'User Rating': 'User_Ratings', 
#         'does not exist' : ' None'
#     }
# )
# print(x)

#____________________________________________________________________________________________________
# Creating columns from other columns 

x = data[['Reviews', 'User Rating']]

y = data['User Rating'] / data['Reviews']

# Creates the new column
z = data['Rating_by_reviews'] = y 

print('New column: ', data)

# #____________________________________________________________________________________________________
# # Useful Methods 

# # prints first fews rows
# x = data.head()
# print(x)

# # # brief description of data 
# x = data.describe()
# print(x)


# # #____________________________________________________________________________________________________
# # # DO NOT COMMENT OUT VARIABLE # #
# # #____________________________________________________________________________________________________
# # cleaver variable nameing scheme 
# user_rating = data['User Rating']
# print(user_rating)

# # grabing the min and max of a set of data 
# x = user_rating.min(), user_rating.max()
# print(x)

# # adds all of the data together
# x = user_rating.sum()
# print(x)

# x = user_rating.sum() / len(user_rating)
# print(x)

# # displays the average
# x = user_rating.mean()
# print(x)

# # displays standard deviation
# x = user_rating.std()
# print(x)

# # displays the median
# x = user_rating.median()
# print(x)

# # displays brief description
# x = user_rating.describe()
# print(x)

# x = user_rating.quantile(.25)
# print(x)

# x = user_rating.quantile([.2, .4, .6, .8, 1])
# print(x)

# #____________________________________________________________________________________________________
# #____________________________________________________________________________________________________