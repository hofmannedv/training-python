# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# set specific markers in a file if not set
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------
#

# include standard modules
import sys
import os.path

# count number of parameters
numPara = len(sys.argv)
if (numPara < 2):
	print ("called without further parameters. Exiting.")
	sys.exit(1)

# output every argument we were called with
currentArg = 0
for parameter in sys.argv:
	if (currentArg > 0):
		print ("file:", parameter)
		if not (os.path.isfile(parameter)):
			print ("file %s does not exist" % (parameter))
	currentArg += 1

# open file
# - file has to be the first parameter (others are ignored)
# evaluate the first five lines starting at line 0
# look for this comment: // filename
# if there: 
# - done
# - output: comment found (file marked properly)
# if not there: 
# - add the comment at line 0, and save file
# - output: comment found (file marked properly)


