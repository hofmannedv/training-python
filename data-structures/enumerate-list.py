# -----------------------------------------------------------
# demonstrates how to output an enumerated list
#o
# (C) 2018-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
#
# idea is based on: Python Tips - enumerate
# http://book.pythontips.com/en/latest/enumerate.html
# -----------------------------------------------------------

# define list of places
places = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']

# start number
start = 1

# start outputting the list of places beginning with the start number
for number, place in enumerate(places, start):
    print(f"{number}: {place}")
