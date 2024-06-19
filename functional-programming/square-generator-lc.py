# -----------------------------------------------------------
# demonstrates square calculation following functional 
# programming paradigm
#o
# (C) 2024 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define a list of numbers
numbers = [1, 2, 3, 4]

# create the generator object
squares_generator = (value * value for value in numbers)

# iterate over the generator and print the values
for value in squares_generator:
    print(value)

