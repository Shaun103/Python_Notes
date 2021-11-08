def large_cont_sum(arr): 
    
    # Check to see if array is length 0
    if len(arr)==0: 
        return 0

    # # will print the last element in array 
    # print(arr[0], arr[-1])

    # # will print the last element in array
    # for i in range(0, len(arr)): 
    #     if i == (len(arr) -1):
    #         print(arr[i])

    # # Start the max and current sum at the first element
    max_sum=current_sum=arr[0]

    # # For every element in array
    for num in arr[1:]: 
        
        #  # Set current sum as the higher of the two
        current_sum=max(current_sum+num, num)
        
        # # Set max as the higher between the currentSum and the current max
        max_sum=max(current_sum, max_sum) 
        
    return max_sum


x = large_cont_sum([1,2,-1,3,4,10,10,-1,-10])
print(x)