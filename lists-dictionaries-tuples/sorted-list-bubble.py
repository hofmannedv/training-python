# -----------------------------------------------------------
# demonstrates how to create a sorted list using bubble sort
#o
# (C) 2026 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# import standard module
import random

# define list length
listlength = 10

# define empty list, and fill the list with 10 random integers
sortedNumbers = []
for element in range(listlength):
    # choose a number between 0 and 1000
    newNumber = random.randint(0, 1000)
    print ("adding %i to list ... " % newNumber)
    sortedNumbers.append(newNumber)
	
for element in range(listlength):
    for position in range(listlength - 1 - element):
        if sortedNumbers[position] > sortedNumbers[position + 1]:
            sortedNumbers[position], sortedNumbers[position + 1] = sortedNumbers[position + 1], sortedNumbers[position]
            print(sortedNumbers)

# output sorted list
print(sortedNumbers)
