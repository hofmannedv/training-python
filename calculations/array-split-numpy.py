# -----------------------------------------------------------
# demonstrates how to split an array using the NumPy module
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

# define an array 2 x 4
# [ 1 2 3 4 ]
# [ 5 6 7 8 ]
data1 = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])

print ("data:")
print (data1)
print (" ")

# split the array vertical
print ("split the array vertical into two pieces:")
print (np.vsplit(data1,2))
print (" ")

# split the array horizontal
print ("split the array horizontal into two pieces:")
print (np.hsplit(data1,2))
print (" ")

# split the array horizontal after the first and third row
print ("split the array horizontal into three pieces:")
print (np.hsplit(data1,(1,3)))
print (" ")

