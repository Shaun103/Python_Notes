# Table contents____________________________________

    # tuple is immutable
    # contains a sequence of data surrounded by '()'
    # contains less data, (easier on the compiler)
    # lists have more methods than tuples
    # lists occupies more memory than tuples
    #___________________________________

# len function
# iterating
# tuple vs list 
# Creating tuples
# Tuples assignment
# Errors

# Table contents____________________________________

perfect_squares = (1, 4, 9, 16, 25, 36) # tuple
prime_numbers = [2, 3, 5, 7, 11, 13, 17] # list 

# # # len function (length)
# print("# Primes = ", len(prime_numbers))
# print("# Squares = ", len(perfect_squares))

# # # iterating
# for num in prime_numbers:
#     print("Prime: ", num)

# for num in perfect_squares:
#     print("Square: ", num)

# # lists have more methods than tuples
# # lists occupies more memory than tuples

#______________________________________________________________________

# # tuple vs list

import sys 

# print(dir(sys))
# print(help(sys.getsizeof))

# list_eg = [1, 2, 3, 'a', 'b','c', True, 3.14159]
# tuple_eg = (1, 2, 3, 'a', 'b','c', True, 3.14159)

# print("List size: ", sys.getsizeof(list_eg))  # Contains more data

# print("Tuple size: ", sys.getsizeof(tuple_eg)) # contains less data, (easier on the compiler)

# import timeit

# list_test = timeit.timeit(stmt = "[1, 2, 3, 4, 5]", number = 1000000)       # list is less efficient
# tuple_list = timeit.timeit(stmt = "(1, 2, 3, 4, 5)", number = 1000000)      # tuple are more efficient

# print("List time: ", list_test)
# print("Tuple time: ", tuple_list)

#______________________________________________________________________

# # Creating tuples
# contains a single element prints - 'a', needs to contains a comma after the string

empty_tuple = ()
# # test1 = ("a") 
testss = ("a",) 
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)
# # print(test1)
print(testss)
print(test2)
print(test3)

#________________________

# Another way of creating tuples
# place comma after declaing data

test1 = 1, 
test2 = 1, 2
test3 = 1, 2, 3
print(type(test1))
print(type(test2))
print(type(test3))

#________________________

# Tuples assignment 

survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]
print("Age = ", age)
print("Country = ", country)
print("Knows python = ", knows_python)

#________________________

# Assigning using a tuple

survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2
print("Age = ", age)
print("Country = ", country)
print("Knows python?", knows_python)

country = ("Australia", )
print(country)

#________________________

# Errors

# a, b, c = (1, 2, 3, 4) # presents a value error (too many values)
# x, y, z = (1, 2) # value error (too many variables)