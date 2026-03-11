# -----------------------------------------------------------
# demonstrates how to create a sorted list using the python 
# bisect module
#o
# (C) 2015-2026 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# import standard modules
import bisect, random

# define empty list, and fill the list with 10 random integers
sortedNumbers = []
for element in range(10):
    # choose a number between 0 and 1000
    newNumber = random.randint(0, 1000)
    print ("adding %i to list ... " %newNumber)
	
    # insert into sorted list
    bisect.insort(sortedNumbers, newNumber)

# output sorted list
print(sortedNumbers)
