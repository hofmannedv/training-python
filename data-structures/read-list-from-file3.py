# -----------------------------------------------------------
# demonstrates how to read a list from a file using readlines
# a more Pythonic approach
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define empty list
places = []

# open file and read the content in a list
with open('listfile.txt', 'r') as filehandle:
	places = [currentPlace.rstrip() for currentPlace in filehandle.readlines()]

# output list of places
print (places)
