# -----------------------------------------------------------
# demonstrates how to find the largest value in a list of integers
#o
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# list of numbers
numbers = [394, 6, 15, 2, 88, 153]

# preset the maximum number
largestValue = numbers[0]

# iterate through the list
for item in numbers:
	if item > largestValue:
		largestValue = item

# output result
print ("the largest number in", numbers, "is", largestValue)

# as an alternative you may use the max method
largestValue = max(numbers)

# output result
print ("the largest number in", numbers, "is", largestValue)
