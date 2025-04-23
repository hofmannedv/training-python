# -----------------------------------------------------------
# calculate the minimum, and the maximum value element-wise for 
# two arrays of integers using the NumPy module
#o
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

# define a list of integer values
valueList1 = np.array([1, 6, 3, 4, 5])
valueList2 = np.array([2, 4, 3, 1, 9])

print ("data 1: ", valueList1)
print ("data 2: ", valueList2)
print (" ")

# calculate maximum and minimum
print ("calculate the maximum/minimum between data 1 and 2:")
print ("maximum:", np.maximum(valueList1, valueList2))
print ("minimum:", np.minimum(valueList1, valueList2))
print (" ")

# element-wise comparison
print ("compare data 1 and 2:")
print ("greater:      ", np.greater(valueList1, valueList2))
print ("greater-equal:", np.greater_equal(valueList1, valueList2))
print ("equal:        ", np.equal(valueList1, valueList2))
print ("not-equal:    ", np.not_equal(valueList1, valueList2))
print ("less:         ", np.less(valueList1, valueList2))
print ("less-equal:   ", np.less_equal(valueList1, valueList2))
