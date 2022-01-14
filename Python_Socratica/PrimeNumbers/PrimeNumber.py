import time
import math

def is_prime_v1(n):
    """ Return 'True' if 'n' is a prime number. False otherwise"""
    if n == 1:
        return False # 1 is not a prime number

    for d in range(2, n):
        print(d)
        if n % d == 0:
            return False
        return True

def is_prime_v2(n):
    """ Return 'True' if 'n' is a prime number. False otherwise"""
    if n == 1:
        return False # 1 is not a prime number

    max_divisor = math.floor(math.sqrt(n)) # taking the square root of n and rounding down 
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
        return True


def is_prime_v3(n):
    """ Return 'True' if 'n' is a prime number. False otherwise"""
    if n == 1:
        return False # 1 is not a prime number

    # if it's even and not 2 then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False 
    
    max_divisor = math.floor(math.sqrt(n))  # rounding down, getting sqrt of 'n'
    for d in range(3, 1 + max_divisor, 2):  # testing all the odd numbers
        if n % d == 0:
            return False
        return True

#__________________________________

# # Testing 1st function
# for n in range(1, 21):
#     print(n, is_prime_v1(n))

#__________________________________

# # ==== Time 1st Function =====
# #______WARNING: takes a long time to run______
# t0 = time.time()
# for n in range(1, 100000):  
#     is_prime_v1(n)
# t1 = time.time()
# print("Time required: ", t1 = t0)
#__________________________________

# # Testing 2nd function
# for n in range(1, 21):
#     print(n, is_prime_v2(n))

#__________________________________

# # ==== Time 2nd Function =====
# t0 = time.time()
# for n in range(1, 100000):
#     is_prime_v2(n)
# t1 = time.time()
# print("Time 2 required: ", t1 - t0)

#__________________________________
# # Testing 3rd Function 
# for n in range(1, 21):
#     print(n, is_prime_v3(n))

#__________________________________

# # ==== Time 3nd Function =====
# t0 = time.time()
# for n in range(1, 100000):
#     is_prime_v3(n)
# t1 = time.time()
# print("Time 3 required: ", t1 - t0)