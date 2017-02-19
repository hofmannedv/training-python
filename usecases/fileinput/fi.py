
#!/usr/bin/python

# -----------------------------------------------------------
# reads data from the files given as parameter, and outputs
# the line number of the file, and the content of the line
# demonstrates the usage of the fileinput module
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import fileinput

for line in fileinput.input():
	filename = fileinput.filename()
	lineNo = fileinput.filelineno()
	totalLineNo = fileinput.lineno()
	print("%s:%2i:%2i:%s" % (filename,totalLineNo, lineNo, line[:-1]))

