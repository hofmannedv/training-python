#!/usr/bin/python

# -----------------------------------------------------------
# reads data from the specified files, only, and outputs
# the line number of the file, and the content of the line
# demonstrates the usage of the fileinput module
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import fileinput

with fileinput.FileInput(files=('example1', 'example2')) as input:
	filename = input.filename()
	for line in input:
		lineNo = input.filelineno()
		totalLineNo = input.lineno()
		print("%s:%2i:%2i:%s" % (filename,totalLineNo, lineNo, line[:-1]))

