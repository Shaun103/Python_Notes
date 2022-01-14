def finder(arr1,arr2):
    num = 0
    
    for n in arr1:
        num += n
    for n in arr2:
        num -= n
    
    print(num, ': is the missing element')
    
def finder2(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
    
    return arr1[-1]

import collections 

def finder3(arr1, arr2):

    d = collections.defaultdict(int) # if key is not in dictionary, it will add it to the dictionary

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


def finder4(arr1, arry2):
    result = 0 
    
    # Perform an XOR between the numbers in the arrays
    for num in arr1+arr2: 
        result^=num 
        print(result)

    print('Missing number is: ', result)
    # return result 



arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]

# x = finder(arr1,arr2)
# print(x)

# x = finder2(arr1,arr2)
# print(x)

# x = finder3(arr1,arr2)
# print(x)

x = finder4(arr1,arr2)
print(x)