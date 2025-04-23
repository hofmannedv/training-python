# -----------------------------------------------------------
# calculate the average of a list of integers
#o
# (C) 2014-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define a list of values
valueList = [1, 6, 3, 4, 5]

# list length
items = len(valueList)

# check for empty lists, first
if items:
	average = float(sum(valueList) / items)

	# Note:
	# for Python 2.x, the average value is 3.0 (integer value)
	# for Python 3.x, the average value is 3.8 (float value)

	# output average value
	print ("The average value is:", average)
else:
	print ("The list is empty.")

