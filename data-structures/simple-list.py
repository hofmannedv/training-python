# -----------------------------------------------------------
# demonstrates how to create and use a simple-linked list
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
		return

# main program

# create three single nodes
node1 = ListNode(15)
node2 = ListNode(8.2)
node3 = ListNode("Berlin")
