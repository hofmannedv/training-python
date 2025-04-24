# -----------------------------------------------------------
# create a stack class
#o
# (C) 2015-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------
#

# stack class

class Stack:
	def __init__(self):
		"initiate this object"
		self.items = []
		return

	def push(self, item):
		"store an item on the stack"
		self.items.append(item)
		return

	def pop(self):
		"retrieve an item from the stack"
		if not self.isEmpty():
			return self.items.pop()
		else:
			return False

	def isEmpty(self):
		"check for an empty stack"
		return (self.items == [])

	def size(self):
		"count the elements on the stack"
		return len(self.items)

# main program
if __name__ == '__main__':
	stack = Stack()
	
	# define data
	data = [15, 7, [4, 23], 39]
	
	# go through it step by step
	for item in data:
		if isinstance(item, int):
			# we have an integer
			stack.push(item)
		elif isinstance(item, list):
			# we have a list of integers
			for listItem in item:
				stack.push(listItem)
		
	# count total
	total = 0

	# take the items from the stack
	while not stack.isEmpty():
		value = stack.pop()
		print ("added %i to %i" % (value, total))
		total += value

	# output total
	print ("total:", total)
