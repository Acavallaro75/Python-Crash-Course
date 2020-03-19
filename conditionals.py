# If/ Else conditions are used to decide to do something based on something being true or false #
x = 10
y = 50

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if statement #
if x > y:
    print(f'{x} is greater than {y}')

# Simple if-else statement #
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

# Simple else-if statement #
if x > y:
    print(f'{x} is greater than {y}')
elif y == x:
    print(f'{x} equals {y}')
else:
    print(f'{y} is greater than {x}')

# Nested if statements #
if y > x:
    if y == 50:
        if x == 10:
            print('Nested if statements')

# Logical operators (and, or, not) - Used to combine conditional statements

# Simple and statement #
if y > x and y == 50 and x == 10:
    print("Replace the nested if statements")

# Simple or statement #
if y > x or y == 40:
    print(
        f'y is not equal to 40, but this still works because {y} is greater than {x}')

# Simple not statement #
if not(x == y):
    print(f'{x} is not equal to {y}')

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
