# -----------------------------------------------------------
# calculate the minimum, and the maximum value for a list of integers
# using the NumPy module
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

# define a list of values
valueList = np.array([1, 6, 3, 4, 5])
print ("data:")
print (valueList)

# list length
items = np.size(valueList)

# check for empty lists, first
if items:
	# find both the minimum, and the maximum value
	minimumValue = np.min(valueList)
	maximumValue = np.max(valueList)

	# find both the array position for the minimum, and the maximum value
	minimumValuePosition = np.argmin(valueList)
	maximumValuePosition = np.argmax(valueList)

	# output the values and its positions
	print ("The minimum value is %i at position %i." % (minimumValue, minimumValuePosition))
	print ("The maximum value is %i at position %i." % (maximumValue, maximumValuePosition))
else:

	print ("The list is empty.")

