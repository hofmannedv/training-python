# -----------------------------------------------------------
# read file content (C/C++ style)
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define the name of the file to read from
filename = "test.txt"

# open the file for reading
filehandle = open(filename, 'r')
while True:
	# read a single line
	line = filehandle.readline()
	if not line:
		break
	print(line)

# close the connection to that file
filehandle.close()
