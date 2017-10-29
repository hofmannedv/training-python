# -----------------------------------------------------------
# demonstrates how to create and use a double-linked list 
# using the collections module
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

from collections import deque

class ListNode:
	def __init__(self, data):
		"constructor class to initiate this object"

		# store data
		self.data = data
		
		return

# main program

# create three single nodes
node1 = ListNode(15)
node2 = ListNode(8.2)
node3 = ListNode("Berlin")

# create a track (double-ended queue)
track = deque([node1,node2,node3])
print("three items (initial list):")
for item in track:
	print (item.data)

print ("--")

# add an item at the beginning
node4 = ListNode(15)
track.appendleft(node4)
print("four items (added as the head):")
for item in track:
	print (item.data)

print ("--")

# add an item at the end
node5 = ListNode("Moscow")
print("five items (added at the end):")
track.append(node5)
for item in track:
	print (item.data)
