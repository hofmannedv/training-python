# -----------------------------------------------------------
# demonstrates how to allocate memory blocks
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# use the additional numpy module
import numpy as np

# define the memory block size, and the number of elements
memoryBlockSize = 16384
numberOfElements = 10000

# the list of blocks is empty
memoryList = []

# start with the first block
currentBlock = 1

while currentBlock <= numberOfElements:
	# create a block of zeros
	memoryBlock = np.zeros(memoryBlockSize)
	memoryList.append(memoryBlock)
	
	# output the allocated memory
	print ("allocated %i bytes" % (currentBlock * memoryBlockSize))
	currentBlock += 1
