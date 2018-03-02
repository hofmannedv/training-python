# -----------------------------------------------------------
# demonstrates how to compare strings (== operator)
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# using the == operator
listOfPlaces = ["Berlin", "Paris", "Lausanne"]
currentCity = "Lausanne"

for place in listOfPlaces:
	print ("comparing %s with %s: %s" % (place, currentCity, place == currentCity))
