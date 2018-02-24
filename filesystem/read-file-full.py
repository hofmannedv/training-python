# -----------------------------------------------------------
# read entire file content
#
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define the name of the file to read from
filename = "test.txt"

with open(filename, 'r') as filehandle:
	filecontent = filehandle.read()
	print (filecontent)
