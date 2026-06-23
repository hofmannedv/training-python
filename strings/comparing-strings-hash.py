# -----------------------------------------------------------
# demonstrates how to compare strings case-sensitive
# using a hash value
#o
#o#### work in progress #####################################
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

# define list of places
listOfPlaces = [b"Bayswater", b"Table Bay", b"Bejing", b"Bombay"]

# create two SHA256 hash objects
referencePlace = b"Table Bay"
referencePlaceHashed = hashlib.sha256()
# referencePlaceHashed.update(referencePlace.encode("utf-8"))
referencePlaceHashed.update(referencePlace)
placeHashed = hashlib.sha256()

for place in listOfPlaces:
    # placeHashed.update(place.encode("utf-8"))
    placeHashed.update(place)
    print(placeHashed.hexdigest(), ":", referencePlaceHashed.hexdigest())
    if placeHashed.hexdigest() == referencePlaceHashed.hexdigest():
        print (f"{place} matches the reference place {referencePlace}")
