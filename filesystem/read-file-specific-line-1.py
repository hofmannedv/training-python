# -----------------------------------------------------------
# read a specific line from a file, only
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define the name of the file to read from
filename = "test.txt"

# define the line number
lineNumber = 3

print ("line %i of %s is: " % (lineNumber, filename))

with open(filename, 'r') as filehandle:
	currentLine = 1
	for line in filehandle:
		if currentLine == lineNumber:
			print(line)
			break
		currentLine += 1

