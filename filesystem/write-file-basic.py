# -----------------------------------------------------------
# write file content (basic version)
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define the name of the file to write to
filename = "helloworld.txt"

# open the file for reading
filehandle = open(filename, 'w')

filehandle.write('Hello, world!\n')

# close the connection to that file
filehandle.close()
