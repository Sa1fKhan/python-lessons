# Functions
# This script explains how to define and use functions in Python.

# Defining a function
def greet(name):
    """
    This function takes a name as input and prints a greeting.
    """
    print("Hello, " + name + "!")

# Calling a function
greet("Alice")  # This will output: Hello, Alice!
greet("Bob")  # This will output: Hello, Bob!

# Functions can also return values
def add(a, b):
    """
    This function takes two numbers as input and returns their sum.
    """
    return a + b

# Using the return value of a function
result = add(3, 5)
print(result)  # This will output: 8

# Another example of a function that returns a value
def multiply(x, y):
    """
    This function takes two numbers as input and returns their product.
    """
    return x * y

# Using the return value of the multiply function
product = multiply(4, 6)
print(product)  # This will output: 24
