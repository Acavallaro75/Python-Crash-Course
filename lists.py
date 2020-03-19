# A List is a collection of data types which is ordered and changeable. Allows duplicate members. #

# Creating a List #
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Creating a List using a constructor #
moreNumbers = list((6, 7, 8, 9, 10))

print(numbers, moreNumbers)

# Indexing a List for a specific item in that List #
print(fruits[2])

# Get the length of a List #
print(len(fruits))

# Add to the end of a List #
fruits.append('Mangos')
print(fruits)

# Change the value of an item in a List #
fruits[0] = 'Blueberries'

# Remove an item from a List #
fruits.remove('Grapes')
print(fruits)

# Insert a new item into a List in a certain position #
fruits.insert(2, 'Strawberries')
print(fruits)

# Remove an item from a List from a certain position #
fruits.pop(2)
print(fruits)

# Reverse the items in a List #
fruits.reverse()
print(fruits)

# Sort a List alphabetically #
fruits.sort()
print(fruits)

# Sort a List alphabetically in reverse #
fruits.sort(reverse = True)
print(fruits)