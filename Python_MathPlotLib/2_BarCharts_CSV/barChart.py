import numpy as np
import csv 
import pandas as pd
from matplotlib import pyplot as plt 
from collections import Counter

# plt.style.use('fivethirtyeight')
# plt.xkcd() # # Catoon style (AdultSwim: Home Movies)

#______________________________________________________________

# #________________________
# # first data

# ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# # list within index (numpy array)
# x_indexes = np.arange(len(ages_x))
# width = 0.25

# dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# # Bar plot 
# plt.bar(x_indexes - width, dev_y, width=width, color='#444444', label='All Devs')

# #________________________
# # Second data

# py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
# plt.bar(x_indexes, py_dev_y, width=width,  color='#5a7d9a', label='Python') # plotting second x and y axis

# #________________________
# # Third data 

# js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
# plt.bar(x_indexes + width, js_dev_y, width=width, color='#adad3b', label='JavaScript')



# #________________________

# plt.legend()

# plt.xticks(ticks=x_indexes, labels=ages_x) # plot x axis correctly

# plt.title('Median Salary (USD) by Age') # labeling title 
# plt.xlabel('Ages')  # labeling x axis         
# plt.ylabel('Median Salary (USD)') # labeling y axis 

# plt.tight_layout()

# plt.show()

#______________________________________________________________
#______________________________________________________________
# grabbing/cleaning data CSV method

# path = '/Users/User/Desktop/Python/Python_MathPlotLib/2_BarCharts_CSV/barchart_data.csv'

# with open(path) as csv_file:
#     csv_reader = csv.DictReader(csv_file)   # iterator we can loop over

#     language_counter = Counter() # languages and its popularity
    
#     # row = next(csv_reader)  # grabs the first line
#     # print(row['LanguagesWorkedWith'].split(';'))

#     for row in csv_reader:
#             language_counter.update(row['LanguagesWorkedWith'].split(';'))

# # print(language_counter)   
# # print(language_counter.most_common(15)) # first 15 most common 

# # #___________________________
# # # Storing data in seperate lists
# languages = []  # language list
# popularity = [] # popularity list


# for item in language_counter.most_common(15):   # looping through lanaguage Counter
#     languages.append(item[0])
#     popularity.append(item[1])

# # # Printing seperatly 
# # print(languages)
# # print(popularity)

# # #___________________________
# # # verticle bar chart
# # plt.bar(languages, popularity)

# # #___________________________
# # # Horizontal bar chart
# languages.reverse()
# popularity.reverse()

# plt.barh(languages, popularity)

# plt.title('Most popular Languages') # labeling title 
# plt.ylabel('Programming Languages')  # labeling y axis         
# plt.xlabel('Number of People Who Use') # labeling x axis 
# plt.tight_layout()
# plt.show()

#______________________________________________________________
#______________________________________________________________
# Pandas Method

path = '/Users/User/Desktop/Python/Python_MathPlotLib/2_BarCharts_CSV/barchart_data.csv'
data = pd.read_csv(path)

#________________________
# grabbing the rows using pandas
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()    # creating a empty counter

#________________________
# looping through languages
for response in lang_responses:
        language_counter.update(response.split(';')) # split returns a tuple of unique values

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])   # every item in first column
    popularity.append(item[1])  # every item in second column

#________________________
# places largest on top smallest on bottom
languages.reverse()
popularity.reverse()

#________________________
# plots the bar graph
plt.barh(languages, popularity)

plt.title('Most popular Languages') # labeling title 
plt.ylabel('Programming Languages')  # labeling y axis         
plt.xlabel('Number of People Who Use') # labeling x axis 

plt.tight_layout()

plt.show()