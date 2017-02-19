#!/usr/bin/python

# -----------------------------------------------------------
# reads data from the specified files, only, and uses a
# special hook to process compressed files, too. Outputs the 
# file name, only.
# demonstrates the usage of the fileinput module
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import fileinput

for line in fileinput.input(files=['example1', 'example.tar.gz'], openhook=fileinput.hook_compressed):
	filename = fileinput.filename()
	print (filename)
	fileinput.nextfile()

