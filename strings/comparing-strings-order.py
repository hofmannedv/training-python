# -----------------------------------------------------------
# demonstrates how to compare strings (different operators)
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define the strings
listOfPlaces = ["Berlin", "Paris", "Lausanne"]
currentCity = "Lausanne"

for place in listOfPlaces:
	if place < currentCity:
		print ("%s comes before %s" % (place, currentCity))
	elif place > currentCity:
		print ("%s comes after %s" % (place, currentCity))
	else:
		print ("%s is similar to %s" % (place, currentCity))
