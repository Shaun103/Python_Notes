# ________________Table contents_________________
# Fibonacci
# Memoization
    # Implemented explicitly
# Implemented Python Tools
# Implemented Python Tools with raised errors    
# ________________Table contents_________________

# ___________
# Fibonacci 
# ___________

def fibonacci(n): 
    if n == 1:
        return 1 
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

# for n in range(1, 11):
#     print(n, ":", fibonacci(n))

# for n in range(1, 101):
#     print(n, ":", fibonacci(n))

# _______________________________
# Memoization
# Implemented explicitly 
# _______________________________

fibonacci_cache = {}

def fibonacci2(n):
    # If we have cached the value, then return it 
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2: 
        value = fibonacci2(n-1) + fibonacci2(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value 
    return value 

# for n in range(1, 1001):
#     print(n, ":", fibonacci2(n))

# _______________________________
# # Implemented Python Tools
# _______________________________

from functools import lru_cache  # Least, Recently, Used, Cache
@lru_cache(maxsize = 1000)       # add memoization 

def fibonacci3(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci3(n-1) + fibonacci3(n-2)

# for n in range(1, 501):
#     print(n, ":", fibonacci3(n))

# ______________________________________________
# Implemented Python Tools with raised errors 
# ______________________________________________

from functools import lru_cache  # Least, Recently, Used, Cache
@lru_cache(maxsize = 1000)       # add memoization 

def fibonacci3(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # Fibonacci Calculations    
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci3(n-1) + fibonacci3(n-2)

for n in range(1, 51):
    print(n, ":", fibonacci3(n))

for n in range(1, 51):
    print(fibonacci3(n+1) / fibonacci3(n))  # # Efficiency , outputs "Golden Rule" 

# print(fibonacci3(-1)) # # Type error positive integer
# print(fibonacci3(1)) # # Type error n must be a integer