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
		print(stack.pop())
		print(stack)
	except:
		# list is empty
		print("at the end of list")
		break

