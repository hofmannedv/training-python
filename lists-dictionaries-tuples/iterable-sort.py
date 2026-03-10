# -----------------------------------------------------------
# demonstrates how to sort a dictionary by keys with the help of
# iterators
#
# (C) 2015-2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define a generator function
def sortedDictGenerator(dictionary):

    # retrieve the keys as a list
    dictionaryKeys = list(dictionary.keys())

    # sort the keys in place
    sortedKeys = sorted(dictionaryKeys)

    # return the current key as an iterator
    for currentKey in sortedKeys:
        # return a single element, only
        yield currentKey

# define a dictionary of capitals
capitals = {
    "Norway": "Oslo",
    "Germany": "Berlin",
    "France": "Paris"
}
print("original list (unsorted):", capitals)

# output list by keys in sorted order
print("list sorted by keys:")

for currentKey in sortedDictGenerator(capitals):
    print("%s: %s" % (currentKey, capitals[currentKey]))
