import builtins

dir() # prints the built in functions
print(dir()) # short for directory 

print(dir(builtins)) # prints all of the built in functions

# ____________________________________________

help(pow)  # Details how to use different built in functions
print(pow(2, 10))

help(hex)
hex(10)

# ____________________________________________
# help('modules')  # take a second to load

# import bleach  # # cleans HTML code of malicious text
# print(dir(bleach))
# print(help(bleach.clean))

# import math
# print(dir())  # shows up in the directory 

# print(dir(math)) ## displays the differnt functions
# print(help(math.radians))

# print(math.radians(180))