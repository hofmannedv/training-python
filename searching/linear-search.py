# -----------------------------------------------------------
# search a value in a list using linear seach using a while loop
#o
# (C) 2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

def linearSearch(data, value):
    """search value in unordered data using a while loop"""

    result = False                     # assumption: value not in list

    numberOfItems = len(data)
    if numberOfItems:
        # list of data is not empty -- let's search in it
        position = 0
        while position < numberOfItems:
            if value == data[position]:
                result = True
                break
            position = position + 1

    return result


data = [34, 12, 67, 55, 10]
value = 125
result = linearSearch(data, value)
if result:
    print(value, "in", data)
else:
    print(value, "not in", data)

