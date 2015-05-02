# -----------------------------------------------------------
# lists the files in the current directory according to a certain
# pattern
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import required python standard modules
import fnmatch, os

# retrieve the files in the current directory
listOfFiles = os.listdir('.')

# define the filename pattern to look for
pattern = "*.py"

# define matches
matches = 0

# go through the list entry by entry
for entry in listOfFiles:
	if fnmatch.fnmatch(entry, pattern):
		# increase the number of matches
		matches += 1
		
		# output the filename
		print(entry)

# output the number of matches
print ("total matches: %i" % (matches))
