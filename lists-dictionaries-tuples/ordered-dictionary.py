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
