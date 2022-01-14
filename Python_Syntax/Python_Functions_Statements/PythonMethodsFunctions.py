#CONTENTS________________________________________________________________________
# Append - adds element to the end of the list 
# Count - count the number of occurrences
# Extend - combines two seperate lists
# Insert - insert element to a specified index 
# Pop - deletes instances at desired index 
# Remove - removes every instance of the desired input 
# Reverse - reverses order of list 
# Sort - forward organizes list 
# help - 
# CONTENTS________________________________________________________________________

# Functions________________________________________________________________________ 
# Correctly checks if a number in a list is even 
# Map function - allows you to "map" a function to an iterable object
# Filter Function - returns iterable items for which the function(item) is true
# Tuple unpacking
# Finds the max price in a list of tuples
# Functions________________________________________________________________________

# Functions________________________________________________________________________
# Random Functions - testFunctions
# creating random numbers 
# Keeps track of upper/lowercase
# Checks if a function is in a range
# Reverses string 
# Capitalizes first letter in a string 
# Checks if two numbers add to 20
# Checks to see if two strings start with the same letter
# Returns lower of two numbers 
# Multply all numbers within a list
# Checks to see if a string/word is a palidrome
# Checks to see if a string contains all the letters from the alphabet
# Functions________________________________________________________________________


#___________________________________________________________________________
# Variables 
myList = [1,2,3,4,5,6,7,8,9,10]
myList2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
mytuple = (100, 200, 300, 400, 500)

#___________________________________________________________________________

# #####################
# Append - adds to the end of a list 
myList.append(100)
print("Append: ", myList)

# #####################
# # Count - lists the number of occurences
# xyz = myList.count(2)
# print("COUNT: ", xyz)

# #####################
# # Extend - does not return anything "xyz = myList.extend..."
# myList.extend(myList2)
# print("EXTEND: ", myList)

# #####################
# # Insert
# myList.insert(-1, mytuple)
# print('INSERT: ', myList)

# #####################
# # Pop - deletes instances at desired index 
# myList.pop(0)
# print("POP: ", myList)

# #####################
# # Remove - removes every instance of the desired input 
# myList.remove(100)
# print("Remove: ", myList)

# #####################
# # Reverse - reverses order of list 
# myList.reverse()
# print("REVERSE", myList)

# ####################
# # Sort - forward organizes list 
# lst = [
#     45,645,6456,784,9456,48,89,156,789,
#     4516,489,123,489,487,1,123,21,2,456,
#     456,456,7,897,89]

# lst.sort()
# print("SORTED: ", lst)

# ####################
# help
# help(myList)


# ####################
# # Creating Functions
    # return - when you want to save the resulting variable 
    # after it has been manipulated 

## Adds two numbers  
# def name_or_function(arg1, arg2):
#     return arg1 + arg2 

# x = name_or_function(100, 200)
# print(x)

# ## checks to see if number is even or not 
# def check_even(number):
#     return number % 2 == 0 

# x = check_even(564723805)
# print(x)

####################
# Correctly checks if a number in a list is even 
# def check_even_list(num_list):
#     # Go through each number
#     for number in num_list:
#         # Once we get a "hit" on an even number, we return True
#         if number % 2 == 0:
#             return print(True)
#         # Don't do anything if its not even
#         else:
#             pass
#     # Notice the indentation! This ensures we run through the entire for loop    
#     return print(False)

# check_even_list([1,2,3])
# check_even_list([1,3,5])


##########################
# Function Tuple unpacking
# stock_prices = [   # list of tuples 
#     ('AAPL',200),
#     ('MSFT',400),
#     ('GOOG',300)
#     ]

# def stock_check(stock_prices):
#     for stock,price in stock_prices:
#         print(stock,price)

# stock_check(stock_prices)

##########################
# Finds the max price in a list of tuples 
# stock_prices = [   # list of tuples 
#     ('AAPL',200),
#     ('MSFT',400),
#     ('GOOG',300)
#     ]

# def checking_stock(list):
#     current_max = 0
#     stock_name = ''
#     for stock,price in stock_prices:
#         if price > current_max:
#             current_max = price
#             stock_name = stock
#         else:
#             pass
#     return print(stock_name, current_max)

