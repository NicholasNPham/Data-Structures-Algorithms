import time

def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f"{func.__name__} ran in: {t2} seconds")
    return wrapper

@tictoc
def do_this():
    # Simulating running code
    time.sleep(1.3)

@tictoc
def do_that():
    time.sleep(.4)

do_this()
do_that()
print('Done')

"""
decorators allow you to use one function for multiple instances instead of creating multiple functions. 
At my level it was reusing lines of code and turning into a function. This is essentially the next level up of code. 
As you progress you turn lines of code into function.
Then decorators allow you to turn functions into a decorator.

In this example, I could have created a time to run program in each function,
However with just one function and a decorator above all functions. I can use 1 function for all functions. 
"""