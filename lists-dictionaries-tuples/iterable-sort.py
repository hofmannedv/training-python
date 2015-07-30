# -----------------------------------------------------------
# demonstrates how to sort a dictionary by keys with the help of
# iterators
#
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define a generator function
def sortedDictGenerator(dictionary):

	# retrieve the keys
	dictionaryKeys = dictionary.keys()

	# sort the keys in place
	dictionaryKeys.sort()

	# return the current key as an iterator
	for currentKey in dictionaryKeys:
		# return a single element, only
		yield currentKey

# define a dictionary of capitals
capitals = {
	"Norway": "Oslo",
	"Germany": "Berlin",
	"France": "Paris"
}
print("original list (unsorted):", capitals)

# output list by keys in sorted order
print("list sorted by keys:")

for currentKey in sortedDictGenerator(capitals):
	print("%s: %s" % (currentKey, capitals[currentKey]))

