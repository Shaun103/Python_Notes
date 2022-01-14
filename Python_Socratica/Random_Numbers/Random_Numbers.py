import random 

print(dir(random))  # prints the functions the random module uses
print(help(random.random)) # displays documentation of the random module

# ____________________
# displays ten random numbers
# numbers being chosen are each equally randomly generated

# for i in range(10):
#     print(random.random())

# _________________________________________________
# intervals all exist between 3 - 7 (not inclusive)
# Explicity describing the uniform function
def my_random():
    # Random, Scale, Shift return...
    return 4*random.random() + 3

# for i in range(10):
#     print(my_random())

# ____________________________________________________________
# Using the uniform from random function - normal distribution 

# for i in range(10):
#     print(random.uniform(3, 7))

# ____________________________________________________________
# Generating numbers from a bell curve
# Mean - Numbers will group around
# std - how tightly packed the numbers will be grouped by 

# for i in  range(20):
#     print(random.normalvariate(0, 1))  # Mean, std 

# for i in  range(20):
#     print(random.normalvariate(0, 9))  # Larger std, more widely spread out

# for i in  range(20):
#     print(random.normalvariate(0, 0.2)) # Small std, tightly grouped together

# for i in  range(20):
#     print(random.normalvariate(5, 0.2)) # Tightly grouped around 5 


# ____________________________________________________________
# Random integer from numbers 1 - 6 
# Randint

for i in range(20): # calling 20 times
    print(random.randint(1, 6))
# ____________________________________________________________
# choice
# when you want a random selection from a list of non-numerical values

outcomes = ["rock", "paper", "scissor"]

for i in range(20):
    print(random.choice(outcomes))