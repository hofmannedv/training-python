# -----------------------------------------------------------
# demonstrates the usage of boolean arrays using NumPy
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
