#____________________Table_of_Contents_________________________#

# Function returning
# Python's list comprehensions are awesome
# Python has a HTTP server
# first-class functions
# "is" vs "=="
# In-place value swapping
# Function argument unpacking
# standard string repr for dicts
# Using namedtuple
# The get() method on dicts
# How to sort a Python dict by value

#____________________Table_of_Contents_________________________#

# Function returning
def my_add(a: int, b: int) -> int:
    return a + b

x = my_add(100, 200)

print(x) 
##################################

# # Python's list comprehensions are awesome

# # Example: 
#     # vals = [expression 
#     #         for value in collection 
#     #         if condition]

even_squares = [x * x for x in range(10) if not x % 2]
print(even_squares)
##################################

# # Python has a HTTP server built into the
# # standard library. This is super handy for
# # previewing websites.

# # Python 3.x
# $ python3 -m http.server

# # Python 2.x
# $ python -m SimpleHTTPServer 8000

# # (This will serve the current directory at
# #  http://localhost:8000)
##################################

# Because Python has first-class functions they can
# be used to emulate switch/case statements

def dispatch(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None

def dispatch(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


x = dispatch('mul', 2, 8)

y = dispatch('div', 2, 8)

z = dispatch('add', 2, 8)

s = dispatch('unknown', 2, 8)

print("Answers: ", x, y, z, s)

##################################

# # "is" vs "=="

# a = [1, 2, 3]
# b = a

# a is b # True: variables are equal 
# a == b # True: pointing to the same object

# c = list(a)  ###
# a == c # True
# a is c # False: is not pointing to the same object


# # • "is" expressions evaluate to True if two 
# #   variables point to the same object

# # • "==" evaluates to True if the objects 
# #   referred to by the variables are equal

##################################

# # Why Python Is Great:
# # In-place value swapping

# # Let's say we want to swap
# # the values of a and b...
# a = 23
# b = 42

# # The "classic" way to do it
# # with a temporary variable:
# tmp = a
# a = b
# b = tmp

# # Python also lets us
# # use this short-hand:
# a, b = b, a

##################################

# # Why Python Is Great:
# # Function argument unpacking

# def myfunc(x, y, z):
#     print(x, y, z)

# tuple_vec = (1, 0, 1)
# dict_vec = {'x': 1, 'y': 0, 'z': 1}

# myfunc(*tuple_vec)

# myfunc(**dict_vec)


##################################

# # The standard string repr for dicts is hard to read:
# my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
# x = my_mapping
# print(x)

# # The "json" module can do a much better job:
# import json
# print(json.dumps(my_mapping, indent = 4, sort_keys = True))

# # Note this only works with dicts containing
# # primitive types (check out the "pprint" module):
# # json.dumps({all: 'yup'})
# # TypeError: keys must be a string

##################################

# # Why Python is Great: Namedtuples
# # Using namedtuple is way shorter than
# # defining a class manually:

# from collections import namedtuple
# Car = namedtuple('Car', 'color mileage')

# # Our new "Car" class works as expected:
# my_car = Car('red', 3812.4)
# x = my_car.color
# print(x)
# x = my_car.mileage
# print(x)

# # We get a nice string repr for free:
# x = my_car
# print(x) # Car(color='red' , mileage=3812.4)

# # Like tuples, namedtuples are immutable:
# # x = my_car.color = 'blue' # #Error
# # print(x)

##################################

# # The get() method on dicts
# # and its "default" argument

# name_for_userid = {
#     382: "Alice",
#     590: "Bob",
#     951: "Dilbert",
# }

# def greeting(userid):
#     return "Hi %s!" % name_for_userid.get(userid, "Invalid number")

# greeting(382) # "Hi Alice!"

# greeting(333333) # "Invalid number"

##################################

# # How to sort a Python dict by value
# # (== get a representation sorted by value)

# xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

# x = sorted(xs.items(), key=lambda x: x[1]) # [('d', 1), ('c', 2), ('b', 3), ('a', 4)] # # x[1] sort low high
# print(x) 
#                     # Or:
# import operator
# x = sorted(xs.items(), key=operator.itemgetter(0)) # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# print(x)

##################################