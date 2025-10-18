# identity() takes an argument x and returns it upon invocation.
def identity(x):
    return x
# The same thing above but in one line. [keyword] [a bound variable]: [a body]
lambda x: x

lambda x: x + 1
# print((lambda x: x + 1)(2)) # prints 3

add_one = lambda x: x + 1
# print(add_one(2)) # prints 3

# the lambda function in a normal function:
def add_one(x):
    return x + 1

full_name = lambda first, last: f'Full Name: {first.title()} {last.title()}'
# print(full_name("nicholas", "nhat truong pham"))

"""
Python does not encourage using immediately invoked lambda expressions. It simply results from a lambda expression being "CALLABLE" unlike the body of a normal function.
Lambda functions are frequently used with "HIGHER-ORDER FUNCTIONS", which take one mor more functions as arguments or return one or more functions. 
"""

high_ord_func = lambda x, func: x + func(x)
# print(high_ord_func(2, lambda x: x * x))
# print(high_ord_func(2, lambda x: x + 3))

# Unlike lambda forms in other languages, where they add functionality, Python lambdas are only a shorthand notation if you are too lazy to define a function.

import dis
add = lambda x, y: x + y

# div_zero = lambda x: x // 0
"""
div_zero = lambda x: x // 0
                     ~~^^~~
ZeroDivisionError: integer division or modulo by zero
"""

odd_or_even = lambda x: x % 2 and 'odd' or 'even'

# Decorators

def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(*args)
    return wraps

@some_decorator # This is the decorator that calls the function above.
def decorated_function(x):
    print(f"With argument '{x}'")

# decorated_function("Python")
"""
Calling function 'decorated_function'
With argument 'Python'
"""

# Defining a decorator
def trace(f):
    def wrap(*arg, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {arg}, kwargs: {kwargs}")
        return f(*arg, **kwargs)

    return wrap

# Applying decorator to function
@trace
def add_two(x):
    return x + 2

# calling the decorated function
# add_two(3)

# Applying decorator to a lambda
# print((trace(lambda x: x ** 2))(3))

# print(list(map(trace(lambda x: x*2), range(3))))

def outer_func(x):
    y = 4
    return lambda z: x + y + z

for i in range(3):
    closure = outer_func(i)
    # print(f"closure({i+5}) = {closure(i+5)}")
    """
    closure(5) = 9
    closure(6) = 11
    closure(7) = 13
    """

def wrap(n):
    def f():
        print(n)
    return f

numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(wrap(n)) # appends the strings and also calls wrap function

# for f in funcs:
#     f()
"""
one
two
three
"""

# Learning unittest

"""
import unittest

addtwo = lambda x: x + 2
class LambdaTest(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(add_two(2), 4)

    def test_add_two_point_two(self):
        self.assertEqual(add_two(2.2), 4.2)

    def test_add_three(self):
        self.assertEqual(add_two(3), 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)
"""

