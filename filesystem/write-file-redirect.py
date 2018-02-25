# -----------------------------------------------------------
# write file content via redirection
# works for Python 2.x
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# idea taken from:
# https://stackoverflow.com/questions/4110891/python-how-to-simply-redirect-output-of-print-to-a-txt-file-with-a-new-line-crea
# -----------------------------------------------------------

# define the name of the file to write to
filename = "helloworld.txt"

# define content
filecontent = ["Hello, world", "a second line", "and a third line"]

with open(filename, 'w') as filehandle:
	# redirect the output of print to the file handle
	for line in filecontent:
		print >>filehandle, line

