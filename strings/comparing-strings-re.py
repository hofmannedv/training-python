# -----------------------------------------------------------
# demonstrates how to compare strings case-insensitive
# using a regular expression
#o
# (C) 2018-2026 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# import the additional module
import re

# define list of places
listOfPlaces = ["Bayswater", "Table Bay", "Bejing", "Bombay"]

# define search string
pattern = re.compile("[Bb]ay")

for place in listOfPlaces:
    if pattern.search(place):
        print (f"{place} matches the search pattern")
