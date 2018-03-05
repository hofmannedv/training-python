# -----------------------------------------------------------
# demonstrates how to compare strings case-insensitive
# using a regular expression
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import the additional module
import re

# define list of places
listOfPlaces = ["Bayswater", "Table Bay", "Bejing", "Bombay"]

# define search string
pattern = re.compile("[Bb]ay")

for place in listOfPlaces:
	if pattern.search(place):
		print ("%s matches the search pattern" % place)
