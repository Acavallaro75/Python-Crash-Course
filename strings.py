# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods #

letter = 'd'
name = 'Andrew Cavallaro'
age = 29

# Concatenation #
print('Hello, my name is ' + name + ' and I am ' + str(age) + ' years old.')

# String Formatting #

# Positional Arguments #
print('Hello, my name is {name} and I am {age} years old.'.format(
    name=name, age=age))

# F-Strings
print(f'Hello, my name is {name} and I am {age} years old.')

# String Methods #

# Capitalize the first letter of a String #
print(name.capitalize())

# Make all characters in a String uppercase #
print(name.upper())

# Make all characters in a String lowercase #
print(name.lower())

# Make lowercase characters uppercase and uppercase characters lowercase in a String #
print(name.swapcase())

# Get the number of characters in a String #
print(len(name))

# Replace characters in a String with new characters #
print(name.replace('drew', 'nMarie'))

# Count the number of occurrences of a character in a String #
print(name.count(letter))

# Check if a String starts with a certain character or set of characters #
print(name.startswith('And'))

# Check if a String ends with a certain character or set of characters #
print(name.endswith('ew'))

# Split the String and turn it into a list of Strings or an array of characters #
print(name.split())

# Find the index of a character in a String #
print(name.find('r'))

# Checks if a String is all alphanumeric #
print(name.isalnum())

# Checks if a String is all alphabetical #
print(name.isalpha())

# Checks if a String is all numerical #
print(name.isnumeric())
