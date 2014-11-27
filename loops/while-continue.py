# -----------------------------------------------------------
# demonstrates the usage of continue to skip the execution of 
# statements in a loop
#o
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define list
shoppingCart = ["banana", "apple", "grapefruit", "strawberry", "orange"]

# output list content
print (shoppingCart)

# simple version with index
# initiate index
itemIndex = 0

# use an endless loop
while itemIndex < len(shoppingCart):
	# print even elements, only, and skip the odd ones
	if itemIndex % 2 == 1:
		# skip
		# increment itemIndex
		itemIndex += 1
		continue
	else:
		print (itemIndex, shoppingCart[itemIndex])
		# increment itemIndex
		itemIndex += 1

