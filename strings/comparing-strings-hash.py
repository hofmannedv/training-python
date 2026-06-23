# -----------------------------------------------------------
# demonstrates how to compare strings case-sensitive
# using a SHA256 hash value
#o
# (C) 2026 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# import the additional module
import hashlib

# create a SHA256 hash object as reference
referencePlace = "Table Bay"
referencePlaceHashed = hashlib.sha256()
referencePlaceHashed.update(referencePlace.encode("utf-8"))
print("Reference:")
print(f"{referencePlace}: {referencePlaceHashed.hexdigest()}")
print("")

# define list of places
listOfPlaces = ["Bayswater", "Table Bay", "Bejing", "Bombay"]

# see if two places are identical
for place in listOfPlaces:
    placeHashed = hashlib.sha256()
    placeHashed.update(place.encode("utf-8"))
    print(f"{place}: {placeHashed.hexdigest()}")
    if placeHashed.hexdigest() == referencePlaceHashed.hexdigest():
        print(f"{place} and {referencePlace} are identical")

