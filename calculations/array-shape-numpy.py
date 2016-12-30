# -----------------------------------------------------------
# demonstrates how to reshape an array using the NumPy module
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

# define an array 1 x 6
data = np.array([10, 1, 8, 23, 4, 56])
print ("data 1 x 6: ")
print (data)
print ("shape: ", data.shape)
print ("dimension: ", data.ndim)
print (" ")

# reshaping the array to 2 x 3
reshapedData = np.reshape(data, (2,3))
print ("reshaped data 2 x 3:")
print (reshapedData)
print ("shape: ", reshapedData.shape)
print ("dimension: ", reshapedData.ndim)

# changing the order
data2 = np.array([[1,2,3], [4,5,6]])
print ("data2 2 x 3:")
print (data2)
print (" ")

print ("1 x 6 in C-like order:")
print (data2.reshape(6, order='C'))
print (" ")

print ("1 x 6 in Fortran-like order:")
print (data2.reshape(6, order='F'))
