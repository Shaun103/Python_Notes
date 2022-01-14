import random

# _______________Table Contents_______________________

# Random walk
# Random Walk2
# Number Random Walk

# _______________Table Contents_______________________

# Random walk

def random_walk(n):
    """ Return coordinates after 'n' block random walk"""
    x = 0 
    y = 0 
    for i in range(n):
        step = random.choice(['N','E','S','W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = + 1
        else:
            x = x -1
    return (x, y)

for i in range(25):
    walk = random_walk(10)
    print(walk, 'Distance from home = ', abs(walk[0]) + abs(walk[1]))

# ______________________________________

# More compact than the top
# Random Walk2

def random_walk2(n):
    """ Return coordinates after 'n' block random walk"""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    
    return (x, y)

for i in range(25):
    walk = random_walk2(10)
    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

# __________________________________________

# Number Random Walk 10000

number_of_walks = 10000

for walk_length in range(1, 31): # length 1 to 30 blocks 

    no_transport = 0 # number of walks 4 fewer blocks from home

    for i in range(number_of_walks):
        (x, y) = random_walk2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size = ", walk_length,
            " / % of no transport = ", 100 * no_transport_percentage)       

# __________________________________________

# # Find the least amount of walks within five blocks

for walk_length in range(1, 31): # length 1 to 30 blocks 

    no_transport = 0 # number of walks 4 fewer blocks from home

    for i in range(number_of_walks):
        (x, y) = random_walk2(walk_length)
        distance = abs(x) + abs(y)
        if distance == 5:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size = ", walk_length," / % of no transport = ", 100 * no_transport_percentage)   