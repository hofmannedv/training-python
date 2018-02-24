# -----------------------------------------------------------
# read file content (multiple lines)
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# following the discussion here:
# https://stackoverflow.com/questions/5832856/how-to-read-file-n-lines-at-a-time-in-python
# -----------------------------------------------------------

from itertools import islice

# define the name of the file to read from
filename = "test.txt"

# define the number of lines to read
numberOfLines = 5

with open(filename, 'r') as inputFile:
	linesCache = islice(inputFile, numberOfLines)
	
	for currentLine in linesCache:
		print (currentLine)

