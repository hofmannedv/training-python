# -----------------------------------------------------------
# demonstrates how to write and call a function returning a tuple
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# a function with two parameters
def functionTuple(operand1, operand2):
	print("in functionTuple.")
	print("parameters: %i, %i" % (operand1, operand2))

	# define a tuple as a return value
	return (operand1 + 1, operand2 + 2)

# main program
returnValue = functionTuple(1,5)
print("return value:", returnValue)

