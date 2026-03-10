# -----------------------------------------------------------
# demonstrates how to extract the items of a dictionary using items()
#o
# (C) 2015-2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define an array (dictionary)
capital = {
    "France": "Paris",
    "Switzerland": "Bern",
    "Germany": "Berlin"
}

# output dictionary content (key-value-pairs)
print (capital)

# extract the items of the dictionary
entries = capital.items()

# count the items
print("number of items:", len(entries))
print(entries)
