# Conditionals
# This script explains how to use conditional statements in Python.

# Example of an 'if' statement
age = 10
if age > 5:
    print("You are older than 5 years.")  # This will output if the condition is True

# You can use 'elif' (else if) and 'else' to test multiple conditions
if age > 15:
    print("You are older than 15 years.")
elif age > 10:
    print("You are older than 10 years but not older than 15.")
else:
    print("You are 10 years old or younger.")

# Another example with a different age
age = 12
if age > 15:
    print("You are older than 15 years.")
elif age > 10:
    print("You are older than 10 years but not older than 15.")
else:
    print("You are 10 years old or younger.")

# Combining conditions using 'and' and 'or'
if age >= 10 and age <= 15:
    print("You are between 10 and 15 years old.")
if age < 10 or age > 15:
    print("You are either younger than 10 or older than 15.")
