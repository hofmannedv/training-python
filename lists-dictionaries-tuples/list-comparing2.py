# -----------------------------------------------------------
# demonstrates how to compare lists element by element
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# works for all Python releases 
#
# ideas taken from: 
# http://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches

def compareLists1(list1, list2):
	# binary comparison
	result = set(list1) & set(list2)
	return result

def compareLists2(list1, list2):
	# set intersection
	result = set(list1).intersection(list2)
	return result

# define three lists
numbers1 = [23, 61, 82]
numbers2 = [1, 155, 17]
numbers3 = [61, 23, 82]
numbers4 = [23, 61, 82]

# output dictionary content (key-value-pairs)
print (numbers1)
print (numbers2)
print (numbers3)
print (numbers4)

# compare the lists
# list 1 and 2 (returns an empty set)
print(compareLists1(numbers1, numbers2))
print(compareLists2(numbers1, numbers2))

# list 1 and 3 (returns a set with three elements)
print(compareLists1(numbers1, numbers3))
print(compareLists2(numbers1, numbers3))

