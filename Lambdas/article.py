# identity() takes an argument x and returns it upon invocation.
def identity(x):
    return x
# The same thing above but in one line. [keyword] [a bound variable]: [a body]
lambda x: x

lambda x: x + 1
print((lambda x: x + 1)(2)) # prints 3

add_one = lambda x: x + 1
print(add_one(2)) # prints 3

# the lambda function in a normal function:
def add_one(x):
    return x + 1

full_name = lambda first, last: f'Full Name: {first.title()} {last.title()}'
print(full_name("nicholas", "nhat truong pham"))

"""
Python does not encourage using immediately invoked lambda expressions. It simply results from a lambda expression being "CALLABLE" unlike the body of a normal function.
Lambda functions are frequently used with "HIGHER-ORDER FUNCTIONS", which take one mor more functions as arguments or return one or more functions. 
"""

high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))
print(high_ord_func(2, lambda x: x + 3))

# Unlike lambda forms in other languages, where they add functionality, Python lambdas are only a shorthand notation if you are too lazy to define a function.

# Stopped around 1/5 of the whole website