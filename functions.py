"""
    - A function is a block of code which only runs when it is called
    - In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces
"""


# Creating a function #
def say_hello(name='Sam'):
    print(f'Hello {name}')


say_hello('Andrew')


# Return values from a function #
def get_sum(x, y):
    total = x + y
    return total


answer = get_sum(5, 7)
print(answer)
