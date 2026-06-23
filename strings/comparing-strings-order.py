# -----------------------------------------------------------
# demonstrates how to compare strings (different operators)
#o
# (C) 2018-2026 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define the strings
listOfPlaces = ["Berlin", "Paris", "Lausanne"]
currentCity = "Lausanne"

for place in listOfPlaces:
    if place < currentCity:
        print (f"{place} comes before {currentCity}")
    elif place > currentCity:
        print (f"{place} comes after {currentCity}")
    else:
        print (f"{place} is similar to {currentCity}")
