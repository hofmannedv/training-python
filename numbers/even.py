# -----------------------------------------------------------
# demonstrates how to figure out even, and odd numbers
#o
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

def isEven(number):
	# set default value: not even (False)
	even = False

	# test for a zero remainder
	if number % 2 == 0:
		even = True

	return even

# list of numbers
numbers = [394, 6, 15, 2, 88, 153]

# iterate through the list
for item in numbers:
	if isEven(item):
		print (item, "is even")
	else:
		print (item, "is odd")
