# -----------------------------------------------------------
# demonstrates how to find an entry in a list
#o
# (C) 2021-2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

def compareLists1(list1, list2):
    # binary comparison
    result = set(list1) & set(list2)
    return result

def compareLists2(list1, list2):
    # set intersection
    result = set(list1).intersection(list2)
    return result

def isEntryInCache(searchEntry):
    global cache
    result = False

    for entry in cache:
        if (compareLists1(entry, searchEntry)):
            result = True
            break

    return result

# define a list of lists named cache
numbers1 = [1, 155, 17]
numbers2 = [23, 61, 82]
numbers3 = [15, 23, 82]
cache = []
numbers4 = [23, 61, 82]

newEntries = [numbers1, numbers2, numbers3]
for item in newEntries:
    cache.append(item)
    print(cache)
    print(isEntryInCache(numbers4))

