# -----------------------------------------------------------
# demonstrates how to compare strings case-insensitive
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# using the == operator
listOfPlaces = ["Berlin", "Paris", "Lausanne"]
currentCity = "lausANne"

for place in listOfPlaces:
	print ("comparing %s with %s: %s" % (place, currentCity, place.lower() == currentCity.lower()))
