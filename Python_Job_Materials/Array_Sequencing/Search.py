# def seq_search(arr, ele):

#     pos = 0
#     found = False

#     while pos < len(arr) and not found: 

#         if arr[pos] == ele:
#             found = True
        
#         else: 
#             pos += 1
    
#     return found 

# arr = [1, 2, 3, 4, 5]

# x = seq_search(arr, 1)


# print(x)

# /////////////////////////////////////////////// #
# def ordered_seq_search(arr, ele):

#     """
#     Input array must be ordered/sorted before hand!
#     """
#     pos = 0
#     found = False
#     stopped = False

#     while pos < len(arr) and not found and not stopped: 

#         if arr[pos] == ele:
#             found = True
        
#         else: 

#             if arr[pos] > ele:
#                 stopped = True
#             else: 
#                 pos += 1
    
#     return found 


# arr = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
# x = ordered_seq_search(arr, 11)
# print(x)

# ////////////////////////////////////////////////////////
#_____________________binary search_____________________ 
# starts by examining the middle item
# if item is greater than middle half, lower is used
# if item is smaller than middle half, upper half is used 
# ////////////////////////////////////////////////////////

# def binary_search(arr, ele):
#     first = 0 # index markers
#     last = len(arr) - 1  # index markers
#     found = False

#     while first <= last and not found:

#         mid = int((first + last) / 2) # middle index 
        
#         if arr[mid] == ele:
#             found = True
#         else:
#             if ele < arr[mid]:   # Left (upper) half of list
#                 last = mid - 1
#             else:                # Right (lower) half of the list
#                 first = mid + 1
#     return found 

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # works only on sorted arrays 
# x = binary_search(arr, 10)
# print(x)


# /////////////////
# Recursive Search
# def rec_bin_search(arr, ele):

#     if len(arr) == 0:
#         return False
#     else:
#         mid = int(len(arr) / 2)
#         if arr[mid] == ele:
#             print(ele)
#             return True
#         else: 
#             if ele < arr[mid]:
#                 print(ele)
#                 return rec_bin_search(arr[:mid], ele)
#             else:
#                 print(ele)
#                 return rec_bin_search(arr[mid + 1:], ele)

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # works only on sorted arrays
# x = rec_bin_search(arr, 10)
# print(x)
