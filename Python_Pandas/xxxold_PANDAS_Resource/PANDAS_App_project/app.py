import pandas as pd
import matplotlib.pyplot as plt

path = '/Users/User/Desktop/Python/Dash_Python/Dash_Test_Bar_Graph/bestsellers_with_categories.csv' 

# Selects the n rows
data = pd.read_csv(path, nrows=20)

print(data) # Prints all data

print(data.head()) # prints first five rows

print(type(data))

print(data[['Author', 'Name']]) # merges two data sets together

#################################
# Shows data price over than 20
#################################
x = data[data['Price'] > 20]
# print(x.head())
print(x.shape)

x = data.plot.scatter(x='Author', y='Price', alpha=0.5)




#################################
### Covid data 
#################################
# import plotly.express as px

# data_canada = px.data.gapminder().query("country == 'Canada'")

# fig = px.bar(data_canada, x='year', y='pop')

# fig.show()



# path = '/Users/User/Desktop/Python/PANDAS_Python/COVID19_state.csv'
# data = pd.read_csv(path)

# with open(path) as f:
#     first_line = f.readline()

# x = first_line.split(',')

# print(x)


# import plotly.express as px

# data_canada = px.data.gapminder().query("country == 'Canada'")

# fig = px.bar(data, x='State', y='Deaths')
# fig.show()

################################
################################
################################
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider, Button, RadioButtons

# fig, ax = plt.subplots()
# plt.subplots_adjust(left=0.25, bottom=0.25)
# t = np.arange(0.0, 1.0, 0.001)
# a0 = 5
# f0 = 3
# delta_f = 5.0
# s = a0 * np.sin(2 * np.pi * f0 * t)
# l, = plt.plot(t, s, lw=2)
# ax.margins(x=0)

# axcolor = 'lightgoldenrodyellow'
# axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
# axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

# sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0, valstep=delta_f)
# samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)


# def update(val):
#     amp = samp.val
#     freq = sfreq.val
#     l.set_ydata(amp*np.sin(2*np.pi*freq*t))
#     fig.canvas.draw_idle()


# sfreq.on_changed(update)
# samp.on_changed(update)

# resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
# button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


# def reset(event):
#     sfreq.reset()
#     samp.reset()
# button.on_clicked(reset)

# rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
# radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


# def colorfunc(label):
#     l.set_color(label)
#     fig.canvas.draw_idle()
# radio.on_clicked(colorfunc)

# # Initialize plot with correct initial active value
# colorfunc(radio.value_selected)

# plt.show()