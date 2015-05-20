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

# traversing the linked list
def traverseList (startNode):
	"traverse the linked list, and output the node data"

	# define currentNode
	currentNode = startNode

	# counted nodes
	count = 0

	while currentNode is not None:
		# retrieve and output node data
		print ("node:", currentNode.data)
	
		# jump to the linked node
		currentNode = currentNode.next
		
		# increase counter by one
		count = count + 1

	return count

# main program

# create three single nodes
node1 = ListNode(15)
node2 = ListNode(8.2)
node3 = ListNode("Berlin")

# link the objects
node1.next = node2
node2.next = node3

# output the full node list
# loop through the list of nodes up to the end
count = traverseList(node1)

print ("%i nodes visited" % count)
