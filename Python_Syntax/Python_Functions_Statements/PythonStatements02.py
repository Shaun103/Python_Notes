
#CONTENTS __________________________________________________________________
# if/else - elif

# for-loop through strings 
# for-loop tuple 
## tuple unpacking

# Dictionary 
# Dictionaries methods 
# Dictionary keys
# Dictionary sorting
#### converts into a list then selects keys/values 

### While loops 

# Useful functions 
    ## Enumerate function - dont have to worry about updating loop count
    ## Zip - combines returns list of tuples 
    ## in/not in - Boolean Results
    ## Min/Max
    ## random Shuffle
    ##random randint

# Input 
# Square numbers in range and turn into list
# Timeit module
#__________________________________________________________________


#__________________________________________________________________
# if/else - elif
person = 'George'

if person == 'Sammy': 
    print('Welcome Sammy')
else: 
    print("Welcome, what's your name?")

if person == 'Sammy': 
    print('Welcome Sammy!')
elif person == 'George':
    print('Welcome George!')
else: 
    print("Welcome, what's your name?")

#__________________________________________________________________
## lists 
listRange = list(range(0,101)) 
print("\n")
print("Displays contents of list: 1 - 101 ")
for num in listRange:
    if num % 2 == 0:
        print(num)

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('\n')
print("Displays contents of list: 1 - 10 ")
for num in myList:
    print(num)            # displays contents of list 

print('\n')
print("Displays even numbers of myLists")
for num in myList:
    if num % 2 == 0:        # prints on even numbers 
        print(num)

#__________________________________________________________________
## for-loop through strings 
myString = 'This is a string'
for letter in myString:
    print(letter)



#__________________________________________________________________
# # for-loop tuple 
# tup = (1, 2, 3, 4, 5)

# for t in tup:
#     print(t)

# list2 = [(2,4),(6,8),(10,12)]

# for tup in list2:
#     print(tup)

# ## tuple unpacking
# for (t1,t3) in list2:
#     print(t1)


#__________________________________________________________________
## Dictionaries
d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print(item)

# Dictionaries methods 
## keys 
for key,values in d.items():
    print(key)
    print(values)

# Dictionary keys 
# converts into a list then selects keys/values
x = list(d.keys())
x2 = list(d.values())

print(x)
print(x2)

#__________________________________________________________________
# Dictionary sorting
# # How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
print(sorted(xs.items(), key=lambda x: x[1]))
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)] # output

#### Or:

import operator
print(sorted(xs.items(), key=operator.itemgetter(1)))
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)] # output

#__________________________________________________________________
# # Dictionary merging
# # How to merge two dictionaries
# # in Python 3.5+

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}

# z = {**x, **y}
# print(z)
# # {'c': 4, 'a': 1, 'b': 3} # output

# # In Python 2.x you could
# # use this:
# z = dict(x, **y)
# print(z)
# # {'a': 1, 'c': 4, 'b': 3} # output
# # In these examples, Python merges dictionary keys
# # in the order listed in the expression, overwriting 
# # duplicates from left to right.


#__________________________________________________________________
#While loops 
x = 0
while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x += 1
    if x == 3:
        print('Breaking because x = 3')
        break
    else:
        print('continuing...')
        continue

#__________________________________________________________________
# Enumerate function - dont have to worry about updating loop count
# myString = 'abcdefghijklmnopqrstuvwxyz'
# for i, letter in enumerate(myString):
#     print("At index {} the letter is {}".format(i,letter))

#__________________________________________________________________
# # Zip - returns list of tuples 
# mylist1 = [1, 2, 3, 4, 5]
# mylist2 = ['a','b','c','d','e']
# test1 = list(zip(mylist1, mylist2))
# print(test1)

# y = list(zip(mylist1,mylist2))
# print(y)

# for item1, item2 in zip(mylist1,mylist2):
#   print('For this tuple, first item was {} and second item was {}'
#   .format(item1,item2))

#__________________________________________________________________
# In/Not In - Boolean Results
# print(41 in mylist1)
# print(41 not in mylist1)

#__________________________________________________________________
# # Min/Max
# print(max(mylist1))
# print(min(mylist2))

#__________________________________________________________________
# # Random Shuffle
# from random import shuffle
# shuffle(mylist1)
# print(mylist1)

#__________________________________________________________________
# # Random randint - # random number between 0 - 100 
# from random import randint
# x = randint(0, 100)  
# print(x)

#__________________________________________________________________
# Input 
# xyz = int(input('Enter Something into this box: '))
# if xyz <= 10:
#     print("Yes that number is less than 10!")
# else:
#     print("That number is greater than 10")
# print(xyz)

#__________________________________________________________________
# Square numbers in range and turn into list
lst = [x**2 for x in range(0, 11)]
print("Square rooting each number 0 - 11: ")
print(lst)

# Nested list comprehensions
lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst)

#---------------------------Practice Testing-------------------------------#
# mylist = []
# x = 0

# while x < 3:
#     xyz = int(input("Enter a number: "))
#     mylist.append(xyz)
#     x += 1

# print(mylist)

# mylist.insert(-1, 100)

# print(mylist)

#///////////////////
# sentence = 'Print only the words that start with s in this sentence'

# for word in sentence.split():
#     if word[0] == 's':
#         print(word)


# xyz = range(0,11)
# for num in xyz:
#     if num % 2 == 0: 
#         print(num) 

# mylist = []

# xyz = range(0,50)
# for num in xyz:
#     if num % 3 == 0: 
#         mylist.append(num)

# print(mylist)
#///////////////////

#///////////////////
# sentence = 'Print every word in this sentence that has an even number of letters'
# for word in sentence.split():
#     if len(word) % 2 == 0:
#         print(word)

# for x in range(1,100):
#     if  x % 3 == 0 and x % 5 == 0:
#         print("FizzBuzz")
#     elif x % 3 == 0:
#         print("FIZZ")
#     elif x % 5 == 0:
#         print("BUZZ")
#     else:
#         print(x)


# sentence = 'Create a list of the first letters of every word in this string'
# xyz = [word for word in sentence.split()]
# print(xyz)

#///////////////////
#/////Timeit module
# The "timeit" module lets you measure the execution
# time of small bits of Python code

# import timeit
# x = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# print(x)
# # 0.3412662749997253

# x = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# print(x)
# # 0.2996307989997149

# x = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
# print(x)
# 0.24581470699922647
#///////////////////
#---------------------------testing-------------------------------#

