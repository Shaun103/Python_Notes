import pandas as pd 
from matplotlib import pyplot as plt


plt.style.use('fivethirtyeight')

path = '/Users/User/Desktop/Python/Python_MathPlotLib/chartData/DATA_AgeDevPythonJavaScript.txt'

data = pd.read_csv(path)

ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='All Devs')


overal_median = 57287 # fills above and below 57,287

#  overal_median FILL __________________________________________________________

# # fills/shades python line above overal_median - BLUE
# plt.fill_between(ages, py_salaries, overal_median, 
#                 alpha=0.25, where=(py_salaries > overal_median), interpolate=True)

# # fills/shades python line below overal_median - RED
# plt.fill_between(ages, py_salaries, overal_median, 
#                 alpha=0.25, color='red', where=(py_salaries <= overal_median), interpolate=True)

#  __________________________________________________________

# fills/shades python line above dev_salaries - BLUE
plt.fill_between(ages, py_salaries, dev_salaries, 
                alpha=0.25, label='Above Avg', where=(py_salaries > dev_salaries), interpolate=True)

# fills/shades python line below dev_salaries - RED
plt.fill_between(ages, py_salaries, dev_salaries, 
                alpha=0.25, label='Below Avg', color='red', where=(py_salaries <= dev_salaries), interpolate=True)


plt.legend()

plt.title("Median Salary (USD) by Age")
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout() # padding align, a little nicer

plt.show()
