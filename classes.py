'''
    - A class is like a blueprint for creating objects
    - An object has properties and methods(functions) associated with it
    - Almost everything in Python is an object
'''


# Creating a class #
class User:
    # Constructor #
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} years old'

    def has_birthday(self):
        self.age += 1


# Inheritance #
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} years old and my balance is {self.balance}'


# Creating a User Object #
andrew = User('Andrew Cavallaro', 'andrew.cavallarojr@gmail.com', 29)

# Accessing the properties of the Object #
andrew.has_birthday()

print(andrew.name, andrew.email, andrew.age)

# Accessing the functions inside of the class #
print(andrew.greeting())

# Initializing a Customer Object #
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

# Accessing the functions inside of the Customer class #
janet.setBalance(500)

print(janet.greeting())
