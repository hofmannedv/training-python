# -----------------------------------------------------------
# demonstrates how to write and call a function returning a tuple
#o
# (C) 2015-2025 Frank Hofmann, Berlin/Freiburg, Germany
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# a function with two parameters
def functionTuple(operand1, operand2):
	print("in functionTuple.")
	print("parameters: %i, %i" % (operand1, operand2))

	# define a tuple as a return value
	return (operand1 + 1, operand2 + 2)

# main program
returnValue = functionTuple(1,5)

# output result
print("return value:", returnValue)

