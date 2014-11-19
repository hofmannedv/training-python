# -----------------------------------------------------------
# demonstrates the usage of a for loop to interate through a list
# using a range
#o
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define list
shoppingCart = ["banana", "apple", "grapefruit", "carrot", "potato"]

# define list boundaries
lowerBound = 2
upperBound = 4

print ("lower bound:", lowerBound)
print ("upper bound:", upperBound)
print ()

# get the number of list items
listRange = range(lowerBound, upperBound + 1)
listItems = len(listRange)
for itemIndex in listRange:
	print (itemIndex, shoppingCart[itemIndex])

print ("----------------")
print ("total:", listItems, "items")
print ()

# use an additional step value
step = 2

listRange = range(lowerBound, upperBound + 1, step)
listItems = len(listRange)
for itemIndex in listRange:
	print (itemIndex, shoppingCart[itemIndex])

print ("----------------")
print ("total:", listItems, "items")


