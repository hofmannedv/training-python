# -----------------------------------------------------------
# demonstrates how to use the filter function
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define a function that returns True based on a condition
def test(operand):
	# default return value: False
	returnValue = False

	# test condition
	if (operand > 3):
		returnValue = True

	# return the result of the test
	return returnValue

# define list of values that will be tested
valueList = [1, 4, -5, 6]

# evaluate the values
z = filter(test, valueList)

# output the basic value list
print(valueList)

# output all the values that match the condition in test()
for element in z:
	print(element)

