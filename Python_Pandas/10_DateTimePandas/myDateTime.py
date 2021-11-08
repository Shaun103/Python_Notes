import pandas as pd


# Resources
# __________________________________________________________________________________
# Dates formatted 
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# DateOffset objects
# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects
# __________________________________________________________________________________

d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
df = pd.read_csv('ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser)


print(df.head())
print(df.shape)

# __________________________________________________________________________________

print(df.loc[0, 'Date'])

# __________________________________________________________________________________

# print(df.loc[0, 'Date'].day_name())  # ERROR

# __________________________________________________________________________________

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')

# __________________________________________________________________________________

print(df['Date'])   # converts 

print(df.loc[0, 'Date'].day_name())

# __________________________________________________________________________________

print(df['Date'].dt.day_name())

df['DayOfWeek'] = df['Date'].dt.day_name()

print(df)

# __________________________________________________________________________________

print(df['Date'].min()) # Earliest date

print(df['Date'].max()) # most recent date 

# __________________________________________________________________________________

# # Time delta - time between two dates 

print(df['Date'].max() - df['Date'].min())

# filt1 = (df['Date'] >= '2019') & (df['Date'] < '2020')

filt2 = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))

print(df.loc[filt2])

# __________________________________________________________________________________

df.set_index('Date', inplace=True)
# print(df)

# __________________________________________________________________________________

print(df['2019'])   

print(df['2020-01':'2020-02'])

print(df['2020-01':'2020-02']['Close'].mean())

print(df['2020-01':'2020-02'].head(24))

print(df.loc['2020-01']['High'])

print(df.loc['2020-01']['High'].max())

# __________________________________________________________________________________

# 'W' weeks, 'D daily' - https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects

print(df['High'].resample('D').max()) 

highs = df['High'].resample('D').max()

print(highs['2020-01-01'])

print(df.resample('W').mean())

print(df.resample('W').agg({'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'}))