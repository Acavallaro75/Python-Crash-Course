# Python has functions for creating, reading, updating, and deleting files #

# Open a file #
myFile = open('test.txt', 'w')

# Get information about the file #
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Writing to a file #
myFile.write('I love Python')
myFile.write(' and JavaScript.')
myFile.close

# Append to a file #
myFile = open('test.txt', 'a')
myFile.write(' I also like Java.')
myFile.close

# Reading from a file #
myFile = open('test.txt', 'r+')
text = myFile.read(100)
print(text)
