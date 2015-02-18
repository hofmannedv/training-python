# -----------------------------------------------------------
# demonstrates the usage of pass statement in a while loop
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define list
deviceNumbers = [1, 4, 1, 29]

# output list content
print (deviceNumbers)

# simple version with index
# initiate index
itemIndex = 0

# use a while loop
while itemIndex < len(deviceNumbers):
	# retrieve current list item
	currentDeviceNumber = deviceNumbers[itemIndex]

	if currentDeviceNumber == 1:
		print("discovered value 1 at position %i" % (itemIndex))
	else:
		# nothing happens otherwise, so far
		pass

	# increase itemIndex
	itemIndex += 1
