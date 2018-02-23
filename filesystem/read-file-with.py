# -----------------------------------------------------------
# read file content (with statement)
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define the name of the file to read from
filename = "test.txt"

with open(filename, 'r') as filehandle:
	for line in filehandle:
		print(line)

