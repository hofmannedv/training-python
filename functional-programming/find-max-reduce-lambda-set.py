# -----------------------------------------------------------
# demonstrates finding the maximum value following functional 
# programming paradigm using a set instead of a list
#o
# (C) 2024 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import reduce from the functools module
from functools import reduce

# define a list of numbers
numbers = (1, 3, 5, 6, 2)

# define a lambda function to compare two numbers
compare_numbers = lambda a, b: a if a > b else b

# apply reduce () to numbers
print("The maximum element of the set is", reduce(compare_numbers, numbers))
