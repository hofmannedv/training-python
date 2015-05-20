# -----------------------------------------------------------
# demonstrates the usage of a for loop to interate through a list
#o
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define list
shoppingCart = ["banana", "apple", "grapefruit"]

# output list content
# - without index
for item in shoppingCart:
	print (item)

# print empty line for decoration
print ()

# - using an index
# get the number of list items
listItems = len(shoppingCart)
for itemIndex in range(listItems):
	print (itemIndex, shoppingCart[itemIndex])

print ("----------------")
print ("total:", listItems, "items")

