# -----------------------------------------------------------
# demonstrates how to create and use a double-linked list
#o
# (C) 2015-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

class ListNode:
	def __init__(self, data):
		"constructor class to initiate this object"

		# store data
		self.data = data
		
		# store reference (next item)
		self.next = None
		# store reference (previous item)
		self.previous = None
		return
	
	def getData(self):
		"method to return the value of the node"
		return self.data
	
	def setData(self, value):
		"method to save or modify the node value"
		self.data = value
		return

	def getNext(self):
		"method to return the reference to the next node"
		return self.next
	
	def getPrevious(self):
		"method to return the reference to the previous node"
		return self.previous
	
	def hasValue(self, value):
		"method to compare the value with the node data"
		if self.data == value:
			return True
		else:
		    return False

class DoubleLinkedList:
	def __init__(self):
		"constructor to initiate this object"

		self.head = None
		self.tail = None
		return

	def listLength(self):
		"returns the number of list items"
		
		count = 0
		currentNode = self.head

		while currentNode is not None:
			# increase counter by one
			count = count + 1
			
			# jump to the linked node
			currentNode = currentNode.getNext()
		
		return count

	def outputList(self):
		"outputs the list (the value of the node, actually)"
		currentNode = self.head

		while currentNode is not None:
			print (currentNode.getData())

			# jump to the linked node
			currentNode = currentNode.getNext()
		
		return

	def addListitem(self, item):
		"add an item at the end of the list"

		if isinstance(item, ListNode):
			if self.head is None:
				self.head = item
				item.previous = None
				item.next = None
				self.tail = item
			else:
				self.tail.next = item
				item.previous = self.tail
				self.tail = item
		
		return

	def unorderedSearch (self, value):
		"search the linked list for the node that has this value"

		# define currentNode
		currentNode = self.head

		# define position
		nodeId = 1

		# define list of results
		results = []

		while currentNode is not None:
			if currentNode.hasValue(value):
				results.append(nodeId)
			
			# jump to the linked node
			currentNode = currentNode.getNext()
			nodeId = nodeId + 1
		
		return results

	def removeListitemById(self, itemId):
		"remove the list item with the item id"
		
		currentId = 1
		currentNode = self.head

		while currentNode is not None:
			previousNode = currentNode.getPrevious()
			nextNode = currentNode.getNext()

			if currentId == itemId:
				# if this is the first node (head)
				if previousNode is not None:
					previousNode.next = nextNode
					if nextNode is not None:
						nextNode.previous = previousNode
				else:
					self.head = nextNode
					if nextNode is not None:
						nextNode.previous = None
				# we don't have to look any further
				return
 
			# needed for the next iteration
			currentNode = nextNode
			currentId = currentId + 1
				
		return

# main program

# create three single nodes
node1 = ListNode(15)
node2 = ListNode(8.2)
node3 = ListNode("Berlin")
node4 = ListNode(15)

track = DoubleLinkedList()
print ("track length: %i" % track.listLength())

for currentNode in [node1, node2, node3, node4]:
	track.addListitem(currentNode)
	print ("track length: %i" % track.listLength())
	track.outputList()

results = track.unorderedSearch(15)
print (results)

track.removeListitemById(4)
track.outputList()
