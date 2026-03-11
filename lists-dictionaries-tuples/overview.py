# -----------------------------------------------------------
# demonstrates how to create lists, dictionaries, and tuples
#o
# (C) 2014-2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# list of numbers, only
numbersList = [394, 6, 15, 2, 88, 153]

# a list with mixed values - integers, strings, floats, and boolean value
mixedList = [1184, "orange", 3.56, True]
print (numbersList)
print (mixedList)
print (numbersList + mixedList)

# a tuple of numbers (a fixed list that cannot be changed)
numbersTuple = (23, 17, -6, 516)
smallTuple = (45, "Henry")
print (numbersTuple)
print (smallTuple)
print (numbersTuple + smallTuple)

# define a dictionary
book = {}
book['isbn'] = "3-145-789"
book['title'] = "Learning Python"
print (("title, isbn: %s, %s") % (book['title'], book['isbn']))
