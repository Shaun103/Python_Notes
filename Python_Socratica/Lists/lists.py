# _______________Table of Contents_______________

            # Order is very important 

# Creating lists
# Index slicing
# Multiple different data types
# Contains duplicates
# Concatenation 

# _______________Table of Contents_______________


# # Creating lists

example = list()

    # or 

primes = []


primes = [2, 3, 5, 7, 11, 13]
print(primes)

primes.append(17)       # adding to a list 
primes.append(19)
print(primes)


print(primes[0])  # first index
print(primes[-1]) # last element

#________________________________

# Index slicing
# beginning value is included, the ending value is not

print(primes[2:5]) # from the 3rd position to the 6th position

print(primes[0:6])

#________________________________

# Multiple different data types

example = [128, True, "Alpha", 1.732, [64, False]]

#________________________________

# Contains duplicates

rolls = [4, 7, 2, 7, 12, 4, 7]
print(rolls)

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

# ________________________________

# Concatenation 

print(numbers + letters)    

#________________________________

# # Helpful resources

print(dir(numbers))                # functions that can be called on numbers object       
print(help(numbers.reverse))       # viewing the reverse method

#________________________________

numbers.reverse()
print(numbers)