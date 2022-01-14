from matplotlib import pyplot as plt 

# # displays styles of grid
print(plt.style.available)

# # Using styles
plt.style.use('fivethirtyeight')
# plt.style.use('seaborn-notebook')
# plt.xkcd() # # Catoon style (AdultSwim: Home Movies)


# _____________________________
# first line data 
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# k = black line, -- = dashed line
# plt.plot(ages_x, dev_y, 'k--', label='All Devs') # plotting the x and y axis 

plt.plot(ages_x, dev_y, color='#444444', linestyle='--', linewidth=3, label='All Devs')

# _____________________________
# second line data 
py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

# b = solid blue line, marker='o', color='b', marker='.',
plt.plot(py_dev_x, py_dev_y,  color='#5a7d9a', label='Python') # plotting second x and y axis

#________________________
# third line 
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x, js_dev_y, color='#adad3b', linewidth=3, label='JavaScript')


#______________
# labeling categories

plt.xlabel('Ages')  # labeling x axis         
plt.ylabel('Median Salary (USD)') # labeling y axis 
plt.title('Median Salary (USD) by Age') # labeling title 


plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('plot.png')
plt.show()










