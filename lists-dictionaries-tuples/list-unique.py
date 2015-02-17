# -----------------------------------------------------------
# shows how to get an unique list
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# ideas are taken from Peter Bengtsson's blog:
# Fastest way to uniqify a list in Python
# http://www.peterbe.com/plog/uniqifiers-benchmark

def uniqueNotOrderPreserving(itemList):
	# get an unique list without preserving the item order

	# initiate an empty dictionary
	itemKeys = {}

	# step through the list elements one after the other
	for element in itemList:
		itemKeys[element] = True

	# extract the dictionary keys
	uniqueList = itemKeys.keys()
	return uniqueList

def uniqueOrderPreserving(itemList):
	# get an unique list preserving the item order
	
	# define result
	seen = set()
	
	result = [x for x in itemList if x not in seen and not seen.add(x)]
	return result

# define a list
numbers = [12, 67, 3, 45, 12, 7, 3]
print (numbers)

# unique list
unique1 = uniqueNotOrderPreserving(numbers)
unique2 = uniqueOrderPreserving(numbers)

print("unique but not order preserving:", unique1)
print("unique but order preserving:", unique2)
