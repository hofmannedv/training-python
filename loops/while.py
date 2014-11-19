# -----------------------------------------------------------
# demonstrates the usage of a while loop to interate through a list
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

while itemIndex < len(shoppingCart):
	print (itemIndex, shoppingCart[itemIndex])
	# increment itemIndex
	itemIndex += 1

