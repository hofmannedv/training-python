# -----------------------------------------------------------
# calculate the minimum, and the maximum value for a list of integers
#o
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define a list of values
valueList = [1, 6, 3, 4, 5]

# list length
items = len(valueList)

# check for empty lists, first
if items:
	minimumValue = min(valueList)
	maximumValue = max(valueList)

	# output average value
	print ("The minimum value is:", minimumValue)
	print ("The maximum value is:", maximumValue)
else:
	print ("The list is empty.")

