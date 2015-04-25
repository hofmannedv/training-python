# -----------------------------------------------------------
# demonstrates how to use the map function
#
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define a simple function 
def powerValue(operand):
	return operand * operand

# define a list of operands
operandList1 = [2.0, 4.0, 2.5]
operandList2 = (1.0, 2.0, 3.5)

# output result
for currentList in (operandList1, operandList2):

	# start with first element at position #0
	currentPosition = 0

	# call powerValue for each item from operand list
	results = map(powerValue, currentList)

	# output results
	for i in results:
		# output a float value with 2 digits
		print("%5.2f:%6.2f" % (currentList[currentPosition],i))

		# increase current position
		currentPosition += 1
