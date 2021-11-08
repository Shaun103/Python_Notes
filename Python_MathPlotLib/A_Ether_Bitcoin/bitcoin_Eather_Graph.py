import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

path = '/Users/User/Desktop/Python/Data/bitcoin_Ether.csv'
data = pd.read_csv(path)

bitcoin = data['Bitcoin'][:15]
ether = data['Ether'][:15]
timestamp = data['Timestamp'][:15]

#_____________________________________________________________________

# width of the bars
barWidth = 0.3
 
# grabing bar one: Bitcoin
bars1 = bitcoin
 
# grabing bar two: ether 
bars2 = ether

# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1] 

# Create style
plt.style.use('seaborn-whitegrid')

# Plotting bitcoin
plt.bar(r1, bars1, width=barWidth, color='#A9E2F3', edgecolor='black', capsize=7, label='Bitcoin')

# Plotting ether
plt.bar(r2, bars2, width=barWidth, color='#A9BCF5', edgecolor='black', capsize=7, label='Ether')

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], timestamp, rotation=80)

plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.tight_layout()

plt.show()