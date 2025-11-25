# Define a list

my_list = [4, 7, 0]

# Create an iterator from the list
iterator = iter(my_list)
# Get the first element of the iterator
# print(next(iterator)) # prints 4
# Get the second element of the iterator
# print(next(iterator))
# Get the third element of the iterator
# print(next(iterator))

# Output: 4 7 0

# Using a for loop

# define a list
my_list = [4, 7, 0]

for element in my_list:
    # print(element) # prints 4, 7, 0
    pass

# Working of for loop for iterators
# Create a list of integers
my_list = [1, 2, 3, 4, 5]
# Create an iterator from the list
iterators = iter(my_list)
# iterate through the elements of the iterator
for element in iterators:
    # print each element
    # print(element)
    pass

# Building Custom Iterators
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
# print(next(i)) # prints 1
# print(next(i)) # prints 2
# print(next(i)) # prints 4
# print(next(i)) # prints 8
# print(next(i)) # raises StopIteration exception

for i in PowTwo(3):
    # print(i)
    pass

# Python Infinite Iterators

from itertools import count
# Create an infinite iterator that starts at 1 and increments by 1 each time
infinite_iterator = count(1)
# print the 5 elements of the infinite iterator
for i in range(5):
    # print(next(infinite_iterator))
    pass # prints 1, 2, 3, 4, 5