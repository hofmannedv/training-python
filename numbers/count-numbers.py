# -----------------------------------------------------------
# demonstrates how to count numbers in a list
#o
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

def isNumber(value):
	# set default value: not a number (False)
	aNumber = False

	# follow the principle: "it is easier to ask forgiveness than
	# permission" as recommended here:
	# http://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not
	try:
		value += 1
		aNumber = True
	except TypeError:
		aNumber = False

	return aNumber

# list of numbers
numbersList = [394, "6", 15.5, 2, "orange", 153]
numbers = 0
print (numbersList)

# iterate through the list
for item in numbersList:
	if isNumber(item):
		print (item, "is a number")
		numbers += 1
	else:
		print (item, "is not a number")

# print the # of numbers
print (("The list contains %i numbers") % (numbers))
