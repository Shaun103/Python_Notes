

# _______________Table Contents_______________________

# Example of a set
# Remove method 
# Discard method
# Clear a set
# Union - combines two sets


# _______________Table Contents_______________________


# ________________________________________________

# # Example of a set


example = set()


print(dir(example)) # displays the list of functions you can apply to a set 
# add function looks promising

hel = help(example.add) # confirms what we are wanting to do 
print(hel)  

example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")
print(example)  # may appear in a different order, order does not matter
                # sets do not contain duplicate elements

                # remove from a set "remove" function 

# ________________________________________________

# # Remove method 
hel = help(example.remove)  # Help material
print(hel)

ex = example.remove(42)  # calling method 
l = len(example)        # length to see if the set strank
print(l)
print(example)          # Displays the set



# ________________________________________________

# # Discard method

hel = help(example.discard)  # removes an element from a set, no element found, does nothing
print(hel)
example.discard(50)     # nothing happens, 50 does not appear within the set
print(example)

# ________________________________________________

# # Clear a set

example2 = set([28, True, 2.71828, "Helium"])
l = len(example2)
print(example2)
example2.clear()  # clears the entire set 
print(example2)

# ________________________________________________

# # Union - combines two sets

odd = set([1, 3, 5, 7, 9])
even = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

x = odd.union(even)
print(x)

x = even.union(odd)
print(x)

x = odd.intersection(primes)  # three prime odd numbers
print(x)

x = even.intersection(primes)  # one prime even number
print(x)

x = even.intersection(odd)      # there are no even and odd numbers
print(x)

x = primes.union(composites)    # the number 1 is missing because 1 is neither prime nor composite
print(x)

# ________________________________________________

# # testing to see if an opperator is in a set  

test = 2 in primes  # True
print(test)

test = 6 in primes  # False 
print(test)

test = 9 not in even
print(test)
