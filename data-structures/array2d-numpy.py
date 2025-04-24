# -----------------------------------------------------------
# demonstrates how to create and use an 2d array using NumPy
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

class Array2D:
	def __init__(self, rows, columns):
		"constructor class to initiate this object"

		# set array size
		self.rows = rows
		self.columns = columns

		# define an array with zero values
		self.arrayData = np.zeros((self.rows, self.columns))
		
		return
	
	def getSize(self):
		"return the size of the 2d array"
		return self.arrayData.shape

	def getDimension(self):
		"return the dimension of the 2d array"
		return self.arrayData.ndim

	def getNumberOfElements(self):
		"count the number of elements in the 2d array"
		return self.arrayData.size

	def print(self):
		"output the array 2d content"
		print (self.arrayData)
		return
	
	def getElementValue(self, column, row):
		"get the element value at array position x,y"
		
		if row <= self.rows:
			arrayRow = self.arrayData[row]
			if column <= self.columns:
				# return success
				return self.arrayData[row][column]
			else:
				# return failure
				return False
		else:
			# return failure
			return False

	def setElementValue(self, column, row, value):
		"set the element value at array position x,y"
		
		if row <= self.rows:
			arrayRow = self.arrayData[row]
			if column <= self.columns:
				self.arrayData[row][column] = value
				# return success
				return True
			else:
				# return failure
				return False
		else:
			# return failure
			return False


# main program

# define 2d array of size 3x3
array2 = Array2D(3,3)
print ("2D array size:", array2.getSize())

print ("number of array items:", array2.getNumberOfElements())

print ("dimensions of the array:", array2.getDimension())

# output array content
array2.print()

# set value at [1,1] = 15
if array2.setElementValue(1, 1, 15) == False:
	print ("array index out of range")
else:
	print ("position (1,1) set to 15")

# set value at [5,0] = 7
if array2.setElementValue(0, 5, 7) == False:
	print("array index (0,5) out of range")
else:
	print ("position (0,5) set to 7")

# output array content
array2.print()

# output specific array value
print ("value at (2,2):", array2.getElementValue(2,2))

