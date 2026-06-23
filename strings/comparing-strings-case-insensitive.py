# -----------------------------------------------------------
# demonstrates how to compare strings case-insensitive
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# using the == operator
listOfPlaces = ["Berlin", "Paris", "Lausanne"]
currentCity = "lausANne"

for place in listOfPlaces:
    print (f"comparing {place} with {currentCity}: {place.lower() == currentCity.lower()}")
