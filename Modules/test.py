import main

main.add(1, 2) # prints 3

# The dir() built-in function
# print(dir(main)) # this prints all the function names in the "main" module

print(main.__name__) # prints main

a = 1
b = "hello"

import math

print(dir()) # prints ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'main', 'math']

