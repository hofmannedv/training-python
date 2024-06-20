# -----------------------------------------------------------
# demonstrates square calculation following functional 
# programming paradigm
#o
# (C) 2024 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define a single value
number = 4

# define an anonymous lambda function to do the calculation
square = lambda x: x**2

# output the result: 16
print("the square of", number, "is", int(square(number)))
