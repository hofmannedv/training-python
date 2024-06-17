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

# use map(), and a function to do the calculation
squared_numbers = map(square, numbers)

# output the result: [1, 4, 9, 16]
print("numbers:", numbers)
print("squared numbers:", list(squared_numbers)) 
