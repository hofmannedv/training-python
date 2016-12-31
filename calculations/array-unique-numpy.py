# -----------------------------------------------------------
# demonstrates how to sort, and unique an array using NumPy
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

# define an array with a name list
nameList = np.array(['Felix', 'Hans', 'Hanna', 'Felix', 'Katja'])
uniqueNameList = np.unique(nameList)

print ("name list            : ", nameList)
print ("unique, sorted names : ", uniqueNameList)

# define an array with values
valueList = np.array([10, 15, 2, 6, 78, 10, 8, 15])
uniqueValueList = np.unique(valueList)

print ("value list           : ", valueList)
print ("unique, sorted values: ", uniqueValueList)
