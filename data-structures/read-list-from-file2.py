# -----------------------------------------------------------
# demonstrates how to read a list from a file using readlines
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define empty list
places = []

# open file and read the content in a list
with open('listfile.txt', 'r') as filehandle:
	filecontents = filehandle.readlines()

	for line in filecontents:
		# remove linebreak which is the last character of the string
		currentPlace = line[:-1]
		
		# add item to the list
		places.append(currentPlace)

# output list of places
print (places)
