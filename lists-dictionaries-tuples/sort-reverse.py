# -----------------------------------------------------------
# demonstrates how to sort lists
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define basic list
numbers = [56, 22, 73, 105]

# sorting numbers ascending
sortedNumbers = sorted(numbers)

# reversing the list
reversedNumbers = reversed(numbers)

# output
print("original list:", numbers)
print("sorted list:", sortedNumbers)

# reversed returns an iterator object, so we have to use a loop
print("reversed list:")
for i in reversedNumbers:
	# print the value, followed by a single space
	print(i, end=" ")

# output an empty line at the end
print()
