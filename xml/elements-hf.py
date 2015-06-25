# -----------------------------------------------------------
# demonstrates how to work with lxml module to extract xml 
# fields
#
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# include standard modules
from lxml import etree
import sys

def extractXml(filename):
	# read given file
	filehandle = open(filename, "r")

	# parse into xml structure
	tree = etree.parse(filehandle)
	
	# output each tag, and its according value
	for element in tree.iter():
		print("%s" % (element.tag))
	
	# close given file
	filehandle.close()

	return

# main program
if __name__ == "__main__":
	if len(sys.argv) > 1:
		filename = sys.argv[1]
		
		# extract fields from xml file
		extractXml(filename)

		# return with exit code 0
		sys.exit(0)
	else:
		# output error message
		print ("filename as commandline argument missing")
		
		# return with exit code 1
		sys.exit(1)

