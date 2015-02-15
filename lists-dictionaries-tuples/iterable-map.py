# -----------------------------------------------------------
# demonstrates how to use the map function
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

def powerValue(operand):
	return operand * operand

# define a list of operands
operandList = [2.0, 4.0, 2.5]

# call powerValue for each item from operand list
results = map(powerValue, operandList)

# output result
for i in results:
	print(i)
