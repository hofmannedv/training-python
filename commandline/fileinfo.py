#!/usr/bin/python

# -----------------------------------------------------------
# demonstrates how to work with commandline arguments using
# docopt (http://docopt.org/)
#
# example fileinfo program
# based my blog post here: 
# http://www.stackabuse.com/python-list-files-in-a-directory/
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

"""Usage:
    ./fileinfo.py
    ./fileinfo.py [--help | -h]
    ./fileinfo.py [--verbose | -v]
    ./fileinfo.py [--files | -f]
    ./fileinfo.py [--dirs | -d]
   
   Options:
    --help -h     display help information
    --verbose -v  increase the verbosity of output
    --files -f    display files only
    --dirs -d     display directories only
"""

# include docopt module
from docopt import docopt

# import other modules
import os, fnmatch

if __name__ == '__main__':
	arguments = docopt(__doc__)
	#print (arguments)
	
	# define which information to show
	showFiles = True
	showDirectories = True
	path = "."
	selection = "*"
	verbose = False
	
	if arguments["--verbose"]:
		print("enabling verbose output ")
		verbose = True
	
	if arguments["--files"]:
		showDirectories = False
	
	if arguments["--dirs"]:
		showFiles = False
	
	# define display path
	displayPath = path
	
	for root, dirs, files in os.walk(displayPath):
		if showFiles:
			for filename in files:
				print(filename)
		if showDirectories:
			for dirname in dirs:
				print(dirname)
