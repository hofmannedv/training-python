
#!/usr/bin/python

# -----------------------------------------------------------
# reads data from stdin or files given as a parameter
# demonstrates the usage of the fileinput module
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import fileinput

for line in fileinput.input():
	# do we read from stdin?
	if fileinput.isstdin():
		print ("data read from stdin")
		break
	else:
		# detect the name of the file which is currently processed
		filename = fileinput.filename()
		print ("data read from %s" % filename)
		fileinput.nextfile()
