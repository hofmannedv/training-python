# -----------------------------------------------------------
# measure the time to find the largest value in a list of integers
#o
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import required time module
import time

def findMaxIterative(numbers):

	# preset the possible maximum number
	largestValue = numbers[0]

	# iterate through the list
	for item in numbers:
		if item > largestValue:
			largestValue = item

	return largestValue

def findMaxInternal(numbers):

	# as an alternative you may use the max method
	largestValue = max(numbers)

	return largestValue

# list of numbers
numbers = (394, 6, 15, 2, 88, 153, 12, 65, 1055, 4, 23, 45)

# define number of iterations
iterations = 5000000

# evaluate iterative search
startTime1 = time.time()
for i in range(iterations):
	largestValue = findMaxIterative(numbers)
endTime1 = time.time()

# calculate and output interval time
seconds = endTime1 - startTime1
print ("iterative search took %.2f seconds" % seconds)

# evaluate internal search
startTime1 = time.time()
for i in range(iterations):
	largestValue = findMaxInternal(numbers)
endTime1 = time.time()

# calculate and output interval time
seconds = endTime1 - startTime1
print ("internal search took %.2f seconds" % seconds)
