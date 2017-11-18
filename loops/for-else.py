# -----------------------------------------------------------
# demonstrates the usage of a for loop with else condition
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define list
shoppingCart = ["banana", "apple", "grapefruit"]

# output list content

# use an endless loop
itemsRange = range(len(shoppingCart))
for itemIndex in itemsRange:
	print (itemIndex, shoppingCart[itemIndex])
	# increment itemIndex
else:
	print ("reached end of list")
