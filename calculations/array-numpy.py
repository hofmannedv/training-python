# -----------------------------------------------------------
# demonstrates various array calculations using the NumPy module
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

# define an array similar to a list with 15 elements (0-14)
matrix1 = np.arange(15)
print ("matrix 1:")
print (matrix1)

# define an empty matrix with 3 rows, and 4 columns
matrix2 = np.zeros((3,4))
print ("matrix 2:")
print (matrix2)

# define a matrix with ones -- 4 rows, and 3 columns
matrix3 = np.ones((4,3))
print ("matrix 3:")
print (matrix3)

# define a square n x n identity matrix (3x3)
matrix4 = np.identity(3)
print ("matrix 4:")
print (matrix4)

# define a 3 x 4 matrix with individual values
matrix5 = np.array([[1,2,3], [10,-5,6], [3,7,15], [8,20,11]])
print ("matrix 5:")
print (matrix5)

# add two matrices of the same size
print ("sum of matrix 3 and 5:")
print (matrix3 + matrix5)

# subtract two matrices of the same size
print ("subtracting matrix 5 from 3:")
print (matrix3 - matrix5)

# scalar operations -- multiplication
factor = 4
print ("scaling matrix 5 by 4:")
print (matrix5 * factor)

# scalar operations -- power
factor = 2
print ("powering matrix 5 by 2:")
print (matrix5 ** factor)
