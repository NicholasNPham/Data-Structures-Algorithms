"""

As our program grows bigger, it may contain many lines of code. Instead of putting everything in a single file, we can use modules to separate codes in separate files as per their functionality. This makes our code organized and easier to maintain.

Module is a file that contains code to perform a specific task. A module may contain variables, functions, classes etc. Let's see an example,

"""

def add(a, b):
    result = a + b
    return result

# Import Standard Math Module
import math

# use math.pi to get value of pi
mathpi = math.pi
# print("The value of pi is", math.pi) # prints The value of pi is 3.141592653589793

import math as m
pi = m.pi
# print(pi) # prints 3.141592653589793

# Python from...import statement

# import only pi from math module
from math import pi
pi = pi
# print(pi) #prints 3.141592653589793

# Import all names

# import all names from the standard module math
from math import *
pi = pi
# print("The value of pi is", pi) # prints The value of pi is 3.141592653589793

