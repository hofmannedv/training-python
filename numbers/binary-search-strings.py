# -----------------------------------------------------------
# demonstrates a binary search in a list of strings
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

name = "Reto"
sortedNamesList = ["Anna", "Berta", "Claus", "Felix", "Reto", "Urs", "Zoe"]

minElement = 0
maxElement = len(sortedNamesList)

while True:
	median = (maxElement + minElement) // 2
	print ("min:%i max:%i median:%i" % (minElement, maxElement, median))
	if minElement > maxElement:
		print ("element %s not found" % name)
		break
	if sortedNamesList[median] == name:
		print ("got %s at position %i" % (name, median))
		break
	else:
		if sortedNamesList[median] < name:
			minElement = median + 1
		else:
			maxElement = median - 1
