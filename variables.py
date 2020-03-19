# A variable is a container for a value, which can be of various types #

'''
This is a multiline comment or docstring (used to define a functions purpose)
They can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# Singular Assignment #
x = 1             # int
y = 2.5           # double
name = 'Andrew'   # String
is_cool = True    # Boolean

# Multiple Assignment #
a, b, NAME, IS_COOL = (1, 2.5, 'Andrew', True)

# Basic Math #
z = x + 5         # addition
z = 5 - x         # subtraction
z = x * 5         # multiplication
z = 5 / x         # division
z = 5 % 5         # remainder

# Check the type of variable #
print(type(x), x)
print(type(y), y)


# Type Casting #
x = str(x)
y = int(y)

print(type(x), x)
print(type(y), y)