# General Syntax for Decorators
"""
@mydecorator
def dosomething():
    pass
"""

def start_end_decorator(func):

    def wrapper():

        # Something Before
        print("Start")
        func()
        # Something After
        print("End")

    return wrapper

@start_end_decorator
def print_name():
    print("Nick")

# This is the same thing as the decorator
# print_name = start_end_decorator(print_name)

print_name()
