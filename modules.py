'''
    - A module is basically a file containing a set of functions to include in your application
    - There are core Python modules, modules you can install using the pip package manager (including Django)
'''

# Import a core Python module #
import datetime
from datetime import date

# Import a core Python module #
import time
from time import time

# Import a pip module #
import camelcase
from camelcase import CamelCase

# Import a custom module such as the one in the validator.py file #
import validator
from validator import validate_email

# Using the imported core module #
today = datetime.date.today()

print(today)

# Using the imported part of the core module #
now = date.today()
timestamp = time()

print(now)
print(timestamp)

# Using the imported pip module #
test = CamelCase()

print(test.hump('hello there world'))

# Using the imported custom module #
email = 'test@test.com'

if validate_email(email):
    print(f'{email} is a valid email')
else:
    print(f'{email} is not a valid email')
