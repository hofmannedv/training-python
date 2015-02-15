# -----------------------------------------------------------
# demonstrates how to use a function name as parameter
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define a square function
def square(operand):
	return operand * operand

# define a function calculation x^3
def three(operand):
	return operand * operand * operand

# output function
def output(lowerBound, upperBound, step, functionName):
	for x in range(lowerBound, upperBound, step):
		# output the value, and the according function value
		print("%i: %i" % (x, functionName(x)))

	print()

	return

# main program
# use function name as 4th parameter
output(2,11,2,square)		# use square function
output(2,11,2,three)		# use three function

