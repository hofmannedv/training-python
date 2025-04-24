# -----------------------------------------------------------
# demonstrates how to read a list from a file
#o
# (C) 2018-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define empty list
places = []

# open file and read the content in a list
with open('listfile.txt', 'r') as filehandle:
	for line in filehandle:
		# remove linebreak which is the last character of the string
		currentPlace = line[:-1]
		
		# add item to the list
		places.append(currentPlace)

# output list of places
print (places)
