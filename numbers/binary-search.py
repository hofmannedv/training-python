# -----------------------------------------------------------
# demonstrates a binary search in a list of numbers
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

number = 23
sortedNumberList = [1, 5, 12, 17, 18, 19, 26, 32, 33, 36, 37, 47, 89]

minElement = 0
maxElement = len(sortedNumberList)

while True:
	median = (maxElement + minElement) // 2
	print ("min:%i max:%i median:%i" % (minElement, maxElement, median))
	if minElement > maxElement:
		print ("element %i not found" % number)
		break
	if sortedNumberList[median] == number:
		print ("got %i at position %i" % (number, median))
		break
	else:
		if sortedNumberList[median] < number:
			minElement = median + 1
		else:
			maxElement = median - 1
