# Chart: BIG O Cheat sheet
# __________________________________________

# # Operation	            Big-O Efficiency
# index []	            O(1)
# index assignment	    O(1)
# append	            O(1)
# pop()	                O(1)
# pop(i)	            O(n)
# insert(i,item)	    O(n)
# del operator	        O(n)
# iteration	            O(n)
# contains (in)	        O(n)
# get slice [x:y]	    O(k)
# del slice	            O(n)
# set slice	            O(n+k)
# reverse	            O(n)
# concatenate	        O(k)
# sort	                O(n log n)
# multiply	            O(nk) 

# Operation	            Big-O Efficiency
# copy	                O(n)
# get item	            O(1)
# set item	            O(1)
# delete item	        O(1)
# contains (in)	        O(1)
# iteration	            O(n)

# __________________________________________

import timeit

def sum1(n):
    final_sum = 0
    for x in range(n+1):
        final_sum += x
    return final_sum

def sum2(n):
    return (n*(n+1)) // 2


print(timeit.timeit('sum1(10)', setup='from __main__ import sum1', number=1000))
print(timeit.timeit('sum2(10)', setup='from __main__ import sum2', number=1000))

#___________________________________________________________________


# def func_constant(values):
#     print(values[0])

# lst = [1, 2, 3]

# func_constant(lst)


#___________________________________________________________________

# def method1():
#     l = []
#     for n in range(10000):
#         l = l + [n]

# def method2():
#     l = []
#     for n in range(10000):
#         l.append(n)

# def method3():
#     l = [n for n in range(10000)]

# def method4():
#     l = range(10000) # Python 3: list(range(10000))


# print(timeit.timeit('method1', setup='from __main__ import method1', number=1000))
# print(timeit.timeit('method2', setup='from __main__ import method2', number=1000))
# print(timeit.timeit('method3', setup='from __main__ import method3', number=1000))
# print(timeit.timeit('method4', setup='from __main__ import method4', number=1000))
