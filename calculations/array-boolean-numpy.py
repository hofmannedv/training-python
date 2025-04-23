# -----------------------------------------------------------
# demonstrates the usage of boolean arrays using NumPy
# 
# (C) 2016-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# requirements:
# * Python 3.x
# * NumPy for Python 3 (http://www.numpy.org/)

# import external NumPy module
import numpy as np

# define an array with 10 random numbers
valueList = np.random.randn(10)
print ("data: ", valueList)

# count the positive values
print ("positive values in data: ", (valueList > 0).sum())
print ("negative values in data: ", (valueList < 0).sum())

# define a boolean array
bools = np.array([True, False, True])
print ("data: ", bools)
if bools.any():
	print ("data contains True values")

if bools.all():
	print ("data contains True values, only")

print (" ")

# define two arrays
valueList1 = np.array([1740, 23, 165, 18, 44])
valueList2 = np.array([1760, 23, 155, 19, 44])

print ("data 1: ", valueList1)
print ("data 2: ", valueList2)
print ("elements of data 2 that are in data 1:")
print (np.in1d(valueList1, valueList2))
print (" ")

# intersection of two lists
print ("the intersection of data 1 and 2 is:")
print (np.intersect1d(valueList1, valueList2))
print (" ")

# the union of two lists
print ("the union of data 1 and 2 is:")
print (np.union1d(valueList1, valueList2))
print (" ")

# set difference -- elements that exist in data 1 but not 2
print ("the elements that are in data 1 but not data 2 are:")
print (np.setdiff1d(valueList1, valueList2))
print (" ")

# set xor difference -- elements that are in either of the data 
# sets but not both
print ("the elements that are either in data 1 or 2 but not both:")
print (np.setxor1d(valueList1, valueList2))
print (" ")

