# -----------------------------------------------------------
# write file content from a file buffer
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define the name of the output file
filename = "helloworld.txt"

# open the file for writing
filehandle = open(filename, 'w')

# define the file content
filebuffer = ["a first line of text", "a second line of text", "a third line"]

# add line terminators
filehandle.writelines("%s\n" % line for line in filebuffer)

# close the connection to that file
filehandle.close()
