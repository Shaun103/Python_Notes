


# __________________________________________________________
#               Table of contents

# DYNAMIC ARRAY 
# DYNAMIC ARRAY Exercise class
# Anagram funtion
# Array pair sum 
# Easier array pair sum

# __________________________________________________________

# __________________________________________________________
#               Dynamic array 
# Displays space grabing for data 
# Displays how programs grab more space than what is needed
# so that it is not constantly grabbing space
# __________________________________________________________

# import sys

# n = 50 # Set n 

# data = []

# for i in range(n):

#     # Number of elements
#     a = len(data)

#     # Actual size in bytes
#     b = sys.getsizeof(data)

#     print('Length: {0:3d}; Size in bytes: {1:4d} '.format(a, b))  # 'd' base 10 format

#     # Increase length by one
#     data.append(n)
# __________________________________________________________


#               DYNAMIC ARRAY Exercise class
# CLASS (Similar to Python List)
# As the array gets full, the array doubles in size
# No matter how large the data in the array grows, 
# it takes up the same amount of space

# import ctypes

# class DynamicArray(object):

#     def __init__(self):
#         self.n = 0 # Count actual elements (Default is 0)
#         self.capacity = 1 # Default Capacity
#         self.A = self.make_array(self.capacity)
        
#     def __len__(self):
        
#         # Return number of elements sorted in array
#         return self.n
    
#     def __getitem__(self,k):
        
#         # Return element at index k
#         if not 0 <= k < self.n:
#             return IndexError('K is out of bounds!') # Check it k index is in bounds of array
        
#         return self.A[k] #Retrieve from array at index k
        
#     def append(self, ele): 
      
#         # Add element to end of the array
#         if self.n == self.capacity:
#             self._resize(2 * self.capacity) # Double capacity if not enough room # important method, double the capacity so it will keep growing
        
#         self.A[self.n] = ele # Set self.n index to element
#         self.n += 1
        
#     def _resize(self, new_cap):
        
#         # Resize internal array to capacity new_cap
#         B = self.make_array(new_cap) # New bigger array
        
#         for k in range(self.n): # Reference all existing values
#             B[k] = self.A[k]
            
#         self.A = B # Call A the new bigger array
#         self.capacity = new_cap # Reset the capacity
        
#     def make_array(self, new_cap):

#         # Returns a new array with new_cap capacity
#         return (new_cap * ctypes.py_object)() 


# arr = DynamicArray()

# # Check to see if array works
# arr.append(1)
# print(len(arr))
# # _____________________

# # Checks array 
# x = list(range(1, 50))
# for i in x:
#     arr.append(arr)
# print(len(arr))

# # _____________________

# x = len(arr)
# print('The length: ',x)

# x = sys.getsizeof(arr)
# print('The size: ', x, "bytes")

# _____________________

# __________________________________________________________
#                   Anagram funtion
# An anagram is a play on words created by rearranging the 
# letters of the original word to make a new word or phrase


# //////////////////////////////////////////
# Perfered way if asked in an interview
# //////////////////////////////////////////

# def anagram(s1, s2):
#     s1 = s1.replace(' ','').lower()
#     s2 = s2.replace(' ','').lower()

#     return sorted(s1) == sorted(s2)

# x = anagram('clint eastwood', 'old west action')
# print(x)

# # __________________________________________________________
# def anagram2(s1,s2):
#     # Remove spaces and lowercase letters
#     s1 = s1.replace(' ','').lower()
#     s2 = s2.replace(' ','').lower()
    
#     # Edge Case to check if same number of letters
#     if len(s1) != len(s2):
#         return False
    
#     # Create counting dictionary (Note could use DefaultDict from Collections module)
#     count = {}

#     # Fill dictionary for first string (add counts)
#     for letter in s1:
#         if letter in count:
#             print(count)
#             count[letter] += 1
#         else:
#             count[letter] = 1
            
#     # Fill dictionary for second string (subtract counts)
#     for letter in s2:
#         if letter in count:
#             print(count)
#             count[letter] -= 1
#         else:
#             count[letter] = 1
    
#     # Check that all counts are 0
#     for k in count:
#         if count[k] != 0:
#             return False

#     # Otherwise they're anagrams
#     return True

# x = anagram2('clint eastwood', 'old west action')
# print(x)


# __________________________________________________________
#                   Array pair sum 
# __________________________________________________________

# def pair_sum(arr, k): # 'k' the integer number we are trying to sum up to it  
    
#     if len(arr) < 2:
#         return
    
#     # Sets for tracking
#     seen = set()
#     output = set()
    
#     for num in arr:
#         target = k - num    # target we are reaching for
        
#         # Add it to set if target hasn't been seen
#         if target not in seen:
#             seen.add(num)
#         else:
#         # Add a tuple with the corresponding pair
#             output.add((min(num, target),  max(num, target)))
    
#     # return len(output) # return len(output)
#     # FOR TESTING
    
#     # Nice one-liner for printing output
#     print('\n'.join(map(str, list(output))))

# y = [1, 3, 2, 2, 2, 5, -1]
# x = pair_sum(y, 4)

# print(x)

# ________________________________________
# Easier way of doing the same as the top
# ________________________________________

l = [1, 2, 3, 2, -1, 5, 4, 0]
k = 4

def fun(l, k):

    target = 0
    seen = set()
    output = set()

    for num in l:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((num, target))
    print(output)

fun(l, k)