# -----------------------------------------------------------
# demonstrates various basic list operations
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define two lists
cities1 = ["Paris", "Bordeaux", "Metz"]
cities2 = ["Bern", "Locarno", "Lausanne"]

print(cities1)
print(cities2)

# adding another list element
cities1.append("Lyon")
print("modified:", cities1)

# substituting the second element
cities1[1] = "Nancy"
print("modified:", cities1)

# substituting a number of elements
cities1[1:3] = cities2
print("modified:", cities1)

# removing the first element
del cities1[:1]
print("modified:", cities1)
