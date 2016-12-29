# -----------------------------------------------------------
# calculate the total for a list of items using the NumPy module
# 
# (C) 2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# requirements:
# * Python 3.x
# * NumPy for Python 3 (http://www.numpy.org/)

# import external NumPy module
import numpy as np

# define a list of single values
valueList = np.array([100, 13, 35, 8, -7, 1688])

# number of items
numberOfItems = valueList.size

# define total value
total = 0

# calculate the total using sum from NumPy
total = np.sum(valueList)

# calculate the cumulative sum using cumsum from NumPy
cumulativeSum = np.cumsum(valueList)

# output the total sum
print ("Data: ", valueList)
# ... using C-like syntax
print ("Total for %i items: %i" % (numberOfItems, total))
print ("Cumulative sums: ", cumulativeSum)