# checking_stock(stock_prices)

# # Map function - allows you to "map" a function to an iterable object
# def splicer(mystring):
#     if len(mystring) % 2 == 0:
#         return 'even'
#     else:
#         return mystring[0]

# mynames = ['John','Cindy','Sarah','Kelly','Mike']
# x = list(map(splicer, mynames))

# print(x)

##########################
# # Filter Function - true or false only return 
# def check_even(num):
#     return print(num % 2 == 0)

# nums = [0,1,2,3,4,5,6,7,8,9,10]
# list(filter(check_even, nums))




#___________________________________________________________________________
#                               Random Functions
#___________________________________________________________________________

##########################
# Returns lower of two numbers 
# def lesser_of_two_events(a,b):
#     if a < b: 
#         return print(a) 
#     else:
#         return print(b) 

# lesser_of_two_events(100,10)

##########################
# Checks to see if two strings start with the same letter
# def animal_crackers(text):
#     wordlist = text.split()
#     x = wordlist[0][0] == wordlist[1][0]
#     print(x)
    
#     return x

# animal_crackers('Levelheaded Llama')

##########################
# checks if two numbers add to 20
# def makes_twenty(a,b): 
#     if a + b == 20:
#         print(True)
#         return True
#     else:
#         print(False)
#         return False

# makes_twenty(10,15)

##########################
### index slicing 
# name = "Alison"
# print(name[:3])
# print(name[3:])

##########################
# Capitalizes first letter in a string 
# def old_macdonald(name):
#     if len(name) > 3:
#         return print(name[:3].capitalize() + name[3:].capitalize())
#     else:
#         return 'Name is too short!'

# old_macdonald('macdonald')

##########################
# Reverses string 
# def master_yoda(string):
#     return print(' '.join(string.split()[::-1]))

# master_yoda('I am home')

##########################
# checks if a function is in a range 
# def ran_check(num, low, high):
#     if num > low and num < high:
#         print("{} is in the range between {} and {}".format(num,low,high))
#     else: 
#         print("{} is out of range between {} and {}".format(num,low,high))

# def ran_check1(num, low, high):
#     if num > low and num < high:
#         return print(True)
#     else: 
#         return print(False)
 
# ran_check(15,2,7)
# ran_check1(15,2,7)

##########################
# keeps track of upper/lowercase 
# def up_low(s):
#     d={"upper":0, "lower":0}
#     for c in s:
#         if c.isupper():
#             d["upper"]+=1
#         elif c.islower():
#             d["lower"]+=1
#         else:
#             pass
#     print("Original String : ", s)
#     print("No. of Upper case characters : ", d["upper"])
#     print("No. of Lower case Characters : ", d["lower"])


# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'

# up_low(s)

##########################
# multply all numbers within a list
# def multiply(list):
#     total = 1
#     for num in list:
#         total = total * num

#     print(total)

# myList = [1,2,3,-4]
# multiply(myList)

##########################
# Checks to see if a string/word is a palidrome 
# def palindrome(string):
#     string = string.replace(' ','')
#     if string[::-1] == string:
#         print(True)
#     else:
#         print(False)

# palindrome('nurses run')

##########################
# Checks to see if a string contains all the letters from the alphabet
import string

# def ispangram(str1, alphabet=string.ascii_lowercase): 
#     # Create a set of the alphabet
#     alphaset = set(alphabet)  
    
#     # Remove spaces from str1
#     str1 = str1.replace(" ",'')
    
#     # Lowercase all strings in the passed in string
#     # Recall we assume no punctuation 
#     str1 = str1.lower()
    
#     # Grab all unique letters in the string as a set
#     str1 = set(str1)
    
#     # Now check that the alpahbet set is same as string set
#     return print(str1 == alphaset)

# ispangram("The quick brown fox jumps over the lazy dog")
#___________________________________________________________________________
# creating random numbers 
import random 

randomlist = []
for i in range(0,5):
    n = random.randint(1,31)
    randomlist.append(n)
    
print(randomlist)

#___________________________________________________________________________