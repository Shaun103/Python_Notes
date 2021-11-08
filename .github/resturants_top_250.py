import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


# 'header=None' = 1st column not assumed as header
df = pd.read_csv('/Users/User/Desktop/Python/Data/Data_Resturant/top250.csv')

# print('\n')
# x = df.dtypes       # displays column data sets
# print(x)

# x = df.head()       # displays first four columns 
# print(x)

restaurantAndSales = df[['Restaurant', 'Sales']][:10]
restaurant = restaurantAndSales['Restaurant']
sales = restaurantAndSales['Sales']
print(restaurant)
print(sales)

fig = plt.figure(figsize = (10, 5))

mycolor = 'black', 'red', 'green', 'blue', 'cyan'

# creating the bar plot
plt.bar(restaurant, sales, color=(0.2, 0.4, 0.6, 0.6), width = 0.4)
plt.xlabel("Restaurants")
plt.ylabel("Sales")
plt.title("Top 10 restaurant sales")
plt.show()