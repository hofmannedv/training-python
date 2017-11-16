# -----------------------------------------------------------
# demonstrates the usage of a while loop with else condition
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
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
while itemIndex < len(shoppingCart):
	print (itemIndex, shoppingCart[itemIndex])
	# increment itemIndex
	itemIndex += 1
else:
	print ("reached end of list")
