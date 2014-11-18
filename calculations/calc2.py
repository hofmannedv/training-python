# -----------------------------------------------------------
# calculate the total for a list of items
# 
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define a list of single values
valueList = [100, 13, 35, 8, -7, 1688]

# number of items
numberOfItems = len(valueList)

# define total value
total = 0

# calculate the total sum
for singleValue in valueList:
	total = total + singleValue

# output the total sum
# ... using C-like syntax
print ("Total for %i items: %i" % (numberOfItems, total))
