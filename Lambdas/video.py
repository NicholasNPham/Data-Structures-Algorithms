"""
Lambda
- A Lambda function is functionally the same as a regular function in Python
- Also known as an 'anonymous functions'
    - Meaning that they are not bound to an identifier

- Whats the point then?
    - They are made to be passed into a higher-order function
        - Higher Order Function:
            - A function that can either take in another function as an input or return a function as an output or both.
"""

def add(x, y):
    return x + y
print(add(4,5)) # prints 9

# Two cases
add2 = lambda x, y: x+y # Might as well use a function
lambda x, y: x+y

print(add2(4,5)) # prints 9
print((lambda x, y: x+y)(4,5)) # prints 9

def my_map(myFunc, myIter):
    result = []
    for item in myIter:
        newItem = myFunc(item) # The lambda function is the myFunc function that cubed the item which is each num in list
        result.append(newItem)
    return result


nums = [3, 4, 5, 6, 7] # nums is the iterable list

cubed = my_map(lambda x: x**3, nums) # the myFunc is the lambda function in one line

print(cubed) # prints [27, 64, 125, 216, 343]




