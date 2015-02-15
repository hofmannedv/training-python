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

# add an element
capitals.add("Tokio")
print("modified:", capitals)

# remove an element
capitals.discard("Bern")
print("modified:", capitals)

# count the number of elements
print("number of elements:", len(capitals))

# clear the set
capitals.clear()
print("empty set:", capitals)

