# General Syntax for Decorators
"""
@mydecorator
def dosomething():
    pass
"""

import functools

def start_end_decorator(func):

    @functools.wraps(func) # Help on function add5 in module __main__:
    def wrapper(*args, **kwargs):

        # Something Before
        print("Start")
        result = func(*args, **kwargs)
        # Something After
        print("End")
        return result

    return wrapper

@start_end_decorator
# def print_name():
#     print("Nick")
def add5(x):
    return x+5

# This is the same thing as the decorator
# print_name = start_end_decorator(print_name)

print(help(add5)) # prints wrapper(*args, **kwargs)
print(add5.__name__) # prints wrapper