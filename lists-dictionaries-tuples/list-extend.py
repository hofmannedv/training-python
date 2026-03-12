# -----------------------------------------------------------
# demonstrates how to extend a list by multiple items
#o
# (C) 2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define a list of places
cities1 = ["Paris", "Bordeaux", "Metz"]
cities2 = ["Bern", "Locarno", "Lausanne"]

print("cities #1:", cities1)
print("cities #2:", cities2)

# adding another list element
cities1.extend(cities2)
print("modified:", cities1)

