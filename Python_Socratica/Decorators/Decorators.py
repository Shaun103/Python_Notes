# ______________________________Table Contents______________________________

# Calling the function
# Function aliasing
# Using function decorator
# returning values from decorated functions 
# Decorator on a method
# How long it takes a function/method to run 
# Prints date time, and summation 

# ______________________________Table Contents______________________________


#____________________________________

# Calling the function

def f1(func):
    def wrapper():
        print(" Started ")
        func()
        print(" Ended ")
    
    return wrapper

def f():
    print("Hello")


# # Function aliasing

# f1(f)   # does not work

# x = f1(f)

# x()

# f1(f)()     # # Calls the function

#____________________________________

# Using function decorator

# def f1(func):
#     def wrapper(*args, **kwargs):       # any amount of arguments *args, **kwargs
#         print(" Started ")
#         func(*args, **kwargs)       # passed in function
#         print(" Ended ")
    
#     return wrapper


# @f1               # # Decorator: the function, you can now call by 'f'
# def f(a, b='This is the argument'):
#     print(a, b)

# f("Hi!")

#____________________________________

# returning values from decorated functions 

# def f1(func):
#     def wrapper(*args, **kwargs):       # any amount of arguments *args, **kwargs
#         print(" Started ")              # 'do some code'

#         val = func(*args, **kwargs)     # important code
        
#         print(" Ended ")                # 'do some code'
#         return val                      # #  return the val at end, entire function runs
    
#     return wrapper

# @f1           # # Decorator 
# def add(x,y):
#     return x + y 

# print(add(4, 5))

#____________________________________

# # Decorator on a method

# def before_after(func):
#     def wrapper(*args):
#         print('Before')
#         func(*args)         # important method
#         print('After')

#     return wrapper

# class Test:
#     @before_after               # decorator
#     def decorated_method(self):
#         print("run")

# t = Test()      # # setting Class to 't'

# t.decorated_method()    # calling Class on the decorated method

#____________________________________

# How long it takes a function/method to run

# import time


# def timer(func):
#     def wrapper():
#         before = time.time()
#         func()
#         print("Function took: ", time.time() - before, " seconds")

#     return wrapper

# @timer              # # decorator
# def run():
#     time.sleep(2.0000)

# run()

#____________________________________

# prints date time, and summation 

import datetime

def log(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write("Called function with " + " ".join([str(arg) for arg in args]) + " at " + 
            str(datetime.datetime.now()) + "\n")

        val = func(*args, **kwargs)
        
        return val

    return wrapper

@log                        # decorator
def run(a, b, c=9, d=11):
    print(a+b+c+d)

run(100, 3000, c=10, d=11)

# pass more arguments 
run(100, 3000, 10, 11)