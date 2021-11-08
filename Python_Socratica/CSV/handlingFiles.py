# ________________Table Contents________________

# Displays document (CSV file)
# allows indexing
# Printing data by index
# Strip method 
# Printing data
# Strip method 
# Split method
# Putting everything together
# Using the CSV module 
# Printing to file

# ________________Table Contents________________

path = "/Users/User/Desktop/Python/Python_Socratica/CSV/googleData.csv"
file = open(path)
# ____________________________________
# allows indexing
# lines = [line for line in open(path)]  


# ____________________________________
# Displays document (CSV file)
# for line in file:
#     print(line)

# ____________________________________
# # Printing data by index
  
# print(lines[0])  # prints first line
# print(lines[1])  # prints second line

# # ____________________________________
# # Strip method - removes any trailing or leading white space

# x = lines[0].strip()
# print(x)
# x = lines[1].strip()
# print(x)

# ____________________________________
# Split method - divides the string into individual elements

# x = lines[1].split(',')
# print(x)

# ____________________________________
# # Putting everything together

# dataset = [line.strip().split(',') for line in open(path)]
# print(dataset[0])

# # ____________________________________
# # Using the CSV module 

# import csv
# from  datetime import datetime

# # print(dir(csv))  # contains functions for excel

# path = "/Users/User/Desktop/Python/Python_Socratica/CSV/googleData.csv"
# file = open(path, newline ='') # newline = '' - data sets may end with a new line, character, or both
# reader = csv.reader(file)

# header = next(reader)  # The first line is the header

# data = [row for row in reader]  # read the remaining data 
# print(header)
# print(data[0])

# # ____________________________________________________________

import csv
from  datetime import datetime

# print(dir(csv))  # contains functions for excel

path = "/Users/User/Desktop/Python/Python_Socratica/CSV/googleData.csv"
file = open(path, newline ='') # newline = '' - data sets may end with a new line, character, or both
reader = csv.reader(file)

header = next(reader) # first line is a category header

data = []   # list we are appending categories 

# # Looping through the data
for row in reader:                  # row = [Date, Open, High, Low, Close, Volume, Adj. Close]
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])      # 'open' is a builtin python function
    high = float(row[2])            # high stock 
    low = float(row[3])             # low stock
    close = float(row[4])           # numbers when the stock closed
    volume = int(row[5])            # number of stock shared
    adj_close = float(row[6])       # takes into account how the market can change

    data.append([date, open_price, high, low, close, volume, adj_close])
    
# prints the first line of the array 
print(data[0]) # # prints the first line 

# ____________________________________________________________
# Printing to file

# Creates the file "google_returns.csv"
returns_path = "/Users/User/Desktop/Python/Python_Socratica/CSV/google_returns.csv"

file = open(returns_path, 'w', newline='')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])     # writting header row

for i in range(len(data) - 1):
    todays_row = data[i]                    # Grabs each row
    todays_date = todays_row[0]             # The first row from todays_row
    todays_price = todays_row[-1]           # last row from todays_row
    yesterdays_row = data[i+1]              
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    
    # writer.writerow([todays_date, daily_return])
    formatted_date = todays_date.strftime('%m/%d/%Y')   # strftime - string format time
    writer.writerow([formatted_date, daily_return])