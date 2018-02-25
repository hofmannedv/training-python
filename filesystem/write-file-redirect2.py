# -----------------------------------------------------------
# write file content via redirection
# works for Python 2.x and 3.x
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# idea taken from:
# https://www.blog.pythonlibrary.org/2016/06/16/python-101-redirecting-stdout/
# -----------------------------------------------------------

# import sys module
import sys

# define the name of the output file
filename = "helloworld.txt"

# preserve the stdout channel
original = sys.stdout

# define content
filecontent = ["Hello, world", "a second line", "and a third line"]

with open(filename, 'w') as filehandle:
	# set the new output channel
	sys.stdout = filehandle
	
	for line in filecontent:
		print(line)
	
	# restore the old output channel
	sys.stdout = original

