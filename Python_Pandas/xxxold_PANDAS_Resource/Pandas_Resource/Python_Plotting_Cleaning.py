import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# ///////////////////////////////////////////////////////////////////////////////
# Resources____________________________ #
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# https://datatofish.com/line-chart-python-matplotlib/
# ///////////////////////////////////////////////////////////////////////////////


# ///////////////////////////////////////////////
# Table of contents____________________________ #

# Displays data types
# shows the first four rows
# Shows the last four rows
# Useful methods
# sets column names
# Turns a column (1st) into a date type
# index (search by) date
# Search by date 
# Plotting

# //////////////////////////////////////////////////////// #

# 'header=None' = 1st column not assumed as header
df = pd.read_csv('/Users/User/Desktop/Python/Data/btc-market-price.csv')


# # /////////////////////////
# Displays data types
x = df.dtypes
print(x)

# # /////////////////////////
# # shows the first four rows
x = df.head()
print(x)

# # /////////////////////////
# # Shows the last four rows
x = df.tail()
print(x)

# # /////////////////////////
# # Useful methods
x = df.shape
x = df.info()
print(x)

# # # //////////////////////////////
# # #              Part A 
# # #          Search by date 
# # # //////////////////////////////
print('\n')
df.columns = ['Timestamp', 'Price'] # sets column names
df['Timestamp'] = pd.to_datetime(df['Timestamp']) # # Turns a column (1st) into a date type
df.set_index('Timestamp', inplace=True) # index (search by) date
x = df.loc['2017-09-29'] # access data now by date
print(x)

# # # //////////////////////////////
# # #              Part B
# # #          Search by date 
# # #      Does the same as Part A 
# # # //////////////////////////////
df = pd.read_csv('/Users/User/Desktop/Python/Data/btc-market-price.csv',
    header = None,
    names=['Timestamp', 'Price'],
    index_col=0,
    parse_dates=True
)
print(df)

# # # //////////////////////////////
# Plotting  
# # # //////////////////////////////
Year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
Unemployment_Rate = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]

plt.plot(Year, Unemployment_Rate)
plt.show()

# # # # //////////////////////////////
# Working with files
eth = pd.read_csv('/Users/User/Desktop/Python/Data/bitcoin_Ether.csv')
bitcoin = eth['Bitcoin'].head()
ether = eth['Ether'].head()

N = 5
plt.style.use('seaborn-pastel')
ind = np.arange(N) 
width = 0.35       
plt.bar(ind, bitcoin, width, label='Bitcoin')
plt.bar(ind + width, ether, width, label='Ether')
plt.ylabel('Price')
plt.title('Bitcoin vs Ether')

plt.xticks(ind + width / 2, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend(loc='best')
plt.show()