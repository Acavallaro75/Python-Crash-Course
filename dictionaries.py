'''
    - A Dictionary is a collection which is unordered, changeable, and indexed
    - Dictionaries allow no duplicate members
'''

# Creating a Dictionary #
person = {
    'firstName': 'Andrew',
    'lastName': 'Cavallaro',
    'age': 29
}

# Creating a Dictionary using a constructor #
anotherPerson = dict(firstName='AnnMarie', lastName='Medico', age=24)

# To get a value from a Dictionary #
print(person['firstName'])

# Getting a value from a Dictionary using the get() method #
print(person.get('lastName'))

# Adding a key to a Dictionary #
person['phone'] = '941-662-9984'

print(person.get('phone'))

# Get all of the keys in a Dictionary #
print(person.keys())

# Get all of the items in a Dictionary #
print(person.items())

# How to copy a Dictionary #
person2 = person.copy()

print(person2)

# Adding a key to a copy of a Dictionary #
person2['city'] = 'Port Charlotte'

print(person2.get('city'))

# Remove an item from a Dictionary #
del(person['age'])
person.pop('phone')

print(person)

# Clear the contents of a Dictionary #
person.clear()

print(person)

# Get the length of a Dictionary #
print(len(person2))

# Creating a List of Dictionaries #
people = [
    {'name': 'AnnMarie', 'age': 24},
    {'name': 'Joe', 'age': 80},
    {'name': 'Andrew', 'age': 29}
]

print(people[1]['name'])
