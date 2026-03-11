# -----------------------------------------------------------
# demonstrates how to work with sets (basic operations)
#o
# (C) 2015-2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define set of capitals based on a list
capitals = set(["Berlin", "Oslo", "Paris"])
print("original:", capitals)

# define another set of places
places = {"Toronto", "Washington", "Berlin", "Oslo"}
print("places:", places)

# add an element to the second list
capitals.add("Tokio")
print("modified (add):", capitals)

# remove an element
# - remove() raises error if element is not present
try:
    capitals.remove("Bern")
    print("modified (remove):", capitals)
except:
    print("cannot remove Bern from the set. Entry does not exist in the set.")
    print("unmodified set:", capitals)

# - discard() does not raise an error if element is not present
capitals.discard("Hamburg")
print("modified (discard):", capitals)

# count the number of elements
print("number of elements:", len(capitals))

# union both set of places
placesList = places.union(capitals)
print("new places list:", placesList)

# clear the set
capitals.clear()
print("empty set:", capitals)

