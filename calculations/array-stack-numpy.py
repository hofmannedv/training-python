# -----------------------------------------------------------
# demonstrates how to stack arrays using the NumPy module
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

# define an array 2 x 2
# [ 1 2 ]
# [ 3 4 ]
data1 = np.array([[ 1,  2], [ 3,  4]])

# define another array 2 x 2
# [ 5 6 ]
# [ 7 8 ]
data2 = np.array([[ 5,  6], [ 7,  8]])

print ("data:")
print (data1)
print (data2)
print (" ")

# stack the two arrays vertical
print ("stack the two arrays vertical:")
print (np.vstack((data1,data2)))
print (" ")

# stack the two arrays horizontal
print ("stack the two arrays horizontal:")
print (np.hstack((data1,data2)))
print (" ")

