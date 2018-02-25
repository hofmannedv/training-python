# -----------------------------------------------------------
# write file content (basic version using a with command)
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define the name of the file to write to
filename = "helloworld.txt"

# open the file for writing
with open(filename, 'w') as filehandle:
	filehandle.write('Hello, world!\n')

