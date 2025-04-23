# -----------------------------------------------------------
# calculate the minimum, and the maximum value for a list of integers
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
	minimumValue = min(valueList)
	maximumValue = max(valueList)

	# output average value
	print ("The minimum value is:", minimumValue)
	print ("The maximum value is:", maximumValue)
else:
	print ("The list is empty.")

