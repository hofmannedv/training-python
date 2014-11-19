# -----------------------------------------------------------
# demonstrates the usage of a for loop to interate through a list
# and printing the uneven elements, only
#o
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define list
shoppingCart = ["banana", "apple", "grapefruit", "carrot", "potato"]

# get the number of list items
listItems = range(len(shoppingCart))
printedItems = 0
for itemIndex in listItems:
	if itemIndex % 2 == 1:
		print (itemIndex, shoppingCart[itemIndex])
		printedItems += 1

print ("----------------")
print ("total:", printedItems, "items")
print ()

