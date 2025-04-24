# -----------------------------------------------------------
# demonstrates how to read a list from a file in JSON format
#o
# (C) 2018-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
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
