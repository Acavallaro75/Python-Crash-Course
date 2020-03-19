# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string) #
people = ['John', 'Paul', 'Sarah', 'Susan']

# Simple for loop #
for person in people:
    print(f'Current person: {person}')

# Breaking out of a loop #
for person in people:
    if person == 'Sarah':
        break
    print(f'Current person: {person}')

# Continuing through a loop #
for person in people:
    if person == 'Sarah':
        continue
    print(f'Current person: {person}')

# Loop over a range #
for i in range(len(people)):
    print(people[i])

# Loop over a custom range #
for i in range(0, 10):
    print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true #
count = 0

# Simple while loop #
while count <= 10:
    print(f'Count: {count}')
    count += 1
