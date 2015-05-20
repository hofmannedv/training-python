# -----------------------------------------------------------
# demonstrates how to create and use a double-linked list
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
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

# main program

# create three single nodes
node1 = ListNode(15)
node2 = ListNode(8.2)
node3 = ListNode("Berlin")

# link the objects
node1.next = node2
node2.previous = node1
node2.next = node3
node3.previous = node2

# output the full node list
# define start node
startNode = node1

# define currentNode
currentNode = startNode

# loop through the list of nodes up to the end
while currentNode is not None:
	# retrieve and output node data
	data = currentNode.data
	print ("node:", data)
	
	# jump to the linked node
	currentNode = currentNode.next
