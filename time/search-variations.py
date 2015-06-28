# -----------------------------------------------------------
# time measurements: search in a list of numbers
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define python standard module
import time

def incrementalSearch(sortedNumberList, number):

	# verify the list elements one by one

	# define minimal element	
	minElement = 0

	# define maximum element
	maxElement = len(sortedNumberList)

	# start with minimal element
	currentElement = minElement

	while currentElement < maxElement:
		# did we find the element in the list?
		if sortedNumberList[currentElement] == number:
			# yes, return its position in the list
			print ("got %i at position %i" % (number, currentElement))
			return currentElement
		else:
			# no, continue searching
			print ("comparison of %i at position %i failed" % (number, currentElement))
			currentElement += 1

	# if not successfull, return -1
	print ("element %i not found" % number)
	return -1

def binarySearch(sortedNumberList, number):

	# use a binary search to look for the given number in that sorted
	# list (ascending)

	# define minimal element	
	minElement = 0

	# define maximum element
	maxElement = len(sortedNumberList)

	while True:
		# calculate middle element
		median = (maxElement + minElement) // 2
		print ("min:%i max:%i median:%i" % (minElement, maxElement, median))
	
		# did we finish?
		if minElement > maxElement:
			print ("element %i not found" % number)
			return (-1)

		# element found at median position
		if sortedNumberList[median] == number:
			print ("got %i at position %i" % (number, median))
			return (median)
		else:
			# continue searching
			if sortedNumberList[median] < number:
				# search in the right part of the list
				minElement = median + 1
			else:
				# search in the left part of the list
				maxElement = median - 1

# main program

# define the number to look for
number = 23

# define the list of numbers
sortedNumberList = (1, 5, 12, 17, 18, 19, 26, 32, 33, 36, 37, 47, 89)

# evaluate incremental search
startTime1 = time.time()
listPosition = incrementalSearch(sortedNumberList, number)
endTime1 = time.time()

# calculate and output interval time
seconds = endTime1 - startTime1
print ("incremental search took %.8f seconds" % seconds)

# evaluate binary search
startTime1 = time.time()
listPosition = binarySearch(sortedNumberList, number)
endTime1 = time.time()

# calculate and output interval time
seconds = endTime1 - startTime1
print ("binary search took %.8f seconds" % seconds)


