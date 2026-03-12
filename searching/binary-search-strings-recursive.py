# -----------------------------------------------------------
# demonstrates a binary search in a list of strings using recursion
#o
# (C) 2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

def binarySearch(data, searchTerm):
    # define result as False: search term not found in data
    result = False

    print("analyzing", data, "for", searchTerm)

    maxElement = len(data)
    # continue searching only if we have data
    if maxElement > 0:
        median = maxElement // 2
        middleData = data[median]

        if middleData == searchTerm:
            result = True
        else:
            if middleData > searchTerm:
                result = binarySearch(data[:median], searchTerm)
            else:
                result = binarySearch(data[median+1:], searchTerm)
    return result

# define a list of first names in ascending order
sortedNamesList = ["Anna", "Berta", "Claus", "Felix", "Reto", "Urs", "Zoe"]

print("Claus is in names list:", binarySearch(sortedNamesList, "Claus"))
print("Hartmut is in names list:", binarySearch(sortedNamesList, "Hartmut"))
