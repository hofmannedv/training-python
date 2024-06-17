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

# transform list into an iterator
numbersIT = iter(numbers)

# loop though the items one after the next
while True:
    try:
        value = next(numbersIT)
        square = value * value
        print("the square of number", value, "is", square)
    except StopIteration:
        print("end if iterator reached")
        break

