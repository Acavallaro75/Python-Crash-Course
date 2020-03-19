''' 
    - A Tuple is a collection which is ordered and unchangeable
    - Tuples allow for duplicate members
'''

# Creating a Tuple #
numbers = (1, 2, 3, 4, 5)
fruits = ('Apples', 'Oranges', 'Grapes')

# Creating a Tuple using a constructor #
moreNumbers = tuple((6, 7, 8, 9, 10))

# Tuples with one value #
evenMoreNumbers = (11,)

print(numbers, moreNumbers, type(evenMoreNumbers))

# To get a value from a Tuple #
print(fruits[1])

# How to delete a Tuple #
del(evenMoreNumbers)

# Get the length of a Tuple #
print(len(fruits))


'''
    - A Set is a collection which is unordered and un-indexed
    - No duplicate members are allowed in a Set
'''

# Creating a Set #
vegetables = {'Carrots', 'Broccoli', 'Cauliflower'}

# Checking if an item is in a Set #
print('Carrots' in vegetables)

# Add an item to a Set #
vegetables.add('Peas')

print(vegetables)

# Remove an item from a Set #
vegetables.remove('Peas')

print(vegetables)

# Clear an entire Set #
vegetables.clear()

print(vegetables)

# Delete an entire Set #
del vegetables
