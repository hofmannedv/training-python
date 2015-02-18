# -----------------------------------------------------------
# demonstrates how to work with sets (basic operations)
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define set of capitals
capitals = set(["Berlin", "Oslo", "Bern"])
print("original:", capitals)

# define set of other places
places = {"Toronto", "Washington", "Berlin", "Oslo"}
print("places:", places)

# add an element
capitals.add("Tokio")
print("modified:", capitals)

# remove an element
# - remove() raises error if element is not present
capitals.remove("Bern")
print("modified:", capitals)

# - discard() does not rais an error if element is not present
capitals.discard("Hamburg")
print("modified:", capitals)

# count the number of elements
print("number of elements:", len(capitals))

# union both set of places
placesList = places.union(capitals)
print("new places list:", placesList)

# clear the set
capitals.clear()
print("empty set:", capitals)

