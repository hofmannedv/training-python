# -----------------------------------------------------------
# compares the creation of sorted lists using the python 
# bisect module, and the "usual" way
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import standard modules
import bisect, random, time

def sortListDefault():
	# define empty list, and fill with 200000 randomized integers
	sortedNumbers = []
	for element in range(200000):
		# choose a number between 0 and 1000
		newNumber = random.randint(0, 1000)
		
		# add number to list
		#print ("adding %i to list ... " %newNumber)
		sortedNumbers.append(newNumber)

	# sort the list in-place
	sortedNumbers.sort()

	return

def sortListBisect():
	# define empty list, and fill with 200000 randomized integers
	sortedNumbers = []
	for element in range(200000):
		# choose a number between 0 and 1000
		newNumber = random.randint(0, 1000)
		#print ("adding %i to list ... " %newNumber)
	
		# insert into sorted list
		bisect.insort(sortedNumbers, newNumber)

	return

# evaluate default sort
startTime1 = time.time()
listPosition = sortListDefault()
endTime1 = time.time()

# calculate and output interval time
seconds = endTime1 - startTime1
print ("default sort took %.8f seconds" % seconds)

# evaluate bisect sort
startTime1 = time.time()
listPosition = sortListBisect()
endTime1 = time.time()

# calculate and output interval time
seconds = endTime1 - startTime1
print ("bisect sort took %.8f seconds" % seconds)


