# -----------------------------------------------------------
# demonstrates various basic list operations
#o
# (C) 2015-2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define two lists
cities1 = ["Paris", "Bordeaux", "Metz"]
cities2 = ["Bern", "Locarno", "Lausanne"]

# combine these lists
citiesList = cities1 + cities2
print(cities1)
print(cities2)
print(citiesList)

# combine these lists with additional counter
citiesList = cities1 + cities2 * 2
print(cities1)
print(cities2)
print(citiesList)

# output elements 2 to 4, only
# - line by line using a while loop
index = 2
while index < 5:
    print(citiesList[index])
    index += 1

# - all at once using indexes (as a sub-list)
print(citiesList[2:5])

# output list in reverse order
print(citiesList[::-1])
