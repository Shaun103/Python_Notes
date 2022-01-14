import itertools
import string 
import sys 


def main() -> None:
    
#     def f():        # not iterable 
#         return 1
#         return 2
#         return 3
    
#     print(f())

#     # for x in f():    # not iterable, cannot loop through 
#     #     print(x)

#     def g():        # returns a generator object  
#         yield 1
#         yield 2
#         yield 3
    
#     print(g())


#     for x in g():
#         print(x)
# #_____________________________________________#

#     def letters():
#         for c in string.ascii_lowercase:
#             yield c 
    
#     for letter in letters():
#         print(letter)


#_____________________________________________#


    # def prime_numbers():
    #     # Handle the first prime
    #     yield 2
    #     prime_cache = [2] # cache of the prime numbers

    #     # Loop over positive, odd integers
    #     for n in itertools.count(3, 2):     # never ending for loop
    #         is_prime = True

    #         # check to see if any prime number divides n 
    #         for p in prime_cache:
    #             if n % p == 0:      # p divides n evenly, it is not prime!
    #                 is_prime = False
    #                 break

    #         #is it prime?
    #         if is_prime:
    #             prime_cache.append(n)
    #             yield n


    # for p in prime_numbers():
    #     print(p)
    #     if p > 100:
    #         break

#_____________________________________________#

    squares = (x**2 for x in itertools.count(1))

    print(type(squares))
    print(sys.getsizeof(squares))

    # for x in squares:
    #     print(x)
    
    #     if x > 500:
    #         squares.close()

if __name__ == "__main__":
    main() 