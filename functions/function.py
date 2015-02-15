# -----------------------------------------------------------
# demonstrates how to write and call a function, basically
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# a simple function without parameters
def functionOne():
	print("in functionOne.")

	# define a boolean value as a return value
	return True

# another function with a parameter
def functionTwo(parameter):
	print("in functionTwo")
	print("parameter has this value:", parameter)

	# define a single return value
	return 7

# main program
# - calling functionOne without parameters
returnValue1 = functionOne()
print("return value:", returnValue1)
print()

# - calling functionTwo with a parameter 1
returnValue2 = functionTwo(1)
print("return value:", returnValue2)

