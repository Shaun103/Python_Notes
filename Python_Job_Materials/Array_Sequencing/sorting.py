# /////////////////////////////////////////////////////
#                      Resources
# https://www.toptal.com/developers/sorting-algorithms
# https://visualgo.net/bn/sorting?slide=2
# https://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/tree/master/Sorting%20and%20Searching/


#                   Table of Contents
# Bubble Sort
# Insertion Sort
# Shell Sort
# Merge Sort
# Quick Sort
# Selection Sort


#                        Bubble Sort
# makes multiple passess through a list 
# Bubble Sort compares adjacent items and exchanges those that are out of order
# each pass through the list places the next largest value in its proper place 


# def bubble_sort(arr):
#     for n in range(len(arr)-1,0,-1):
#         print('This is the n:', n)
#         for k in range(n):
#             print('This is the k:', k) 
#             if arr[k] > arr[k + 1]:
#                 temp = arr[k]
#                 arr[k] = arr[k+1]
#                 arr[k+1] = temp
#     print(arr)

# arr1 = [1, 2, 3, 4, 5]
# x = list(range(len(arr1)-1, 0, -1)) # leaves out the last number
# print(x)

# arr2 = [5, 3, 7, 2]
# bubble_sort(arr2)



#                          Selection Sort
# One exchange for every pass
# After the first pass, the largest item is in the correct place. 
# After the second pass, the next largest is in place. 
# Requires n-1 passes to sort n items, since the final 
# item must be in place after the (n-1) st pass

# def selection_sort(arr):
    
#     # For every slot in array
#     for fillslot in range(len(arr)-1,0,-1):
#         positionOfMax=0

#         # For every set of 0 to fillslot+1
#         for location in range(1,fillslot+1):
#             # Set maximum's location
#             if arr[location]>arr[positionOfMax]:
#                 positionOfMax = location

#         temp = arr[fillslot]
#         arr[fillslot] = arr[positionOfMax]
#         arr[positionOfMax] = temp

#     print(arr)

# arr = [5, 8, 3, 10, 11]
# selection_sort(arr)



#                           Insertion Sort 
# Shifts the items that are greater to the right
# Always maintains a sorted sublist in the lower positions of the list
# Each new item is then "inserted" back into the previous sublist such 
# that the sorted sublist is one item larger

# def insertion_sort(arr):
    
#     # For every index in array
#     for i in range(1,len(arr)):
        
#         # Set current values and position
#         currentvalue = arr[i]
#         position = i
        
#         # Sorted Sublist
#         while position>0 and arr[position-1]>currentvalue:
            
#             arr[position]=arr[position-1]
#             position = position-1

#         arr[position]=currentvalue

#     print(arr)

# arr =[3, 5, 4, 6, 8, 1, 2, 12, 41, 25]
# insertion_sort(arr)
# arr


#                              Shell Sort
# improves on the insertion sort by breaking the original list into a number 
# of smaller units each of which is sorted using an insertion sort

# def shell_sort(arr):
#     sublistcount = len(arr) // 2
    
#     # While we still have sub lists
#     while sublistcount > 0:
#         for start in range(sublistcount):
#             # Use a gap insertion
#             gap_insertion_sort(arr,start,sublistcount)

#         #
#         # print('After increments of size: ', sublistcount) 
#         # print('The list is: ', arr)

#         sublistcount = sublistcount // 2

#     print(arr)

# def gap_insertion_sort(arr,start,gap):
#     for i in range(start+gap,len(arr),gap):

#         currentvalue = arr[i]
#         position = i

#         # Using the Gap
#         while position>=gap and arr[position-gap]>currentvalue:
#             arr[position]=arr[position-gap]
#             position = position-gap
        
#         # Set current value
#         arr[position]=currentvalue

# arr = [45,67,23,45,21,24,7,2,6,4,90]
# shell_sort(arr)


#                               Merge Sort
# recursive algoithm that continually splits a list in half
# if list is empty it is sorted by definition (the base case)
# if the list has more than one item we split the list and recursively invoke a 
# merge sort on both halves. Once the two halves are sorted, the fundamental operation
# called merge is preformed. 
# merging - the process of taking two smaller sorted lists and combining them together 
# into a single sorted new list

# def merge_sort(arr):
    
#     if len(arr)>1:
#         mid = len(arr)//2
#         lefthalf = arr[:mid]
#         righthalf = arr[mid:]

#         merge_sort(lefthalf)
#         merge_sort(righthalf)

#         i=0
#         j=0
#         k=0
#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 arr[k]=lefthalf[i]
#                 i=i+1
#             else:
#                 arr[k]=righthalf[j]
#                 j=j+1
#             k=k+1

#         while i < len(lefthalf):
#             arr[k]=lefthalf[i]
#             i=i+1
#             k=k+1

#         while j < len(righthalf):
#             arr[k]=righthalf[j]
#             j=j+1
#             k=k+1

#     print(arr)

# arr = [11,2,5,4,7,6,8,1,23]
# merge_sort(arr)



#                              Quick Sort
# first selects a value which is called a pivot value
# pivot value - to assist with splitting the list
# the actual position where the pivot value belongs in the final sorted list, commonly 
# called the split point, will be used to divide the list for subsequent calls to the quick sort

# def quick_sort(arr):
    
#     quick_sort_help(arr,0,len(arr)-1)

# def quick_sort_help(arr,first,last):
    
#     if first<last:
        

#         splitpoint = partition(arr,first,last)

#         quick_sort_help(arr,first,splitpoint-1)
#         quick_sort_help(arr,splitpoint+1,last)
#     print(arr)


# def partition(arr,first,last):
    
#     pivotvalue = arr[first]

#     leftmark = first+1
#     rightmark = last

#     done = False
#     while not done:

#         while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
#             leftmark = leftmark + 1

#         while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
#             rightmark = rightmark -1

#         if rightmark < leftmark:
#             done = True
#         else:
#             temp = arr[leftmark]
#             arr[leftmark] = arr[rightmark]
#             arr[rightmark] = temp

#     temp = arr[first]
#     arr[first] = arr[rightmark]
#     arr[rightmark] = temp


#     return rightmark

# arr = [2,5,4,6,7,3,1,4,12,11]
# quick_sort(arr)