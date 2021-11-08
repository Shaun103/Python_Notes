# do not use a pie chart if you have more than five items to display

from matplotlib import pyplot as plt 

plt.style.use('fivethirtyeight')

# slices = [120, 80, 30, 20]   # slices = [120, 80] the same

# plt.pie(slices)
# labels = ['Sixity', 'Forty', 'Extra1', 'Extra2']
# colors = ['#008fd5', '#fc4f30', '#FFFF00', '#6d904f']

# plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})


# plt.title("My Awesome Pie Chart")
# plt.tight_layout()
# plt.show()

# colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #35ae37
# Green = #6d904f

#
#_______________________________________________________________
#

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.1,0] # enphasizes python

plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'}, 
        explode=explode, startangle=90, autopct='%1.1f%%', shadow=True)

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()
