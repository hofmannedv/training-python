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

# removing up to the second element
del cities1[:1]
print("modified:", cities1)

# removing a specific element
cities1.remove("Lyon")
print("modified:", cities1)

# inserting an element at position 2
cities1.insert(2, "Blois")
print("modified:", cities1)

# sorting the list
cities1.sort()
print("sorted:", cities1)

# reversing the list
cities1.reverse()
print("reversed:", cities1)

# counting elements
print("number of 'Lausanne':", cities1.count("Lausanne"))

# searching the positition in the list
print("position of 'Blois' in the list:", cities1.index("Blois"))
