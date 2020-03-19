'''
    - JSON is commonly used with data API'S
    - Here how we can parse JSON into a Python Dictionary
'''

# Import the JSON core module #
import json

# Sample JSON #
userJSON = '{"firstName": "Andrew", "lastName": "Cavallaro", "age": 29}'

# Parse JSON to Python Dictionary #
user = json.loads(userJSON)

print(user)
print(user['firstName'])

# Creating a Dictionary #
car = {'make': 'Ford', 'model': 'Mustang', 'year': 2020}

# Parsing Python Dictionary into JSON #
carJSON = json.dumps(car)

print(carJSON)
