# -----------------------------------------------------------
# demonstrates how to use ordered dictionaries from the 
# collections module
#o
# (C) 2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
#
# with inspiration from:
# * https://x.com/driscollis/status/2079189497598894486/photo/1
# * Python OrderedDict sorting: Keys and values
#   https://www.w3resource.com/python-exercises/extended-data-types/python-extended-data-types-index-ordereddict-exercise-2.php
# -----------------------------------------------------------

from collections import OrderedDict

# define a dictionary with names, and collected points
points = {
    'Thomas': 15,
    'John'  : 12,
    'Clara' : 14,
    'Zoe'   : 7
}

print("Unsorted dictionary:")
for name, value in points.items():
    print(f"{name:<10}: {value:3d}")

print(" ")
print("sorting items by name ...")
print(" ")

# convert data structure to OrderedDict
orderedPoints = OrderedDict(points.items())

# sort dictionary by name (key)
sortedOrderedPointsByName = OrderedDict(sorted(orderedPoints.items(), key=lambda item: item[0]))

print("Sorted dictionary:")
print(sortedOrderedPointsByName)

for name, value in sortedOrderedPointsByName.items():
    print(f"{name:<10}: {value:3d}")

print(" ")
print("sorting items by value ...")
print(" ")

# sort dictionary by value
sortedOrderedPointsByValue = OrderedDict(sorted(orderedPoints.items(), key=lambda item: item[1]))

print("Sorted dictionary:")
print(sortedOrderedPointsByValue)

for name, value in sortedOrderedPointsByValue.items():
    print(f"{name:<10}: {value:3d}")


