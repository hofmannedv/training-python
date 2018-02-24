# -----------------------------------------------------------
# read specific line of a file using the linecache module
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import linecache module
import linecache

# define the name of the file to read from
filename = "test.txt"

# define lineNumber
lineNumber = 3

# retrieve specific line
line = linecache.getline(filename, lineNumber)
print ("line %i of %s:" % (lineNumber, filename))
print (line)

