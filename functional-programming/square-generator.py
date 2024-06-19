# -----------------------------------------------------------
# demonstrates square calculation following functional 
# programming paradigm
#o
# (C) 2024 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

def square(valueList):
    """Return the square of a number"""

    for value in valueList:
        yield value * value

# define a list of numbers
numbers = [1, 2, 3, 4]

for value in square(numbers):
    print(value)

