# -----------------------------------------------------------
# search a value in a list using in operator
#o
# (C) 2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

def easySearch(data, value):
    """search value in unordered data using the in operator"""

    result = False                     # assumption: value not in list

    if value in data:
        result = True

    return result


data = [34, 12, 67, 55, 10]
value = 125
result = easySearch(data, value)
if result:
    print(value, "in", data)
else:
    print(value, "not in", data)

