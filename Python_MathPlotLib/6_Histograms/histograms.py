# allows to create bins(groups), and plot the number of occurences 

from matplotlib import pyplot as plt
import pandas as pd 

plt.style.use('seaborn-whitegrid')
# plt.style.use('fivethirtyeight')

path = '/Users/User/Desktop/Python/Python_MathPlotLib/chartData/HistogramData.txt'
data = pd.read_csv(path)

# ___________________________________________________________
# test data

# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

# # bins = [10, 20, 30, 40, 50, 60] # breaking up bins manually; 10-20, 20-30, 30-40...
# bins = [20, 30, 40, 50, 60]

# # plt.hist(ages, bins=5, edgecolor='black')
# plt.hist(ages, bins=bins, edgecolor='black')

# plt.title('Ages of Respondents')
# plt.xlabel('Ages')
# plt.ylabel('Total Respondents')

# plt.tight_layout()

# plt.show()

# ___________________________________________________________
# Manipulating large data.csv

ids = data['Responder_id']
ages = data['Age']

median_age = 29
color = '#fc4f30'

# manualy setting up bins
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 

# histogram bars
plt.hist(ages, bins=bins, edgecolor='black', log=True)  # log = logorythmic, shows small data values

# axis vertical line
plt.axvline(median_age, color=color, label='Age Median', linewidth=1)

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()
