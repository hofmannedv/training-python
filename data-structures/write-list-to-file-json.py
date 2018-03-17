# -----------------------------------------------------------
# demonstrates how to write a list to a file in JSON format
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

# define list with values
basicList = [1, "Cape Town", 4.6]

# open output file for writing
with open('listfile.txt', 'w') as filehandle:
	json.dump(basicList, filehandle)
