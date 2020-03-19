# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Creating a function #
def sayHello(name = 'Sam'):
    print(f'Hello {name}')

sayHello('Andrew')

# Return values from a function #
def getSum(x, y):
    total = x + y
    return total

answer = getSum(5, 7)
print(answer)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

