# -----------------------------------------------------------
# demonstrates the usage of break to exit a while loop
#o
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define list
shoppingCart = ["banana", "apple", "grapefruit"]

# output list content
#
# simple version with index
# initiate index
itemIndex = 0

# use an endless loop
while True:
	# test itemIndex, first
	if itemIndex >= len(shoppingCart):
		# we have reached the end of the list, so exit the loop
		break
    # otherwise ...
	print (itemIndex, shoppingCart[itemIndex])
	# increment itemIndex
	itemIndex += 1

