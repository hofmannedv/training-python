# -----------------------------------------------------------
# demonstrates square calculation following functional 
# programming paradigm
#o
# (C) 2024 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

def square(value):
    """Return the square of a number"""
    return value * value

# define a list of numbers
numbers = [1, 2, 3, 4]

# use a for loop, and a function to do the calculation
squared_numbers = []
for value in numbers:
    squared_numbers.append(square(value))

# output the result: [1, 4, 9, 16]
print("numbers:", numbers)
print("squared numbers:", list(squared_numbers)) 
