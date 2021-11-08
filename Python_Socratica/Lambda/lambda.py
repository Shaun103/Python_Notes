# You cannot use lambda expressions for multiline functions
# Good for small throw away functions 

# # _______________________Table Contents______________________
# Format: 
# lambda : "What is my purpose?"  # no arguments passed
# lambda x: 3*x + 1 # one argument and expression
# lambda x, y, z: 3/(1/x + 1/y + 1/z) # (Harmonic mean) three arguments and expression

# Write a function to compute 3x+1
# Formating lambda function
# Using lambda function

# Function that makes functions....
# _______________________Table Contents______________________

# Write a function to compute 3x+1

def f(x):
    return 3*x + 1

print(f(2))

# _____________________________________________________________
# Formating lambda function
g = lambda x: 3*x + 1  # does not have a name

print(g(2))

# _____________________________________________________________
# # Using lambda function

# strip() removes white space, title() capitalizes first letter

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()  
print(full_name("          leonhard", "EULER"))


# _____________________________________________________________

# Creating a function that orders by first name
# Splits by white space " "
# Access the last piece with [-1] and lower the string

# # Unordered
scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", 
                "Arthur C. Clarke", "Frank Herbert", "Orson Scott Card", 
                "Douglas Adams", "H. G. Wells", "Leigh Brackett"]


help(scifi_authors.sort)  # displays key arugment that will be used for sorting

# # Splits by white space " " Access the last piece with [-1] and lower the string
scifi_authors.sort(key=lambda name: name.split(" "[-1].lower()))

print(scifi_authors)
print('\n')
# _____________________________________________________________
# Function that makes functions....
# Trajectory of a cannon ball
# Think of the arugments 'a', 'b', 'c' are default values

def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a * x** 2 + b * x + c

f = build_quadratic_function(5, 3, -3)

print('Start Here:')
print(f(0))
print(f(1))
print(f(2))

# _____________________________________________________________
# Function without a call
# Not the most readable code, but it is possible
# build_quadratic_function(3, 0, 1) # function creates 3x^2+1 evaluated for x = 2 