# -----------------------------------------------------------
# demonstrates how to use a list as a stack
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define list (stack)
stack = [3, 7, 12, 15]
print(stack)

while True:
	try:
		# pop last element
		# retrieve the element
		value = stack.pop()
		print("taken from stack:", value)
		print("current stack:", stack)
	except:
		# list is empty -- we cannot take more elements
		print("at the end of list")
		break

