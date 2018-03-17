# -----------------------------------------------------------
# demonstrates how to read a list from a file in JSON format
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define imported json modules
try: 
	import simplejson as json
except ImportError: 
	import json

# open output file for reading
with open('listfile.txt', 'r') as filehandle:
	basicList = json.load(filehandle)

print (basicList)
