# great for tracking a total, and tracking a total of specifc type

from matplotlib import pyplot as plt 

plt.style.use('fivethirtyeight')

minutes = [1,2,3,4,5,6,7,8,9]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['player1', 'player2', 'player3']
colors = ['#6d904f', '#B40404', '#008fd5']

# plt.pie([5,4,3], labels=['Player1', 'Player2', 'Player3'])
plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

# plt.legend(loc='lower left')
plt.legend(loc=(0.07, 0.05))

plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()

# colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #35ae37
# Green = #6d904f


#_______________________________________________________________